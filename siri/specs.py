# Elas Barbershop tips series: one entry per video.
# Scene types: hook, point, rows, compare, tip, cta; business/story: shop, chart, split, morph, follow (tools/style_biz.py).
# Optional "tts" on a scene overrides the spoken text (e.g. to add <break> tags) while captions use "vo". Each scene has one voiceover line ("vo").
# Cue words ("cs", "cue") are words in the voiceover that trigger an on-screen element.

def hook(vo, lines, hl, icon, sub): return dict(t="hook", vo=vo, lines=lines, hl=hl, icon=icon, sub=sub)
def point(vo, title, sub, icon, cs=None): return dict(t="point", vo=vo, title=title, sub=sub, icon=icon, cs=cs)
def tip(vo, title, sub, icon="check", cs=None): return dict(t="tip", vo=vo, title=title, sub=sub, icon=icon, cs=cs)
def rows(vo, head, items): return dict(t="rows", vo=vo, head=head, items=items)
def row(icon, label, desc, cue): return dict(icon=icon, label=label, desc=desc, cue=cue)
def compare(vo, L, R): return dict(t="compare", vo=vo, L=L, R=R)
def side(label, icon, items, cue): return dict(label=label, icon=icon, items=items, cue=cue)
def cta(vo, ask, word, reply): return dict(t="cta", vo=vo, ask=ask, word=word, reply=reply)

A, B, C = "TIPS RAMBUT", "GAYA LELAKI", "REALITI BARBER"
BASE_TT = ["#elasbarbershop", "#fyp"]
BASE_IG = ["#elasbarbershop", "#barbershopmalaysia", "#reelsmalaysia"]

