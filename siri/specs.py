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
def split(vo, title, costs, **kw): return dict(t="split", vo=vo, title=title, costs=costs, **kw)
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

# ---------------------------------------------------------------- 30-day calendar batch (3–24 Dec 2026)
E_, F_, G_, D_ = "RAHSIA DUNIA BARBER", "SEMINIT ILMU BARBER", "BARBER BUKAN BIASA", "BISNES DI SEBALIK GUNTING"
def V(slug, series, topic, tags, scenes, music="lofi", **kw):
    return dict(slug=slug, series=series, music=music, topic_id=topic, tags=tags, scenes=scenes, **kw)

def tts(scene, text):
    scene["tts"] = text; return scene

VIDEOS += [
 V("25-barber-pembedahan", E_, 42, ["#sejarahbarber", "#faktamenarik", "#barbersurgeon", "#tahukahanda", "#lelakimalaysia"], [
   hook("Tahukah anda, suatu masa dahulu barber juga melakukan pembedahan?", ["BARBER JUGA", "BUAT", "PEMBEDAHAN?"], [2], "razor", "Kisah benar zaman dahulu"),
   point("Di Eropah zaman pertengahan, barber bukan sahaja menggunting rambut. Mereka juga mencabut gigi, merawat luka dan melakukan bekam darah.",
         ["BARBER-", "SURGEON"], "Cabut gigi, rawat luka, bekam", "bandage", "mencabut"),
   point("Kenapa barber? Kerana mereka mahir menggunakan pisau tajam, dan doktor pada masa itu sedikit dan mahal.",
         ["KENAPA", "BARBER?"], "Mahir pisau, doktor pula mahal", "scissors", "mahir"),
   tts(point("Di England, pada tahun 1540, barber dan pakar bedah disatukan dalam satu persatuan rasmi.",
         ["TAHUN", "1540"], "Barber & pakar bedah, satu persatuan", "book", "england"),
       "Di England, pada tahun seribu lima ratus empat puluh, barber dan pakar bedah disatukan dalam satu persatuan rasmi."),
   tts(point("Hanya pada tahun 1745, pakar bedah berpisah dan membentuk persatuan mereka sendiri.",
         ["BERPISAH", "TAHUN 1745"], "Pakar bedah bawa haluan sendiri", "calendar", "berpisah"),
       "Hanya pada tahun seribu tujuh ratus empat puluh lima, pakar bedah berpisah dan membentuk persatuan mereka sendiri."),
   tip("Hari ini, barber fokus pada rambut dan janggut. Tetapi warisan itu masih ada pada tiang barber merah dan putih.",
       ["WARISAN", "MASIH ADA"], "Lihat pada tiang barber", "pole", "warisan"),
   cta("Nak lagi fakta macam ni? Komen FAKTA.", ["Nak lagi", "fakta menarik?"], "FAKTA", "Kami kongsi lagi!"),
 ]),
 V("26-styling-powder", F_, 52, ["#stylingpowder", "#produkrambut", "#rambutnipis", "#rambutlelaki", "#menshairstyle"], [
   hook("Rambut nampak leper walaupun dah guna produk? Mungkin anda perlukan hair styling powder.", ["RAMBUT", "NAMPAK", "LEPER?"], [2], "powder", "Cuba hair styling powder"),
   point("Hair styling powder ialah serbuk ringan yang memberi volume dan tekstur, terutamanya di bahagian akar rambut.",
         ["VOLUME DI", "AKAR RAMBUT"], "Serbuk ringan, rambut lebih naik", "powder", "volume"),
   point("Hasilnya matte, tidak berkilat, dan rambut tidak terasa berat.", ["MATTE &", "RINGAN"], "Tak berkilat, tak berat", "hair-texture", "matte"),
   point("Ia sangat sesuai untuk rambut nipis atau halus yang susah naik.", ["SESUAI RAMBUT", "NIPIS"], "Rambut halus yang susah naik", "hair-thin", "nipis"),
   tip("Cara guna, tabur sedikit pada akar rambut yang kering, kemudian urut dengan hujung jari dan bentukkan.",
       ["TABUR DI AKAR,", "URUT & BENTUK"], "Pada rambut yang kering", "hand", "tabur"),
   tip("Ingat, sedikit pun dah cukup. Terlalu banyak boleh buat rambut rasa kesat.", ["SEDIKIT", "DAH CUKUP"], "Terlalu banyak = kesat", "check", "sedikit"),
   cta("Pernah cuba styling powder? Komen POWDER.", ["Pernah cuba", "styling powder?"], "POWDER", "Kongsi pengalaman!"),
 ]),
 V("27-barber-jutawan", G_, 62, ["#kerjayabarber", "#usahawanmalaysia", "#motivasi", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Bolehkah seorang barber menjadi jutawan? Boleh, tetapi bukan dengan menggunting rambut sahaja.", ["BARBER JADI", "JUTAWAN?"], [1], "coin", "Boleh, tapi bukan dengan gunting sahaja"),
   point("Satu kerusi ada had. Masa anda terhad, jadi pendapatan daripada menggunting sahaja juga terhad.",
         ["SATU KERUSI", "ADA HAD"], "Masa terhad, pendapatan terhad", "clock", "kerusi"),
   point("Ramai yang berkembang dengan membuka lebih banyak cawangan dan membina pasukan.", ["CAWANGAN &", "PASUKAN"], "Bina sistem, bukan kerja seorang", "shop", "cawangan"),
   point("Ada juga yang mengajar, membuka akademi, atau melancarkan produk sendiri.", ["AKADEMI &", "PRODUK"], "Ilmu & jenama jadi sumber baharu", "book", "mengajar"),
   point("Semua ini memerlukan ilmu kewangan, disiplin, dan masa bertahun-tahun.", ["ILMU, DISIPLIN", "& MASA"], "Tiada jalan pintas", "calendar", "disiplin"),
   tip("Jadi, kemahiran gunting ialah permulaan. Perniagaan yang membawa anda lebih jauh.", ["GUNTING ITU", "PERMULAAN"], "Bisnes bawa anda lebih jauh", "trophy", "permulaan"),
   cta("Apa impian anda dalam industri barber? Komen IMPIAN.", ["Apa impian", "anda?"], "IMPIAN", "Kami nak dengar!"),
 ], music="trap", footnote="*Tiada jaminan pendapatan. Kejayaan bergantung pada usaha dan keadaan masing-masing."),
 V("28-untung-satu-potongan", D_, 32, ["#bisnesbarber", "#usahawanmalaysia", "#tipsbisnes", "#barbershopmalaysia", "#lelakimalaysia"], [
   hook("Berapa sebenarnya untung kedai daripada satu potongan rambut? Jawapannya mungkin mengejutkan anda.", ["BERAPA UNTUNG", "SATU", "POTONGAN?"], [2], "coin", "Jawapannya mungkin mengejutkan"),
   split("Katakan satu potongan berharga dua puluh lima ringgit. Hampir separuh pergi kepada gaji atau komisen barber. Kemudian sewa dan bil, produk dan alatan, dan kos lain seperti pemasaran. Bakinya, keuntungan mungkin cuma beberapa ringgit.",
         ["KE MANA PERGI", "RM25 ANDA?"], [("Gaji / komisen", 12), ("Sewa & bil", 5), ("Produk & alat", 3), ("Kos lain", 2)],
         base=25, lead_text="Daripada satu potongan RM25, baki untuk kedai:"),
   tip("Sebab itu, kedai perlu ramai pelanggan tetap, dan kawalan kos yang ketat, untuk terus untung.", ["PELANGGAN TETAP", "+ KAWAL KOS"], "Kunci untung yang stabil", "check", "pelanggan"),
   cta("Terkejut dengan angka ni? Komen UNTUNG.", ["Terkejut dengan", "angka ni?"], "UNTUNG", "Kami kongsi lagi!"),
 ], footnote="*Angka dalam video ialah contoh ilustrasi, bukan angka sebenar Ela's Barbershop."),
 V("29-sejarah-barber", E_, 43, ["#sejarahbarber", "#faktamenarik", "#barberlife", "#tahukahanda", "#lelakimalaysia"], [
   hook("Pekerjaan barber antara yang tertua di dunia. Jom lihat sejarahnya.", ["ANTARA KERJA", "TERTUA", "DI DUNIA"], [1], "razor", "Sejarah ribuan tahun"),
   point("Di Mesir purba, barber sudah wujud ribuan tahun dahulu, mencukur dengan pisau daripada batu dan gangsa.", ["MESIR", "PURBA"], "Pisau batu & gangsa", "sun", "mesir"),
   point("Di Rom purba, kedai barber menjadi tempat lelaki berkumpul, berbual dan berkongsi berita.", ["ROM", "PURBA"], "Tempat lelaki berkumpul & berbual", "talk", "rom"),
   point("Di Eropah zaman pertengahan, barber juga merawat luka dan mencabut gigi.", ["ZAMAN", "PERTENGAHAN"], "Barber juga merawat luka", "bandage", "eropah"),
   point("Kini, barber moden menggabungkan seni, teknik dan perniagaan.", ["BARBER", "MODEN"], "Seni, teknik & bisnes", "clipper", "moden"),
   cta("Suka sejarah macam ni? Komen SEJARAH.", ["Suka sejarah", "macam ni?"], "SEJARAH", "Kami kongsi lagi!"),
 ]),
 V("30-hair-spray-keras", F_, 53, ["#hairspray", "#produkrambut", "#tipsrambut", "#rambutlelaki", "#menshairstyle"], [
   hook("Kenapa rambut jadi keras macam plastik selepas guna hair spray?", ["KENAPA RAMBUT", "JADI KERAS?"], [1], "spray", "Selepas guna hair spray"),
   point("Hair spray membentuk lapisan nipis apabila ia kering. Lapisan inilah yang mengunci bentuk rambut.", ["LAPISAN", "PENGUNCI"], "Bentuk lapisan bila kering", "spray", "lapisan"),
   point("Jika disembur terlalu banyak atau terlalu dekat, lapisan jadi tebal dan rambut terasa keras.", ["TERLALU BANYAK,", "TERLALU DEKAT"], "Lapisan tebal = keras", "cross", "dekat"),
   tip("Sembur dari jarak kira-kira dua puluh hingga tiga puluh sentimeter, dengan semburan yang nipis.", ["SEMBUR", "20–30 CM"], "Semburan nipis dan rata", "ruler", "jarak"),
   tip("Pilih flexible hold jika anda mahu rambut kekal kemas, tetapi masih boleh bergerak.", ["PILIH", "FLEXIBLE HOLD"], "Kemas tapi masih bergerak", "check", "flexible"),
   cta("Ada soalan pasal produk rambut? Komen SPRAY.", ["Soalan pasal", "produk rambut?"], "SPRAY", "Kami jawab!"),
 ]),
 V("31-kemahiran-vs-ego", G_, 63, ["#barberlife", "#motivasi", "#kerjayabarber", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Dalam dunia barber, ego boleh menghalang anda menjadi lebih baik.", ["KEMAHIRAN", "ATAU", "EGO?"], [2], "mirror", "Ego boleh menghalang anda"),
   point("Barber yang ego rasa dia sudah tahu semua, jadi dia berhenti belajar.", ["BERHENTI", "BELAJAR"], "Rasa dah tahu semua", "cross", "ego"),
   point("Barber yang mahu berkembang terima teguran, sama ada daripada pelanggan atau rakan sekerja.", ["TERIMA", "TEGURAN"], "Daripada pelanggan & rakan", "talk", "teguran"),
   point("Malah, kadang-kadang kita boleh belajar teknik baharu daripada barber yang lebih muda.", ["BELAJAR DARI", "YANG MUDA"], "Ilmu tak kenal umur", "sprout", "muda"),
   point("Pelanggan pun lebih percaya barber yang mendengar, bukan yang bercakap sahaja.", ["DENGAR", "PELANGGAN"], "Dengar dulu, baru potong", "chat", "mendengar"),
   tip("Ingat, ego membuat kita berhenti. Kemahiran membuat kita terus naik.", ["TURUNKAN EGO,", "NAIKKAN SKILL"], "Kemahiran bawa anda jauh", "trophy", "kemahiran"),
   cta("Setuju atau tidak? Komen SETUJU.", ["Setuju", "atau tidak?"], "SETUJU", "Kongsi pendapat!"),
 ], music="trap"),
 V("32-modal-buka-kedai", D_, 33, ["#bisnesbarber", "#bukakedai", "#usahawanmalaysia", "#barbershopmalaysia", "#lelakimalaysia"], [
   hook("Nak buka barbershop sendiri? Ini perkara yang perlu ada dalam bajet modal anda.", ["MODAL BUKA", "BARBERSHOP"], [1], "shop", "Senarai semak sebelum mula"),
   point("Pertama, sewa dan deposit kedai, serta kos ubah suai.", ["SEWA &", "UBAH SUAI"], "Deposit, sewa awal, renovasi", "shop", "sewa"),
   point("Kedua, kerusi barber, cermin, sinki dan perabot.", ["KERUSI &", "PERABOT"], "Kerusi, cermin, sinki", "mirror", "kerusi"),
   point("Ketiga, alatan seperti clipper, trimmer, gunting dan alat sterilisasi.", ["ALATAN", "BARBER"], "Clipper, trimmer, sterilisasi", "clipper", "alatan"),
   point("Keempat, lesen perniagaan dan permit daripada pihak berkuasa tempatan.", ["LESEN &", "PERMIT"], "Ikut syarat PBT anda", "book", "lesen"),
   point("Kelima, dan ramai terlupa, modal pusingan untuk beberapa bulan pertama.", ["MODAL", "PUSINGAN"], "Gaji, bil & stok bulan awal", "calendar", "pusingan"),
   tip("Jumlah modal bergantung pada lokasi dan saiz kedai. Buat bajet terperinci sebelum mula.", ["BUAT BAJET", "DULU"], "Ikut lokasi & saiz kedai", "check", "bajet"),
   cta("Ada soalan pasal modal? Komen MODAL.", ["Ada soalan", "pasal modal?"], "MODAL", "Kami bantu jawab!"),
 ]),
 V("33-pencipta-clipper", E_, 44, ["#sejarahbarber", "#clipper", "#faktamenarik", "#barberlife", "#lelakimalaysia"], [
   hook("Siapa yang mencipta mesin gunting rambut? Ceritanya bermula lebih seratus tahun lalu.", ["SIAPA CIPTA", "MESIN", "GUNTING?"], [2], "clipper", "Lebih 100 tahun lalu"),
   point("Sebelum ada mesin, barber hanya menggunakan gunting, sikat dan pisau cukur.", ["DULU CUMA", "GUNTING"], "Gunting, sikat & pisau cukur", "scissors", "sebelum"),
   tts(point("Sekitar tahun 1850-an, seorang tukang gunting dari Serbia, Nikola Bizumić, dipercayai mencipta mesin gunting manual.",
         ["CLIPPER", "MANUAL"], "Dipercayai Nikola Bizumić, 1850-an", "hand", "manual"),
       "Sekitar tahun lapan belas lima puluhan, seorang tukang gunting dari Serbia, Nikola Bizumich, dipercayai mencipta mesin gunting manual."),
   tts(point("Kemudian pada tahun 1919, Leo J. Wahl dari Amerika Syarikat memperkenalkan mesin gunting elektrik yang praktikal.",
         ["CLIPPER", "ELEKTRIK"], "Leo J. Wahl, 1919", "bolt", "elektrik"),
       "Kemudian pada tahun sembilan belas sembilan belas, Leo Wahl dari Amerika Syarikat memperkenalkan mesin gunting elektrik yang praktikal."),
   tip("Sejak itu, clipper menjadi alat utama setiap barber, terutamanya untuk gaya fade.", ["ALAT UTAMA", "BARBER"], "Terutamanya untuk fade", "clipper", "utama"),
   cta("Barber, clipper apa yang anda guna? Komen CLIPPER.", ["Barber, clipper", "apa anda guna?"], "CLIPPER", "Kongsi pilihan anda!"),
 ]),
 V("34-cara-guna-serum", F_, 54, ["#hairserum", "#produkrambut", "#tipsrambut", "#rambutlelaki", "#menshairstyle"], [
   hook("Ramai guna hair serum, tapi cara yang salah buat rambut nampak berminyak.", ["CARA BETUL", "GUNA HAIR", "SERUM"], [2], "dropper", "Elak rambut berminyak"),
   point("Hair serum membantu mengurangkan rambut kembang dan memberi kilauan.", ["KURANG KEMBANG,", "LEBIH BERKILAT"], "Fungsi utama serum", "drop", "kembang"),
   tip("Pertama, ambil satu atau dua titis sahaja.", ["1–2 TITIS", "SAHAJA"], "Sedikit dah cukup", "dropper", "titis"),
   tip("Kedua, gosok di tapak tangan, kemudian sapu pada bahagian tengah hingga hujung rambut.", ["TENGAH HINGGA", "HUJUNG"], "Gosok di tapak tangan dulu", "hand", "hujung"),
   tip("Ketiga, elakkan kulit kepala, supaya akar rambut tidak nampak berminyak.", ["ELAK KULIT", "KEPALA"], "Akar tak nampak berminyak", "scalp", "elakkan"),
   point("Serum boleh digunakan pada rambut lembap atau kering. Ikut arahan pada produk anda.", ["LEMBAP ATAU", "KERING"], "Ikut arahan produk", "check", "lembap"),
   cta("Pernah tersalah guna serum? Komen SERUM.", ["Pernah tersalah", "guna serum?"], "SERUM", "Kami bantu!"),
 ]),
 V("35-pembantu-ke-pemilik", G_, 64, ["#kerjayabarber", "#motivasi", "#barberlife", "#usahawanmalaysia", "#lelakimalaysia"], [
   hook("Dari menyapu lantai kedai, sehingga memiliki barbershop sendiri. Begini perjalanannya.", ["PEMBANTU", "KE PEMILIK"], [1], "broom", "Perjalanan biasa dalam industri"),
   point("Ramai bermula sebagai pembantu. Menyapu lantai, mencuci rambut, dan memerhati barber senior bekerja.", ["MULA SEBAGAI", "PEMBANTU"], "Sapu, cuci & perhati", "broom", "pembantu"),
   point("Kemudian, belajar dan berlatih sehingga dipercayai memegang pelanggan sendiri.", ["BELAJAR &", "BERLATIH"], "Sampai dipercayai pelanggan", "scissors", "berlatih"),
   point("Selepas beberapa tahun, membina nama, pelanggan tetap, dan kemahiran yang matang.", ["BINA NAMA &", "PELANGGAN"], "Pelanggan tetap ikut anda", "star", "nama"),
   point("Sebelum buka kedai, belajar asas bisnes dan kumpul modal sedikit demi sedikit.", ["BELAJAR BISNES", "& KUMPUL MODAL"], "Sedikit demi sedikit", "coin", "modal"),
   tip("Perjalanan ini panjang. Tetapi setiap pemilik barbershop pernah bermula dari bawah.", ["SEMUA BERMULA", "DARI BAWAH"], "Sabar & konsisten", "sprout", "bawah"),
   cta("Kongsi perjalanan anda. Komen MULA.", ["Kongsi perjalanan", "anda!"], "MULA", "Semangat!"),
 ], music="trap"),
 V("36-kesilapan-pemilik", D_, 34, ["#bisnesbarber", "#usahawanmalaysia", "#tipsbisnes", "#barbershopmalaysia", "#lelakimalaysia"], [
   hook("Lima kesilapan yang selalu dilakukan oleh pemilik barbershop baharu.", ["5 KESILAPAN", "PEMILIK", "BAHARU"], [2], "shop", "Elakkan dari awal"),
   point("Satu, letak harga terlalu murah semata-mata untuk menarik pelanggan.", ["HARGA TERLALU", "MURAH"], "Susah naik harga kemudian", "tag", "harga"),
   point("Dua, tiada rekod kewangan. Tak tahu sebenarnya untung atau rugi.", ["TIADA REKOD", "KEWANGAN"], "Untung atau rugi pun tak tahu", "book", "rekod"),
   point("Tiga, campur duit peribadi dengan duit perniagaan.", ["CAMPUR DUIT", "PERIBADI"], "Asingkan akaun dari hari pertama", "coin", "campur"),
   point("Empat, abaikan pemasaran. Kedai yang bagus pun perlu dikenali.", ["ABAIKAN", "PEMASARAN"], "Kedai bagus pun perlu dikenali", "camera", "pemasaran"),
   point("Lima, tiada SOP dan latihan untuk pekerja.", ["TIADA SOP", "& LATIHAN"], "Servis jadi tak konsisten", "check", "latihan"),
   cta("Pemilik kedai, pernah buat yang mana? Komen nombornya.", ["Pernah buat", "yang mana?"], "3", "Kongsi pengalaman!"),
 ]),
 V("37-gaya-100-tahun", E_, 45, ["#gayarambut", "#sejarahrambut", "#menshairstyle", "#rambutlelaki", "#lelakimalaysia"], [
   tts(hook("Bagaimana gaya rambut lelaki berubah dalam tempoh 100 tahun?", ["100 TAHUN", "GAYA RAMBUT", "LELAKI"], [0], "cut-sidepart", "Dari 1920-an hingga kini"),
       "Bagaimana gaya rambut lelaki berubah dalam tempoh seratus tahun?"),
   tts(point("Tahun 1920-an hingga 1940-an, rambut disikat licin ke belakang atau belah tepi dengan pomade.", ["1920-AN", "SLICK BACK"], "Licin, kemas, berkilat", "cut-sidepart", "licin"),
       "Tahun sembilan belas dua puluhan hingga empat puluhan, rambut disikat licin ke belakang atau belah tepi dengan pomade."),
   tts(point("Tahun 1950-an, gaya pompadour dan quiff yang tinggi di depan menjadi ikutan.", ["1950-AN", "POMPADOUR"], "Tinggi di bahagian depan", "cut-quiff", "pompadour"),
       "Tahun sembilan belas lima puluhan, gaya pompadour dan quiff yang tinggi di depan menjadi ikutan."),
   tts(point("Tahun 1960-an dan 1970-an, rambut lebih panjang dan bebas mula popular.", ["1960–70-AN", "RAMBUT PANJANG"], "Lebih bebas & santai", "cut-long", "panjang"),
       "Tahun sembilan belas enam puluhan dan tujuh puluhan, rambut lebih panjang dan bebas mula popular."),
   tts(point("Tahun 1980-an dan 1990-an, kita nampak mullet, belah tengah dan rambut tercacak.", ["1980–90-AN", "MULLET & SPIKY"], "Belah tengah pun popular", "cut-fringe", "mullet"),
       "Tahun sembilan belas lapan puluhan dan sembilan puluhan, kita nampak mullet, belah tengah dan rambut tercacak."),
   point("Kini, fade, textured crop dan gaya bertekstur paling banyak diminta.", ["KINI:", "FADE & TEKSTUR"], "Kemas tapi santai", "fade-mid", "fade"),
   cta("Gaya era mana yang anda suka? Komen ERA.", ["Gaya era mana", "anda suka?"], "ERA", "Kongsi pilihan!"),
 ]),
]

