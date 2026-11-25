"""ELA'S AI Content Studio: topic database, 30-day calendar and performance log.

usage:
  python3 studio/tools/studio.py topics [--cat D] [--status Idea]
  python3 studio/tools/studio.py add "Tajuk baharu?" --cat D
  python3 studio/tools/studio.py status <id> <Status> [--slug <siri-slug>]
  python3 studio/tools/studio.py calendar [--days 30] [--start 2026-11-26]
  python3 studio/tools/studio.py perf <id> views=1200 likes=80 ...      (record real numbers)
  python3 studio/tools/studio.py report                                   (best categories from perf.json)
  python3 studio/tools/studio.py make <id> [--render]                     (build 9:16 + 16:9 for a topic that has a spec)

Status flow: Idea > Research > Script > Storyboard > Production > Rendering > Review > Approved > Scheduled > Published.
"""
import argparse, datetime as dt, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE)
ROOT = os.path.dirname(STUDIO)
TOPICS = f"{STUDIO}/content/topics.json"
CAL = f"{STUDIO}/content/calendar.json"
PERF = f"{STUDIO}/content/performance.json"
STATUSES = ["Idea", "Research", "Script", "Storyboard", "Production", "Rendering", "Review", "Approved", "Scheduled", "Published"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
HARI = dict(Mon="Isnin", Tue="Selasa", Wed="Rabu", Thu="Khamis", Fri="Jumaat", Sat="Sabtu", Sun="Ahad")
METRICS = ["views", "reach", "likes", "comments", "shares", "saves", "watch_time_s", "avg_view_s", "completion_rate", "followers", "ctr"]


def load():
    return json.load(open(TOPICS))


def save(db):
    json.dump(db, open(TOPICS, "w"), ensure_ascii=False, indent=1)


def cmd_topics(a):
    db = load()
    for t in db["topics"]:
        if a.cat and t["category"] != a.cat.upper():
            continue
        if a.status and t["status"].lower() != a.status.lower():
            continue
        print(f'{t["id"]:>3}  {t["category"]}  {t["status"]:<10} {t["title"]}' + (f'  [{t["slug"]}]' if t.get("slug") else ""))


def cmd_add(a):
    db = load()
    cat = a.cat.upper()
    if cat not in db["categories"]:
        sys.exit(f"unknown category {cat}; choose from {', '.join(db['categories'])}")
    norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
    if any(norm(t["title"]) == norm(a.title) for t in db["topics"]):
        sys.exit("topic already exists")
    c = db["categories"][cat]
    t = dict(id=max(x["id"] for x in db["topics"]) + 1, category=cat, category_name=c["name"], subseries=c["subseries"],
             style=c["style"], title=a.title, status="Idea", slug=None, needs_fact_check=cat in ("A", "E", "F"))
    db["topics"].append(t); save(db)
    print(f"added #{t['id']}: {t['title']}")


def cmd_status(a):
    db = load()
    if a.status not in STATUSES:
        sys.exit(f"status must be one of: {' > '.join(STATUSES)}")
    for t in db["topics"]:
        if t["id"] == a.id:
            t["status"] = a.status
            if a.slug:
                t["slug"] = a.slug
            save(db); print(f'#{t["id"]} -> {t["status"]}'); return
    sys.exit("no such topic")


def existing_schedule():
    """Mon/Wed/Fri posts already scheduled in Metricool (siri/JADUAL.md)."""
    out = {}
    path = f"{ROOT}/siri/JADUAL.md"
    if os.path.exists(path):
        for m in re.finditer(r"\| \w+ (\d{4}-\d\d-\d\d) \| ([0-9a-z-]+) \|", open(path).read()):
            out[m.group(1)] = m.group(2)
    return out


def cmd_calendar(a):
    db = load()
    start = dt.date.fromisoformat(a.start) if a.start else dt.date.today() + dt.timedelta(days=1)
    booked = existing_schedule()
    by_slug = {t["slug"]: t for t in db["topics"] if t.get("slug")}
    used = {t["id"] for t in db["topics"] if t["status"] != "Idea"}
    if os.path.exists(CAL):  # keep topics already placed on a date
        for e in json.load(open(CAL)).get("days", []):
            if e.get("topic_id") and e["date"] < start.isoformat():
                used.add(e["topic_id"])
    pool = {c: [t for t in db["topics"] if t["category"] == c and t["id"] not in used] for c in db["categories"]}
    days = []
    for i in range(a.days):
        d = start + dt.timedelta(days=i)
        wd = DAYS[d.weekday()]; iso = d.isoformat()
        if iso in booked:
            t = by_slug.get(booked[iso])
            days.append(dict(date=iso, day=wd, category=t["category"] if t else None, topic_id=t["id"] if t else None,
                             title=t["title"] if t else booked[iso], status="Scheduled", source="siri (Metricool)"))
            continue
        cat = db["weekday_plan"][wd]
        cand = pool.get(cat) or []
        if not cand:  # category exhausted: fall back to the category with most topics left
            cat = max(pool, key=lambda c: len(pool[c])); cand = pool[cat]
        if not cand:
            days.append(dict(date=iso, day=wd, category=None, topic_id=None, title="(tiada tajuk tersisa)", status="Idea")); continue
        t = cand.pop(0)
        days.append(dict(date=iso, day=wd, category=cat, topic_id=t["id"], title=t["title"], status=t["status"], source="studio"))
    json.dump(dict(start=start.isoformat(), days=days), open(CAL, "w"), ensure_ascii=False, indent=1)
    md = ["# Kalendar kandungan 30 hari — Di Sebalik Kerusi Barber", "",
          f"Mula {start.isoformat()}, waktu Malaysia. Isnin/Rabu/Jumaat yang sudah dijadual (siri tips) dikekalkan; hari lain diisi daripada pangkalan 70 tajuk ikut tema hari.", "",
          "| Tarikh | Hari | Kategori | # | Tajuk | Status |", "|---|---|---|---|---|---|"]
    for e in days:
        md.append(f'| {e["date"]} | {HARI[e["day"]]} | {e["category"] or ""} | {e["topic_id"] or ""} | {e["title"]} | {e["status"]} |')
    open(f"{STUDIO}/content/CALENDAR.md", "w").write("\n".join(md) + "\n")
    print("\n".join(md[5:]))


def cmd_perf(a):
    db = load()
    if not any(t["id"] == a.id for t in db["topics"]):
        sys.exit("no such topic")
    perf = json.load(open(PERF)) if os.path.exists(PERF) else {"entries": []}
    rec = {"topic_id": a.id, "recorded": dt.date.today().isoformat(), "platform": a.platform}
    for kv in a.metrics:
        k, v = kv.split("=", 1)
        if k not in METRICS:
            sys.exit(f"unknown metric {k}; use {', '.join(METRICS)}")
        rec[k] = float(v)
    perf["entries"].append(rec)
    json.dump(perf, open(PERF, "w"), indent=1); print("recorded", rec)


def cmd_report(a):
    if not os.path.exists(PERF):
        sys.exit("no performance data yet: record real numbers with `perf` first")
    db = load(); cat = {t["id"]: t["category"] for t in db["topics"]}
    agg = {}
    for e in json.load(open(PERF))["entries"]:
        c = cat.get(e["topic_id"], "?"); s = agg.setdefault(c, dict(n=0, views=0, eng=0))
        s["n"] += 1; s["views"] += e.get("views", 0)
        s["eng"] += sum(e.get(k, 0) for k in ("likes", "comments", "shares", "saves"))
    print("cat  posts  avg_views  engagement_rate")
    for c, s in sorted(agg.items(), key=lambda kv: -kv[1]["views"] / max(1, kv[1]["n"])):
        print(f'{c:<4} {s["n"]:>5}  {s["views"] / s["n"]:>9.0f}  {100 * s["eng"] / max(1, s["views"]):>6.1f}%')


def cmd_make(a):
    import subprocess
    sys.path.insert(0, f"{ROOT}/siri")
    from specs import VIDEOS
    v = next((v for v in VIDEOS if v.get("topic_id") == a.id), None)
    if not v:
        db = load(); t = next((t for t in db["topics"] if t["id"] == a.id), None)
        if t and t.get("slug"):
            v = next((v for v in VIDEOS if v["slug"] == t["slug"]), None)
    if not v:
        sys.exit(f"topic #{a.id} has no script yet: add an entry with topic_id={a.id} to siri/specs.py (ask Claude: 'tulis skrip untuk tajuk {a.id}')")
    slug = v["slug"]
    for extra in ([], ["--16x9"]):
        subprocess.run([sys.executable, f"{ROOT}/siri/tools/build.py", *extra, slug], check=True)
    for d, other in ((slug, "elas-outro-16x9.html"), (slug + "-16x9", "elas-outro.html")):
        f = f"{ROOT}/siri/{d}/compositions/{other}"
        if os.path.exists(f):
            os.remove(f)
    if a.render:
        subprocess.run([f"{ROOT}/siri/tools/finish.sh", slug], check=True)
        print(f"renders: siri/renders/{slug}.mp4 and siri/renders/landscape/{slug}-16x9.mp4")
    db = load()
    for t in db["topics"]:
        if t["id"] == a.id and t["status"] in ("Idea", "Research", "Script", "Storyboard", "Production"):
            t["status"] = "Review" if a.render else "Production"; t["slug"] = slug
    save(db)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    x = sp.add_parser("topics"); x.add_argument("--cat"); x.add_argument("--status"); x.set_defaults(f=cmd_topics)
    x = sp.add_parser("add"); x.add_argument("title"); x.add_argument("--cat", required=True); x.set_defaults(f=cmd_add)
    x = sp.add_parser("status"); x.add_argument("id", type=int); x.add_argument("status"); x.add_argument("--slug"); x.set_defaults(f=cmd_status)
    x = sp.add_parser("calendar"); x.add_argument("--days", type=int, default=30); x.add_argument("--start"); x.set_defaults(f=cmd_calendar)
    x = sp.add_parser("perf"); x.add_argument("id", type=int); x.add_argument("metrics", nargs="+"); x.add_argument("--platform", default="all"); x.set_defaults(f=cmd_perf)
    x = sp.add_parser("report"); x.set_defaults(f=cmd_report)
    x = sp.add_parser("make"); x.add_argument("id", type=int); x.add_argument("--render", action="store_true"); x.set_defaults(f=cmd_make)
    a = p.parse_args(); a.f(a)


if __name__ == "__main__":
    main()