VIDEOS = [
 dict(slug="01-air-panas-sejuk", series=A, music="lofi",
  tags=["#tipsrambut", "#rambutsihat", "#penjagaanrambut", "#hairtipsmalaysia", "#lelakimalaysia"],
  scenes=[
   hook("Air panas atau air sejuk? Mana lebih baik untuk rambut anda?", ["AIR PANAS", "ATAU", "AIR SEJUK?"], [2], "shower", "Mana lebih baik untuk rambut?"),
   compare("Air panas memang selesa, tapi boleh buang minyak semula jadi dan buat kulit kepala kering. Air sejuk lebih lembut, tapi kurang berkesan tanggalkan minyak dan kotoran.",
     side("AIR PANAS", "steam", [("-", "Buang minyak semula jadi"), ("-", "Kulit kepala kering")], "panas"),
     side("AIR SEJUK", "snow", [("+", "Lebih lembut"), ("-", "Kurang tanggal minyak")], "sejuk")),
   tip("Jawapannya, guna air suam untuk syampu. Ia bersihkan tanpa buat kulit kepala terlalu kering.", ["GUNA", "AIR SUAM"], "Untuk syampu & cuci kulit kepala", "thermo", "bersihkan"),
   tip("Kemudian, bilas akhir dengan air sejuk. Ramai rasa rambut nampak lebih licin dan kemas.", ["BILAS AKHIR", "AIR SEJUK"], "Rambut nampak lebih licin & kemas", "drop", "ramai"),
   cta("Ada soalan pasal rambut? Komen RAMBUT, kami jawab.", ["Ada soalan", "pasal rambut?"], "RAMBUT", "Kami jawab!"),
  ]),
 dict(slug="02-kulit-kepala-berminyak", series=A, music="lofi",
  tags=["#kulitkepala", "#rambutberminyak", "#tipsrambut", "#hairtipsmalaysia", "#penjagaanrambut"],
  scenes=[
   hook("Kenapa kulit kepala cepat berminyak, walaupun baru cuci pagi tadi?", ["KENAPA KULIT", "KEPALA CEPAT", "BERMINYAK?"], [2], "oil", "Walaupun baru cuci pagi tadi"),
   point("Pertama, faktor semula jadi. Hormon dan genetik buat sesetengah orang memang lebih berminyak.", ["HORMON &", "GENETIK"], "Ada orang memang lebih berminyak", "dna", "hormon"),
   point("Kedua, cuaca panas dan peluh. Di Malaysia, ini memang biasa.", ["CUACA PANAS", "& PELUH"], "Biasa di cuaca Malaysia", "sun", "malaysia"),
   point("Ketiga, selalu sentuh rambut. Minyak dari tangan pindah ke rambut.", ["SELALU SENTUH", "RAMBUT"], "Minyak tangan pindah ke rambut", "hand", "minyak"),
   point("Keempat, produk berat yang tak dibilas sampai bersih.", ["PRODUK", "TAK DIBILAS"], "Pomade & gel berat tertinggal", "jar", "dibilas"),
   tip("Tipnya, guna syampu lembut, air suam, dan tukar sarung bantal selalu.", ["SYAMPU LEMBUT", "+ AIR SUAM"], "Dan tukar sarung bantal selalu", "check", "tukar"),
   cta("Nak tahu produk yang sesuai? Komen MINYAK, kami cadangkan.", ["Nak produk", "yang sesuai?"], "MINYAK", "Kami cadangkan!"),
  ]),
 dict(slug="03-stres-rambut-gugur", series=A, music="lofi",
  tags=["#rambutgugur", "#stres", "#tipsrambut", "#kesihatanrambut", "#hairtipsmalaysia"],
  scenes=[
   hook("Adakah tekanan hidup boleh menyebabkan rambut gugur?", ["STRES BOLEH", "BUAT RAMBUT", "GUGUR?"], [2], "stress", "Ini jawapannya"),
   point("Ya, boleh. Tekanan yang teruk boleh buat lebih banyak rambut masuk fasa rehat, kemudian gugur.", ["YA,", "BOLEH"], "Lebih banyak rambut masuk fasa rehat", "hairfall", "tekanan"),
   point("Biasanya, rambut mula gugur dua hingga tiga bulan selepas tempoh tertekan.", ["2–3 BULAN", "KEMUDIAN"], "Gugur selalunya datang lewat", "calendar", "bulan"),
   point("Berita baiknya, ia selalunya sementara, dan rambut boleh tumbuh semula.", ["SELALUNYA", "SEMENTARA"], "Rambut boleh tumbuh semula", "sprout", "tumbuh"),
   tip("Tidur cukup, makan seimbang, dan kalau gugur berterusan, jumpa doktor.", ["TIDUR CUKUP,", "MAKAN SEIMBANG"], "Gugur berterusan? Jumpa doktor.", "check", "berterusan"),
   cta("Pernah alami? Komen GUGUR, kami kongsi lebih banyak tips.", ["Pernah alami", "rambut gugur?"], "GUGUR", "Kami kongsi tips!"),
  ]),
 dict(slug="04-gaya-ikut-bentuk-muka", series=B, music="lofi",
  tags=["#gayarambut", "#bentukmuka", "#rambutlelaki", "#menshairstyle", "#haircutmalaysia"],
  scenes=[
   hook("Gaya rambut yang sama boleh nampak lain pada muka yang berbeza. Ini cara pilih.", ["PILIH GAYA", "IKUT BENTUK", "MUKA"], [2], "face-oval", "5 bentuk, 5 pilihan"),
   point("Muka bujur. Bertuah, hampir semua gaya sesuai.", ["MUKA", "BUJUR"], "Hampir semua gaya sesuai", "face-oval", "hampir"),
   point("Muka bulat. Pilih tepi pendek dan volume di atas, macam quiff atau fade.", ["MUKA", "BULAT"], "Tepi pendek, volume atas: quiff, fade", "face-round", "tepi"),
   point("Muka segi empat. Textured crop atau side part nampak kemas dan maskulin.", ["MUKA SEGI", "EMPAT"], "Textured crop, side part", "face-square", "textured"),
   point("Muka bentuk hati. Fringe atau rambut panjang sederhana, untuk imbangkan dahi yang luas.", ["MUKA BENTUK", "HATI"], "Fringe, panjang sederhana", "face-heart", "fringe"),
   point("Muka panjang. Elakkan terlalu tinggi di atas. Fringe dan tepi yang sedikit penuh lebih sesuai.", ["MUKA", "PANJANG"], "Elak terlalu tinggi; fringe lebih sesuai", "face-long", "elakkan"),
   cta("Tak pasti bentuk muka anda? Komen MUKA, kami bantu.", ["Tak pasti", "bentuk muka?"], "MUKA", "Kami bantu nilai!"),
  ]),
 dict(slug="05-gaya-nampak-muda", series=B, music="lofi",
  tags=["#gayarambut", "#rambutlelaki", "#menshairstyle", "#haircutmalaysia", "#nampakmuda"],
  scenes=[
   hook("Lima gaya rambut yang boleh buat lelaki nampak lebih muda dan segar.", ["5 GAYA", "NAMPAK LEBIH", "MUDA"], [2], "star", "Segar & kemas"),
   point("Satu, textured crop. Ringkas, bertekstur, dan senang urus.", ["TEXTURED", "CROP"], "Ringkas & senang urus", "cut-crop", "ringkas"),
   point("Dua, quiff. Volume di depan beri tenaga pada wajah.", ["QUIFF"], "Volume depan, wajah lebih bertenaga", "cut-quiff", "volume"),
   point("Tiga, side part dengan low fade. Kemas, sesuai untuk kerja.", ["SIDE PART +", "LOW FADE"], "Kemas untuk kerja", "cut-sidepart", "kemas"),
   point("Empat, crew cut. Pendek, bersih, dan sentiasa nampak terurus.", ["CREW", "CUT"], "Pendek & sentiasa terurus", "cut-crew", "pendek"),
   point("Lima, messy fringe. Santai dan muda, sesuai untuk dahi yang luas.", ["MESSY", "FRINGE"], "Santai, sesuai dahi luas", "cut-fringe", "santai"),
   cta("Yang mana sesuai untuk anda? Komen MUDA, kami cadangkan.", ["Nak cuba", "yang mana?"], "MUDA", "Kami cadangkan!"),
  ]),
 dict(slug="06-kenapa-tak-sama-gambar", series=B, music="lofi",
  tags=["#haircut", "#rambutlelaki", "#barberlife", "#haircutmalaysia", "#tipsrambut"],
  scenes=[
   hook("Bawa gambar ke barber, tapi hasilnya tak sama? Ini sebabnya.", ["KENAPA TAK", "SAMA MACAM", "GAMBAR?"], [2], "photo", "4 sebab utama"),
   point("Pertama, jenis rambut berbeza. Tebal, nipis, lurus atau kerinting, semuanya beri hasil lain.", ["JENIS RAMBUT", "BERBEZA"], "Tebal, nipis, lurus, kerinting", "hair-texture", "tebal"),
   point("Kedua, bentuk kepala dan muka tak sama dengan model dalam gambar.", ["BENTUK KEPALA", "LAIN"], "Tak sama dengan model", "face-oval", "model"),
   point("Ketiga, gambar dah di-styling, ada lampu cantik, kadang-kadang diedit.", ["GAMBAR DAH", "DI-STYLING"], "Lampu, produk, kadang diedit", "camera", "lampu"),
   point("Keempat, rambut anda mungkin belum cukup panjang untuk gaya itu.", ["PANJANG", "TAK CUKUP"], "Perlu tunggu rambut tumbuh", "ruler", "panjang"),
   tip("Tipnya, bawa gambar, dan tanya barber apa yang realistik untuk rambut anda.", ["TANYA APA YANG", "REALISTIK"], "Gambar + bincang = hasil lebih tepat", "chat", "tanya"),
   cta("Ada gambar gaya idaman? Komen GAMBAR, kami bantu nilai.", ["Ada gaya", "idaman?"], "GAMBAR", "Kami bantu nilai!"),
  ]),
 dict(slug="07-low-mid-high-fade", series=B, music="lofi",
  tags=["#fade", "#lowfade", "#midfade", "#highfade", "#haircutmalaysia", "#menshairstyle"],
  scenes=[
   hook("Low fade, mid fade, high fade. Apa bezanya?", ["LOW, MID", "ATAU HIGH", "FADE?"], [2], "clipper", "Bezanya pada ketinggian"),
   rows("Low fade bermula sedikit atas telinga, nampak halus dan profesional. Mid fade bermula di paras pelipis, lebih seimbang. High fade bermula tinggi, dekat bahagian atas kepala, nampak berani dan kontras.",
     "Fade bermula di mana?",
     [row("fade-low", "LOW FADE", "Sedikit atas telinga. Halus & profesional.", "low"),
      row("fade-mid", "MID FADE", "Paras pelipis. Seimbang.", "mid"),
      row("fade-high", "HIGH FADE", "Tinggi, dekat atas. Berani & kontras.", "high")]),
   tip("Pertama kali cuba? Mula dengan low atau mid fade dulu.", ["MULA DENGAN", "LOW / MID"], "Untuk kali pertama", "check", "mula"),
   cta("Anda geng fade yang mana? Komen low, mid atau high.", ["Anda geng", "fade mana?"], "MID", "Kami tunggu!"),
  ]),
 dict(slug="08-gaya-rambut-nipis", series=B, music="lofi",
  tags=["#rambutnipis", "#gayarambut", "#rambutlelaki", "#menshairstyle", "#haircutmalaysia"],
  scenes=[
   hook("Rambut nipis? Gaya yang betul boleh buat ia nampak lebih penuh.", ["RAMBUT", "NIPIS?"], [1], "hair-thin", "Gaya betul, nampak lebih penuh"),
   point("Satu, potong lebih pendek. Crew cut atau buzz cut buat rambut nampak lebih tebal.", ["POTONG LEBIH", "PENDEK"], "Crew cut, buzz cut", "cut-crew", "crew"),
   point("Dua, textured crop. Tekstur di atas sorok bahagian yang jarang.", ["TEXTURED", "CROP"], "Tekstur sorok bahagian jarang", "cut-crop", "tekstur"),
   point("Tiga, tepi pendek. Bila tepi rapat, bahagian atas nampak lebih penuh.", ["TEPI", "PENDEK"], "Atas nampak lebih penuh", "clipper", "bila"),
   point("Empat, guna produk matte, bukan gel berkilat yang buat rambut nampak melekat.", ["PRODUK", "MATTE"], "Elak gel berkilat", "jar", "bukan"),
   cta("Rambut anda nipis juga? Komen NIPIS, kami cadangkan gaya.", ["Rambut anda", "nipis juga?"], "NIPIS", "Kami cadangkan!"),
  ]),
 dict(slug="09-lima-kesilapan-lelaki", series=B, music="lofi",
  tags=["#grooming", "#penampilan", "#lelakimalaysia", "#mensgrooming", "#tipslelaki"],
  scenes=[
   hook("Lima kesilapan lelaki bila jaga penampilan. Anda buat yang mana?", ["5 KESILAPAN", "LELAKI"], [0], "cross", "Bila jaga penampilan"),
   point("Satu, tunggu terlalu lama untuk potong rambut.", ["TUNGGU", "TERLALU LAMA"], "Potongan hilang bentuk", "calendar", "potong"),
   point("Dua, janggut dan garisan leher tak dikemas.", ["JANGGUT", "TAK DIKEMAS"], "Garisan leher pun penting", "beard", "garisan"),
   point("Tiga, letak gel atau pomade terlalu banyak.", ["PRODUK", "TERLALU BANYAK"], "Sikit dah cukup", "jar", "terlalu"),
   point("Empat, abaikan kulit kepala dan kelemumur.", ["ABAIKAN", "KULIT KEPALA"], "Kelemumur jejas penampilan", "scalp", "kelemumur"),
   point("Lima, pilih gaya yang tak sesuai dengan bentuk muka.", ["GAYA TAK", "SESUAI MUKA"], "Pilih ikut bentuk muka", "face-oval", "bentuk"),
   cta("Anda pernah buat nombor berapa? Komen nombornya.", ["Anda pernah", "buat yang mana?"], "3", "Jom betulkan!"),
  ]),
 dict(slug="10-cantik-di-kedai", series=B, music="lofi",
  tags=["#stylingrambut", "#rambutlelaki", "#menshairstyle", "#tipsrambut", "#hairtipsmalaysia"],
  scenes=[
   hook("Kenapa rambut nampak cantik di kedai, tapi tak menjadi bila di rumah?", ["CANTIK DI", "KEDAI, TAPI", "DI RUMAH?"], [2], "mirror", "Ini sebabnya"),
   point("Pertama, barber guna blow dryer untuk bentuk rambut dari akar.", ["BLOW", "DRYER"], "Bentuk rambut dari akar", "hairdryer", "akar"),
   point("Kedua, produk dan jumlah yang betul.", ["PRODUK", "YANG BETUL"], "Jenis & jumlah", "jar", "jumlah"),
   point("Ketiga, teknik. Arah sikat dan cara letak produk.", ["TEKNIK", "STYLING"], "Arah sikat, cara letak produk", "comb", "arah"),
   tip("Tipnya, minta barber ajar cara styling. Tiga minit pun cukup.", ["MINTA BARBER", "AJAR"], "3 minit pun cukup", "chat", "tiga"),
   cta("Nak tips styling di rumah? Komen STYLING.", ["Nak tips", "styling?"], "STYLING", "Kami ajar!"),
  ]),
 dict(slug="11-berapa-kerap-potong", series=B, music="lofi",
  tags=["#haircut", "#rambutlelaki", "#grooming", "#haircutmalaysia", "#tipsrambut"],
  scenes=[
   hook("Berapa kerap lelaki perlu potong rambut?", ["BERAPA KERAP", "PERLU", "POTONG?"], [2], "calendar", "Bergantung pada gaya"),
   rows("Untuk fade dan rambut pendek, setiap dua hingga tiga minggu. Panjang sederhana, empat hingga enam minggu. Rambut panjang, enam hingga lapan minggu, untuk kemaskan hujung.",
     "Secara umum:",
     [row("fade-mid", "FADE / PENDEK", "Setiap 2–3 minggu", "fade"),
      row("cut-crop", "SEDERHANA", "Setiap 4–6 minggu", "sederhana"),
      row("cut-long", "PANJANG", "Setiap 6–8 minggu", "panjang")]),
   tip("Ada janggut? Kemaskan setiap satu hingga dua minggu.", ["JANGGUT:", "1–2 MINGGU"], "Supaya garisan kekal kemas", "beard", "kemaskan"),
   cta("Bila kali terakhir anda potong? Komen POTONG.", ["Bila kali", "terakhir potong?"], "POTONG", "Jom tempah slot!"),
  ]),
 dict(slug="12-janggut-ikut-muka", series=B, music="lofi",
  tags=["#janggut", "#beardstyle", "#grooming", "#mensgrooming", "#lelakimalaysia"],
  scenes=[
   hook("Janggut yang sesuai boleh ubah bentuk wajah anda. Ini panduannya.", ["JANGGUT", "IKUT BENTUK", "MUKA"], [0], "beard", "Panduan ringkas"),
   point("Muka bulat. Janggut lebih panjang di dagu, tepi pendek, supaya nampak lebih panjang.", ["MUKA", "BULAT"], "Panjang di dagu, tepi pendek", "face-round-b", "tepi"),
   point("Muka segi empat. Janggut penuh dengan hujung dibulatkan, untuk lembutkan rahang.", ["MUKA SEGI", "EMPAT"], "Penuh, hujung dibulatkan", "face-square-b", "hujung"),
   point("Muka panjang. Tepi lebih penuh, dagu lebih pendek.", ["MUKA", "PANJANG"], "Tepi penuh, dagu pendek", "face-long-b", "tepi"),
   point("Muka bentuk hati. Janggut penuh di dagu, untuk imbangkan dagu yang runcing.", ["MUKA BENTUK", "HATI"], "Penuh di dagu", "face-heart-b", "janggut"),
   cta("Nak bentuk janggut yang sesuai? Komen JANGGUT.", ["Nak janggut", "yang kemas?"], "JANGGUT", "Kami bantu!"),
  ]),
 dict(slug="13-rambut-dan-keyakinan", series=B, music="lofi",
  tags=["#keyakinandiri", "#gayarambut", "#grooming", "#lelakimalaysia", "#motivasi"],
  scenes=[
   hook("Potongan rambut boleh ubah keyakinan diri. Kenapa?", ["RAMBUT &", "KEYAKINAN", "DIRI"], [1], "confident", "Kenapa ia berkait?"),
   point("Pertama, bila nampak kemas, ramai rasa lebih yakin, dan ia nampak pada postur dan senyuman.", ["NAMPAK KEMAS,", "RASA YAKIN"], "Nampak pada postur & senyuman", "mirror", "postur"),
   point("Kedua, tanggapan pertama. Rambut antara benda pertama yang orang perasan.", ["TANGGAPAN", "PERTAMA"], "Antara yang orang perasan dulu", "person", "rambut"),
   point("Ketiga, gaya yang sesuai kurang leceh. Anda tak perlu risau tentang rambut sepanjang hari.", ["KURANG", "RISAU"], "Gaya sesuai, kurang leceh", "clock", "risau"),
   cta("Anda rasa paling yakin bila? Komen YAKIN.", ["Bila anda", "paling yakin?"], "YAKIN", "Lepas potong, kan?"),
  ]),
 dict(slug="14-apa-barber-nak-anda-tahu", series=C, music="trap",
  tags=["#barberlife", "#barbermalaysia", "#realitibarber", "#haircut", "#barbershop"],
  scenes=[
   hook("Lima perkara yang barber nak sangat pelanggan tahu.", ["APA BARBER", "NAK ANDA", "TAHU"], [2], "scissors", "5 perkara"),
   point("Satu, bawa gambar. Ia lebih jelas daripada penerangan panjang.", ["BAWA", "GAMBAR"], "Lebih jelas dari penerangan", "photo", "jelas"),
   point("Dua, beritahu rutin anda. Guna produk atau tak, dan berapa kerap styling.", ["BERITAHU", "RUTIN ANDA"], "Produk, styling, kerja", "chat", "produk"),
   point("Tiga, datang tepat pada masa temujanji.", ["DATANG", "TEPAT MASA"], "Supaya tak kejar masa", "clock", "temujanji"),
   point("Empat, cakap awal kalau nak ubah sesuatu. Lebih awal, lebih mudah.", ["CAKAP", "AWAL-AWAL"], "Lebih awal, lebih mudah ubah", "mirror", "lebih"),
   point("Lima, kalau tak puas hati, beritahu. Barber yang baik nak betulkan.", ["TAK PUAS HATI?", "BERITAHU"], "Barber yang baik nak betulkan", "thumb", "barber"),
   cta("Ada soalan untuk barber? Komen BARBER, kami jawab.", ["Ada soalan", "untuk barber?"], "BARBER", "Kami jawab!"),
  ]),
 dict(slug="15-potong-sikit-sahaja", series=C, music="trap",
  tags=["#barberlife", "#potongsikit", "#barbermalaysia", "#haircut", "#lawak"],
  scenes=[
   hook("Pelanggan cakap, potong sikit sahaja ya. Barber pula tertanya, sikit tu berapa?", ['"POTONG SIKIT', 'SAHAJA."'], [1], "scissors", "Sikit tu berapa?"),
   point("Masalahnya, sikit bagi setiap orang tak sama. Ada yang maksudkan satu sentimeter, ada yang lima.", ['"SIKIT"', "TAK SAMA"], "1 cm? 5 cm?", "ruler", "sentimeter"),
   point("Jadi, tunjuk dengan jari berapa panjang nak buang.", ["TUNJUK", "DENGAN JARI"], "Berapa panjang nak buang", "hand", "berapa"),
   point("Atau sebut nombor clipper untuk bahagian tepi.", ["SEBUT NOMBOR", "CLIPPER"], "Contoh: nombor 2 di tepi", "clipper", "bahagian"),
   point("Paling senang, tunjuk gambar rambut masa baru potong dulu.", ["TUNJUK", "GAMBAR LAMA"], "Masa baru potong dulu", "photo", "gambar"),
   cta("Pernah cakap potong sikit je? Komen SIKIT.", ["Pernah cakap", "potong sikit?"], "SIKIT", "Kami faham!"),
  ]),
 dict(slug="16-kenapa-potong-lama", series=C, music="trap",
  tags=["#barberlife", "#fade", "#barbermalaysia", "#haircut", "#detail"],
  scenes=[
   hook("Kenapa barber ambil masa lama untuk satu potongan?", ["KENAPA", "POTONG", "LAMA SANGAT?"], [2], "clock", "Ini yang berlaku"),
   point("Pertama, konsultasi. Faham apa yang anda nak sebelum mula.", ["KONSULTASI"], "Faham kehendak anda dulu", "chat", "faham"),
   point("Kedua, blending fade perlukan banyak lapisan supaya licin tanpa garisan.", ["BLENDING", "FADE"], "Licin tanpa garisan", "clipper", "licin"),
   point("Ketiga, semak kiri dan kanan supaya simetri.", ["KIRI-KANAN", "SIMETRI"], "Semak berulang kali", "mirror", "simetri"),
   point("Keempat, detail. Garisan, leher, dan styling akhir.", ["DETAIL", "AKHIR"], "Garisan, leher, styling", "razor", "garisan"),
   cta("Anda lebih suka cepat atau kemas? Komen jawapan anda.", ["Cepat atau", "kemas?"], "KEMAS", "Kami setuju!"),
  ]),
 dict(slug="17-lima-jenis-pelanggan", series=C, music="trap",
  tags=["#barberlife", "#lawak", "#barbermalaysia", "#pelanggan", "#barbershop"],
  scenes=[
   hook("Lima jenis pelanggan di barbershop. Anda yang mana?", ["5 JENIS", "PELANGGAN"], [0], "person", "Anda yang mana?"),
   point("Satu, si ikut suka abang. Percaya penuh pada barber.", ['"IKUT SUKA', 'ABANG"'], "Percaya penuh", "thumb", "percaya"),
   point("Dua, si bawa sepuluh gambar, semua gaya lain-lain.", ["SI 10", "GAMBAR"], "Semua gaya lain-lain", "photo", "semua"),
   point("Tiga, si tidur. Duduk sahaja, terus lena.", ["SI", "TIDUR"], "Duduk, terus lena", "sleep", "duduk"),
   point("Empat, si bercerita. Sesi potong jadi sesi luahan.", ["SI", "BERCERITA"], "Sesi potong, sesi luahan", "talk", "sesi"),
   point("Lima, si potong sikit je. Kita dah tahu ceritanya.", ['SI "SIKIT', 'JE"'], "Kita dah tahu ceritanya", "scissors", "kita"),
   cta("Anda yang mana? Komen nombornya.", ["Anda", "yang mana?"], "2", "Haha, kami tahu!"),
  ]),
 dict(slug="18-kenapa-harga-naik", series=C, music="trap",
  tags=["#barberlife", "#barbermalaysia", "#hargagunting", "#barbershop", "#realitibarber"],
  scenes=[
   hook("Kenapa harga gunting rambut semakin naik?", ["KENAPA HARGA", "GUNTING", "NAIK?"], [2], "tag", "Kos di sebalik tabir"),
   point("Pertama, sewa kedai dan bil elektrik terus meningkat.", ["SEWA &", "BIL"], "Terus meningkat", "shop", "bil"),
   point("Kedua, alatan berkualiti. Clipper, blade, dan alat sterilisasi.", ["ALATAN", "BERKUALITI"], "Clipper, blade, sterilisasi", "clipper", "clipper"),
   point("Ketiga, produk penjagaan dan kebersihan yang lebih baik.", ["PRODUK &", "KEBERSIHAN"], "Untuk keselesaan anda", "spray", "kebersihan"),
   point("Keempat, kemahiran. Latihan dan pengalaman ambil masa bertahun.", ["KEMAHIRAN", "& LATIHAN"], "Bertahun-tahun belajar", "trophy", "latihan"),
   cta("Bagi anda, apa paling penting? Komen jawapan anda.", ["Apa paling", "penting?"], "KUALITI", "Kami setuju!"),
  ]),
 dict(slug="19-sebelum-pelanggan-datang", series=C, music="trap",
  tags=["#barberlife", "#behindthescenes", "#barbermalaysia", "#barbershop", "#kebersihan"],
  scenes=[
   hook("Apa yang berlaku di barbershop sebelum pelanggan pertama datang?", ["SEBELUM", "PELANGGAN", "DATANG"], [1], "shop", "Di sebalik tabir"),
   point("Mula-mula, kedai dibersihkan dan disusun.", ["BERSIH &", "SUSUN"], "Lantai, kerusi, cermin", "broom", "disusun"),
   point("Kemudian, semua alat dicuci dan disterilkan.", ["STERILKAN", "ALAT"], "Setiap alat, setiap hari", "spray", "disterilkan"),
   point("Clipper diminyakkan, dan blade diperiksa supaya tajam.", ["MINYAK &", "SEMAK BLADE"], "Supaya potongan licin", "clipper", "blade"),
   point("Akhir sekali, semak senarai temujanji hari itu.", ["SEMAK", "TEMUJANJI"], "Supaya semua tepat masa", "calendar", "temujanji"),
   cta("Nak tempah slot? Komen TEMPAH.", ["Nak tempah", "slot?"], "TEMPAH", "Kami bersedia!"),
  ]),
 dict(slug="20-barber-lama-vs-baru", series=C, music="trap",
  tags=["#barberlife", "#barbermalaysia", "#pengalaman", "#barbershop", "#realitibarber"],
  scenes=[
   hook("Barber berpengalaman dan barber baharu. Apa bezanya?", ["BARBER LAMA", "VS", "BARBER BARU"], [1], "scissors", "Semua bermula dari baharu"),
   compare("Barber baharu biasanya ambil masa lebih lama, dan masih membina teknik. Barber berpengalaman lebih pantas, blending lebih licin, dan konsisten.",
     side("BAHARU", "sprout", [("o", "Masa lebih lama"), ("o", "Masih bina teknik")], "baharu"),
     side("PENGALAMAN", "trophy", [("+", "Lebih pantas"), ("+", "Blending licin"), ("+", "Konsisten")], "berpengalaman")),
   tip("Barber berpengalaman juga pandai baca rambut, dan beri nasihat styling.", ["BACA RAMBUT", "& NASIHAT"], "Bukan sekadar potong", "chat", "nasihat"),
   tip("Tapi ingat, setiap barber hebat pernah jadi barber baharu. Beri mereka peluang.", ["SEMUA PERNAH", "JADI BAHARU"], "Beri mereka peluang", "sprout", "beri"),
   cta("Ada barber kegemaran? Komen dan tag mereka.", ["Barber", "kegemaran anda?"], "BARBER", "Tag mereka!"),
  ]),
]


