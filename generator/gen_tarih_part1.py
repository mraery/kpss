# -*- coding: utf-8 -*-
"""
KPSS Tarih Müfredatı ve Soru Üreticisi (18 Ünite - 54 Ders - 540 Soru)
"""
import os
from common import (
    make_concept_card, make_mc, make_tf, make_fib, make_match,
    make_lesson, make_unit, esc
)

def get_tarih_units():
    units_data = [
        # Ünite 1
        {
            "id": "kpss_tar_u1",
            "num": 1,
            "title": "İslamiyet Öncesi Türk Tarihi & Kültür Medeniyet",
            "subject": "KPSS Tarih",
            "color": "0xFF0284C7",
            "lessons": [
                {
                    "title": "İlk Türk Devletleri ve Siyasi Tarih",
                    "desc": "Asya Hun, I. ve II. Göktürk, Uygurlar ve Diğer Türk Boyları",
                    "concept": {
                        "title": "İslamiyet Öncesi Devlet Kurucuları ve Hükümdarlar",
                        "rule": "- Asya Hun: Teoman (kurucu), Mete Han (en parlak, onlu ordu sistemi, Islıklı ok).\n- I. Göktürk: Bumin Kağan (kurucu), Mukan Kağan (en parlak). Türk adıyla kurulan ilk devlet.\n- II. Göktürk (Kutluk): Kutluk Kağan (İlteriş unvanı, kurucu), Bilge Kağan, Kültigin, Vezir Tonyukuk.\n- Uygurlar: Kutluk Bilge Kül Kağan (kurucu), Bögü Kağan (Maniheizmi kabul etti, yerleşik hayata geçildi).",
                        "tip": "Maniheizm dini et yemeyi ve savaşmayı yasakladığı için Uygurların savaşçı özelliğini zayıflatmış fakat mimari, şehircilik, minyatür, fresko ve matbaa gibi kültürel alanlarda çığır açmıştır!",
                        "emoji": "🏹"
                    },
                    "questions": [
                        ("mc", "Tarihte Türk adını resmi bir devlet adı olarak kullanan ve 38 harfli Orhun alfabesini oluşturan ilk Türk devleti hangisidir?",
                         ["I. Göktürk Devleti", "Asya Hun Devleti", "Uygur Devleti", "Avarlar", "Hazarlar"], 0,
                         "Göktürkler (Kök Türkler) tarihte 'Türk' adını ilk defa resmi devlet adı olarak kullanan devlettir."),
                        ("mc", "Bögü Kağan döneminde Maniheizm dinini kabul ederek yerleşik hayata geçen, tapınak ve saray mimarisi geliştiren ilk Türk devleti aşağıdakilerden hangisidir?",
                         ["Uygurlar", "Göktürkler", "Karahanlılar", "Hunlar", "Peçenekler"], 0,
                         "Uygurlar Maniheizm dinini kabul ederek çadır ve göçebe yaşamdan yerleşik şehircilik ve tapınak mimarisine geçen ilk Türk devletidir."),
                        ("mc", "Bizans ordusunda ücretli askerlik yaparken 1071 Malazgirt Savaşı'nda Büyük Selçuklu saflarına geçerek savaşın kazanılmasında rol oynayan Türk toplulukları hangisinde birlikte verilmiştir?",
                         ["Peçenekler - Uzlar (Oğuzlar)", "Hazarlar - Avarlar", "Bulgarlar - Macarlar", "Kırgızlar - Karluklar", "Türgişler - Kıpçaklar"], 0,
                         "Peçenekler ve Uzlar Bizans ordusunda paralı askerlik yaparken Malazgirt Savaşı sırasında Selçuklu tarafına geçmiştir."),
                        ("tf", "İslamiyet öncesi Türk devletlerinde göçebe yaşam tarzı nedeniyle uzun süreli hapis cezaları yaygın olarak uygulanmıştır.",
                         False, "Göçebe yaşam nedeniyle hapis cezaları genelde 10 günü aşmaz, taşınabilir ve kısa süreli cezalar uygulanırdı."),
                        ("fib", "Orhun Abideleri'nde Türk milletini derleyip toparladığı için ... unvanı verilen hükümdar Kutluk Kağan'dır.",
                         ["İlteriş", "Aygucı", "Tarkan", "Tudun"], "İlteriş",
                         "Kutluk Kağan'a devleti toparlayan, birleştiren anlamında 'İlteriş' unvanı verilmiştir."),
                        ("match", "Türk devletleri ile kurucularını eşleştiriniz:",
                         [("Asya Hun", "Teoman"), ("I. Göktürk", "Bumin Kağan"), ("II. Göktürk", "Kutluk Kağan"), ("Uygurlar", "Kutluk Bilge Kül Kağan")],
                         "Asya Hun kurucusu Teoman, I. Göktürk kurucusu Bumin, II. Göktürk Kutluk, Uygur Kutluk Bilge Kül Kağan'dır."),
                        ("mc", "Musevilik dinini benimseyen tek Türk devleti olup Hazar Barış Çağı'nı (Pax Hazarica) yaşatan devlet hangisidir?",
                         ["Hazarlar", "Avarlar", "Bulgarlar", "Kıpçaklar", "Macarlar"], 0,
                         "Hazarlar Museviliği kabul eden ilk ve tek Türk devletidir. Ticaret yollarını güvenceye alarak barış çağı yaşatmışlardır."),
                        ("mc", "İstanbul'u Sasaniler ile birlikte iki kez kuşatan ilk Türk devleti aşağıdakilerden hangisidir?",
                         ["Avarlar (Juan-Juan)", "Hazarlar", "Hunlar", "Göktürkler", "Uygurlar"], 0,
                         "Avarlar hem Asya'da hem Avrupa'da devlet kurmuş ve İstanbul'u tarihte ilk kez kuşatan Türk devleti olmuştur."),
                        ("mc", "Kendi adına para bastıran ilk Türk hükümdarı kimdir ve hangi devletin başındadır?",
                         ["Baga Tarkan - Türgişler", "Mete Han - Hunlar", "Bumin Kağan - Göktürkler", "Bögü Kağan - Uygurlar", "Bilge Kağan - Göktürkler"], 0,
                         "Türgiş hükümdarı Baga Tarkan kendi adına madeni para (Yarmak) bastıran ilk Türk hükümdarıdır.")
                    ]
                },
                {
                    "title": "İslamiyet Öncesi Kültür, Teşkilat ve Hukuk",
                    "desc": "Kut Anlayışı, Kurultay, Veraset ve Töre",
                    "concept": {
                        "title": "Devlet Teşkilatı Kavramları",
                        "rule": "- Kut: Devleti yönetme yetkisinin Gök Tengri tarafından hükümdara verildiği inancı. Kan yoluyla hanedanın tüm erkeklerine geçer.\n- Kurultay (Toy / Kengeş): Devlet işlerinin görüşüldüğü meclis. Katılanlara 'Toygun' denir. Hatun da katılır.\n- İkili Teşkilat: Doğu (Kutsal, Hakan yönetir), Batı (Yabgu yönetir).\n- Töre: Sözlü hukuk kurallarıdır. Hakan dahi töreye uymak zorundadır (Hukukun üstünlüğü).",
                        "tip": "Kut kan yoluyla tüm hanedan erkek üyelerine geçtiği için 'Taht kavgaları' ve 'Devletlerin kısa sürede parçalanması' kaçınılmaz olmuştur. Bu durum merkeziyetçi yapıyı zayıflatır!",
                        "emoji": "👑"
                    },
                    "questions": [
                        ("mc", "İslamiyet öncesi Türk devletlerinde 'Kut' inancının hanedanın tüm erkek üyelerine kan bağıyla geçmesi aşağıdakilerden hangisine doğrudan neden olmuştur?",
                         ["Sık sık taht kavgalarının çıkmasına ve devletlerin bölünmesine", "Halkın sınıflara ayrılmasına", "Törenin yazıya geçirilmesine", "Göçebe yaşamın sona ermesine", "Kadınların yönetimden dışlanmasına"], 0,
                         "Kut anlayışı hanedanın tüm erkek üyelerine saltanat hakkı verdiği için taht kavgalarına ve devletlerin çabuk bölünmesine yol açmıştır."),
                        ("mc", "İslamiyet öncesi Türklerde kurultaya başkanlık eden hükümdarın bulunmadığı zamanlarda kurultayı yöneten ve başbakan anlamına gelen görevli hangisidir?",
                         ["Aygucı (Üge)", "Tudun", "Buyruk", "Tarkan", "Tigin"], 0,
                         "Aygucı veya Üge hükümdar olmadığı zamanlarda kurultaya başkanlık eden vezir/başbakandır."),
                        ("mc", "Türklerde cenaze törenlerine ..., mezar taşlarına ... ve ölülerin ardından yakılan ağıtlara ... denirdi. Boşluklara sırasıyla hangileri gelmelidir?",
                         ["Yuğ - Balbal - Sagu", "Kurgan - Yuğ - Koşuk", "Balbal - Kurgan - Sagu", "Uçmağ - Balbal - Sav", "Yuğ - Tamu - Sagu"], 0,
                         "Cenaze töreni 'Yuğ', mezar taşı 'Balbal', ölen kişinin ardından okunan ağıt ise 'Sagu'dur."),
                        ("tf", "İslamiyet öncesi Türk toplumunda Avrupa'daki gibi kölelik ve katı sosyal sınıf ayrımı bulunmaz.",
                         True, "Toprak mülkiyeti devlete ait olduğu için Türklerde feodalite ve aristokratik köle sınıfı oluşmamıştır."),
                        ("fib", "İslamiyet öncesi Türklerde sözlü hukuk kurallarına ... adı verilirdi.",
                         ["Töre", "Yarlık", "Şeriat", "Ferman"], "Töre",
                         "Yazısız gelenek, görenek ve adalet kurallarının bütününe Töre denirdi."),
                        ("match", "İslamiyet öncesi kavramları anlamlarıyla eşleştiriniz:",
                         [("Kurgan", "Mezar"), ("Uçmağ", "Cennet"), ("Tamu", "Cehennem"), ("Balbal", "Mezar Taşı")],
                         "Kurgan mezar, Uçmağ cennet, Tamu cehennem, Balbal ise mezar taşıdır."),
                        ("mc", "Uygurlarda duvar resimlerine ne ad verilirdi?",
                         ["Fresko", "Hat", "Minyatür", "Çini", "Ebru"], 0,
                         "Uygurlar döneminde tapınak duvarlarına yapılan yaş alçı üzeri resimlere 'Fresko' denirdi."),
                        ("mc", "Mete Han tarafından oluşturulan ve günümüz kara kuvvetlerinin de kuruluş yılı (MÖ 209) kabul edilen askeri sistem hangisidir?",
                         ["Onlu Teşkilat", "Tımar Sistemi", "Yeniçeri Ocağı", "İkili Teşkilat", "Kurultay"], 0,
                         "Mete Han MÖ 209'da onbaşı, yüzbaşı, binbaşı ve tümenbaşı esasına dayalı onlu teşkilatı kurmuştur."),
                        ("mc", "İslamiyet öncesi Türk devletlerinde hükümdarın eşi olan Hatun'un elçi kabul edebilmesi ve kurultaya katılabilmesi neyi gösterir?",
                         ["Kadının yönetimde ve diplomaside söz sahibi olduğunu", "Monarşinin tamamen kaldırıldığını", "Kut anlayışının sona erdiğini", "Anaerkil aile yapısının zorunlu olduğunu", "Ordunun kadınlardan oluştuğunu"], 0,
                         "Hatun'un devlet meclisine katılması ve elçileri karşılaması Türklerde kadının siyasi otoritede yer aldığını kanıtlar.")
                    ]
                },
                {
                    "title": "İslamiyet Öncesi Kupa Sınavı 🏆",
                    "desc": "Tüm İslamiyet Öncesi Türk Tarihi & Kültür Medeniyet Kupa Sınavı",
                    "concept": {
                        "title": "İslamiyet Öncesi Şifreler ve Sınav Hapı",
                        "rule": "- İlk yazılı Türk abideleri: Orhun Abideleri (Bilge Kağan, Kültigin, Tonyukuk adına dikildi).\n- İlk Türk şairi: Aprınçur Tigin (Uygurlar).\n- Dünyanın en uzun destanı: Manas Destanı (Kırgızlar).\n- İlk posta teşkilatı ve vergi tahsildarı: Tudun (Vergi memuru), Tutuk (Askeri vali).\n- Hükümdarlık sembolleri: Otağ (çadır), Örgin (taht), Tuğ (sancak), Davul (köbürge), Kotuz (sorguç), Kurşak (kemer), Kılıç.",
                        "tip": "ÖSYM Soru Tuzağı: Hükümdarlık sembolleri arasında 'Hutbe okutmak', 'Hilat giymek', 'Çetr (saltanat şemsiyesi)' ve 'Sikke bastırmak (İslami yazılı)' İSLAMİYET ÖNCESİNDE ASLA YOKTUR! Bunlar İslamiyet ile gelmiştir!",
                        "emoji": "🏆"
                    },
                    "questions": [
                        ("mc", "Aşağıdakilerden hangisi İslamiyet öncesi Türk hükümdarlık sembollerinden biri DEĞİLDİR?",
                         ["Hutbe okutmak", "Otağ (Hükümdar Çadırı)", "Örgin (Taht)", "Tuğ (Sancak)", "Kotuz (Sorguç)"], 0,
                         "Hutbe okutmak İslami bir hükümdarlık alametidir; İslamiyet öncesinde kesinlikle yer almaz."),
                        ("mc", "Avrupa Hun Devleti'nin en parlak dönemi hangisidir ve Avrupalılar bu hükümdara hangi unvanı vermiştir?",
                         ["Attila - Tanrının Kırbacı (Flagellum Dei)", "Balamir - Cesur Kavim", "Rua - Büyük Hakan", "Uldız - Güneş Batmayan Kral", "Mete Han - Şanyü"], 0,
                         "Avrupa Hun hükümdarı Attila Avrupalılar tarafından 'Tanrı'nın Kırbacı' olarak adlandırılmış, Nibelungen destanında 'Etzel' adıyla anılmıştır."),
                        ("mc", "Moğol hakimiyetini kabul eden ilk Türk topluluğu hangisidir?",
                         ["Kırgızlar", "Uygurlar", "Karluklar", "Hazarlar", "Türgişler"], 0,
                         "Moğollara itaat eden ilk Türk devleti/topluluğu Kırgızlar (Müslüman olarak ise Karluklar) olmuştur."),
                        ("tf", "Orhun Abideleri Danimarkalı dilbilimci Vilhelm Thomsen tarafından 1893 yılında okunup çözülmüştür.",
                         True, "Vilhelm Thomsen Orhun yazıtlarının Türkçe olduğunu tespit edip çözen ilk bilim insanıdır."),
                        ("fib", "İslamiyet öncesi Türklerde mezar üzerine dikilen ve öldürülen düşman sayısını simgeleyen heykelciklere ... denir.",
                         ["Balbal", "Kurgan", "Kümbet", "Yarlık"], "Balbal",
                         "Balbal mezar taşı heykelcikleridir."),
                        ("match", "Destanları ait oldukları Türk topluluklarıyla eşleştiriniz:",
                         [("Ergenekon - Bozkurt", "Göktürkler"), ("Türeyiş - Göç", "Uygurlar"), ("Oğuz Kağan", "Hunlar"), ("Manas", "Kırgızlar")],
                         "Ergenekon Göktürklere, Türeyiş Uygurlara, Oğuz Kağan Asya Hunlarına, Manas Kırgızlara aittir."),
                        ("mc", "Türklerin tarih boyunca kullandığı alfabelerin kronolojik sıralaması hangisinde doğrudur?",
                         ["Orhun -> Uygur -> Arap -> Latin", "Uygur -> Orhun -> Kiril -> Latin", "Arap -> Orhun -> Latin -> Göktürk", "Orhun -> Latin -> Arap -> Kiril", "Göktürk -> Latin -> Arap -> Uygur"], 0,
                         "Türkler sırasıyla Orhun, Uygur, Arap ve Latin alfabelerini (ayrıca Kiril ve Soğd) kullanmışlardır."),
                        ("mc", "İslamiyet öncesi Türklerde 'Yargu' kurumu ne işe yarardı?",
                         ["Hakan başkanlığında toplanan yüksek siyasi mahkeme", "Vergi toplama dairesi", "Sınır karakolu", "Elçi karşılama heyeti", "Savaş meclisi"], 0,
                         "Yargu İslamiyet öncesinde devlete karşı işlenen büyük suçların yargılandığı siyasi yüksek mahkemedir."),
                        ("mc", "İlk düzenli Türk ordusunu kuran Mete Han, orduda haberleşmeyi sağlamak için hangi silahı icat etmiştir?",
                         ["Islıklı Ok", "Turan Yay", "Gürz", "Kargı", "Mancınık"], 0,
                         "Mete Han hedefe yöneldiğinde ses çıkaran ve ordunun tek bir noktaya odaklanmasını sağlayan ıslıklı oku icat etmiştir.")
                    ],
                    "is_exam": True
                }
            ]
        },
        # Ünite 2: İlk Müslüman Türk Devletleri
        {
            "id": "kpss_tar_u2",
            "num": 2,
            "title": "İlk Müslüman Türk Devletleri & Türk-İslam Medeniyeti",
            "subject": "KPSS Tarih",
            "color": "0xFF0284C7",
            "lessons": [
                {
                    "title": "Karahanlı, Gazneli ve Büyük Selçuklu Devleti",
                    "desc": "Talas Savaşı, İslamlaşma ve İlk Büyük Türk-İslam Devletleri",
                    "concept": {
                        "title": "İlk Türk-İslam Devletleri Özellikleri",
                        "rule": "- Talas Savaşı (751): Karluk Türkleri Abbasilere yardım etti. Türkler kitleler halinde İslamiyet'e girdi, kağıt Semerkant'ta üretildi.\n- Karahanlılar: Orta Asya'da kurulan ilk Müslüman Türk devleti. Satuk Buğra Han (Abdülkerim) zamanında İslamiyet resmi din oldu. Resmi dil Türkçe!\n- Gazneliler: Alp Tegin kurdu, Gazneli Mahmut en parlak dönem (Sultan unvanını kullanan ilk Türk hükümdarı, Hindistan'a 17 sefer).\n- Büyük Selçuklu: Tuğrul ve Çağrı Beyler kurdu (1040 Dandanakan ile resmen kuruldu). Alparslan (1071 Malazgirt ile Anadolu'nun kapılarını açtı). Melikşah en parlak dönem.",
                        "tip": "Karahanlılar halkı ve yöneticisi tamamen Türk olduğu için Türkçeyi resmi dil yapmış ve milli kimliğini korumuştur. Gazneliler ve Büyük Selçuklu'da ise halk çok uluslu olduğu için resmi dil Farsça, bilim dili Arapça olmuştur!",
                        "emoji": "🕌"
                    },
                    "questions": [
                        ("mc", "Tarihte 'Sultan' unvanını kullanan ilk Türk hükümdarı kimdir?",
                         ["Gazneli Mahmut", "Tuğrul Bey", "Alparslan", "Satuk Buğra Han", "Melikşah"], 0,
                         "Abbaso Halifesi tarafından Şii Büveyhoğullarına karşı koruduğu için Gazneli Mahmut'a 'Sultan' unvanı verilmiştir."),
                        ("mc", "Büyük Selçuklu Devleti'nin resmen kurulmasını sağlayan ve Gaznelilerin çöküş sürecini başlatan 1040 tarihli savaş hangisidir?",
                         ["Dandanakan Savaşı", "Pasinler Savaşı", "Malazgirt Savaşı", "Yassıçemen Savaşı", "Katvan Savaşı"], 0,
                         "1040 Dandanakan Savaşı ile Büyük Selçuklu resmen kurulmuş, Gazneliler zayıflayarak yıkılış sürecine girmiştir."),
                        ("mc", "1071 Malazgirt Savaşı sonrası Abbasi Halifesi tarafından Sultan Alparslan'a hangi unvan verilmiştir?",
                         ["Ebu'l Feth (Fetihlerin Babası)", "Sultanu'l Azam", "Şah-ı Cihan", "İlteriş", "Melikü'l Meşrık"], 0,
                         "Sultan Alparslan Ani Kalesi ve Malazgirt zaferlerinden ötürü 'Ebu'l Feth' (Fetihlerin Babası) unvanını almıştır."),
                        ("tf", "Talas Savaşı'ndan sonra kağıt Çin dışında ilk kez Semerkant'ta üretilmiştir.",
                         True, "Semerkant 'Şehirlerin Şahı' olarak bilinir ve kağıt üretimi burada başlamıştır."),
                        ("fib", "Büyük Selçuklu Devleti'nde Hasan Sabbah'ın kurduğu ... tarikatı Batinilik propagandasıyla devlet adamlarına suikastlar düzenlemiştir.",
                         ["Haşhaşilik", "Babailik", "Karametilik", "Hurufilik"], "Haşhaşilik",
                         "Alamut Kalesi merkezli Haşhaşi tarikatı Vezir Nizamülmülk dahil birçok Selçuklu devlet adamını şehit etmiştir."),
                        ("match", "Şehir unvanlarını eşleştiriniz:",
                         [("Buhara", "İslam'ın Roması"), ("Semerkant", "Şehirlerin Şahı"), ("İsfahan", "Nısf-ı Cihan (Dünyanın Yarısı)"), ("Kaşgar", "Işıldayan İnci")],
                         "Buhara İslam'ın Roması, Semerkant Şehirlerin Şahı, İsfahan Nısf-ı Cihan, Kaşgar Işıldayan İnci'dir."),
                        ("mc", "Büyük Selçuklu Devleti'nin yıkılış sürecine girmesine neden olan 1141 tarihli savaş hangisidir?",
                         ["Katvan Savaşı (Karahıtaylar)", "Kösedağ Savaşı", "Dandanakan Savaşı", "Yassıçemen Savaşı", "Ayn Calut Savaşı"], 0,
                         "Sultan Sencer döneminde Moğol kökenli Karahıtaylara karşı kaybedilen 1141 Katvan Savaşı yıkılışı hızlandırmıştır."),
                        ("mc", "Mısır'da kurulan ilk Türk-İslam devleti aşağıdakilerden hangisidir?",
                         ["Tolunoğulları", "İhşidiler (Akşitler)", "Eyyubiler", "Memlükler", "Fatımiler"], 0,
                         "Ahmet bin Tolun tarafından 868'de kurulan Tolunoğulları Mısır'da kurulan ilk Türk-İslam devletidir."),
                        ("mc", "Moğolları tarihte ilk kez durduran ve 1260 Ayn Calut Savaşı ile hezimete uğratan Türk-İslam devleti hangisidir?",
                         ["Memlükler", "Büyük Selçuklu", "Eyyubiler", "Harzemşahlar", "Altın Orda"], 0,
                         "Sultan Baybars komutasındaki Memlükler 1260 Ayn Calut ve 1277 Elbistan savaşlarında Moğolları mağlup etmiştir.")
                    ]
                },
                {
                    "title": "İlk Türk-İslam Edebi Eserleri ve Bilginleri",
                    "desc": "Kutadgu Bilig, Divanü Lugati't-Türk, Farabi, İbn-i Sina",
                    "concept": {
                        "title": "4 Temel Türk-İslam Eseri",
                        "rule": "- Kutadgu Bilig (Yusuf Has Hacip): İlk Türk-İslam eseri, siyasetname türündedir, aruz ölçüsüyle yazılmıştır. Tabgaç Buğra Han'a sunuldu.\n- Divanü Lugati't-Türk (Kaşgarlı Mahmut): İlk Türkçe sözlük, ansiklopedi ve Türk dünyası haritası içerir. Araplara Türkçeyi öğretmek için yazıldı. Abbasi Halifesi El-Muktedi Billah'a sunuldu.\n- Atabetü'l-Hakayık (Edip Ahmet Yükneki): Hakikatlerin eşiği, ahlak ve öğüt kitabıdır. Dad İspehsalar Bey'e sunuldu.\n- Divan-ı Hikmet (Hoca Ahmet Yesevi): İlk Türk tasavvuf eseri, dörtlük ve hece ölçüsü ağırlıklıdır. Yesevilik tarikatının temelidir.",
                        "tip": "ÖSYM bu 4 eseri yazarları, sunuldukları kişiler ve içerikleri bakımından eşleştirme sorusu olarak defalarca sormuştur!",
                        "emoji": "📚"
                    },
                    "questions": [
                        ("mc", "Türk tarihinin ilk siyasetnamesi kabul edilen ve mutluluk veren bilgi anlamına gelen 'Kutadgu Bilig' adlı eser kime aittir?",
                         ["Yusuf Has Hacip", "Kaşgarlı Mahmut", "Edip Ahmet Yükneki", "Ahmet Yesevi", "Ali Şir Nevai"], 0,
                         "Kutadgu Bilig 1069 yılında Yusuf Has Hacip tarafından Tabgaç Buğra Han'a sunulmuştur."),
                        ("mc", "Araplara Türkçeyi öğretmek ve Türkçenin zengin bir dil olduğunu kanıtlamak amacıyla ilk Türkçe sözlüğü yazan ve ilk dünya haritasını çizen bilgin kimdir?",
                         ["Kaşgarlı Mahmut", "Yusuf Has Hacip", "Farabi", "Biruni", "Harezmi"], 0,
                         "Kaşgarlı Mahmut Divanü Lugati't-Türk adlı eserinde Türk boylarını ve coğrafyasını haritayla tanıtmıştır."),
                        ("mc", "Batıda 'Avicenna' olarak tanınan ve 'El-Kanun fi't-Tıbb' (Tıbbın Kanunu) adlı eseri Avrupa üniversitelerinde yüzlerce yıl ders kitabı olarak okutulan İslam bilgini kimdir?",
                         ["İbn-i Sina", "Farabi", "İbn-i Rüşd", "Razi", "Gazali"], 0,
                         "İbn-i Sina tıp dünyasının öncüsü olup Batıda Avicenna olarak bilinir."),
                        ("tf", "Nizamiye Medreseleri Büyük Selçuklu Veziri Nizamülmülk tarafından açılan tarihin ilk üniversite düzeyindeki eğitim kurumlarındandır.",
                         True, "Bağdat'ta kurulan Nizamiye Medreseleri Batinilik faaliyetlerine karşı Sünni inancı korumak ve devlet adamı yetiştirmek için kurulmuştur."),
                        ("fib", "Felsefe alanındaki derin bilgisi nedeniyle Aristo'dan sonra 'Muallim-i Sani' (İkinci Öğretmen) unvanını alan Türk-İslam bilgini ...'dir.",
                         ["Farabi", "İbn-i Sina", "Gazali", "Harezmi"], "Farabi",
                         "Farabi Birleşmiş Milletler fikrini ilk ortaya atan (El-Medinetü'l Fazıla) ve Muallim-i Sani unvanlı filozoftur."),
                        ("match", "Eserleri yazarları ile eşleştiriniz:",
                         [("Kutadgu Bilig", "Yusuf Has Hacip"), ("Divanu Lugati't-Türk", "Kaşgarlı Mahmut"), ("Atabetü'l-Hakayık", "Edip Ahmet Yükneki"), ("Divan-ı Hikmet", "Ahmet Yesevi")],
                         "Kutadgu Bilig Yusuf Has Hacip, Divanü Lugati't-Türk Kaşgarlı Mahmut, Atabetü'l-Hakayık Edip Ahmet, Divan-ı Hikmet Hoca Ahmet Yesevi'ye aittir."),
                        ("mc", "Sıfır (0) rakamını ilk kez matematiğe kazandıran ve cebir ilminin kurucusu kabul edilen bilim insanı hangisidir?",
                         ["Harezmi", "Ömer Hayyam", "Ali Kuşçu", "Uluğ Bey", "Biruni"], 0,
                         "Harezmi 'El-Cebr ve'l-Mukabele' adlı eseriyle cebrin kurucusudur ve sıfırı kullanmıştır."),
                        ("mc", "Gazneli Mahmut'un 'Sarayımın en değerli hazinesidir' dediği ve astronomi alanında çalışmalar yapan ünlü bilgin kimdir?",
                         ["Biruni", "Farabi", "İbn-i Heysem", "Uluğ Bey", "İbn-i Rüşd"], 0,
                         "Biruni dünyanın çapını ve eksen eğikliğini çok hassas hesaplayan büyük Türk-İslam bilginidir."),
                        ("mc", "İslam dünyasında pozitif bilimler ile dini bilimleri uzlaştıran ve Nizamiye Medresesi başmüderrisi olan düşünür kimdir?",
                         ["İmam Gazali", "Farabi", "İbn-i Rüşd", "Molla Fenari", "Zemahşeri"], 0,
                         "Gazali 'İhyau Ulumi'd-Din' ve 'Tehafütü'l-Felasife' eserleriyle meşhur büyük İslam alimidir.")
                    ]
                },
                {
                    "title": "İlk Türk-İslam Devletleri Kupa Sınavı 🏆",
                    "desc": "Tüm İlk Müslüman Türk Devletleri & Medeniyet Kupa Sınavı",
                    "concept": {
                        "title": "Kupa Sınavı Hap Özeti",
                        "rule": "- İkta Sistemi: Toprak gelirlerinin devlete asker besleme şartıyla devlet görevlilerine bırakılması. Hazineye yük olmadan ordu yetiştirir, tarımsal üretimde sürekliliği sağlar.\n- Gulam Sistemi: Savaş esirleri veya satın alınan çocukların özel askeri eğitimle saray ordusu (Hassa) yapılması.\n- Ribat: Karahanlılar döneminde sınır güvenliği için yapılan, sonradan kervansaraylara dönüşen askeri ve ticari yapılar.\n- Cami mimarisinde kubbe geleneğini başlatanlar: Karahanlılar.",
                        "tip": "İkta sistemi hem Büyük Selçuklu'da uygulanmış hem de Osmanlı'daki Tımar sistemine ilham vermiştir. Taşrada asayişi sağlar, merkezi otoriteyi güçlendirir!",
                        "emoji": "🏆"
                    },
                    "questions": [
                        ("mc", "Büyük Selçuklu Devleti'nde Sultan Alparslan ve Melikşah dönemlerinde vezirlik yapan, 'Siyasetname' adlı eseri yazan ve kendi adıyla medreseler kuran ünlü devlet adamı kimdir?",
                         ["Nizamülmülk", "Ali Şir Nevai", "Sadrettin Konevi", "Köprülü Mehmet", "Kemalettin İsmail"], 0,
                         "Vezir Nizamülmülk Siyasetname'nin yazarı ve Nizamiye Medreseleri'nin kurucusudur."),
                        ("mc", "Mısır'da 'Hicaz (Mekke ve Medine) bölgesine egemen olan ilk Türk devleti' hangisidir?",
                         ["İhşidiler (Akşitler)", "Tolunoğulları", "Eyyubiler", "Memlükler", "Osmanlılar"], 0,
                         "Muhammed bin Togaç tarafından kurulan İhşidiler (Akşitler) kutsal topraklara hakim olan ilk Türk devletidir."),
                        ("mc", "1187 Hıttin Savaşı ile Kudüs'ü Haçlılardan geri alarak III. Haçlı Seferi'nin başlamasına neden olan komutan ve kurduğu devlet hangisidir?",
                         ["Selahaddin Eyyubi - Eyyubiler", "Baybars - Memlükler", "Tuğrul Bey - Selçuklular", "Gazneli Mahmut - Gazneliler", "Alparslan - Büyük Selçuklu"], 0,
                         "Selahaddin Eyyubi 1187 Hıttin Savaşı'nda Kudüs'ü Haçlılardan kurtararak 'Kudüs Fatihi' olmuştur."),
                        ("tf", "Memlüklerde diğer Türk devletlerinin aksine kut kan bağı yerine 'her güçlü emirin sultan olabilme hakkı' veraset sistemini farklı kılmıştır.",
                         True, "Memlüklerde başarılı komutan ve emirler tahta çıkabildiği için sık sık hükümdar değişmiştir."),
                        ("fib", "İlk Türk-İslam devletlerinde kervansaray niteliği taşıyan ve sınır karakolu olarak da kullanılan yapılara ... denir.",
                         ["Ribat", "Kümbet", "Külliye", "İmaret"], "Ribat",
                         "Ribatlar Karahanlılarda tüccarların güvenliğini sağlayan ilk kervansaray örnekleridir."),
                        ("match", "Devlet ve başkent eşleştirmesi yapınız:",
                         [("Gazneliler", "Gazne"), ("Karahanlılar", "Balasagun"), ("Büyük Selçuklu", "İsfahan / Rey"), ("Tolunoğulları", "Fustat")],
                         "Gaznelilerin Gazne, Karahanlıların Balasagun/Kaşgar, Selçukluların Rey/İsfahan/Merv, Tolunoğullarının Fustat'tır."),
                        ("mc", "Celali Takvimi'ni Sultan Melikşah adına hazırlayan ünlü şair, matematikçi ve astronom kimdir?",
                         ["Ömer Hayyam", "Ali Kuşçu", "Uluğ Bey", "Harezmi", "Nasirüddin Tusi"], 0,
                         "Ömer Hayyam Güneş yılı esaslı Celali Takvimi'ni Melikşah için hazırlamış ve Rubaileriyle ünlenmiştir."),
                        ("mc", "Türk-İslam devletlerinde çarşı, pazar ve esnafı denetleyen, fiyatların (narh) uygulanmasını sağlayan görevli hangisidir?",
                         ["Muhtesip", "Hacibü'l Hüccab", "Emir-i Dad", "Subaşı", "Kadıü'l Kudat"], 0,
                         "Muhtesip belediye zabıtası ve piyasa denetçisidir."),
                        ("mc", "Aşağıdakilerden hangisi Büyük Selçuklu Devleti'nin zayıflayıp parçalanmasıyla ortaya çıkan 'Atabeylikler'den biri DEĞİLDİR?",
                         ["Danişmentliler", "Zengiler (Musul)", "Böriler (Şam)", "İldenizoğulları (Azerbaycan)", "Salgurlular (Fars)"], 0,
                         "Danişmentliler Malazgirt sonrası Anadolu'da kurulan I. Dönem Türk beyliğidir; Atabeylik değildir.")
                    ],
                    "is_exam": True
                }
            ]
        }
    ]
    return units_data
