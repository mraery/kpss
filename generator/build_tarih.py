# -*- coding: utf-8 -*-
"""
KPSS Tarih Müfredatı Tam Üretici (18 Ünite - 54 Ders - 540 Soru)
"""
import os
from common import (
    make_concept_card, make_mc, make_tf, make_fib, make_match,
    make_lesson, make_unit
)

def generate_tarih_dart():
    # 18 ünitenin tam listesi
    unit_defs = [
        # 1. İslamiyet Öncesi
        (1, "İslamiyet Öncesi Türk Tarihi & Kültür Medeniyet", "KPSS Tarih", 0xFF0284C7, [
            ("İlk Türk Devletleri ve Hükümdarlar", "Asya Hun, I. ve II. Göktürk, Uygurlar ve Boylar",
             "İslamiyet Öncesi Devlet Kurucuları",
             "- Asya Hun: Teoman kurucu, Mete Han en parlak dönem (MÖ 209 Onlu sistem).\n- I. Göktürk: Bumin Kağan kurucu (Türk adıyla ilk devlet), Mukan Kağan en parlak.\n- II. Göktürk (Kutluk): Kutluk Kağan kurucu (İlteriş unvanı), Bilge Kağan, Kül Tigin, Vezir Tonyukuk.\n- Uygurlar: Kutluk Bilge Kül Kağan kurucu, Bögü Kağan (Maniheizm dini, yerleşik hayat).",
             "Maniheizm Uygurlarda et yemeyi ve savaşı yasaklayarak savaşçılığı zayıflatmış fakat mimari, matbaa, şehirleşme ve minyatürü geliştirmiştir!", "🏹",
             [("mc", "Tarihte Türk adını resmi devlet adı olarak kullanan ve 38 harfli Orhun alfabesini oluşturan ilk Türk devleti hangisidir?",
               ["I. Göktürk Devleti", "Asya Hun Devleti", "Uygur Devleti", "Avarlar", "Hazarlar"], 0, "Bumin Kağan tarafından kurulan Göktürkler Türk adıyla kurulan ilk devlettir."),
              ("mc", "Bögü Kağan döneminde Maniheizmi kabul ederek yerleşik hayata geçen ve tapınak mimarisi başlatan ilk Türk devleti hangisidir?",
               ["Uygurlar", "Göktürkler", "Karahanlılar", "Hunlar", "Peçenekler"], 0, "Uygurlar Maniheizm dinini kabul ederek yerleşik hayata geçmiştir."),
              ("mc", "1071 Malazgirt Savaşı'nda Bizans ordusundan Selçuklu saflarına geçen Türk boyları hangileridir?",
               ["Peçenekler - Uzlar", "Hazarlar - Bulgarlar", "Avarlar - Macarlar", "Kıpçaklar - Kırgızlar", "Türgişler - Karluklar"], 0, "Peçenekler ve Uzlar Malazgirt Zaferi'nin kazanılmasında kilit rol oynamıştır."),
              ("mc", "Musevilik dinini benimseyen tek Türk devleti aşağıdakilerden hangisidir?",
               ["Hazarlar", "Avarlar", "Bulgarlar", "Kıpçaklar", "Macarlar"], 0, "Hazarlar Museviliği kabul eden tek Türk devletidir."),
              ("mc", "İstanbul'u Sasaniler ile birlikte iki kez kuşatan ilk Türk devleti hangisidir?",
               ["Avarlar (Juan-Juan)", "Hazarlar", "Hunlar", "Göktürkler", "Uygurlar"], 0, "Avarlar İstanbul'u tarihte ilk kuşatan Türk devletidir."),
              ("mc", "Kendi adına madeni para (Yarmak) bastıran ilk Türk hükümdarı kimdir?",
               ["Baga Tarkan (Türgişler)", "Bumin Kağan", "Mete Han", "Attila", "Kutluk Kağan"], 0, "Türgiş hükümdarı Baga Tarkan kendi adına para bastıran ilk kağandır."),
              ("tf", "İslamiyet öncesi Türk devletlerinde göçebe hayat sebebiyle hapis cezaları genelde 10 günü aşmazdı.",
               True, "Taşınabilir yaşam tarzı nedeniyle uzun süreli hapis cezası uygulanmazdı."),
              ("fib", "Orhun Abideleri'nde Türk milletini derleyip toparladığı için Kutluk Kağan'a ... unvanı verilmiştir.",
               ["İlteriş", "Aygucı", "Tarkan", "Tudun"], "İlteriş", "İlteriş devleti toparlayan, birleştiren demektir."),
              ("match", "Türk devletleri ile kurucularını eşleştiriniz:",
               [("Asya Hun", "Teoman"), ("I. Göktürk", "Bumin Kağan"), ("II. Göktürk", "Kutluk Kağan"), ("Uygurlar", "Kutluk Bilge Kül Kağan")], "Temel Türk devlet kurucularıdır.")]),
            ("Devlet Teşkilatı, Veraset ve Töre", "Kut İnancı, Kurultay, Sosyal Yapı ve Hukuk",
             "Devlet İdaresi ve Töre Kuralları",
             "- Kut: Devleti yönetme yetkisinin Gök Tengri tarafından hanedana verilmesi. Taht kavgalarına ve devletlerin bölünmesine yol açar.\n- Kurultay (Toy): Hakan, Hatun ve boy beylerinin katıldığı meclis.\n- İkili Teşkilat: Doğu (Kutsal, Hakan), Batı (Yabgu).\n- Töre: Hakan dahil herkesin uymak zorunda olduğu yazısız hukuk kurallarıdır.",
             "Kut kan yoluyla tüm erkek akrabalara geçtiği için 'veraset belirsizliği' yaşanmış ve devletler çok çabuk parçalanmıştır!", "👑",
             [("mc", "İslamiyet öncesi Türklerde hükümdarın olmadığı zamanlarda kurultaya başkanlık eden vezir hangisidir?",
               ["Aygucı (Üge)", "Tudun", "Buyruk", "Tarkan", "Tigin"], 0, "Aygucı başbakan yetkisindeki vezirdir."),
              ("mc", "Aşağıdakilerden hangisi İslamiyet öncesi Türk hükümdarlık alametlerinden biri DEĞİLDİR?",
               ["Hutbe okutmak", "Otağ (Çadır)", "Örgin (Taht)", "Tuğ (Sancak)", "Kotuz (Sorguç)"], 0, "Hutbe okutmak İslami bir hükümdarlık sembolüdür; İslamiyet öncesinde kesinlikle yoktur."),
              ("mc", "Türklerde cenaze törenlerine ..., mezar taşlarına ... ve ağıtlara ... denirdi. Sıralama nasıldır?",
               ["Yuğ - Balbal - Sagu", "Kurgan - Yuğ - Koşuk", "Balbal - Kurgan - Sagu", "Uçmağ - Balbal - Sav", "Yuğ - Tamu - Sagu"], 0, "Cenaze Yuğ, mezar taşı Balbal, ağıt Sagu'dur."),
              ("mc", "Türk toplumunda en küçük basamaktan en büyüğe doğru sosyal sıralama hangisidir?",
               ["Oguş - Urug - Boy - Bodun - İl", "Urug - Oguş - Boy - İl - Bodun", "Boy - Bodun - İl - Oguş - Urug", "Oguş - Boy - Urug - İl - Bodun", "İl - Bodun - Boy - Urug - Oguş"], 0, "Oguş (aile), Urug (sülale), Boy (kabile), Bodun (millet), İl (devlettir)."),
              ("mc", "Mete Han tarafından kurulan ve Türk ordusunun temeli sayılan askeri sistem hangisidir?",
               ["Onlu Teşkilat (MÖ 209)", "Tımar Sistemi", "Gulam Sistemi", "Yeniçeri Ocağı", "İkta Sistemi"], 0, "Mete Han MÖ 209'da Onlu Teşkilatı kurmuştur."),
              ("mc", "Törede hiçbir zaman değiştirilemeyen adalet ilkesi hangisidir?",
               ["Könilik", "Uzluk", "Tüzlük", "Kişilik", "Yarlık"], 0, "Könilik adalet demektir ve törenin değişmez çekirdeğidir."),
              ("tf", "İslamiyet öncesi Türk toplumunda Avrupa'daki gibi katı kölelik ve soylular sınıfı oluşmamıştır.",
               True, "Toprağın devlete ait olması feodal sınıf ayrımını engellemiştir."),
              ("fib", "İslamiyet öncesi Türklerde cennet kavramına ... denirdi.",
               ["Uçmağ", "Tamu", "Kurgan", "Kam"], "Uçmağ", "Uçmağ cennet, Tamu cehennemdir."),
              ("match", "Kavramları eşleştiriniz:",
               [("Kurgan", "Mezar"), ("Uçmağ", "Cennet"), ("Tamu", "Cehennem"), ("Balbal", "Mezar taşı")], "Türk inanç ve defin kavramlarıdır.")]),
            ("İslamiyet Öncesi Türk Tarihi Kupa Sınavı 🏆", "Tüm Konuları Kapsayan Kupa Denemesi",
             "Kupa Sınavı Hap Bilgileri",
             "- İlk yazılı Türk abideleri: Orhun Abideleri (II. Göktürk).\n- İlk vezir ve anı yazarı: Vezir Tonyukuk.\n- En uzun destan: Manas Destanı (Kırgızlar).\n- İlk Türk şairi: Aprınçur Tigin (Uygurlar).",
             "ÖSYM Soru Tuzağı: İslamiyet öncesinde 'Para bastırmak', 'Hilat giymek', 'Menşur almak' ve 'Hutbe' yoktur!", "🏆",
             [("mc", "Orhun Abideleri hangi devlet döneminde dikilmiştir?",
               ["II. Göktürk (Kutluk)", "I. Göktürk", "Asya Hun", "Uygurlar", "Karahanlılar"], 0, "Orhun Abideleri II. Göktürk döneminde dikilmiştir."),
              ("mc", "Avrupa Hun hükümdarı Attila Avrupalılarca hangi unvanla anılmıştır?",
               ["Tanrının Kırbacı (Flagellum Dei)", "Cesur Kral", "Güneşin Hakanı", "Büyük İlteriş", "Yabgu"], 0, "Attila Tanrının Kırbacı olarak adlandırılmıştır."),
              ("mc", "Moğol hakimiyetini kabul eden ilk Türk devleti hangisidir?",
               ["Kırgızlar", "Uygurlar", "Karluklar", "Hazarlar", "Türgişler"], 0, "Moğollara itaat eden ilk Türk devleti Kırgızlardır."),
              ("mc", "Orhun Abideleri'ni Danimarkalı dilbilimci Vilhelm Thomsen çözerken okuduğu ilk kelime hangisidir?",
               ["Tengri (Tanrı)", "Türk", "Kül Tigin", "Kağan", "Orhun"], 0, "Thomsen yazıtlarda ilk olarak 'Tengri' kelimesini çözmüştür."),
              ("mc", "Türk tarihinin ilk veziri, ilk tarihçisi ve Türklerin 'Bismark'ı olarak anılan devlet adamı kimdir?",
               ["Vezir Tonyukuk", "Bumin Kağan", "İlteriş Kağan", "Bögü Kağan", "Mukan Kağan"], 0, "Vezir Tonyukuk kendi anıtını dikerek tarihteki ilk Türk anı yazarı olmuştur."),
              ("mc", "Dünyanın en uzun destanı olan Manas Destanı kime aittir?",
               ["Kırgızlar", "Kazaklar", "Özbekler", "Uygurlar", "Kıpçaklar"], 0, "Manas Destanı Kırgızlara aittir."),
              ("tf", "Orhun Abideleri Bilge Kağan, Kül Tigin ve Vezir Tonyukuk adına dikilmiştir.",
               True, "Orhun Abideleri Moğolistan sınırlarında bulunan 3 ana taştan oluşur."),
              ("fib", "İslamiyet öncesi Türklerde askeri valiye ... denirdi.",
               ["Tutuk", "Tudun", "Buyruk", "Tarkan"], "Tutuk", "Tutuk askeri vali, Tudun vergi memurudur."),
              ("match", "Destanları boylarla eşleştiriniz:",
               [("Ergenekon", "Göktürkler"), ("Türeyiş", "Uygurlar"), ("Oğuz Kağan", "Hunlar"), ("Manas", "Kırgızlar")], "Milli Türk destanlarıdır.")],
             True)
        ]),
        # 2. İlk Müslüman Türk Devletleri
        (2, "İlk Müslüman Türk Devletleri & Türk-İslam Medeniyeti", "KPSS Tarih", 0xFF0284C7, [
            ("Devletler ve Siyasi Tarih", "Karahanlılar, Gazneliler, Büyük Selçuklu ve Mısır Devletleri",
             "İlk Türk-İslam Devletleri Özeti",
             "- Talas Savaşı (751): Karluklar Abbasilere yardım etti, İslamlaşma başladı, kağıt Çin dışına çıktı.\n- Karahanlılar: Orta Asya'da ilk Müslüman Türk devleti. Satuk Buğra Han Müslüman oldu. Resmi dil Türkçe!\n- Gazneliler: Sultan unvanını ilk kullanan Gazneli Mahmut'tur.\n- Büyük Selçuklu: 1040 Dandanakan ile kuruldu, 1071 Malazgirt ile Anadolu kapıları açıldı.",
             "Karahanlılar milli kimliğini koruyarak resmi dili Türkçe yapmıştır. Gazneli ve Selçuklularda Farsça ve Arapça öne çıkmıştır!", "🕌",
             [("mc", "Tarihte 'Sultan' unvanını kullanan ilk Türk hükümdarı kimdir?",
               ["Gazneli Mahmut", "Tuğrul Bey", "Alparslan", "Melikşah", "Satuk Buğra Han"], 0, "Abbaso Halifesi Şii tehlikesine karşı koruduğu için Gazneli Mahmut'a Sultan unvanını vermiştir."),
              ("mc", "Büyük Selçuklu Devleti'nin resmen kurulmasını sağlayan ve Gaznelileri yıkan 1040 savaşı hangisidir?",
               ["Dandanakan Savaşı", "Pasinler Savaşı", "Malazgirt Savaşı", "Katvan Savaşı", "Yassıçemen Savaşı"], 0, "Dandanakan Savaşı ile Büyük Selçuklu kurulmuştur."),
              ("mc", "1071 Malazgirt Zaferi'nden sonra Halife Sultan Alparslan'a hangi unvanı vermiştir?",
               ["Ebu'l Feth (Fetihlerin Babası)", "Sultanu'l Azam", "Şah-ı Cihan", "Sultan-ı Rum", "Melikü'l Mülk"], 0, "Alparslan Ebu'l Feth unvanını almıştır."),
              ("mc", "Mısır'da kurulan ve Hicaz'a (Mekke-Medine) egemen olan ilk Türk-İslam devleti hangisidir?",
               ["İhşidiler (Akşitler)", "Tolunoğulları", "Eyyubiler", "Memlükler", "Osmanlılar"], 0, "İhşidiler kutsal topraklara hakim olan ilk Türk devletidir."),
              ("mc", "1187 Hıttin Savaşı ile Kudüs'ü Haçlılardan kurtaran hükümdar kimdir?",
               ["Selahaddin Eyyubi", "Sultan Baybars", "Nurettin Zengi", "Alparslan", "Kılıç Arslan"], 0, "Selahaddin Eyyubi Kudüs Fatihi unvanını almıştır."),
              ("mc", "Moğolları tarihte ilk kez 1260 Ayn Calut Savaşı'nda mağlup eden devlet hangisidir?",
               ["Memlükler", "Büyük Selçuklu", "Eyyubiler", "Harzemşahlar", "Altın Orda"], 0, "Sultan Baybars komutasındaki Memlükler Moğolları durdurmuştur."),
              ("tf", "Talas Savaşı'ndan sonra kağıt Çin dışında ilk kez Semerkant'ta üretilmiştir.",
               True, "Semerkant kağıt üretim merkezi olmuş ve Şehirlerin Şahı unvanını almıştır."),
              ("fib", "Büyük Selçuklu Devleti'nde Hasan Sabbah'ın kurduğu ... tarikatı devlete suikastlar düzenlemiştir.",
               ["Batinilik (Haşhaşiler)", "Babailik", "Hurufilik", "Bektaşilik"], "Batinilik (Haşhaşiler)", "Batinilik Nizamülmülk dahil birçok devlet adamını şehit etmiştir."),
              ("match", "Şehir unvanlarını eşleştiriniz:",
               [("Buhara", "İslam'ın Roması"), ("Semerkant", "Şehirlerin Şahı"), ("İsfahan", "Nısf-ı Cihan"), ("Kaşgar", "Işıldayan İnci")], "Tarihi Türk-İslam şehirleri unvanlarıdır.")]),
            ("Kültür, Edebiyat ve Bilim", "İlk Edebi Eserler, Farabi, İbn-i Sina ve Harezmi",
             "İlk Edebi Eserler Tablosu",
             "- Kutadgu Bilig (Yusuf Has Hacip): İlk Türk-İslam eseri, siyasetnamedir.\n- Divanü Lugati't-Türk (Kaşgarlı Mahmut): İlk Türkçe sözlük, ansiklopedi ve ilk dünya haritası.\n- Atabetü'l-Hakayık (Edip Ahmet Yükneki): Hakikatlerin eşiği, ahlak kitabıdır.\n- Divan-ı Hikmet (Ahmet Yesevi): İlk tasavvuf eseridir.",
             "ÖSYM bu 4 eseri yazarları ve içerikleri bakımından eşleştirme sorusu olarak defalarca sormuştur!", "📚",
             [("mc", "Türk tarihinin ilk siyasetnamesi kabul edilen ve mutluluk veren bilgi anlamına gelen eser hangisidir?",
               ["Kutadgu Bilig", "Divanü Lugati't-Türk", "Siyasetname", "Atabetü'l-Hakayık", "Divan-ı Hikmet"], 0, "Yusuf Has Hacip Kutadgu Bilig'in yazarıdır."),
              ("mc", "Araplara Türkçeyi öğretmek amacıyla ilk Türkçe sözlüğü yazan ve ilk dünya haritasını çizen bilgin kimdir?",
               ["Kaşgarlı Mahmut", "Yusuf Has Hacip", "Farabi", "Biruni", "Harezmi"], 0, "Kaşgarlı Mahmut Divanü Lugati't-Türk eserini yazmıştır."),
              ("mc", "Batıda 'Avicenna' olarak tanınan ve 'El-Kanun fi't-Tıbb' kitabının yazarı olan İslam bilgini kimdir?",
               ["İbn-i Sina", "Farabi", "İbn-i Rüşd", "Razi", "Gazali"], 0, "İbn-i Sina tıbbın hükümdarıdır."),
              ("mc", "Aristo'dan sonra felsefe alanında 'Muallim-i Sani' (İkinci Öğretmen) unvanını alan filozof kimdir?",
               ["Farabi", "İbn-i Sina", "Gazali", "Harezmi", "Biruni"], 0, "Farabi Muallim-i Sani unvanlı büyük filozoftur."),
              ("mc", "Sıfır (0) rakamını ilk kez matematiğe kazandıran ve cebir ilminin kurucusu kabul edilen bilgin kimdir?",
               ["Harezmi", "Ömer Hayyam", "Ali Kuşçu", "Biruni", "Nasirüddin Tusi"], 0, "Harezmi cebrin kurucusudur."),
              ("mc", "Gazneli Mahmut'un 'Sarayımın en değerli hazinesidir' dediği ünlü astronom kimdir?",
               ["Biruni", "Farabi", "İbn-i Heysem", "Uluğ Bey", "Ali Şir Nevai"], 0, "Biruni dünyanın çapını ve eksen eğikliğini hesaplamıştır."),
              ("tf", "Nizamiye Medreseleri Vezir Nizamülmülk tarafından Bağdat'ta kurulan üniversite düzeyindeki kurumlardır.",
               True, "Batinilik tehlikesine karşı ilmi savunma amacıyla açılmıştır."),
              ("fib", "Felsefede Aristo'dan sonra 'Muallim-i Sani' unvanını alan Türk-İslam düşünürü ...'dir.",
               ["Farabi", "İbn-i Sina", "Gazali", "Harezmi"], "Farabi", "Farabi pozitif bilimlerin kurucularındandır."),
              ("match", "Eserleri yazarları ile eşleştiriniz:",
               [("Kutadgu Bilig", "Yusuf Has Hacip"), ("Divanu Lugati't-Türk", "Kaşgarlı Mahmut"), ("Atabetü'l-Hakayık", "Edip Ahmet Yükneki"), ("Divan-ı Hikmet", "Ahmet Yesevi")], "Temel Türk-İslam klasik eserleridir.")]),
            ("İlk Türk-İslam Devletleri Kupa Sınavı 🏆", "Devlet Teşkilatı, İkta ve Sınav Soruları",
             "Türk-İslam İdari Teşkilatı",
             "- İkta Sistemi: Toprak gelirlerinin asker besleme karşılığı verilmesidir (Hazineye yük olmadan ordu yetiştirir).\n- Gulam Sistemi: Saray ordusu yetiştirme sistemi.\n- Ribat: Kervansaray ve sınır karakolu yapılarıdır.\n- Muhtesip: Çarşı ve pazar denetçisi zabıtadır.",
             "İkta sistemi hem Büyük Selçuklu'da uygulanmış hem Osmanlı'daki Tımar sistemine ilham vermiştir!", "🏆",
             [("mc", "Büyük Selçuklu'da Alparslan ve Melikşah'a vezirlik yapan, Siyasetname'yi yazan devlet adamı kimdir?",
               ["Nizamülmülk", "Ali Şir Nevai", "Sadrettin Konevi", "Köprülü Mehmet", "Kemalettin İsmail"], 0, "Nizamülmülk Nizamiye Medreseleri ve Siyasetname ile tanınır."),
              ("mc", "Celali Takvimi'ni Sultan Melikşah adına hazırlayan ünlü bilgin ve şair kimdir?",
               ["Ömer Hayyam", "Ali Kuşçu", "Uluğ Bey", "Harezmi", "Nasirüddin Tusi"], 0, "Ömer Hayyam Celali Takvimi'ni hazırlamıştır."),
              ("mc", "Türk-İslam devletlerinde çarşı, pazar ve esnafı denetleyen görevli hangisidir?",
               ["Muhtesip", "Hacib", "Emir-i Dad", "Subaşı", "Kadı"], 0, "Muhtesip piyasa denetimi zabıtasıdır."),
              ("mc", "Memlük Devleti'nde diğer Türk devletlerinden farklı olarak veraset sisteminde hangi kural geçerliydi?",
               ["Her güçlü emirin sultan olabilme hakkı vardı", "Kut sadece padişahın büyük oğluna geçerdi", "Hükümdarı halk seçerdi", "Kadınlar da hükümdar olabilirdi", "Yabancı prensler tahta çıkabilirdi"], 0, "Memlüklerde komutanlar tahta geçebildiği için sık sık taht değişikliği yaşanmıştır."),
              ("mc", "İlk Türk-İslam devletlerinde kervansaray niteliği taşıyan ilk yapılara ne ad verilirdi?",
               ["Ribat", "Kümbet", "Külliye", "İmaret", "Tekke"], 0, "Ribatlar kervansarayların öncüsüdür."),
              ("mc", "Aşağıdakilerden hangisi Büyük Selçuklu'nun yıkılmasıyla ortaya çıkan Atabeyliklerden biri DEĞİLDİR?",
               ["Danişmentliler", "Zengiler", "Böriler", "İldenizoğulları", "Salgurlular"], 0, "Danişmentliler I. Dönem Türk beyliğidir."),
              ("tf", "İkta sahipleri aldıkları vergilerin bir kısmıyla 'Cebelü' adı verilen atlı asker beslemek zorundaydı.",
               True, "İkta sistemi Selçuklu ordusunun omurgasını oluşturan Cebelü süvarilerini yetiştirirdi."),
              ("fib", "Türk-İslam devletlerinde adaletten sorumlu şeri davalara bakan hakimlere ... denirdi.",
               ["Kadı", "Subaşı", "Muhtesip", "Amit"], "Kadı", "Kadılar şeri hukuku uygulardı."),
              ("match", "Kavramları eşleştiriniz:",
               [("İkta", "Toprak gelirli askerlik"), ("Gulam", "Saray köle askerleri"), ("Ribat", "Kervansaray"), ("Hacib", "Hükümdar başdanışmanı")], "Türk-İslam idari kurumlarıdır.")],
             True)
        ])
    ]
    
    # 3'ten 18'e kadar olan kalan ünitelerin şablonlu otomatik jeneratörü
    tarih_units_remaining = [
        (3, "Türkiye Selçuklu Devleti & Anadolu Beylikleri", [
            ("Anadolu'nun Fethi ve I. Beylikler", "Malazgirt Sonrası Kurulan Beylikler (Saltuk, Mengücek, Danişment, Artuk, Çaka)"),
            ("Türkiye Selçuklu Siyasi Tarihi", "Miryokefalon (Yurttutan), Kösedağ ve II. Beylikler Dönemi"),
            ("Selçuklu Ticareti, Ahilik ve Kültür Medeniyet 🏆", "Kervansaraylar, Ahilik Teşkilatı, Sigorta ve Kupa Sınavı")
        ]),
        (4, "Osmanlı Devleti Kuruluş Dönemi (1299-1453)", [
            ("Beylikten Devlete Geçiş", "Osman Bey, Orhan Bey, İskan ve İstimalet Politikaları"),
            ("Balkanlarda Fetihler ve Savaşlar", "Sırpsındığı, I. Kosova, Niğbolu, Ankara Savaşı ve Fetret Devri"),
            ("Kuruluş Dönemi Kupa Sınavı 🏆", "Varna, II. Kosova ve Kuruluş Dönemi Özeti")
        ]),
        (5, "Osmanlı Devleti Yükselme Dönemi (Dünya Gücü Osmanlı)", [
            ("Fatih Sultan Mehmet ve İstanbul'un Fethi", "1453 Fethi, Balkan ve Anadolu Fetihleri, Kanunname-i Ali Osman"),
            ("Yavuz Sultan Selim ve Kanuni Sultan Süleyman", "Çaldıran, Turnadağ, Ridaniye, Mohaç, Preveze ve Kapitülasyonlar"),
            ("Yükselme Dönemi Kupa Sınavı 🏆", "Sokullu Dönemi, Hint Deniz Seferleri ve Kupa Sınavı")
        ]),
        (6, "Osmanlı Kültür ve Medeniyeti - Devlet Teşkilatı & Divan", [
            ("Merkez Teşkilatı ve Padişah", "Veraset Sistemindeki Değişimler, Saray Bölümleri ve Harem"),
            ("Divan-ı Hümayun ve Yönetici Sınıflar", "Seyfiye, İlmiye, Kalemiye Sınıfları ve Divan Üyeleri"),
            ("Devlet Teşkilatı Kupa Sınavı 🏆", "Sadrazam, Şeyhülislam, Kazasker, Nişancı ve Kupa Sınavı")
        ]),
        (7, "Osmanlı Kültür ve Medeniyeti - Toprak, Ordu & Hukuk", [
            ("Toprak Sistemi ve Tımar", "Miri, Mülk, Vakıf Topraklar ve Dirlik Dağılımı"),
            ("Osmanlı Askeri Teşkilatı", "Kapıkulu Ocağı, Yeniçeriler, Tımarlı Sipahiler ve Donanma"),
            ("Toprak ve Ordu Kupa Sınavı 🏆", "Vergi Sistemi, Hukuk, Lonca ve Kupa Sınavı")
        ]),
        (8, "Osmanlı Duraklama Dönemi (XVII. Yüzyıl Arayış Yılları)", [
            ("İç İsyanlar ve Sebepleri", "Celali, İstanbul (Yeniçeri) ve Eyalet İsyanları"),
            ("XVII. Yüzyıl Siyasi Olayları ve Antlaşmalar", "Ferhat Paşa, Kasr-ı Şirin, Bucaş, Karlofça ve İstanbul Antlaşmaları"),
            ("Duraklama Dönemi Kupa Sınavı 🏆", "II. Osman, IV. Murat, Tarhuncu, Köprülüler ve Kupa Sınavı")
        ]),
        (9, "Osmanlı Gerileme Dönemi ve Islahatlar (XVIII. Yüzyıl)", [
            ("Lale Devri ve Yenilikler", "Pasarofça, İbrahim Müteferrika, İlk Elçilikler ve Tulumbacılar"),
            ("XVIII. Yüzyıl Siyasi Olayları", "Prut, Belgrad, Küçük Kaynarca, Yaş ve Ziştovi Antlaşmaları"),
            ("Gerileme Dönemi Kupa Sınavı 🏆", "III. Selim (Nizam-ı Cedit), Askeri Islahatlar ve Kupa Sınavı")
        ]),
        (10, "Osmanlı Dağılma Dönemi ve Fikir Akımları (XIX. Yüzyıl)", [
            ("Demokratikleşme Belgeleri", "Sened-i İttifak, Tanzimat Fermanı, Islahat Fermanı ve Kanun-i Esasi"),
            ("I. ve II. Meşrutiyet Dönemleri", "İttihat ve Terakki, 31 Mart Vakası ve Duyun-ı Umumiye"),
            ("Dağılma Dönemi Kupa Sınavı 🏆", "Fikir Akımları: Osmanlıcılık, İslamcılık, Türkçülük ve Kupa Sınavı")
        ]),
        (11, "XX. Yüzyıl Başlarında Osmanlı ve I. Dünya Savaşı", [
            ("Trablusgarp ve Balkan Savaşları", "Uşi Antlaşması, I. ve II. Balkan Savaşları ve Kaybedilen Topraklar"),
            ("I. Dünya Savaşı Cepheleri", "Kafkas, Kanal, Çanakkale, Irak, Hicaz-Yemen Cepheleri"),
            ("I. Dünya Savaşı Kupa Sınavı 🏆", "Mondros Ateşkesi, Wilson İlkeleri, Gizli Antlaşmalar ve Kupa Sınavı")
        ]),
        (12, "Kurtuluş Savaşı Hazırlık Dönemi", [
            ("Genelgeler Dönemi", "Samsun'a Çıkış, Havza Genelgesi ve Amasya Genelgesi"),
            ("Kongreler ve Misak-ı Milli", "Erzurum Kongresi, Sivas Kongresi, Amasya Görüşmeleri ve Misak-ı Milli"),
            ("Hazırlık Dönemi Kupa Sınavı 🏆", "Heyet-i Temsiliye, Yararlı/Zararlı Cemiyetler ve Kupa Sınavı")
        ]),
        (13, "I. TBMM Dönemi, Ayaklanmalar ve Sevr Antlaşması", [
            ("I. TBMM'nin Açılışı ve Özellikleri", "Meclis Hükümeti Sistemi, Yasama-Yürütme Birliği ve Kanunlar"),
            ("TBMM'ye Karşı Ayaklanmalar ve Sevr", "Hıyanet-i Vataniye, İstiklal Mahkemeleri ve Sevr'in Hukuki Durumu"),
            ("I. TBMM Kupa Sınavı 🏆", "Bilecik Görüşmeleri, Düzenli Ordunun Kurulması ve Kupa Sınavı")
        ]),
        (14, "Kurtuluş Savaşı Muharebeler Dönemi ve Antlaşmalar", [
            ("Doğu ve Güney Cepheleri", "Gümrü Antlaşması, Maraş-Antep-Urfa Savunması ve Ankara Antlaşması"),
            ("Batı Cephesi Savaşları", "I. İnönü, II. İnönü, Kütahya-Eskişehir, Sakarya ve Büyük Taarruz"),
            ("Muharebeler Dönemi Kupa Sınavı 🏆", "Mudanya Ateşkesi, Lozan Barış Antlaşması ve Kupa Sınavı")
        ]),
        (15, "Atatürk İlkeleri ve Türk İnkılabı", [
            ("Atatürk'ün 6 Temel İlkesi", "Cumhuriyetçilik, Milliyetçilik, Halkçılık, Devletçilik, Laiklik, İnkılapçılık"),
            ("Siyasi ve Hukuki İnkılaplar", "Saltanatın Kaldırılması, Cumhuriyetin İlanı, Halifelik, Medeni Kanun"),
            ("Atatürk İlkeleri Kupa Sınavı 🏆", "Eğitim, Kültür ve Toplumsal İnkılaplar ve Kupa Sınavı")
        ]),
        (16, "Atatürk Dönemi İç ve Dış Politika (1923-1938)", [
            ("Çok Partili Hayat Denemeleri", "CHF, TCF, SCF, Şeyh Sait İsyanı, İzmir Suikastı, Menemen Olayı"),
            ("1923-1938 Dış Politika Gelişmeleri", "Musul, Nüfus Mübadelesi, Bozkurt-Lotus, Balkan Antantı, Sadabat Paktı"),
            ("Atatürk Dönemi Kupa Sınavı 🏆", "Montrö Boğazlar Sözleşmesi, Hatay'ın Anavatana Katılması ve Kupa Sınavı")
        ]),
        (17, "Çağdaş Türk ve Dünya Tarihi - II. Dünya Savaşı & Soğuk Savaş", [
            ("İki Savaş Arası Dönem ve II. Dünya Savaşı", "1929 Ekonomik Buhranı, Mihver-Müttefik Blokları ve Türkiye'nin Tutumu"),
            ("Soğuk Savaş Dönemi", "Truman Doktrini, Marshall Planı, NATO, Varşova Paktı ve Kore Savaşı"),
            ("Soğuk Savaş Kupa Sınavı 🏆", "Türkiye'nin NATO'ya Girişi, Bağdat Paktı, Balkan Paktı ve Kupa Sınavı")
        ]),
        (18, "Çağdaş Türk ve Dünya Tarihi - Yumuşama Dönemi ve Sonrası", [
            ("Yumuşama (Detant) Dönemi Olayları", "Küba Krizi, Vietnam Savaşı, Kıbrıs Barış Harekatı ve ASALA"),
            ("SSCB'nin Dağılması ve Türk Cumhuriyetleri", "TİKA, TÜRKSOY, Karabağ Savaşı, Bosna Savaşı ve 21. Yüzyıl"),
            ("Çağdaş Tarih Kupa Sınavı 🏆", "Orta Doğu Gelişmeleri, Körfez Savaşları ve Çağdaş Tarih Kupa Sınavı")
        ])
    ]
    
    # Kalan 16 ünite için zengin soru üreteci
    from gen_tarih_questions import build_unit_questions
    for u_num, u_title, lessons in tarih_units_remaining:
        unit_lessons_data = []
        for l_idx, (l_title, l_desc) in enumerate(lessons):
            is_exam = (l_idx == len(lessons) - 1)
            q_list = build_unit_questions(u_num, l_idx + 1, l_title, is_exam)
            unit_lessons_data.append((l_title, l_desc, q_list["concept_title"], q_list["concept_rule"],
                                     q_list["concept_tip"], q_list["concept_emoji"], q_list["questions"], is_exam))
        unit_defs.append((u_num, u_title, "KPSS Tarih", 0xFF0284C7, unit_lessons_data))
        
    # Dart kodunu birleştir
    dart_lines = [
        "import '../models/lesson_models.dart';",
        "",
        "/// KPSS Quest - KPSS Tarih Müfredatı (18 Ünite - 54 Ders - 540 Soru)",
        "final List<LearningUnit> kpssTarihUnits = [",
    ]
    
    for u_num, u_title, subj, color, l_list in unit_defs:
        lessons_code = []
        for l_idx, l_tuple in enumerate(l_list):
            is_exam = (len(l_tuple) == 8 and l_tuple[7])
            l_title, l_desc, c_title, c_rule, c_tip, c_emoji, questions = l_tuple[:7]
            l_id = f"kpss_tar_u{u_num}_l{l_idx+1}"
            
            q_code_items = []
            # 1. Soru: Concept Card
            q_code_items.append(make_concept_card(
                f"{l_id}_q1", c_title, c_rule, c_tip, c_emoji
            ))
            # 2..10. Sorular
            for q_idx, q in enumerate(questions):
                qid = f"{l_id}_q{q_idx+2}"
                q_type = q[0]
                if q_type == "mc":
                    q_code_items.append(make_mc(qid, q[1], q[2], q[3], q[4]))
                elif q_type == "tf":
                    q_code_items.append(make_tf(qid, q[1], q[2], q[3]))
                elif q_type == "fib":
                    q_code_items.append(make_fib(qid, q[1], q[2], q[3], q[4]))
                elif q_type == "match":
                    q_code_items.append(make_match(qid, q[1], q[2], q[3]))
            
            lessons_code.append(make_lesson(l_id, l_title, l_desc, q_code_items, is_unit_exam=is_exam))
            
        u_id = f"kpss_tar_u{u_num}"
        dart_lines.append(make_unit(u_id, u_num, u_title, subj, hex(color), lessons_code))
        
    dart_lines.append("];")
    return "\n".join(dart_lines)

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "lib", "data")
    out_file = os.path.join(out_dir, "kpss_tarih_units.dart")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(generate_tarih_dart())
    print(f"kpss_tarih_units.dart başarıyla üretildi: {out_file}")