# ---------------------------------------------------------------- Di Sebalik Kerusi Barber (studio/)
def shop(vo, lines, hl): return dict(t="shop", vo=vo, lines=lines, hl=hl)
def chart(vo, title, tts=None): return dict(t="chart", vo=vo, title=title, **({"tts": tts} if tts else {}))
def split(vo, title, costs): return dict(t="split", vo=vo, title=title, costs=costs)
def morph(vo, title, sub, tts=None): return dict(t="morph", vo=vo, title=title, sub=sub, **({"tts": tts} if tts else {}))
def follow(vo, ask, cardsub="Ilmu & rahsia industri barber"): return dict(t="follow", vo=vo, ask=ask, cardsub=cardsub)

DSKB = "DI SEBALIK KERUSI BARBER"
VIDEOS.append(dict(
 slug="21-kedai-penuh-tapi-rugi", series=DSKB, music="lofi", topic_id=31,
 handle="@elasbarbershop.official", tagline="Lebih daripada sekadar gunting rambut.",
 tags=["#bisnesbarber", "#usahawanmalaysia", "#barbershopmalaysia", "#tipsbisnes", "#lelakimalaysia"],
 scenes=[
  shop("Pernah tak anda tengok kedai gunting rambut sentiasa penuh dengan pelanggan, tetapi akhirnya terpaksa tutup?",
       ["PENUH PELANGGAN,", "TAPI RUGI?"], [1]),
  chart("Ramai orang menyangka jualan yang tinggi bermaksud keuntungan yang tinggi. Hakikatnya, dua perkara ini sangat berbeza.",
        ["JUALAN TINGGI", "≠ UNTUNG TINGGI"],
        tts='Ramai orang menyangka jualan yang tinggi bermaksud keuntungan yang tinggi. <break time="0.5s" /> Hakikatnya, dua perkara ini sangat berbeza.'),
  split("Setiap ringgit yang diterima perlu menampung gaji pekerja, sewa kedai, bil elektrik, peralatan, produk dan kos operasi. Jika kos tidak dikawal, semakin banyak pelanggan belum tentu semakin banyak keuntungan.",
        ["KE MANA PERGI", "WANG JUALAN?"],
        [("Gaji pekerja", 40), ("Sewa kedai", 15), ("Bil elektrik", 6), ("Peralatan", 8), ("Produk", 12), ("Kos operasi", 9)]),
  morph("Untuk berjaya dalam industri barber, anda bukan sahaja perlu pandai menggunting rambut. Anda juga perlu pandai menguruskan perniagaan.",
        ["PANDAI GUNTING", "+ PANDAI URUS"], "Urus kewangan, pekerja & kos",
        tts='Untuk berjaya dalam industri barber, anda bukan sahaja perlu pandai menggunting rambut. <break time="0.5s" /> Anda juga perlu pandai menguruskan perniagaan.'),
  follow("Ikuti kami untuk lebih banyak ilmu dan rahsia industri barber.", ["Ikuti kami untuk", "ilmu & rahsia", "industri barber"]),
 ],
 caption="""# Caption — 21-kedai-penuh-tapi-rugi (Di Sebalik Kerusi Barber #1)

## TikTok

Kedai gunting penuh pelanggan, tapi kenapa masih rugi? 🤔
Tengok sampai habis 👇

Pernah nampak kedai macam ni? Komen "BISNES" ✂️

#bisnesbarber #usahawanmalaysia #tipsbisnes #elasbarbershop #fyp #barbershopmalaysia

## Instagram

Kedai gunting penuh pelanggan, tapi kenapa masih rugi? 👇

✂️ Jualan tinggi tak semestinya untung tinggi
✨ Setiap ringgit kena tampung gaji, sewa, bil elektrik, peralatan, produk & kos operasi
⏳ Kos tak dikawal = lebih ramai pelanggan belum tentu lebih untung

Kesimpulannya: pandai gunting saja tak cukup, kena pandai urus bisnes juga.

Ada soalan pasal bisnes barber? Komen "BISNES" atau DM kami 📩
Ikuti @elasbarbershop.official untuk siri Di Sebalik Kerusi Barber.

*Angka dalam video ialah contoh ilustrasi, bukan angka sebenar Ela's Barbershop.

#bisnesbarber #usahawanmalaysia #tipsbisnes #barbershopmalaysia #barbermalaysia #bisneskecil #pengurusankewangan #usahawanmuda #lelakimalaysia #barberlife #reelsmalaysia #elasbarbershop
""",
))

