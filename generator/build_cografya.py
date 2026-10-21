# -*- coding: utf-8 -*-
"""
KPSS Coğrafya Müfredatı ve Soru Üreticisi (15 Ünite - 45 Ders - 450 Soru)
"""
import os
from common import (
    make_concept_card, make_mc, make_tf, make_fib, make_match,
    make_lesson, make_unit, esc
)

_COGRAFYA_UNITS = [
    (19, "Türkiye'nin Coğrafi Konumu ve Jeopolitik Önemi", [
        ("Matematik (Mutlak) Konum ve Sonuçları", "36-42 Kuzey Paralelleri, 26-45 Doğu Meridyenleri, Yerel Saat ve Gölge"),
        ("Göreceli (Özel) Konum ve Jeopolitik", "Üç Kıtayı Bağlayan Konum, Boğazlar, Sınır Kapıları ve Transit Ticaret"),
        ("Coğrafi Konum Kupa Sınavı 🏆", "Tüm Konum Özellikleri, Saat Farkları ve Kupa Sınavı")
    ]),
    (20, "Türkiye'nin Yerşekilleri - Dağlar, Ovalar ve Platolar", [
        ("Dağlar: Kıvrım, Kırık ve Volkanik Dağlar", "Kuzey Anadolu Dağları, Toroslar, Horst-Graben Sistemleri ve Volkan Konileri"),
        ("Platolar ve Ovalar", "Lav, Karstik, Tabaka Düzlüğü ve Aşınım Platoları; Delta ve Tektonik Ovalar"),
        ("Yerşekilleri Kupa Sınavı 🏆", "Deprem Kuşakları, Masif Araziler ve Yerşekilleri Kupa Sınavı")
    ]),
    (21, "Türkiye'nin Su Varlığı - Akarsular, Göller ve Kaynaklar", [
        ("Türkiye'nin Akarsuları ve Havzalar", "Akış Hızı, Rejim, Aşındırma-Biriktirme, Açık ve Kapalı Havzalar"),
        ("Göller ve Kaynak Türleri", "Tektonik, Karstik, Volkanik, Buzul, Set Gölleri; Fay, Artezyen ve Karstik Kaynaklar"),
        ("Su Varlığı Kupa Sınavı 🏆", "Akarsu Rejimleri, Barajlar, Göller ve Kupa Sınavı")
    ]),
    (22, "Dış Kuvvetler, Karstik Şekiller ve Kıyı Tipleri", [
        ("Rüzgar, Buzul ve Dalga Şekilleri", "Mantarkaya, Barkan, Falez, Tombolo, Lagün ve Buzul Sirkleri"),
        ("Karstik Şekiller ve Kıyı Tipleri", "Lapya, Dolin, Uvala, Polye, Traverten; Boyuna, Enine, Dalmaçya, Ria Kıyı Tipleri"),
        ("Dış Kuvvetler Kupa Sınavı 🏆", "Kıyı Tipleri, Aşınım Şekilleri ve Kupa Sınavı")
    ]),
    (23, "Türkiye'nin İklimi, Sıcaklık ve Basınç-Rüzgarlar", [
        ("Sıcaklığı Etkileyen Faktörler ve Basınç", "Enlem, Yükselti, Karasallık-Denizellik; Sibirya, İzlanda, Asor, Basra"),
        ("Rüzgarlar ve Föhn Etkisi", "Kayıp-Sakal Şifresi (Karayel, Yıldız, Poyraz, Samyeli, Kıble, Lodos), Föhn ve Etezyen"),
        ("İklim ve Rüzgarlar Kupa Sınavı 🏆", "İzoterm Haritaları, İndirgenmiş Sıcaklık ve Kupa Sınavı")
    ]),
    (24, "Nem, Yağış Dağılışı ve İklim Tipleri", [
        ("Nem Türleri ve Yağış Çeşitleri", "Mutlak, Maksimum, Bağıl Nem; Orografik, Konveksiyonel ve Cephesel Yağışlar"),
        ("Türkiye'de Görülen İklim Tipleri", "Akdeniz, Karadeniz, Karasal (Step) ve Sert Karasal İklim Özellikleri"),
        ("Yağış ve İklim Kupa Sınavı 🏆", "Yağış Grafikleri, Kuraklık, İklim Rejimleri ve Kupa Sınavı")
    ]),
    (25, "Türkiye'nin Toprak Tipleri ve Bitki Örtüsü", [
        ("Toprak Tipleri: Zonal, Azonal, İntrazonal", "Terra-Rossa, Kahverengi Orman, Çernezyom, Podzol, Alüvyal ve Regosol Topraklar"),
        ("Bitki Örtüsü: Orman, Çalı ve Bozkır", "Maki, Garig, Psödömaki, Antropojen Bozkır ve Dağ Çayırları"),
        ("Toprak ve Bitki Kupa Sınavı 🏆", "Erozyon, Heyelan, Toprak Koruma ve Kupa Sınavı")
    ]),
    (26, "Türkiye'de Nüfusun Dağılışı, Sayımlar ve Göçler", [
        ("Nüfusun Dağılışını Etkileyen Faktörler", "Doğal ve Beşeri Faktörler, Seyrek ve Yoğun Nüfuslu Yöreler"),
        ("Nüfus Piramidi, Sayımlar ve Göçler", "Nüfus Artış Hızı, Yaş Grupları, Mevsimlik Tarım-Turizm Göçleri ve Beyin Göçü"),
        ("Nüfus ve Göç Kupa Sınavı 🏆", "TÜİK Verileri, Bağımlı Nüfus, İç ve Dış Göçler ve Kupa Sınavı")
    ]),
    (27, "Yerleşme Tipleri ve İdari Yapılanma", [
        ("Kırsal Yerleşmeler ve Köy Altı", "Kom, Ağıl, Oba, Yayla, Dam, Mezra, Divan, Mahalle ve Dalyan"),
        ("Kentsel Yerleşmeler ve Şehir Fonksiyonları", "Sanayi, Ticaret, Turizm, İdari, Maden ve Liman Şehirleri"),
        ("Yerleşmeler Kupa Sınavı 🏆", "Mesken Tipleri (Ahşap, Kerpiç, Taş) ve Kupa Sınavı")
    ]),
    (28, "Türkiye'de Tarım ve Başlıca Tarım Ürünleri", [
        ("Tarımı Etkileyen Faktörler ve Sorunlar", "Sulama, Gübreleme, Tohum Islahı, Makineleşme ve Destekleme Alımları"),
        ("Başlıca Tarım Ürünleri ve Yetişme Alanları", "Tahıllar, Sanayi Bitkileri, Baklagiller, Yağlı Tohumlar, Meyveler"),
        ("Tarım Coğrafyası Kupa Sınavı 🏆", "Devlet Tekeli Ürünler, Don Hassasiyeti ve Kupa Sınavı")
    ]),
    (29, "Hayvancılık, Ormancılık ve Su Ürünleri", [
        ("Hayvancılık Türleri ve Dağılışı", "Küçükbaş (Koyun, Kıl Keçisi, Tiftik), Büyükbaş (Mera ve Ahır/Besi), Kümes"),
        ("Arıcılık, İpek Böcekçiliği ve Balıkçılık", "Çam/Kestane/Yayla Balı, Kültür Balıkçılığı, Karadeniz ve Orman Varlığı"),
        ("Hayvancılık ve Orman Kupa Sınavı 🏆", "Besi Hayvancılığı, Orman Ürünleri ve Kupa Sınavı")
    ]),
    (30, "Madenler ve Enerji Kaynakları", [
        ("Metalik Madenler ve Rezerv Alanları", "Demir, Bakır, Boksit, Krom, Bor, Manganez, Kurşun-Çinko, Mermer"),
        ("Enerji Kaynakları: Tükenebilir ve Yenilenebilir", "Taş Kömürü, Linyit, Petrol, Doğalgaz, Hidroelektrik, Rüzgar, Güneş, Jeotermal"),
        ("Maden ve Enerji Kupa Sınavı 🏆", "Termik Santraller, Bor Sanayii, Akkuyu Nükleer ve Kupa Sınavı")
    ]),
    (31, "Türkiye'de Sanayi ve Sanayinin Kuruluş Faktörleri", [
        ("Sanayinin Kuruluş Yerini Etkileyen Faktörler", "Hammaddeye Yakınlık, Enerji, Ulaşım, Pazar ve Sermaye"),
        ("Başlıca Sanayi Kolları ve Merkezleri", "Demir-Çelik, Dokuma-Tekstil, Gıda, Petrokimya, Çimento ve Otomotiv"),
        ("Sanayi Coğrafyası Kupa Sınavı 🏆", "Serbest Ticaret Bölgeleri, OSB'ler ve Kupa Sınavı")
    ]),
    (32, "Ulaşım, Ticaret ve Turizm Coğrafyası", [
        ("Ulaşım Sistemleri ve Ticaret", "Karayolu, Demiryolu (YHT), Denizyolu (Limanlar), Havayolu; Dış Ticaret Açığı"),
        ("Turizm Çeşitleri ve UNESCO Alanları", "Kıyı, Kış, Termal, Yayla, İnanç, Kongre ve Kültür Turizmi"),
        ("Ulaşım ve Turizm Kupa Sınavı 🏆", "Sınır Kapıları, Transit Boru Hatları ve Kupa Sınavı")
    ]),
    (33, "Türkiye'nin Coğrafi Bölgeleri ve Kalkınma Projeleri", [
        ("Bölgesel Kalkınma Projeleri (GAP, DAP, KOP, DOKAP)", "Proje Amaçları, Kapsadığı İller, Sulama ve Sosyoekonomik Etkileri"),
        ("Yeşilırmak (YHGP) ve Zonguldak-Bartın-Karabük (ZBK)", "Havza Islahı, Ağır Sanayi Dönüşümü ve Bölgesel Farklılıklar"),
        ("Bölgesel Projeler Kupa Sınavı 🏆", "Tüm Kalkınma Projeleri, İller ve Coğrafya Final Kupa Sınavı")
    ])
]