# ---------------------------------------------------------------- January 2027 batch (26 Dec – 31 Jan, every free day)
A_ = "SAINS RAMBUT"; C_ = "BARBER BERCERITA"
MED = "*Maklumat umum, bukan nasihat perubatan. Jumpa doktor atau pakar kulit jika masalah berterusan."
VIDEOS += [
 V("38-pomade-gugur", F_, 55, ["#pomade", "#rambutgugur", "#produkrambut", "#tipsrambut", "#lelakimalaysia"], [
   hook("Adakah pomade menyebabkan rambut gugur? Ramai risau, jom tengok faktanya.", ["POMADE BUAT", "RAMBUT", "GUGUR?"], [2], "jar", "Jom tengok faktanya"),
   point("Setakat ini, tiada bukti kukuh bahawa penggunaan pomade yang biasa menyebabkan rambut gugur.", ["TIADA BUKTI", "KUKUH"], "Untuk penggunaan biasa", "check", "bukti"),
   point("Tetapi, jika produk tidak dibilas dan terkumpul di kulit kepala, ia boleh menyebabkan gatal dan kerengsaan.", ["PRODUK", "TERKUMPUL"], "Boleh buat gatal & rengsa", "scalp", "terkumpul"),
   tip("Jadi, bilas sampai bersih, dan jangan tidur dengan pomade di rambut.", ["BILAS SAMPAI", "BERSIH"], "Jangan tidur dengan pomade", "shower", "bilas"),
   tip("Jika rambut gugur berterusan atau kulit kepala merah, jumpa doktor atau pakar kulit.", ["GUGUR BERTERUSAN?", "JUMPA DOKTOR"], "Atau pakar kulit", "check", "doktor"),
   cta("Ada soalan pasal produk rambut? Komen POMADE.", ["Soalan pasal", "produk rambut?"], "POMADE", "Kami jawab!"),
 ], footnote=MED),
 V("39-sikap-barber-pro", G_, 65, ["#barberlife", "#barberprofesional", "#kerjayabarber", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Apa beza barber biasa dengan barber profesional? Lima sikap ini.", ["BARBER BIASA", "VS", "PROFESIONAL"], [2], "scissors", "Lima sikap yang membezakan"),
   point("Satu, tepati masa. Pelanggan tak perlu menunggu tanpa sebab.", ["TEPATI", "MASA"], "Hormati masa pelanggan", "clock", "tepati"),
   point("Dua, kebersihan. Alat disterilkan, tempat kerja kemas.", ["JAGA", "KEBERSIHAN"], "Alat steril, tempat kemas", "broom", "kebersihan"),
   point("Tiga, mendengar sebelum memotong.", ["DENGAR", "DULU"], "Faham kehendak pelanggan", "talk", "mendengar"),
   point("Empat, jujur. Beritahu jika gaya itu tidak sesuai.", ["NASIHAT", "JUJUR"], "Beritahu jika tak sesuai", "chat", "jujur"),
   point("Lima, terus belajar teknik baharu.", ["TERUS", "BELAJAR"], "Ilmu tak pernah habis", "book", "belajar"),
   cta("Mana paling penting bagi anda? Komen nombornya.", ["Mana paling", "penting?"], "4", "Kongsi pendapat!"),
 ], music="trap"),
 V("40-kedai-tutup-setahun", D_, 35, ["#bisnesbarber", "#usahawanmalaysia", "#tipsbisnes", "#barbershopmalaysia", "#lelakimalaysia"], [
   hook("Kenapa ada barbershop yang tutup selepas setahun? Ini antara sebabnya.", ["TUTUP", "SELEPAS", "SETAHUN?"], [2], "shop", "Antara sebab biasa"),
   point("Pertama, lokasi kurang sesuai, dengan sewa yang terlalu tinggi.", ["LOKASI &", "SEWA"], "Sewa tinggi, pelanggan kurang", "shop", "lokasi"),
   point("Kedua, tiada modal simpanan untuk bulan-bulan awal yang perlahan.", ["TIADA MODAL", "SIMPANAN"], "Bulan awal biasanya perlahan", "coin", "simpanan"),
   point("Ketiga, pelanggan datang sekali, tapi tidak kembali.", ["TIADA PELANGGAN", "TETAP"], "Datang sekali, tak kembali", "cross", "kembali"),
   point("Keempat, tiada rekod kewangan, jadi masalah lambat dikesan.", ["TIADA REKOD", "KEWANGAN"], "Masalah lambat dikesan", "book", "rekod"),
   tip("Rancang awal, simpan modal, dan jaga pelanggan sejak hari pertama.", ["RANCANG", "DARI AWAL"], "Modal, rekod & pelanggan tetap", "check", "rancang"),
   cta("Ada pengalaman sendiri? Komen BISNES.", ["Ada pengalaman", "sendiri?"], "BISNES", "Kongsi cerita!"),
 ]),
 V("41-rambut-tentera", E_, 46, ["#sejarahrambut", "#rambuttentera", "#faktamenarik", "#crewcut", "#lelakimalaysia"], [
   hook("Kenapa potongan rambut tentera sangat pendek? Ada sebab praktikalnya.", ["KENAPA RAMBUT", "TENTERA", "PENDEK?"], [2], "cut-crew", "Ada sebab praktikalnya"),
   point("Pertama, kebersihan. Rambut pendek lebih mudah dijaga semasa latihan, dan mengurangkan masalah kutu.", ["LEBIH", "BERSIH"], "Mudah dijaga, kurang kutu", "shower", "kebersihan"),
   point("Kedua, keselamatan. Topi keledar dan topeng gas lebih padat dipakai.", ["LEBIH", "SELAMAT"], "Topi keledar lebih padat", "check", "keselamatan"),
   point("Ketiga, disiplin dan keseragaman. Semua kelihatan sama dan kemas.", ["DISIPLIN &", "SERAGAM"], "Semua nampak kemas & sama", "star", "disiplin"),
   tip("Hari ini, gaya crew cut dan buzz cut pun popular dalam kalangan orang awam.", ["KINI JADI", "TREND"], "Crew cut & buzz cut", "clipper", "popular"),
   cta("Pernah cuba potongan ala tentera? Komen BUZZ.", ["Pernah cuba", "gaya tentera?"], "BUZZ", "Kongsi gambar!"),
 ]),
 V("42-mousse-vs-gel", F_, 56, ["#hairmousse", "#hairgel", "#produkrambut", "#rambutlelaki", "#menshairstyle"], [
   hook("Hair mousse atau hair gel? Ramai tak tahu bezanya.", ["MOUSSE", "ATAU", "GEL?"], [2], "spray", "Ramai tak tahu bezanya"),
   compare("Mousse berbentuk buih ringan, memberi volume dan pegangan lembut. Gel pula memberi pegangan lebih kuat, dengan kesan basah dan berkilat.",
     side("MOUSSE", "spray", [("+", "Ringan & ada volume"), ("+", "Pegangan lembut")], "mousse"),
     side("GEL", "drop", [("+", "Pegangan kuat"), ("o", "Kesan basah & berkilat")], "gel")),
   tip("Rambut nipis dan mahu nampak lebih tebal? Cuba mousse. Mahu gaya kemas yang tahan lama? Pilih gel.", ["PILIH IKUT", "GAYA"], "Nipis: mousse. Kemas: gel.", "check", "nipis"),
   tip("Untuk kedua-duanya, sapu pada rambut yang lembap, dan gunakan sedikit sahaja.", ["RAMBUT LEMBAP,", "SEDIKIT SAHAJA"], "Elak rambut jadi keras", "hand", "lembap"),
   cta("Anda geng mousse atau gel? Komen GEL atau MOUSSE.", ["Geng mousse", "atau gel?"], "GEL", "Kongsi pilihan!"),
 ]),
 V("43-terus-belajar", G_, 66, ["#barberlife", "#kerjayabarber", "#motivasi", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Dah bertahun jadi barber, perlu belajar lagi? Jawapannya, ya.", ["DAH PAKAR,", "PERLU BELAJAR", "LAGI?"], [2], "book", "Jawapannya, ya"),
   point("Trend rambut sentiasa berubah. Gaya yang popular hari ini mungkin berbeza tahun depan.", ["TREND", "BERUBAH"], "Gaya popular sentiasa bertukar", "calendar", "trend"),
   point("Alat dan teknik baharu sentiasa muncul, dan boleh buat kerja lebih cepat dan kemas.", ["ALAT & TEKNIK", "BAHARU"], "Kerja lebih cepat & kemas", "clipper", "alat"),
   point("Pelanggan pun makin bijak. Mereka tengok video, dan mahu hasil yang lebih tepat.", ["PELANGGAN", "MAKIN BIJAK"], "Jangkaan makin tinggi", "camera", "pelanggan"),
   tip("Ikuti kursus, sertai pertandingan, dan belajar daripada barber lain.", ["KURSUS &", "PERTANDINGAN"], "Belajar daripada barber lain", "trophy", "kursus"),
   follow("Ikuti kami untuk lebih banyak ilmu dunia barber.", ["Ikuti kami untuk", "ilmu dunia", "barber"], "Ilmu & inspirasi barber"),
 ], music="trap", handle="@elasbarbershop.official", tagline="Lebih daripada sekadar gunting rambut."),
 V("44-gaji-vs-komisen", D_, 36, ["#bisnesbarber", "#gajibarber", "#usahawanmalaysia", "#barbershopmalaysia", "#lelakimalaysia"], [
   hook("Gaji tetap atau komisen? Ini persoalan besar untuk barber dan pemilik kedai.", ["GAJI TETAP", "ATAU", "KOMISEN?"], [2], "coin", "Untuk barber & pemilik kedai"),
   compare("Gaji tetap memberi pendapatan yang stabil, tetapi kurang ganjaran bila ramai pelanggan. Komisen pula ikut jumlah kerja, tetapi pendapatan boleh naik turun.",
     side("GAJI TETAP", "calendar", [("+", "Pendapatan stabil"), ("-", "Kurang ganjaran prestasi")], "gaji"),
     side("KOMISEN", "coin", [("+", "Ikut jumlah kerja"), ("-", "Boleh naik turun")], "komisen")),
   point("Ramai kedai kini guna gabungan, iaitu gaji asas ditambah komisen.", ["GAJI ASAS", "+ KOMISEN"], "Gabungan dua sistem", "check", "gabungan"),
   tip("Yang penting, sistem itu adil, jelas, dan dipersetujui dari awal.", ["ADIL &", "JELAS"], "Setuju dari awal", "book", "adil"),
   cta("Barber, anda pilih yang mana? Komen GAJI atau KOMISEN.", ["Anda pilih", "yang mana?"], "GAJI", "Kongsi pendapat!"),
 ]),
 V("45-pisau-cukur", E_, 47, ["#sejarahbarber", "#straightrazor", "#faktamenarik", "#barberlife", "#lelakimalaysia"], [
   hook("Sebelum ada pisau cukur pakai buang, barber menggunakan pisau cukur tradisional. Ini sejarahnya.", ["SEJARAH", "PISAU CUKUR", "TRADISIONAL"], [2], "razor", "Sebelum pakai buang"),
   point("Pisau cukur lurus, atau straight razor, digunakan barber selama beratus tahun.", ["STRAIGHT", "RAZOR"], "Digunakan beratus tahun", "razor", "lurus"),
   point("Ia perlu diasah dan dijaga dengan teliti, dan memerlukan tangan yang sangat mahir.", ["PERLU", "KEMAHIRAN"], "Diasah & dijaga teliti", "hand", "diasah"),
   point("Pada awal abad ke-20, pisau cukur keselamatan dengan bilah boleh tukar mula popular.", ["PISAU", "KESELAMATAN"], "Bilah boleh tukar, awal 1900-an", "check", "keselamatan"),
   tip("Hari ini, barber masih guna pisau cukur lurus, tetapi dengan bilah pakai buang untuk kebersihan.", ["BILAH", "PAKAI BUANG"], "Untuk kebersihan pelanggan", "check", "kebersihan"),
   cta("Pernah bercukur dengan pisau cukur lurus? Komen CUKUR.", ["Pernah cukur", "dengan razor?"], "CUKUR", "Kongsi pengalaman!"),
 ]),
 V("46-produk-tak-tahan", F_, 57, ["#produkrambut", "#stylingrambut", "#tipsrambut", "#rambutlelaki", "#menshairstyle"], [
   hook("Pagi rambut kemas, tengah hari dah jatuh? Ini sebabnya.", ["PRODUK", "TAK TAHAN", "LAMA?"], [2], "jar", "Pagi kemas, tengah hari jatuh"),
   point("Pertama, produk disapu pada rambut yang terlalu basah, jadi pegangannya lemah.", ["RAMBUT TERLALU", "BASAH"], "Pegangan jadi lemah", "drop", "basah"),
   point("Kedua, jenis produk tidak sesuai dengan jenis rambut anda.", ["PRODUK", "TAK SESUAI"], "Ikut jenis rambut", "cross", "jenis"),
   point("Ketiga, cuaca panas dan peluh di Malaysia memang mencabar.", ["PANAS &", "PELUH"], "Cuaca Malaysia mencabar", "sun", "panas"),
   point("Keempat, selalu sentuh dan betulkan rambut dengan tangan.", ["SELALU", "SENTUH"], "Bentuk rambut rosak", "hand", "sentuh"),
   tip("Keringkan rambut dengan blow dryer dulu, kemudian baru sapu produk.", ["BLOW DRY", "DULU"], "Baru sapu produk", "hairdryer", "blow"),
   cta("Rambut anda tahan berapa jam? Komen JAM.", ["Tahan berapa", "jam?"], "JAM", "Kongsi jawapan!"),
 ]),
 V("47-sijil-vs-pengalaman", G_, 67, ["#kerjayabarber", "#skm", "#barberlife", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Sijil kemahiran atau pengalaman, mana lebih penting untuk seorang barber?", ["SIJIL ATAU", "PENGALAMAN?"], [1], "book", "Mana lebih penting?"),
   compare("Sijil memberi asas yang betul dan menambah kepercayaan pelanggan. Pengalaman pula mengasah kemahiran dan kepantasan, melalui ribuan potongan.",
     side("SIJIL", "book", [("+", "Asas yang betul"), ("+", "Tambah kepercayaan")], "sijil"),
     side("PENGALAMAN", "scissors", [("+", "Kemahiran diasah"), ("+", "Lebih pantas")], "pengalaman")),
   point("Di Malaysia, contohnya, ada Sijil Kemahiran Malaysia untuk bidang dandanan rambut.", ["CONTOH:", "SKM"], "Sijil Kemahiran Malaysia", "check", "malaysia"),
   tip("Jawapannya, kedua-duanya penting. Sijil membuka pintu, pengalaman membawa anda jauh.", ["KEDUA-DUANYA", "PENTING"], "Sijil buka pintu", "trophy", "kedua"),
   cta("Anda setuju? Komen SETUJU.", ["Anda", "setuju?"], "SETUJU", "Kongsi pendapat!"),
 ], music="trap"),
 V("48-pekerja-bagus-pergi", D_, 37, ["#bisnesbarber", "#pengurusan", "#usahawanmalaysia", "#barbershopmalaysia", "#lelakimalaysia"], [
   hook("Kenapa barber yang bagus selalu meninggalkan kedai? Pemilik kedai, dengar sini.", ["KENAPA PEKERJA", "BAGUS", "PERGI?"], [2], "person", "Pemilik kedai, dengar sini"),
   point("Pertama, tiada peluang untuk berkembang atau naik pangkat.", ["TIADA", "PELUANG"], "Tak nampak masa depan", "sprout", "peluang"),
   point("Kedua, bayaran tidak adil berbanding hasil kerja.", ["BAYARAN", "TAK ADIL"], "Tak setimpal dengan kerja", "coin", "bayaran"),
   point("Ketiga, usaha mereka tidak dihargai.", ["TIDAK", "DIHARGAI"], "Pujian pun jarang", "thumb", "dihargai"),
   point("Keempat, suasana kerja yang tidak sihat.", ["SUASANA", "TAK SIHAT"], "Tekanan & konflik", "stress", "suasana"),
   tip("Beri latihan, bayaran yang adil, dan penghargaan. Pekerja bagus akan kekal.", ["LATIH, BAYAR,", "HARGAI"], "Pekerja bagus akan kekal", "trophy", "latihan"),
   cta("Pernah alami sendiri? Komen nombornya.", ["Pernah alami", "sendiri?"], "2", "Kongsi cerita!"),
 ]),
 V("49-rambut-menipis", A_, 1, ["#rambutnipis", "#rambutgugur", "#kesihatanrambut", "#tipsrambut", "#lelakimalaysia"], [
   hook("Kenapa rambut lelaki semakin menipis? Ini sebab yang paling biasa.", ["KENAPA RAMBUT", "MAKIN", "MENIPIS?"], [2], "hair-thin", "Sebab paling biasa"),
   point("Sebab paling biasa ialah faktor genetik dan hormon, yang dipanggil keguguran rambut corak lelaki.", ["GENETIK &", "HORMON"], "Keguguran rambut corak lelaki", "dna", "genetik"),
   point("Ia biasanya bermula di pelipis atau di bahagian atas kepala, secara perlahan-lahan.", ["PELIPIS &", "UBUN-UBUN"], "Bermula perlahan-lahan", "scalp", "pelipis"),
   point("Faktor lain seperti tekanan, pemakanan dan masalah kesihatan juga boleh menyumbang.", ["FAKTOR", "LAIN"], "Tekanan, pemakanan, kesihatan", "stress", "tekanan"),
   tip("Jika rambut menipis dengan cepat, jumpa doktor atau pakar kulit untuk pilihan rawatan.", ["JUMPA", "PAKAR"], "Ada pilihan rawatan", "check", "doktor"),
   tip("Sementara itu, potongan yang betul boleh buat rambut nampak lebih penuh.", ["POTONGAN", "YANG BETUL"], "Rambut nampak lebih penuh", "scissors", "potongan"),
   cta("Nak cadangan gaya untuk rambut nipis? Komen NIPIS.", ["Nak cadangan", "gaya?"], "NIPIS", "Kami bantu!"),
 ], footnote=MED),
 V("50-budaya-rambut", E_, 48, ["#budaya", "#sejarahrambut", "#faktamenarik", "#rambutlelaki", "#lelakimalaysia"], [
   hook("Bagi sesetengah budaya, rambut bukan sekadar gaya. Ia membawa makna.", ["RAMBUT &", "BUDAYA"], [1], "flag", "Bukan sekadar gaya"),
   point("Bagi lelaki Sikh, rambut tidak dipotong sebagai sebahagian daripada amalan agama, dan dililit dengan serban.", ["SIKH:", "KESH"], "Rambut tak dipotong, berserban", "person", "sikh"),
   point("Dalam masyarakat Melayu, ada adat cukur jambul untuk bayi, sebagai tanda kesyukuran.", ["MELAYU:", "CUKUR JAMBUL"], "Tanda kesyukuran untuk bayi", "razor", "jambul"),
   point("Di Jepun zaman dahulu, samurai mempunyai gaya rambut khas yang dipanggil chonmage.", ["JEPUN:", "CHONMAGE"], "Gaya rambut samurai", "star", "samurai"),
   tip("Sebab itu, barber yang baik menghormati budaya dan kepercayaan setiap pelanggan.", ["HORMATI", "BUDAYA"], "Setiap pelanggan berbeza", "check", "menghormati"),
   cta("Ada adat rambut dalam keluarga anda? Komen ADAT.", ["Ada adat rambut", "dalam keluarga?"], "ADAT", "Kongsi cerita!"),
 ]),
 V("51-cabaran-10-tahun", C_, 28, ["#barberlife", "#realitibarber", "#kerjayabarber", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Sepuluh tahun menjadi barber. Apa cabaran yang orang jarang nampak?", ["CABARAN", "10 TAHUN", "JADI BARBER"], [1], "clock", "Yang orang jarang nampak"),
   point("Berdiri berjam-jam setiap hari boleh memberi kesan kepada belakang dan kaki.", ["BERDIRI", "BERJAM-JAM"], "Belakang & kaki terkesan", "person", "berdiri"),
   point("Trend sentiasa berubah, jadi barber perlu terus belajar.", ["TREND", "BERUBAH"], "Perlu terus belajar", "calendar", "trend"),
   point("Setiap pelanggan berbeza, dan ada hari yang memang menguji kesabaran.", ["UJIAN", "KESABARAN"], "Setiap pelanggan berbeza", "chat", "kesabaran"),
   point("Persaingan pun semakin ramai, terutamanya di kawasan bandar.", ["PERSAINGAN", "SENGIT"], "Kedai baharu di mana-mana", "shop", "persaingan"),
   tip("Tapi bagi yang bertahan, kemahiran dan pelanggan setia ialah ganjaran terbesar.", ["GANJARAN", "TERBESAR"], "Kemahiran & pelanggan setia", "trophy", "ganjaran"),
   cta("Barber, apa cabaran terbesar anda? Komen CABARAN.", ["Cabaran", "terbesar anda?"], "CABARAN", "Kongsi cerita!"),
 ]),
 V("52-terlalu-banyak-produk", F_, 58, ["#produkrambut", "#tipsrambut", "#rambutlelaki", "#menshairstyle", "#lelakimalaysia"], [
   hook("Apa jadi kalau guna produk rambut terlalu banyak?", ["TERLALU BANYAK", "PRODUK", "RAMBUT?"], [2], "jar", "Ini yang berlaku"),
   point("Rambut nampak berminyak dan berat, bukannya kemas.", ["BERMINYAK", "& BERAT"], "Bukannya kemas", "oil", "berminyak"),
   point("Gaya jadi leper, sebab rambut tak mampu menahan berat produk.", ["GAYA JADI", "LEPER"], "Rambut tak tahan berat", "cross", "leper"),
   point("Produk terkumpul di kulit kepala, dan boleh menyebabkan gatal atau serpihan putih.", ["TERKUMPUL DI", "KULIT KEPALA"], "Gatal & serpihan putih", "scalp", "terkumpul"),
   tip("Mula dengan sebesar hujung jari, dan tambah sedikit jika perlu.", ["MULA", "SEDIKIT"], "Tambah jika perlu", "hand", "hujung"),
   tip("Bila guna produk setiap hari, cuci rambut sampai bersih.", ["CUCI SAMPAI", "BERSIH"], "Elak produk terkumpul", "shower", "cuci"),
   cta("Pernah terlebih produk? Komen PRODUK.", ["Pernah terlebih", "produk?"], "PRODUK", "Kongsi pengalaman!"),
 ]),
 V("53-kerjaya-anak-muda", G_, 68, ["#kerjayabarber", "#anakmuda", "#motivasi", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Kenapa golongan muda patut pertimbangkan kerjaya sebagai barber?", ["KERJAYA BARBER", "UNTUK ANAK", "MUDA?"], [2], "scissors", "Ini sebabnya"),
   point("Permintaan sentiasa ada. Rambut sentiasa tumbuh, dan orang perlukan barber.", ["PERMINTAAN", "SENTIASA ADA"], "Rambut sentiasa tumbuh", "calendar", "permintaan"),
   point("Ia kerja kreatif. Setiap potongan ialah hasil seni anda.", ["KERJA", "KREATIF"], "Setiap potongan hasil seni", "star", "kreatif"),
   point("Ada laluan untuk menjadi usahawan, dengan kedai dan pasukan sendiri.", ["LALUAN", "USAHAWAN"], "Kedai & pasukan sendiri", "shop", "usahawan"),
   point("Tetapi ia perlukan latihan, disiplin dan kerja keras.", ["PERLU", "KERJA KERAS"], "Latihan & disiplin", "book", "latihan"),
   follow("Ikuti kami untuk lebih banyak kisah kerjaya barber.", ["Ikuti kami untuk", "kisah kerjaya", "barber"], "Kerjaya & inspirasi barber"),
 ], music="trap", handle="@elasbarbershop.official", tagline="Lebih daripada sekadar gunting rambut.",
   footnote="*Pendapatan bergantung pada kemahiran, lokasi dan usaha masing-masing."),
 V("54-cepat-beruban", A_, 2, ["#uban", "#kesihatanrambut", "#tipsrambut", "#faktarambut", "#lelakimalaysia"], [
   hook("Kenapa ada orang cepat beruban, walaupun masih muda?", ["KENAPA CEPAT", "BERUBAN?"], [1], "hair-texture", "Walaupun masih muda"),
   point("Uban terjadi apabila pigmen warna rambut, iaitu melanin, semakin berkurangan.", ["MELANIN", "BERKURANG"], "Pigmen warna rambut", "drop", "melanin"),
   point("Faktor terbesar ialah genetik. Jika ibu bapa awal beruban, anda juga mungkin begitu.", ["FAKTOR", "GENETIK"], "Ikut keturunan", "dna", "genetik"),
   point("Merokok, dan kekurangan nutrien seperti vitamin B12, juga dikaitkan dengan uban awal.", ["MEROKOK &", "NUTRIEN"], "Contohnya vitamin B12", "cross", "merokok"),
   point("Mitos, cabut satu uban akan buat dua tumbuh. Itu tidak benar, tapi elakkan mencabut kerana ia boleh merosakkan folikel.", ["MITOS", "CABUT UBAN"], "Tak tumbuh dua, tapi elak cabut", "hand", "mitos"),
   tip("Jika uban muncul sangat awal atau tiba-tiba, dapatkan nasihat doktor.", ["NASIHAT", "DOKTOR"], "Jika terlalu awal", "check", "doktor"),
   cta("Bila anda nampak uban pertama? Komen UBAN.", ["Bila uban", "pertama anda?"], "UBAN", "Kongsi cerita!"),
 ], footnote=MED),
 V("55-perang-harga", D_, 38, ["#bisnesbarber", "#hargagunting", "#usahawanmalaysia", "#barbershopmalaysia", "#lelakimalaysia"], [
   hook("Kedai sebelah turunkan harga. Patutkah anda ikut?", ["PERANG", "HARGA"], [1], "tag", "Patutkah anda ikut?"),
   point("Bila semua kedai berlumba menurunkan harga, keuntungan semua orang semakin kecil.", ["UNTUNG", "MENGECIL"], "Semua kedai terjejas", "coin", "keuntungan"),
   point("Kualiti mula terjejas, sebab barber terpaksa memotong lebih cepat untuk menampung kos.", ["KUALITI", "TERJEJAS"], "Kerja terburu-buru", "clock", "kualiti"),
   point("Pelanggan yang datang kerana harga murah, akan pergi bila jumpa yang lebih murah.", ["PELANGGAN", "TAK SETIA"], "Pergi bila jumpa lebih murah", "cross", "murah"),
   tip("Bersaing dengan nilai, iaitu servis, pengalaman dan hasil yang konsisten.", ["BERSAING", "DENGAN NILAI"], "Servis, pengalaman & konsisten", "trophy", "nilai"),
   cta("Harga atau kualiti, mana anda pilih? Komen KUALITI.", ["Harga atau", "kualiti?"], "KUALITI", "Kongsi pendapat!"),
 ]),
 V("56-punca-kelemumur", A_, 3, ["#kelemumur", "#kulitkepala", "#kesihatanrambut", "#tipsrambut", "#lelakimalaysia"], [
   hook("Apa sebenarnya yang menyebabkan kelemumur? Bukan semestinya sebab rambut kotor.", ["PUNCA", "KELEMUMUR"], [1], "scalp", "Bukan semestinya kotor"),
   point("Kelemumur sering dikaitkan dengan sejenis yis yang hidup di kulit kepala, dan minyak semula jadi.", ["YIS &", "MINYAK"], "Biasa ada di kulit kepala", "oil", "yis"),
   point("Kulit kepala yang kering, atau sensitif kepada produk tertentu, juga boleh menyebabkan serpihan.", ["KULIT KERING", "& SENSITIF"], "Reaksi pada produk", "cross", "kering"),
   point("Cuaca, tekanan, dan jarang mencuci rambut boleh menjadikannya lebih teruk.", ["CUACA &", "TEKANAN"], "Boleh jadi lebih teruk", "stress", "cuaca"),
   tip("Cuba syampu anti-kelemumur, dan ikut arahan pada botol.", ["SYAMPU", "ANTI-KELEMUMUR"], "Ikut arahan pada botol", "check", "syampu"),
   tip("Jika gatal teruk, merah, atau tidak sembuh, jumpa doktor atau pakar kulit.", ["TAK SEMBUH?", "JUMPA PAKAR"], "Gatal teruk atau merah", "check", "doktor"),
   cta("Ada masalah kelemumur? Komen KELEMUMUR.", ["Ada masalah", "kelemumur?"], "KELEMUMUR", "Kami kongsi tips!"),
 ], footnote=MED),
 V("57-barbershop-sosial", E_, 49, ["#barbershop", "#komuniti", "#faktamenarik", "#barberlife", "#lelakimalaysia"], [
   hook("Kenapa barbershop sejak dulu menjadi tempat lelaki bersembang?", ["BARBERSHOP", "TEMPAT", "BERSEMBANG?"], [2], "talk", "Sejak dulu lagi"),
   point("Lelaki datang secara berkala, jadi mereka kenal barber dan pelanggan lain.", ["DATANG", "BERKALA"], "Kenal barber & pelanggan lain", "calendar", "berkala"),
   point("Di kerusi barber, ramai rasa selesa untuk bercerita tentang kerja, keluarga dan bola.", ["RUANG", "SELESA"], "Kerja, keluarga & bola", "chat", "selesa"),
   point("Sejak zaman Rom purba, kedai barber memang menjadi tempat bertukar berita.", ["TRADISI", "LAMA"], "Sejak zaman Rom purba", "book", "rom"),
   tip("Sebab itu, barbershop bukan sekadar kedai. Ia sebahagian daripada komuniti.", ["SEBAHAGIAN", "KOMUNITI"], "Bukan sekadar kedai", "shop", "komuniti"),
   cta("Apa topik paling kerap di kerusi barber? Komen TOPIK.", ["Topik paling", "kerap?"], "TOPIK", "Kongsi jawapan!"),
 ]),
 V("58-barber-burnout", C_, 29, ["#barberlife", "#burnout", "#realitibarber", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Barber pun boleh mengalami burnout. Tapi ramai tak bercakap mengenainya.", ["BARBER PUN", "BOLEH", "BURNOUT"], [2], "stress", "Ramai tak bercakap mengenainya"),
   point("Waktu kerja panjang, dan kadang-kadang tiada hari cuti yang betul.", ["WAKTU KERJA", "PANJANG"], "Cuti pun jarang", "clock", "waktu"),
   point("Badan penat kerana berdiri sepanjang hari.", ["PENAT", "FIZIKAL"], "Berdiri sepanjang hari", "person", "badan"),
   point("Emosi juga penat, kerana sentiasa melayan dan mendengar pelanggan.", ["PENAT", "EMOSI"], "Sentiasa melayan pelanggan", "talk", "emosi"),
   tip("Ambil rehat yang cukup, tetapkan had waktu kerja, dan jaga kesihatan.", ["REHAT &", "HAD KERJA"], "Jaga kesihatan diri", "sleep", "rehat"),
   tip("Jika tekanan berterusan, jangan malu untuk dapatkan bantuan profesional.", ["DAPATKAN", "BANTUAN"], "Jangan malu", "check", "bantuan"),
   cta("Barber, bila kali terakhir anda bercuti? Komen CUTI.", ["Bila kali terakhir", "anda bercuti?"], "CUTI", "Jaga diri!"),
 ]),
 V("59-fungsi-keratin", F_, 59, ["#keratin", "#keratintreatment", "#rambutlicin", "#rambutkembang", "#lelakimalaysia"], [
   hook("Apa sebenarnya fungsi keratin pada rambut? Ramai salah faham.", ["APA FUNGSI", "KERATIN?"], [1], "hair-texture", "Ramai salah faham"),
   point("Keratin ialah sejenis protein yang membentuk struktur rambut anda.", ["PROTEIN", "RAMBUT"], "Bina struktur rambut", "dna", "protein"),
   point("Bila rambut rosak atau kembang, lapisan luarnya terbuka dan kasar.", ["RAMBUT", "KEMBANG"], "Lapisan luar terbuka", "hairfall", "kembang"),
   point("Rawatan keratin membantu melicinkan rambut dan mengurangkan kembang, untuk tempoh beberapa bulan.", ["RAWATAN", "KERATIN"], "Licin untuk beberapa bulan", "check", "rawatan"),
   tip("Ia tidak kekal. Ikut penjagaan selepas rawatan, dan guna syampu yang sesuai.", ["TIDAK", "KEKAL"], "Ikut penjagaan selepas rawatan", "shower", "kekal"),
   cta("Nak tahu lebih pasal rawatan keratin? Komen KERATIN.", ["Nak tahu lebih", "pasal keratin?"], "KERATIN", "Kami jawab!"),
 ], footnote="*Hasil dan tempoh bergantung pada jenis rambut."),
 V("60-gunting-ke-syarikat", G_, 69, ["#usahawanmalaysia", "#bisnesbarber", "#kepimpinan", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Daripada memegang mesin gunting, kepada menguruskan sebuah syarikat. Apa yang berubah?", ["DARI GUNTING", "KE SYARIKAT"], [1], "clipper", "Apa yang berubah?"),
   point("Dulu, fokus pada setiap pelanggan di kerusi anda sendiri.", ["DULU: SATU", "KERUSI"], "Fokus pada kerja sendiri", "scissors", "dulu"),
   point("Kini, perlu membina sistem supaya kedai boleh berjalan tanpa anda.", ["BINA", "SISTEM"], "Kedai jalan tanpa anda", "book", "sistem"),
   point("Perlu memilih, melatih dan memimpin pasukan.", ["PIMPIN", "PASUKAN"], "Pilih, latih & pimpin", "person", "pasukan"),
   point("Perlu memahami kewangan, pemasaran dan jenama.", ["KEWANGAN &", "JENAMA"], "Bukan lagi kerja gunting", "coin", "kewangan"),
   tip("Kemahiran gunting membuka jalan. Kemahiran memimpin membawa anda lebih jauh.", ["DARI TANGAN", "KE KEPIMPINAN"], "Pimpin membawa lebih jauh", "trophy", "memimpin"),
   follow("Ikuti kami untuk lebih banyak ilmu bisnes barber.", ["Ikuti kami untuk", "ilmu bisnes", "barber"], "Bisnes & kepimpinan barber"),
 ], music="trap", handle="@elasbarbershop.official", tagline="Lebih daripada sekadar gunting rambut."),
 V("61-topi-botak", A_, 4, ["#mitosrambut", "#rambutgugur", "#kesihatanrambut", "#tipsrambut", "#lelakimalaysia"], [
   hook("Adakah memakai topi setiap hari boleh menyebabkan botak?", ["TOPI BUAT", "BOTAK?"], [1], "cap", "Mitos atau fakta?"),
   point("Untuk kebanyakan orang, memakai topi biasa tidak menyebabkan botak.", ["KEBANYAKANNYA", "MITOS"], "Topi biasa tak buat botak", "check", "kebanyakan"),
   point("Tetapi topi yang terlalu ketat, dipakai lama setiap hari, boleh menarik rambut dan merosakkannya.", ["TERLALU", "KETAT"], "Tarikan berterusan", "cross", "ketat"),
   point("Topi yang kotor dan berpeluh juga boleh merengsakan kulit kepala.", ["KOTOR &", "BERPELUH"], "Boleh rengsakan kulit kepala", "scalp", "kotor"),
   tip("Pilih saiz yang selesa, cuci topi selalu, dan beri kulit kepala bernafas.", ["SELESA &", "BERSIH"], "Cuci topi selalu", "check", "selesa"),
   cta("Anda geng topi? Komen TOPI.", ["Anda geng", "topi?"], "TOPI", "Kongsi gaya!"),
 ], footnote=MED),
 V("62-pelanggan-tetap", D_, 39, ["#bisnesbarber", "#pelanggantetap", "#tipsbisnes", "#barbershopmalaysia", "#lelakimalaysia"], [
   hook("Macam mana nak jadikan pelanggan baharu, pelanggan tetap?", ["BAHARU JADI", "PELANGGAN", "TETAP"], [2], "person", "Ini caranya"),
   point("Ingat nama dan gaya kegemaran mereka.", ["INGAT", "NAMA"], "Dan gaya kegemaran", "chat", "nama"),
   point("Beri hasil yang konsisten setiap kali mereka datang.", ["HASIL", "KONSISTEN"], "Setiap kali datang", "check", "konsisten"),
   point("Hantar peringatan bila tiba masa untuk potong lagi.", ["HANTAR", "PERINGATAN"], "Bila tiba masa potong", "calendar", "peringatan"),
   point("Beri sebab untuk kembali, seperti kad kesetiaan.", ["KAD", "KESETIAAN"], "Sebab untuk kembali", "star", "kesetiaan"),
   tip("Pelanggan tetap ialah aset paling berharga untuk sebuah barbershop.", ["ASET PALING", "BERHARGA"], "Untuk setiap barbershop", "trophy", "aset"),
   cta("Barber, apa tips anda? Komen TIPS.", ["Apa tips", "anda?"], "TIPS", "Kongsi tips!"),
 ]),
 V("63-cukur-lebih-tebal", A_, 5, ["#mitosrambut", "#cukurkepala", "#faktarambut", "#tipsrambut", "#lelakimalaysia"], [
   hook("Betulkah mencukur kepala buat rambut tumbuh lebih tebal?", ["CUKUR KEPALA,", "RAMBUT", "LEBIH TEBAL?"], [2], "razor", "Mitos popular"),
   point("Ini mitos. Mencukur tidak mengubah bilangan atau ketebalan folikel rambut.", ["MITOS", "SEMATA"], "Folikel tak berubah", "cross", "mitos"),
   point("Rambut yang baru tumbuh terasa kasar, kerana hujungnya tumpul selepas dicukur.", ["HUJUNG", "TUMPUL"], "Sebab itu terasa kasar", "hair-texture", "tumpul"),
   point("Ia juga nampak lebih gelap, kerana belum terdedah kepada matahari.", ["NAMPAK", "GELAP"], "Belum terdedah matahari", "sun", "gelap"),
   tip("Nak rambut nampak lebih penuh? Pilih potongan dan produk yang sesuai.", ["POTONGAN", "YANG SESUAI"], "Nampak lebih penuh", "scissors", "potongan"),
   cta("Pernah percaya mitos ni? Komen MITOS.", ["Pernah percaya", "mitos ni?"], "MITOS", "Kongsi mitos lain!"),
 ]),
 V("64-evolusi-barbershop", E_, 50, ["#barbershop", "#sejarahbarber", "#barbermoden", "#barberlife", "#lelakimalaysia"], [
   hook("Dari kedai gunting tepi jalan, kepada barbershop moden. Beginilah evolusinya.", ["EVOLUSI", "BARBERSHOP"], [1], "shop", "Dulu dan kini"),
   point("Dulu, kedai gunting kecil dengan kerusi besi, dan pilihan gaya yang terhad.", ["DULU:", "RINGKAS"], "Kerusi besi, gaya terhad", "scissors", "dulu"),
   point("Kemudian, datang trend fade, skin fade, dan potongan yang lebih detail.", ["TREND", "FADE"], "Potongan lebih detail", "fade-mid", "fade"),
   point("Kini, tempahan dibuat dalam talian, dan ada servis grooming yang lengkap.", ["TEMPAHAN", "ONLINE"], "Servis grooming lengkap", "calendar", "talian"),
   point("Barbershop juga membina jenama sendiri, melalui media sosial.", ["JENAMA &", "MEDIA SOSIAL"], "Barbershop jadi jenama", "camera", "jenama"),
   cta("Anda suka barbershop lama atau moden? Komen MODEN.", ["Lama atau", "moden?"], "MODEN", "Kongsi pilihan!"),
 ]),
 V("65-jangan-pandang-rendah", C_, 30, ["#barberlife", "#hormatibarber", "#realitibarber", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Jangan pandang rendah pekerjaan seorang barber. Ini sebabnya.", ["JANGAN", "PANDANG", "RENDAH"], [2], "confident", "Ini sebabnya"),
   point("Setiap potongan memerlukan kemahiran yang diasah bertahun-tahun.", ["KEMAHIRAN", "BERTAHUN"], "Bukan kerja sehari", "scissors", "kemahiran"),
   point("Barber bertanggungjawab terhadap kebersihan dan keselamatan pelanggan.", ["KEBERSIHAN &", "KESELAMATAN"], "Alat tajam setiap hari", "check", "keselamatan"),
   point("Ramai barber menyara keluarga, dan membina perniagaan sendiri.", ["MENYARA", "KELUARGA"], "Bina perniagaan sendiri", "shop", "keluarga"),
   tip("Setiap kerja yang jujur dan mahir, layak dihormati.", ["LAYAK", "DIHORMATI"], "Kerja jujur & mahir", "trophy", "dihormati"),
   cta("Tag barber yang anda hormati. Komen BARBER.", ["Tag barber", "anda!"], "BARBER", "Hargai mereka!"),
 ]),
 V("66-produk-ikut-rambut", F_, 60, ["#produkrambut", "#jenisrambut", "#tipsrambut", "#rambutlelaki", "#menshairstyle"], [
   hook("Produk rambut yang sama, hasil yang berbeza. Kenapa? Sebab jenis rambut anda.", ["PILIH PRODUK", "IKUT JENIS", "RAMBUT"], [2], "jar", "Hasil berbeza ikut rambut"),
   point("Rambut nipis dan halus, pilih produk ringan seperti mousse atau styling powder.", ["RAMBUT", "NIPIS"], "Mousse atau styling powder", "powder", "nipis"),
   point("Rambut tebal dan kasar, perlukan pegangan kuat seperti wax atau pomade.", ["RAMBUT", "TEBAL"], "Wax atau pomade", "jar", "tebal"),
   point("Rambut kerinting, cuba krim yang melembutkan dan mengawal kembang.", ["RAMBUT", "KERINTING"], "Krim untuk kawal kembang", "hair-texture", "kerinting"),
   point("Kulit kepala berminyak, elakkan produk yang terlalu berat.", ["KULIT KEPALA", "BERMINYAK"], "Elak produk berat", "oil", "berminyak"),
   cta("Tak pasti jenis rambut anda? Komen JENIS, kami bantu.", ["Tak pasti", "jenis rambut?"], "JENIS", "Kami bantu!"),
 ]),
 V("67-ai-dan-barber", G_, 70, ["#ai", "#masadepan", "#barberlife", "#barbermalaysia", "#lelakimalaysia"], [
   hook("Adakah AI akan mengambil alih kerja barber?", ["AI GANTI", "BARBER?"], [1], "bolt", "Ini pandangan kami"),
   point("AI sudah membantu barbershop dengan tempahan, pemasaran, dan cadangan gaya.", ["AI SEBAGAI", "PEMBANTU"], "Tempahan, pemasaran, cadangan gaya", "camera", "tempahan"),
   point("Malah, video ini sendiri dihasilkan dengan bantuan AI.", ["VIDEO INI", "PUN AI"], "Dengan bantuan AI", "check", "video"),
   point("Tetapi AI tidak boleh menggunting rambut, atau memahami pelanggan seperti manusia.", ["SENTUHAN", "MANUSIA"], "Tak boleh diganti", "scissors", "menggunting"),
   tip("Barber yang menggunakan AI dengan bijak, akan lebih maju ke hadapan.", ["GUNA AI", "DENGAN BIJAK"], "Barber akan lebih maju", "trophy", "bijak"),
   follow("Ikuti kami untuk lebih banyak cerita di sebalik kerusi barber.", ["Ikuti kami untuk", "cerita di sebalik", "kerusi barber"], "Lebih daripada sekadar gunting rambut"),
 ], handle="@elasbarbershop.official", tagline="Lebih daripada sekadar gunting rambut."),
]