VIDEOS += [
 dict(slug="22-tiang-barber", series="RAHSIA DUNIA BARBER", music="lofi", topic_id=41,
  handle="@elasbarbershop.official", tagline="Lebih daripada sekadar gunting rambut.",
  tags=["#sejarahbarber", "#tiangbarber", "#faktamenarik", "#barbershopmalaysia", "#lelakimalaysia"],
  scenes=[
   hook("Kenapa tiang barber berwarna merah, putih dan biru? Jawapannya lebih ngeri daripada yang anda sangka.",
        ["KENAPA TIANG", "BARBER MERAH,", "PUTIH & BIRU?"], [2], "pole", "Jawapannya agak ngeri"),
   point("Pada zaman pertengahan di Eropah, barber bukan sahaja menggunting rambut. Mereka juga mencabut gigi dan melakukan bekam darah.",
         ["BARBER", "ZAMAN DAHULU"], "Gunting, cabut gigi & bekam darah", "razor", "mencabut"),
   point("Warna merah melambangkan darah daripada rawatan tersebut.", ["MERAH", "= DARAH"], "Daripada rawatan bekam", "drop", "darah"),
   point("Warna putih pula melambangkan kain pembalut. Kain yang sudah dibasuh dijemur pada tiang di luar kedai, lalu berpusing ditiup angin.",
         ["PUTIH", "= PEMBALUT"], "Kain dijemur pada tiang di luar kedai", "bandage", "pembalut"),
   point("Biru pula dipercayai ditambah di Amerika Syarikat, mengikut warna bendera negara itu.", ["BIRU", "= AMERIKA?"], "Dipercayai ikut warna bendera AS", "flag", "amerika"),
   tip("Hari ini, barber tidak lagi melakukan rawatan begitu. Tiang itu kekal sebagai simbol kedai gunting rambut di seluruh dunia.",
       ["KINI CUMA", "SIMBOL"], "Tanda kedai gunting di seluruh dunia", "pole", "simbol"),
   follow("Ikuti kami untuk lebih banyak fakta menarik dunia barber.", ["Ikuti kami untuk", "fakta menarik", "dunia barber"], "Fakta & sejarah dunia barber"),
  ],
  caption="""# Caption — 22-tiang-barber (Di Sebalik Kerusi Barber: Rahsia Dunia Barber)

## TikTok

Kenapa tiang barber merah, putih & biru? 💈
Tengok sampai habis 👇

Tahu fakta ni sebelum ni? Komen "TIANG" ✂️

#sejarahbarber #tiangbarber #faktamenarik #elasbarbershop #fyp #barbershopmalaysia

## Instagram

Kenapa tiang barber berwarna merah, putih & biru? 💈👇

✂️ Barber zaman pertengahan di Eropah juga mencabut gigi & melakukan bekam darah
✨ Merah = darah, putih = kain pembalut yang dijemur pada tiang
⏳ Biru dipercayai ditambah di Amerika Syarikat, ikut warna bendera

Hari ini, tiang itu kekal sebagai simbol kedai gunting rambut di seluruh dunia.

Tahu fakta ni sebelum ni? Komen "TIANG" atau DM kami 📩
Ikuti @elasbarbershop.official untuk siri Di Sebalik Kerusi Barber.

#sejarahbarber #tiangbarber #faktamenarik #barberpole #barbershopmalaysia #barbermalaysia #sejarah #tahukahanda #lelakimalaysia #reelsmalaysia #elasbarbershop
"""),
 dict(slug="23-pomade-vs-wax", series="SEMINIT ILMU BARBER", music="lofi", topic_id=51,
  handle="@elasbarbershop.official", tagline="Lebih daripada sekadar gunting rambut.",
  tags=["#pomade", "#hairwax", "#produkrambut", "#rambutlelaki", "#menshairstyle"],
  scenes=[
   hook("Pomade atau wax? Ramai lelaki tersalah pilih, sebab itu gaya rambut tak menjadi.",
        ["POMADE", "ATAU", "WAX?"], [2], "jar", "Ramai tersalah pilih"),
   compare("Pomade memberi rambut nampak berkilat dan licin, sesuai untuk gaya kemas seperti slick back dan side part. Wax pula memberi hasil matte dan bertekstur, sesuai untuk gaya santai seperti textured crop.",
     side("POMADE", "jar", [("+", "Berkilat & licin"), ("+", "Slick back, side part")], "pomade"),
     side("WAX", "hair-texture", [("+", "Matte & bertekstur"), ("+", "Textured crop, santai")], "wax")),
   point("Satu lagi beza. Pomade berasaskan air lebih mudah dibilas. Wax pula biasanya boleh dibentuk semula sepanjang hari.",
         ["BILAS &", "BENTUK SEMULA"], "Senang bilas vs boleh restyle", "drop", "berasaskan"),
   tip("Jadi, pilih ikut gaya yang anda mahu. Nak kemas dan berkilat, pilih pomade. Nak natural dan bertekstur, pilih wax.",
       ["PILIH IKUT", "GAYA ANDA"], "Kemas: pomade. Natural: wax.", "check", "pilih"),
   tip("Dan ingat, mula dengan sedikit sahaja. Terlalu banyak produk buat rambut nampak berat dan berminyak.",
       ["MULA DENGAN", "SEDIKIT"], "Terlalu banyak = berat & berminyak", "hand", "sedikit"),
   cta("Anda geng pomade atau wax? Komen di bawah.", ["Geng pomade", "atau wax?"], "WAX", "Kongsi pilihan anda!"),
  ],
  caption="""# Caption — 23-pomade-vs-wax (Di Sebalik Kerusi Barber: Seminit Ilmu Barber)

## TikTok

Pomade atau wax? Ramai tersalah pilih 😅
Tengok sampai habis 👇

Anda geng mana? Komen "POMADE" atau "WAX" ✂️

#pomade #hairwax #produkrambut #elasbarbershop #fyp #haircutmalaysia

## Instagram

Pomade atau wax? Ramai lelaki tersalah pilih 👇

✂️ Pomade: berkilat & licin, sesuai slick back dan side part
✨ Wax: matte & bertekstur, sesuai textured crop dan gaya santai
⏳ Pomade berasaskan air lebih mudah dibilas; wax biasanya boleh dibentuk semula sepanjang hari

Kesimpulannya: pilih ikut gaya yang anda mahu, dan mula dengan sedikit sahaja.

Anda geng pomade atau wax? Komen di bawah atau DM kami 📩

#pomade #hairwax #produkrambut #rambutlelaki #menshairstyle #gayarambut #tipsrambut #haircutmalaysia #hairtipsmalaysia #barbershopmalaysia #reelsmalaysia #elasbarbershop
"""),
 dict(slug="24-barber-bukan-sekadar", series="BARBER BUKAN BIASA", music="lofi", topic_id=61,
  handle="@elasbarbershop.official", tagline="Lebih daripada sekadar gunting rambut.",
  tags=["#barberlife", "#kerjayabarber", "#motivasi", "#barbershopmalaysia", "#lelakimalaysia"],
  scenes=[
   hook("Ramai orang fikir barber cuma tukang gunting rambut. Hakikatnya, kerja seorang barber jauh lebih besar.",
        ["BARBER CUMA", "TUKANG", "GUNTING?"], [2], "confident", "Hakikatnya, jauh lebih besar"),
   point("Pertama, barber ialah artis. Setiap potongan perlukan mata yang tajam, teknik dan latihan bertahun-tahun.",
         ["SEORANG", "ARTIS"], "Mata tajam, teknik & latihan", "scissors", "artis"),
   point("Kedua, barber ialah pendengar. Ramai pelanggan berkongsi cerita hidup mereka di kerusi ini.",
         ["SEORANG", "PENDENGAR"], "Tempat pelanggan berkongsi cerita", "talk", "pendengar"),
   point("Ketiga, barber membina keyakinan. Bila rambut kemas, cara seseorang berjalan pun berubah.",
         ["PEMBINA", "KEYAKINAN"], "Rambut kemas, lebih yakin", "person", "keyakinan"),
   point("Keempat, ramai barber juga pendidik dan usahawan. Mereka melatih barber baharu dan menguruskan perniagaan sendiri.",
         ["PENDIDIK &", "USAHAWAN"], "Melatih barber & urus bisnes", "book", "pendidik"),
   tip("Jadi, lain kali anda duduk di kerusi barber, ingat, anda sedang berjumpa seorang profesional.",
       ["HORMATI", "PROFESION INI"], "Barber ialah seorang profesional", "check", "profesional"),
   follow("Ikuti kami untuk lebih banyak cerita di sebalik kerusi barber.", ["Ikuti kami untuk", "cerita di sebalik", "kerusi barber"], "Cerita & inspirasi dunia barber"),
  ],
  caption="""# Caption — 24-barber-bukan-sekadar (Di Sebalik Kerusi Barber: Barber Bukan Biasa)

## TikTok

Barber cuma tukang gunting? Fikir semula 💈
Tengok sampai habis 👇

Tag barber kegemaran anda & komen "BARBER" ✂️

#barberlife #kerjayabarber #motivasi #elasbarbershop #fyp #barbershopmalaysia

## Instagram

Ramai fikir barber cuma tukang gunting rambut. Hakikatnya, jauh lebih besar 👇

✂️ Artis: mata tajam, teknik & latihan bertahun-tahun
✨ Pendengar: tempat pelanggan berkongsi cerita
⏳ Pembina keyakinan: rambut kemas, lebih yakin
💡 Pendidik & usahawan: melatih barber baharu & urus bisnes

Lain kali anda duduk di kerusi barber, ingat: anda sedang berjumpa seorang profesional.

Tag barber kegemaran anda atau DM kami untuk tempah slot 📩
Ikuti @elasbarbershop.official untuk siri Di Sebalik Kerusi Barber.

#barberlife #kerjayabarber #motivasi #barbermalaysia #barbershopmalaysia #profesionbarber #inspirasi #usahawanmalaysia #lelakimalaysia #reelsmalaysia #elasbarbershop
"""),
]