# Coğrafya ünite kavramları ve özel soru şablonları
_COGRAFYA_CONCEPTS = {
    19: ("Matematik ve Göreceli Konum",
         "- Matematik Konum (36-42 K, 26-45 D): Kuzey Yarımküre, Orta Kuşak (Dört mevsim belirgin, Akdeniz iklimi, Batı rüzgarları, Cephesel yağışlar). Güneyden kuzeye gidildikçe sıcaklık, deniz tuzluluğu ve çizgisel hız azalır; gölge boyu ve yerçekimi artar.\n- Göreceli Konum: Üç tarafı denizlerle çevrili olması, yükseltinin batıdan doğuya artması, transit ticaret, boru hatları.",
         "ÖSYM Şifresi: A-B-C-D (Akdeniz iklimi, Batı rüzgarları, Cephesel yağış, Dört mevsim) -> Türkiye'nin ORTA KUŞAKTA olmasının kesin kanıtlarıdır!", "🌍"),
    20: ("Türkiye'nin Yerşekilleri",
         "- Dağlar: Alp-Himalaya kıvrım kuşağında (Kuzey Anadolu Dağları ve Toroslar). Ege'de kırık dağlar (Kaz, Madra, Yunt, Boz, Aydın, Menteşe horstları; Bakırçay, Gediz, Küçük ve Büyük Menderes grabenleri). Volkanik: Ağrı, Tendürek, Süphan, Nemrut, Erciyes, Hasan, Melendiz, Karacadağ, Kula.\n- Platolar: Obruk, Cihanbeyli, Haymana, Bozok (Tabaka düzlüğü); Teke, Taşeli (Karstik); Erzurum-Kars (Lav); Çatalca-Kocaeli (Aşınım).\n- Ovalar: Delta ovaları (Çukurova, Bafra, Çarşamba, Silifke, Menemen, Balat).",
         "Karstik platolar olan TEKE ve TAŞELİ su tutamadığı için tarıma elverişsizdir ve kıl keçisi yaygındır!", "⛰️"),
    21: ("Türkiye'nin Akarsuları ve Gölleri",
         "- Akarsular: Yatak eğimi ve akış hızları fazladır, hidroelektrik potansiyelleri yüksektir, ulaşıma elverişli değillerdir (Bartın Çayı hariç). En uzun nehir Kızılırmak, sınırlarımız dışına dökülenler Fırat, Dicle, Aras, Kura; dışarıdan gelenler Meriç ve Asi.\n- Göller: Tektonik (Tuz, Beyşehir, Eğirdir, İznik, Sapanca, Burdur); Karstik (Salda, Avlan, Elmalı); Volkanik (Nemrut krater, Meke maar); Set Gölleri (Heyelan set: Tortum, Sera, Abant; Alüvyal set: Köyceğiz, Eymir, Mogan; Kıyı set: Terkos/Durusu, Büyük ve Küçük Çekmece; Volkanik set: Van, Erçek, Nazik, Çıldır).",
         "Van Gölü hem tektonik hem volkanik set gölüdür (Karma yapılı) ve suyu sodalıdır!", "🌊"),
    22: ("Dış Kuvvetler ve Kıyı Tipleri",
         "- Rüzgarlar: İç Anadolu ve Güneydoğu Anadolu'da etkilidir (Mantarkaya, Barkan, Tafoni).\n- Karstik Şekiller: Akdeniz'de kireçtaşı (Kalker), Sivas'ta jips (Alçıtaşı), Çankırı'da kaya tuzu. Aşınım: Lapya, dolin, uvala, polye. Birikim: Traverten, sarkıt, dikit.\n- Kıyı Tipleri: Boyuna (Karadeniz ve Akdeniz), Enine (Ege), Ria (İstanbul-Çanakkale boğazları, Haliç), Dalmaçya (Kaş-Antalya kıyıları), Kalanklı (Mersin). Türkiye'de Haliç, Fiyort ve Skyer KIYI TİPİ KESİNLİKLE YOKTUR!",
         "ÖSYM Tuzağı: Türkiye'de okyanusa kıyımız olmadığı için GEL-GİT etkili değildir, bu yüzden HALİÇ ve VAT kıyı tipleri bulunmaz! Mercan/resif kıyılar da tropikal olmadığı için yoktur!", "🏖️"),
    23: ("Türkiye'nin Sıcaklık ve Rüzgarları",
         "- Basınç Merkezleri: Kışın etkili olanlar: Sibirya (Termik yüksek - çok soğuk ve ayaz), İzlanda (Dinamik alçak - ılık ve yağışlı). Yazın etkili olanlar: Basra (Termik alçak - aşırı sıcak ve çöl sıcağı), Asor (Dinamik yüksek - yaz kuraklığı).\n- Rüzgarlar: Karayel (KB), Yıldız (K), Poyraz (KD) -> Sıcaklığı düşürür. Samyeli/Keşişleme (GD), Kıble (G), Lodos (GB) -> Sıcaklığı artırır.\n- Föhn Rüzgarı: Dağı aşan havanın inerken her 100 metrede 1°C ısınması (Rize'de turunçgil, Iğdır'da pamuk mikroklimasını sağlar).",
         "Rüzgarlar şifresi: Saat yönünde KAYIP-SAKAL (Karayel, Yıldız, Poyraz, Samyeli, Kıble, Lodos)!", "💨"),
    24: ("Nem, Yağış ve İklim Tipleri",
         "- Yağış Tipleri:\n  * Orografik (Yamaç): Karadeniz ve Akdeniz kıyılarında.\n  * Konveksiyonel (Yükselim): İç Anadolu (Kırkikindi), Erzurum-Kars (Yaz yağışları).\n  * Cephesel (Frontal): Akdeniz iklim bölgesinde, sıcak ve soğuk havanın karşılaşmasıyla (Orta kuşak kanıtı).\n- İklimler:\n  * Akdeniz: Yazlar sıcak-kurak, kışlar ılık-yağışlı. Kar yağışı ve don nadirdir.\n  * Karadeniz: Her mevsim yağışlı, yıllık sıcaklık farkı en az olan iklim.\n  * Step (Karasal): En fazla yağış ilkbaharda, yazlar kurak.\n  * Sert Karasal (Erzurum-Kars): En fazla yağış yazın, çayır bitki örtüsü ve büyükbaş hayvancılık.",
         "Türkiye'de en çok yağış alan yer Rize (Yamaç yağışı), en az yağış alan yer Tuz Gölü çevresi ve Iğdır Ovası'dır!", "🌧️"),
    25: ("Toprak Tipleri ve Bitki Örtüsü",
         "- Zonal Topraklar: Terra-Rossa (Akdeniz kalker üzerinde, kireçli, demir oksitli kırmızı renkli), Kahverengi Orman (Karadeniz, humusça zengin), Çernezyom (Erzurum-Kars, en verimli zonal toprak, kara toprak), Podzol (Batı Karadeniz soğuk nemli çam ormanı altı).\n- Azonal Topraklar (Taşınmış, horizonsuz, verimli): Alüvyal (Akarsu), Kolüvyal (Etek), Moren (Buzul), Lös (Rüzgar), Regosol (Volkanik kum).\n- Bitki Örtüsü: Maki (Kızılçam tahribiyle: Zeytin, defne, zakkum, mersin), Garig (Maki tahribi: Lavanta, abdestbozan), Psödömaki (Karadeniz orman tahribi), Bozkır (Geven, gelincik, çoban yastığı).",
         "Çernezyom dünyanın en verimli yerli toprağıdır ancak Erzurum-Kars'ta yaz mevsimi kısa ve iklim sert olduğu için tarımdan çok büyükbaş mera hayvancılığı yapılır!", "🌱"),
    26: ("Türkiye'de Nüfus ve Göçler",
         "- Yoğun Nüfuslu Yerler: Çatalca-Kocaeli, Kıyı Ege, Çukurova, Doğu Karadeniz kıyı şeridi, Ankara, Bursa, Gaziantep.\n- Seyrek Nüfuslu Yerler: Yıldız Dağları (Ulaşım dışında), Menteşe Yöresi (Engebeli), Teke ve Taşeli Platoları (Karstik, susuz), Tuz Gölü çevresi (Kuraklık), Hakkari Yöresi (Yükselti ve engebe).\n- Göçler: Mevsimlik göçler (Çukurova pamuk, Ordu fındık, Akdeniz turizm, yaylacılık). Kalıcı göçler sanayileşmiş merkezlere doğrudur.",
         "Doğu Karadeniz kıyı kuşağı kıyı boyunca dar bir şeritte yerleşildiği için nüfus YOĞUNDUR; ancak iç kısımları çok seyrektir!", "👥"),
    27: ("Kırsal ve Kentsel Yerleşmeler",
         "- Geçici Köy Altı Yerleşmeleri: Yayla (En yaygın), Kom (Doğu Anadolu - hayvancılık), Ağıl (Küçükbaş çiti), Oba (Göçebe çadır), Dam (Ege-Göller hayvancılık).\n- Kalıcı Köy Altı Yerleşmeleri: Mezra (Doğu ve Güneydoğu - tarım ve hayvancılık), Divan (Batı Karadeniz - birbirine uzak mahalleler), Mahalle, Çiftlik (Geniş tarım arazisi).\n- Yapı Malzemeleri: Karadeniz -> Ahşap; İç, Doğu ve Güneydoğu -> Kerpiç; Akdeniz ve volkanik yöreler -> Taş.",
         "Kalıcı köy altı yerleşmelerinde TARIMSAL faaliyet esastır; geçici yerleşmelerde ise HAYVANCILIK öne çıkar!", "🏡"),
    28: ("Türkiye'de Tarım Ürünleri",
         "- Tarımda Verim: En büyük sorun SULAMADIR. GAP ile Şanlıurfa pamuk üretiminde 1. sıraya yükselmiştir.\n- Ürünler:\n  * Buğday-Arpa: İlkbaharda yağış, yazın kuraklık ister. Karadeniz kıyılarında yetişmez.\n  * Zeytin, İncir, Turunçgil: Don olayına karşı son derece hassastır.\n  * Çay: Yıkanmış asitli toprak, bol nem ister (Sadece Doğu Karadeniz - Rize).\n  * Fındık: Karadeniz iklimi (Ordu, Giresun dünyada 1.).\n  * Pamuk: Yüksek sıcaklık ve bol su ister (Şanlıurfa, Ege, Çukurova).\n  * Devlet Kontrolündeki Ürünler: Tütün (Kalite), Pirinç (Sıtma hastalığı riski), Haşhaş ve Kenevir (Uyuşturucu kontrolü), Şekerpancarı (Kota ve çabuk bozulma riski).",
         "Şekerpancarı çabuk bozulduğu için fabrikaları daima tarım alanlarının YANI BAŞINA kurulmak zorundadır!", "🌾"),
    29: ("Hayvancılık, Orman ve Su Ürünleri",
         "- Küçükbaş: Bozkırın yaygın olduğu İç, Doğu ve Güneydoğu'da koyun. En çok kıl keçisi Toroslar'da (Teke ve Taşeli - ormana zarar verir). Tiftik (Ankara) keçisi İç Anadolu'da.\n- Büyükbaş: Yaz yağışlarıyla oluşan gür çayırlardan dolayı Erzurum-Kars ve Doğu Karadeniz'de mera hayvancılığı. Tüketici nüfusa yakınlık nedeniyle Marmara ve Ege'de ahır (besi) hayvancılığı.\n- Arıcılık: Muğla (Çam balı), Ordu, Rize (Anzer), Kars, Hakkari.\n- Balıkçılık: En fazla Karadeniz'de (Tuzluluk az, oksijen ve plankton bol). Ege'de kültür balıkçılığı (Dalyan).",
         "Ahır ve besi hayvancılığında et ve süt üretimi iklime bağımlı DEĞİLDİR; mera hayvancılığında ise yağışa göre dalgalanır!", "🐄"),
    30: ("Madenler ve Enerji Kaynakları",
         "- Madenler:\n  * Demir: Sivas (Divriği), Malatya (Hekimhan-Hasançelebi).\n  * Bakır: Artvin (Murgul), Kastamonu (Küre), Elazığ (Maden).\n  * Boksit (Alüminyum): Konya (Seydişehir), Antalya (Akseki).\n  * Krom: Elazığ (Guleman), Muğla (Fethiye).\n  * Bor: Balıkesir (Bigadiç, Susurluk), Kütahya (Emet), Eskişehir (Kırka), Bursa (Mustafakemalpaşa) - Dünyada 1. sıradayız.\n  * Mermer: Afyonkarahisar, Marmara Adası, Bursa, Muğla (İhracatta 1. madenimiz).\n- Enerji:\n  * Taş Kömürü: Zonguldak (Çatalağzı termik santrali - 1. Jeolojik zaman).\n  * Linyit: Manisa (Soma), Kütahya (Tunçbilek), Muğla (Yatağan), K.Maraş (Afşin-Elbistan) - 3. Jeolojik zaman.\n  * Jeotermal: Denizli (Sarayköy), Aydın (Germencik) - Fay hatları.\n  * Rüzgar: İzmir, Balıkesir, Çanakkale.",
         "İhracatımızda en çok gelir getiren maden İŞLENMİŞ MERMERDİR! Bor ise dünya rezervinin %72'sine sahip olduğumuz stratejik madendir!", "⛏️"),
    31: ("Türkiye'de Sanayi Coğrafyası",
         "- Sanayinin Kuruluş Faktörleri:\n  * Hammaddeye Yakınlık: Rize (Çay), Konya (Şeker), Ayvalık (Zeytinyağı), Seydişehir (Alüminyum), Batman (Petrol rafinerisi).\n  * Enerji Kaynağına Yakınlık: Karabük ve Ereğli Demir-Çelik Fabrikaları (Taş kömürüne yakınlık).\n  * Ulaşım ve Pazar: İskenderun Demir-Çelik (Liman ulaşımı), İstanbul ve İzmir (Liman, pazar ve iş gücü).\n- Rafineriler: Batman (Hammaddeye yakın), İzmit (Tüpraş - Pazar ve liman), İzmir (Aliağa - Liman), Kırıkkale (Orta Anadolu - Güvenlik ve boru hattı).",
         "Karabük ve Ereğli'de demir madeni çıkmamasına rağmen orada demir-çelik fabrikası kurulmasının sebebi TAŞ KÖMÜRÜ (ENERJİ KAYNAĞI)'na yakınlıktır!", "🏭"),
    32: ("Ulaşım, Ticaret ve Turizm",
         "- Ulaşım: En çok yolcu ve yük taşınan iç hat KARAYOLUDUR. Dış ticarette en ucuz ve en çok kullanılan yol DENİZYOLUDUR (Limanlar). Hinterlandı en geniş liman İSTANBUL, hinterlandı en dar liman dağlar kıyıya paralel olduğu için SİNOP'tur.\n- Sınır Kapıları: Kapıkule (Bulgaristan - en işlek kapı), Sarp (Gürcistan), Habur (Irak - Ortadoğu kapısı), Gürbulak (İran), İpsala (Yunanistan).\n- Turizm: UNESCO Mirasları (Göbeklitepe, Divriği, Hattuşa, Nemrut, Pamukkale-Hierapolis, Gordion). Kış turizmi (Uludağ, Palandöken, Erciyes, Kartalkaya).",
         "Sinop doğal bir liman olmasına rağmen arkasındaki Küre Dağları demiryolu ve karayolu ulaşımını kestiği için gelişememiş ve hinterlandı dar kalmıştır!", "🚢"),
    33: ("Bölgesel Kalkınma Projeleri",
         "- GAP (Güneydoğu Anadolu): Amaç sulama ve hidroelektrik enerji üretimi. Fırat ve Dicle nehirleri üzerinde barajlar (Atatürk Barajı, Ilısu/Veysel Eroğlu). Sanayi bitkileri (pamuk, mısır) patlama yapmıştır.\n- KOP (Konya Ovası Projesi): Mavi Tünel ile Göksu Nehri'nin suları Konya kapalı havzasına aktarılmıştır. Yeraltı suyunun çekilmesini ve obruk oluşumunu azaltmayı hedefler.\n- DOKAP (Doğu Karadeniz): Yeşil Yol projesi ile yaylaları birbirine bağlamak, yayla turizmi ve balıkçılığı geliştirmek.\n- DAP (Doğu Anadolu): Büyükbaş hayvancılığı geliştirmek, mera ıslahı ve kış turizmi.\n- ZBK (Zonguldak-Bartın-Karabük): Taş kömürü ve demir-çelik üretimini modernleştirmek, Filyos Vadi Projesi ile liman ve sanayi üssü kurmak.",
         "GAP sadece bir tarım projesi değil, eğitim, sağlık, altyapı ve ulaştırmayı kapsayan entegre bir BÖLGESEL KALKINMA projesidir!", "🏗️")
}

def build_cografya_questions(u_num, l_idx, l_title, is_exam):
    meta = _COGRAFYA_CONCEPTS.get(u_num, (
        f"{l_title} Önemli Bilgiler",
        "Türkiye Coğrafyası müfredat ilkeleri.",
        "ÖSYM soru tarzlarına dikkat ediniz.",
        "🌍"
    ))
    
    q_pool = [
        ("mc", f"{l_title} kapsamında ÖSYM tarafından sorulan coğrafi dağılış ilkesine göre en belirgin özellik hangisidir?",
         ["Bölgesel iklim ve yerşekillerinin ekonomik faaliyetleri doğrudan belirlemesi", "Tüm bölgelerde tarımsal verimin eşit olması", "Yükseltinin sıcaklık üzerinde hiçbir etkisinin bulunmaması", "Nüfusun her bölgeye homojen dağılması", "Akarsuların tamamının kapalı havza oluşturması"], 0,
         "Türkiye'de yerşekilleri ve iklim çeşitliliği tarım, nüfus ve yerleşme üzerinde belirleyici faktördür."),
        ("mc", f"Aşağıdakilerden hangisi {l_title} sürecinde meydana gelen doğal veya beşeri olayların bir sonucu değildir?",
         ["Bütün göllerin sularının tamamen tatlı olması", "Yeryüzü şekillerinin kısa mesafede değişmesi", "Mikroklima alanlarının oluşması", "Farklı tarım ürünlerinin yetişebilmesi", "Ulaşım maliyetlerinin bölgelere göre değişmesi"], 0,
         "Türkiye'deki göllerin suları tektonik, karstik veya volkanik yapılarına göre sodalı, tuzlu, acı veya tatlı olabilir."),
        ("mc", f"{l_title} alanında Türkiye'nin sahip olduğu jeopolitik veya fiziki avantajlar arasında hangisi gösterilebilir?",
         ["Stratejik konumu ve doğal kaynak çeşitliliği", "Tüm topraklarının deniz seviyesinde olması", "Hiçbir fay hattının bulunmaması", "Dört mevsimin hiçbir yerde hissedilmemesi", "Akarsuların tamamının ulaşıma açık olması"], 0,
         "Türkiye üç kıtayı birbirine bağlayan jeopolitik konumu ve genç oluşumlu zengin maden yapısıyla avantajlıdır."),
        ("mc", f"Türkiye coğrafyasında {l_title} ile ilgili olarak aşağıda verilen yargılardan hangisi doğrudur?",
         ["Batıdan doğuya doğru gidildikçe yükselti artar ve sıcaklıklar düşer", "Kuzeye gidildikçe çizgisel hız artar", "Güneye gidildikçe gölge boyu uzar", "Bütün dağlarımız volkanik faaliyetlerle oluşmuştur", "Türkiye'de rüzgar aşındırması en çok Karadeniz'de görülür"], 0,
         "Türkiye'de ortalama yükselti batıdan doğuya doğru artar, buna bağlı olarak karasallık ve don olayları artar."),
        ("mc", f"{l_title} konusuyla ilgili sınav sorularında adayların en sık düştüğü çeldirici unsur hangisidir?",
         ["Gerçek sıcaklık ile deniz seviyesine indirgenmiş sıcaklık farkı", "Meridyenlerin boylarının eşit olması", "Güneşin her gün doğudan doğması", "Akarsuların denize dökülmesi", "Dağların doruklarında kar bulunması"], 0,
         "İndirgenmiş sıcaklık hesaplamalarında yükseltinin etkisi yok sayıldığı için yükseltiye bağlı sıcaklık düşüşü dikkate alınmaz."),
        ("mc", f"Aşağıdaki coğrafi alanlardan hangisi {l_title} bakımından ülkemizde öne çıkan merkezlerdendir?",
         ["Coğrafi koşulların sağladığı potansiyelle gelişen öncü merkezler", "Sürekli kutup iklimi yaşayan bölgeler", "Aktif volkanların lav püskürttüğü dağlar", "Okyanus akıntılarına açık kıyılar", "Ekvatoral yağmur ormanları kuşağı"], 0,
         "Türkiye'nin fiziki ve beşeri coğrafyası kendine özgü Akdeniz ve Orta Kuşak koşullarını yansıtır."),
        ("tf", f"{l_title} çerçevesinde değerlendirildiğinde Türkiye genç oluşumlu (3. ve 4. jeolojik zaman) bir ülkedir.",
         True, "Türkiye'nin genç oluşumlu olması yüksek engebe, kaplıcalar, fay hatları ve linyit-bor zenginliğini açıklar."),
        ("fib", f"{l_title} sürecinde iklim ve yerşekillerinin etkisiyle oluşan doğal çevre şartlarına ... denir.",
         ["Ekosistem", "Horst", "Graben", "Barkan"], "Ekosistem",
         "Canlılar ile cansız çevrenin oluşturduğu etkileşim sistemidir."),
        ("match", "Coğrafi kavramları eşleştiriniz:",
         [("Delta", "Akarsu biriktirmesiyle oluşan ova"),
          ("Horst", "Kırılma ile yükselen dağ kütlesi"),
          ("Maki", "Akdeniz bodur çalı topluluğu"),
          ("Moren", "Buzul biriktirme toprağı")],
         "Temel coğrafi şekil ve terimlerdir.")
    ]
    
    return {
        "concept_title": f"{l_title} - Püf Noktalar",
        "concept_rule": meta[1],
        "concept_tip": meta[2],
        "concept_emoji": meta[3],
        "questions": q_pool
    }

def generate_cografya_dart():
    dart_lines = [
        "import '../models/lesson_models.dart';",
        "",
        "/// KPSS Quest - KPSS Coğrafya Müfredatı (15 Ünite - 45 Ders - 450 Soru)",
        "final List<LearningUnit> kpssCografyaUnits = [",
    ]
    
    for u_num, u_title, lessons in _COGRAFYA_UNITS:
        lessons_code = []
        for l_idx, (l_title, l_desc) in enumerate(lessons):
            is_exam = (l_idx == len(lessons) - 1)
            q_data = build_cografya_questions(u_num, l_idx + 1, l_title, is_exam)
            l_id = f"kpss_cog_u{u_num}_l{l_idx+1}"
            
            q_code_items = [
                make_concept_card(
                    f"{l_id}_q1", q_data["concept_title"], q_data["concept_rule"],
                    q_data["concept_tip"], q_data["concept_emoji"]
                )
            ]
            
            for q_idx, q in enumerate(q_data["questions"]):
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
            
        u_id = f"kpss_cog_u{u_num}"
        dart_lines.append(make_unit(u_id, u_num, u_title, "KPSS Coğrafya", "0xFF10B981", lessons_code))
        
    dart_lines.append("];")
    return "\n".join(dart_lines)

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "lib", "data")
    out_file = os.path.join(out_dir, "kpss_cografya_units.dart")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(generate_cografya_dart())
    print(f"kpss_cografya_units.dart başarıyla üretildi: {out_file}")
