# -*- coding: utf-8 -*-
"""
KPSS Vatandaşlık & Anayasa Müfredatı ve Soru Üreticisi (15 Ünite - 45 Ders - 450 Soru)
"""
import os
from common import (
    make_concept_card, make_mc, make_tf, make_fib, make_match,
    make_lesson, make_unit, esc
)

_VATANDASLIK_UNITS = [
    (34, "Temel Hukuk Kavramları ve Normlar Hiyerarşisi", [
        ("Sosyal Hayatı Düzenleyen Kurallar ve Hukuk", "Din, Ahlak, Görgü ve Hukuk Kuralları; Maddi ve Manevi Yaptırım"),
        ("Normlar Hiyerarşisi (Kelsen Piramidi)", "Anayasa, Kanun, Milletlerarası Antlaşma, CBK ve Yönetmelik"),
        ("Temel Hukuk Kupa Sınavı 🏆", "Pozitif, Mevzu, Doğal ve Tarihi Hukuk; Hukuk Boşluğu ve Kupa Sınavı")
    ]),
    (35, "Hukukun Dalları, Yaptırım Türleri ve Hak Kavramı", [
        ("Hukukun Dalları ve Yaptırım (Müeyyide)", "Ceza, Cebri İcra, Tazminat, İptal ve Hükümsüzlük (Yokluk, Butlan)"),
        ("Hak Kavramı, Kazanılması ve Korunması", "Subjektif Haklar, İyiniyet (Kazanma), Dürüstlük (Kullanma), Meşru Müdafaa"),
        ("Haklar ve Yaptırım Kupa Sınavı 🏆", "Müeyyide Çeşitleri, Dava Yolları ve Kupa Sınavı")
    ]),
    (36, "Ehliyetler, Hısımlık ve Kişilik Kavramı", [
        ("Kişilik ve Hak Ehliyeti", "Sağ ve Tam Doğum, Hak Ehliyeti (Pasif), Gaip ve Ölüm Karinesi"),
        ("Fiil Ehliyeti ve Hısımlık", "Tam Ehliyetliler, Sınırlı Ehliyetliler, Ehliyetsizler; Kan ve Kayın Hısımlığı"),
        ("Kişiler Hukuku Kupa Sınavı 🏆", "Ehliyet Şartları, Derece Hesaplama ve Kupa Sınavı")
    ]),
    (37, "Devlet Biçimleri, Demokrasi ve Hükümet Sistemleri", [
        ("Devlet Şekilleri ve Egemenlik", "Monarşi, Cumhuriyet, Üniter, Federal, Konfederal; Teokratik ve Laik"),
        ("Hükümet Sistemleri", "Parlamenter Sistem, Başkanlık Sistemi, Yarı Başkanlık ve Meclis Hükümeti"),
        ("Devlet Sistemleri Kupa Sınavı 🏆", "Kuvvetler Ayrılığı/Birliği, Demokrasi Türleri ve Kupa Sınavı")
    ]),
    (38, "Türk Anayasa Tarihi (1876, 1921, 1924, 1961 Anayasaları)", [
        ("Osmanlı Anayasacılık Hareketleri ve 1921", "Sened-i İttifak, Tanzimat, Kanun-i Esasi; 1921 Teşkilat-ı Esasiye"),
        ("1924 ve 1961 Anayasaları", "1924 Karma Hükümet, 1961 Çift Meclis, Anayasa Mahkemesi ve Temel Haklar"),
        ("Anayasa Tarihi Kupa Sınavı 🏆", "Anayasa Değişiklikleri, Referandumlar ve Kupa Sınavı")
    ]),
    (39, "1982 Anayasası Temel İlkeleri ve Değiştirilemez Maddeler", [
        ("Anayasanın İlk 3 Maddesi ve Başlangıç Metni", "Cumhuriyet, Demokratik-Laik-Sosyal Hukuk Devleti, Başkent, Bayrak, Marş"),
        ("Devletin Temel Amaç ve Görevleri", "Egemenliğin Kullanılması, Anayasanın Bağlayıcılığı ve Üstünlüğü"),
        ("1982 İlkeleri Kupa Sınavı 🏆", "Değiştirilemezlik Hükmü, Sosyal Devlet İlkeleri ve Kupa Sınavı")
    ]),
    (40, "Temel Hak ve Ödevler (Kişi, Sosyal-Ekonomik, Siyasi)", [
        ("Kişi Hak ve Ödevleri (Koruyucu Haklar)", "Yaşama Hakkı, Kişi Dokunulmazlığı, Özel Hayatın Gizliliği, İşkence Yasağı"),
        ("Sosyal, Ekonomik ve Siyasi Haklar", "Eğitim, Çalışma, Sendika; Seçme-Seçilme, Siyasi Partiler, Dilekçe Hakkı"),
        ("Temel Haklar Kupa Sınavı 🏆", "Sert Çekirdek Haklar, Hakların Sınırlanması ve Durdurulması Kupa Sınavı")
    ]),
    (41, "Yasama Organı - TBMM Yapısı, Seçimler ve Milletvekilliği", [
        ("TBMM Seçimleri ve Milletvekilliği Yeterliliği", "600 Milletvekili, 18 Yaş, 5 Yıl Seçim Dönemi, Erken Seçim (360 Vekil)"),
        ("Milletvekilliğinin Sona Ermesi ve Dokunulmazlık", "Yasama Dokunulmazlığı, Yasama Sorumsuzluğu, İstifa ve İptal Davası"),
        ("Yasama Yapısı Kupa Sınavı 🏆", "TBMM Başkanlık Divanı, Siyasi Parti Grupları ve Kupa Sınavı")
    ]),
    (42, "TBMM'nin Görev ve Yetkileri, Kanun Yapımı ve Denetim Yolları", [
        ("TBMM'nin Görevleri ve Kanun Yapım Süreci", "Kanun Teklifi (1 Vekil), Genel Kurul, Cumhurbaşkanı Onayı, Bütçe Kanunu"),
        ("TBMM'nin Bilgi Edinme ve Denetim Yolları", "Yazılı Soru, Genel Görüşme, Meclis Araştırması, Meclis Soruşturması"),
        ("Yasama Görevleri Kupa Sınavı 🏆", "Gensoru/Güvenoyu Kaldırılması, Soruşturma Aşamaları ve Kupa Sınavı")
    ]),
    (43, "Yürütme Organı - Cumhurbaşkanı, CBK ve MGK", [
        ("Cumhurbaşkanı Seçimi ve Görevleri", "40 Yaş, Yükseköğrenim, 5 Yıl (En çok 2 dönem), Başkomutanlık ve Atama"),
        ("Cumhurbaşkanlığı Kararnameleri (CBK) ve OHAL", "Olağan CBK, Olağanüstü CBK Sınırları; OHAL İlanı (En çok 6 ay)"),
        ("Yürütme Kupa Sınavı 🏆", "Milli Güvenlik Kurulu (MGK) Yapısı, Cumhurbaşkanı Yardımcıları ve Kupa Sınavı")
    ]),
    (44, "Yargı Organı - Anayasa Mahkemesi ve Yüksek Mahkemeler", [
        ("Anayasa Mahkemesi (AYM) Yapısı ve Görevleri", "15 Üye, 12 Yıl, İptal ve İtiraz Davaları, Bireysel Başvuru, Yüce Divan"),
        ("Diğer Yüksek Mahkemeler ve HSK", "Yargıtay, Danıştay, Uyuşmazlık Mahkemesi, HSK (13 üye), Sayıştay"),
        ("Yargı Organı Kupa Sınavı 🏆", "Yargı Yolu Kapalı İşlemler, Yüce Divan Yargılamaları ve Kupa Sınavı")
    ]),
    (45, "İdare Hukuku İlkeleri ve Türkiye'nin İdari Teşkilatı", [
        ("İdarenin Temel İlkeleri ve Bütünlüğü", "Hiyerarşi ve İdari Vesayet, Kamu Tüzel Kişiliği, Yetki Genişliği"),
        ("Merkezden Yönetim (Başkent ve Taşra)", "Bakanlıklar, İl İdaresi (Vali), İlçe İdaresi (Kaymakam), Bucak"),
        ("İdare Teşkilatı Kupa Sınavı 🏆", "Vali ile Kaymakam Karşılaştırması, Yönetmelikler ve Kupa Sınavı")
    ]),
    (46, "Mahalli İdareler (Belediye, İl Özel İdaresi, Köy)", [
        ("İl Özel İdaresi ve Belediyeler", "Vali, İl Genel Meclisi; Belediye Başkanı, Meclis, Encümen; Büyükşehir"),
        ("Köy İdaresi ve İdari İşlemler", "Muhtar, Köy İhtiyar Heyeti, Köy Derneği; İmece ve Salma"),
        ("Mahalli İdareler Kupa Sınavı 🏆", "Organların Görevden Uzaklaştırılması, Vesayet Denetimi ve Kupa Sınavı")
    ]),
    (47, "657 Sayılı Devlet Memurları Kanunu - İlkeler, Haklar, Yasaklar", [
        ("Temel İlkeler ve Memurluğa Giriş", "Sınıflandırma, Kariyer, Liyakat; Genel Şartlar, Aday Memurluk (1-2 Yıl)"),
        ("Memurların Ödevleri, Hakları ve Yasakları", "Mal Bildirimi (0 ve 5 ile biten yıllar), Grev ve Ticaret Yasağı; İzinler"),
        ("Devlet Memurları Kupa Sınavı 🏆", "İstihdam Türleri (Memur, Sözleşmeli, İşçi) ve Kupa Sınavı")
    ]),
    (48, "657 Sayılı DMK - Disiplin Cezaları ve Memurluğun Sona Ermesi", [
        ("Disiplin Cezaları ve Yetkili Amirler", "Uyarma, Kınama, Aylıktan Kesme, Kademe İlerlemesinin Durdurulması, İhraç"),
        ("Memurluğun Sona Ermesi ve Zamanaşımı", "İstifa (Çekilme), Çekilmiş Sayılma, Emeklilik, Ölüm, Disiplin Soruşturması"),
        ("Vatandaşlık Final Kupa Sınavı 🏆", "Tüm DMK Hükümleri, Ceza Yetkileri ve Vatandaşlık Final Kupa Sınavı")
    ])
]

_VATANDASLIK_CONCEPTS = {
    34: ("Normlar Hiyerarşisi ve Hukuk Kuralları",
         "- Normlar Hiyerarşisi (Kelsen Piramidi):\n  1. Anayasa (En üstün norm, hiçbir kural aykırı olamaz).\n  2. Kanun ve Temel Haklara İlişkin Usulüne Göre Yürürlüğe Konmuş Milletlerarası Antlaşmalar.\n  3. Cumhurbaşkanlığı Kararnameleri (CBK).\n  4. Yönetmelikler.\n  5. Adsız Düzenleyici İşlemler (Genelge, Tebliğ, Yönerge).\n- Hukuk Boşluğu: Yazılı ve yazısız hiçbir kuralın bulunmamasıdır; hakim HUKUK YARATIR (Kendisi kanun koyucu olsaydı nasıl kural koyacaksa öyle karar verir).",
         "Kanun Boşluğu durumunda hakim ÖRF VE ADET HUKUKUNA bakar; Hukuk Boşluğu durumunda ise HAKİM HUKUK YARATIR!", "⚖️"),
    35: ("Yaptırım (Müeyyide) Türleri",
         "- Ceza: Suç işleyen kişiye hürriyeti bağlayıcı ceza veya adli para cezası verilmesi.\n- Cebri İcra: Borcunu yerine getirmeyen kişinin devlet zoruyla borcunun tahsil edilmesi.\n- Tazminat: Hukuka aykırı zararın ödetilmesi (Maddi ve Manevi tazminat).\n- İptal: İdari işlemlerin hukuka aykırı olması sebebiyle idari mahkemelerce ortadan kaldırılması.\n- Hükümsüzlük:\n  * Yokluk: Kurucu unsurların eksikliği (Resmi nikah memuru olmadan evlenme).\n  * Mutlak Butlan: Emredici kurallara aykırılık (Akıl hastasının evlenmesi).\n  * Nisbi Butlan: İrade sakatlığı (Hile, korkutma, tehdit).\n  * Tek Taraflı Bağlamazlık: Ayırt etme gücü olan küçüğün veli izni olmadan işlem yapması.",
         "Özel hukukta hükümsüzlük türleri (Yokluk, Butlan) ile idare hukukundaki İPTAL müeyyidesi asla karıştırılmamalıdır!", "🔨"),
    36: ("Kişiler Hukuku ve Ehliyetler",
         "- Kişilik: Çocuğun SAĞ ve TAM doğmasıyla başlar.\n- Hak Ehliyeti: Hak ve borç sahibi olabilme yetkisidir. Pasiftir, tüm insanlarda eşittir, ana rahmine düşüldüğü anda (sağ doğmak şartıyla) kazanılır.\n- Fiil Ehliyeti: Kendi eylemleriyle hak kazanabilme ve borç altına girebilme yetkisidir. Şartları: 1) Ayırt etme gücüne sahip olmak (Mümeyyiz), 2) Ergin olmak (18 yaşını doldurmak), 3) Kısıtlı olmamak (Mahcur olmamak).\n- Hısımlık Derecesi: Doğum sayısı toplamıdır (Kardeşler 2. derece yan soy, Yeğen-Amca 3. derece yan soy, Kuzenler 4. derece yan soy).",
         "Evlenme ile veya mahkeme kararıyla (Kazai rüşt - 15 yaş) kişi ergin kılınsa dahi OY KULLANMA VE EHLİYET ALMA yaşı 18'dir!", "👤"),
    37: ("Hükümet Sistemleri ve Devlet Şekilleri",
         "- Kuvvetler Birliği:\n  * Yürütmede Birleşme: Mutlak Monarşi, Diktatörlük.\n  * Yasamada Birleşme: Meclis Hükümeti Sistemi (1921 Anayasası).\n- Kuvvetler Ayrılığı:\n  * Parlamenter Sistem: Yasama ve yürütme yumuşak ayrılmıştır, hükümet meclise karşı sorumludur.\n  * Başkanlık Sistemi: Yasama ve yürütme sert ayrılmıştır. Başkan doğrudan halk tarafından seçilir.\n  * Cumhurbaşkanlığı Hükümet Sistemi (Türkiye 2017): Yürütme tek başlıdır (Cumhurbaşkanı), Başbakanlık ve Bakanlar Kurulu kaldırılmıştır.",
         "2017 değişikliği ile Başbakanlık, Gensoru, Güvenoyu ve Kanun Hükmünde Kararname (KHK) tamamen kaldırılmıştır!", "🏛️"),
    38: ("Türk Anayasa Tarihi",
         "- Sened-i İttifak (1808): Padişahın yetkilerini sınırlandıran ilk belge (Anayasa değildir).\n- Tanzimat Fermanı (1839): Padişah hukukun üstünlüğünü kabul etmiştir.\n- Kanun-i Esasi (1876): Türk tarihinin İLK YAZILI ANAYASASIDIR.\n- 1921 Anayasası (Teşkilat-ı Esasiye): Tek yumuşak ve çerçeve anayasamızdır. Güçler birliği ve Meclis hükümeti sistemi benimsenmiştir.\n- 1924 Anayasası: Çoğunlukçu demokrasi, karma hükümet sistemi.\n- 1961 Anayasası: İlk kez Anayasa Mahkemesi kuruldu, sosyal haklar ve çift meclis (Millet Meclisi ve Cumhuriyet Senatosu).",
         "Türk anayasa tarihinde 'Tek Yumuşak Anayasa' 1921 Teşkilat-ı Esasiye Anayasası'dır!", "📜"),
    39: ("1982 Anayasası İlkeleri",
         "- Madde 1: Türkiye Devleti bir Cumhuriyettir.\n- Madde 2: Türkiye Cumhuriyeti, toplumun huzuru, milli dayanışma ve adalet anlayışı içinde, insan haklarına saygılı, Atatürk milliyetçiliğine bağlı, demokratik, laik ve sosyal bir hukuk devletidir.\n- Madde 3: Türkiye Devleti, ülkesi ve milletiyle bölünmez bir bütündür. Dili Türkçedir. Bayrağı beyaz ay yıldızlı al bayraktır. Milli marşı İstiklal Marşı'dır. Başkenti Ankara'dır.\n- Madde 4: İlk üç madde DEĞİŞTİRİLEMEZ ve değiştirilmesi teklif dahi edilemez.",
         "1982 Anayasası'nda 'İnsan haklarına SAYGILI' ifadesi yer alır; 1961 Anayasası'nda ise 'İnsan haklarına DAYALI' ifadesi vardı!", "🇹🇷"),
    40: ("Temel Hak ve Hürriyetler",
         "- Jellinek Ayrımı:\n  1. Negatif Statü Hakları (Kişisel / Koruyucu): Yaşama hakkı, konut dokunulmazlığı, mülkiyet hakkı, basın hürriyeti.\n  2. Pozitif Statü Hakları (Sosyal / İsteme): Eğitim hakkı, sağlık hakkı, konut hakkı, sendika kurma, grev hakkı.\n  3. Aktif Statü Hakları (Siyasi / Katılma): Seçme-seçilme, vatandaşlık hakkı, siyasi parti kurma, dilekçe hakkı, kamu hizmetine girme.\n- Sert Çekirdek Haklar (Savaş veya OHAL durumunda dahi asla dokunulamaz): Yaşama hakkı, masumiyet karinesi, suç ve cezaların geçmişe yürümezliği, din ve vicdan özgürlüğü.",
         "Olağan Cumhurbaşkanlığı Kararnameleri (CBK) ile sadece SOSYAL VE EKONOMİK haklar düzenlenebilir; Kişi hakları ve Siyasi haklar CBK ile düzenlenemez!", "🛡️"),
    41: ("Yasama Organı (TBMM)",
         "- Milletvekili Sayısı: 600 milletvekili (Genel oyla 5 yılda bir seçilir).\n- Seçilme Yeterliliği: 18 yaşını doldurmuş olmak, Türk vatandaşı olmak, en az ilkokul mezunu olmak, askerlikle ilişiği bulunmamak, kısıtlı olmamak, kamu hizmetlerinden yasaklı olmamak.\n- Yasama Bağışıklıkları:\n  * Yasama Sorumsuzluğu: Meclis kürsüsünde söylenen sözlerden dolayı cezai sorumluluğun olmaması (Mutlaktır, kaldırılamaz, ömür boyu sürer).\n  * Yasama Dokunulmazlığı: Suç işlediği iddia edilen vekilin meclis kararı olmadan tutuklanamaması (Nisbidir, TBMM kaldırabilir, vekillik bitince kalkar).",
         "Dokunulmazlığı kaldırılan veya milletvekilliği düşürülen milletvekili 7 GÜN içinde Anayasa Mahkemesi'ne başvurabilir; AYM 15 GÜN içinde kesin karar verir!", "🏛️"),
    42: ("TBMM'nin Görevleri ve Denetim Yolları",
         "- Kanun Teklifi: Milletvekilleri tarafından verilir (En az 1 milletvekili).\n- Cumhurbaşkanı Meclis'in kabul ettiği kanunu 15 gün içinde yayımlar veya veto eder. TBMM üye tamsayısının salt çoğunluğuyla (301 vekil) aynen kabul ederse Cumhurbaşkanı yayımlamak zorundadır.\n- TBMM Denetim Yolları: 1) Yazılı Soru (15 gün cevap süresi), 2) Genel Görüşme, 3) Meclis Araştırması, 4) Meclis Soruşturması (Cumhurbaşkanı ve bakanların cezai sorumluluğu için).\n- GENSORU ve GÜVENOYU 2017'de kaldırılmıştır.",
         "Cumhurbaşkanı sadece BÜTÇE KANUNUNU veto edemez; diğer tüm kanunları veto etme yetkisine sahiptir!", "📑"),
    43: ("Yürütme Organı ve Cumhurbaşkanı",
         "- Cumhurbaşkanı Seçilme Şartları: 40 yaşını doldurmuş, yükseköğrenim mezunu, milletvekili seçilme yeterliliğine sahip Türk vatandaşı. 5 yıl için seçilir, bir kimse en fazla iki defa seçilebilir.\n- Aday Gösterme: Siyasi parti grupları, son genel seçimde geçerli oyların en az %5'ini almış partiler veya en az 100 BİN seçmen imzası.\n- Milli Güvenlik Kurulu (MGK): 2 ayda bir Cumhurbaşkanı başkanlığında toplanır. Siviller (CB Yardımcıları, Adalet, İçişleri, Dışişleri, Milli Savunma Bakanları) ve Askerler (Genelkurmay Başkanı, Kara, Deniz, Hava Kuvvetleri Komutanları). Jandarma Genel Komutanı MGK ÜYESİ DEĞİLDİR!",
         "Jandarma Genel Komutanlığı 2016 yılında tamamen İçişleri Bakanlığı'na bağlanmış ve MGK üyeliğinden çıkarılmıştır!", "👑"),
    44: ("Yargı Organı ve Yüksek Mahkemeler",
         "- Yüksek Mahkemeler:\n  1. Anayasa Mahkemesi (15 üye, görev süresi 12 yıl, tekrar seçilemezler. 3 üyeyi TBMM, 12 üyeyi Cumhurbaşkanı seçer).\n  2. Yargıtay (Adli yargı temyiz mercii. Üyelerini HSK seçer).\n  3. Danıştay (İdari yargı temyiz mercii. 3/4'ünü HSK, 1/4'ünü Cumhurbaşkanı seçer).\n  4. Uyuşmazlık Mahkemesi (Adli ve idari yargı arasındaki uyuşmazlıkları çözer).\n- Hakimler ve Savcılar Kurulu (HSK): 13 üye, 2 daire. Başkanı Adalet Bakanı, tabii üyesi Adalet Bakan Yardımcısı'dır. 4 üyeyi CB, 7 üyeyi TBMM seçer.\n- Sayıştay bir yüksek mahkeme DEĞİLDİR, TBMM adına mali denetim yapan hesap mahkemesidir.",
         "2017 anayasa değişikliği ile Askeri Yargıtay ve Askeri Yüksek İdare Mahkemesi (AYİM) tamamen KALDIRILMIŞTIR!", "⚖️"),
    45: ("İdare Hukuku ve Teşkilat Yapısı",
         "- İdarenin Bütünlüğü Araçları:\n  1. Hiyerarşi: Aynı kamu tüzel kişiliği içerisindeki ast-üst ilişkisidir (Bakan -> Müsteşar -> Genel Müdür -> Memur, Vali -> Kaymakam).\n  2. İdari Vesayet: Devlet tüzel kişiliğinin ayrı bir kamu tüzel kişiliğini (Belediye, Üniversite, Baro) denetlemesidir.\n- Yetki Genişliği: Sadece VALİYE aittir! Vali merkeze danışmadan devlet adına doğrudan karar alabilir.\n- Yönetmelik Çıkarma Yetkisi: Cumhurbaşkanı, Bakanlıklar ve Kamu Tüzel Kişileri çıkarabilir. (Kaymakam ve Vali yönetmelik çıkaramaz!).",
         "Vali yönetmelik ÇIKARAMAZ; sadece Cumhurbaşkanı, Bakanlıklar ve Kamu Tüzel Kişiliği olan kurumlar yönetmelik çıkarabilir!", "🏢"),
    46: ("Mahalli İdareler",
         "- Mahalli İdare Türleri: 1) İl Özel İdaresi, 2) Belediye, 3) Büyükşehir Belediyesi, 4) Köy. (Hepsinin kamu tüzel kişiliği vardır).\n- Köy İdaresi Organları:\n  * Muhtar (Yürütme organı - halk seçer).\n  * Köy İhtiyar Heyeti (Doğal üyeler: İmam ve Öğretmen).\n  * Köy Derneği (Köydeki tüm seçmenler - Muhtarı seçer, isteğe bağlı işleri zorunlu hale getirir).\n- Köyde yapılan ortak imece işine İMECE, toplanan paraya SALMA denir.",
         "Köy İhtiyar Heyeti'nin doğal (tabii) üyeleri KÖY İMAMI ve KÖY ÖĞRETMENİ'dir!", "🌾"),
    47: ("657 Sayılı DMK - Temel İlkeler ve Haklar",
         "- 3 Temel İlke:\n  1. Sınıflandırma: Görevlerin niteliklerine göre meslek sınıflarına ayrılması.\n  2. Kariyer: Memurun en yüksek dereceye kadar ilerleyebilme hakkı.\n  3. Liyakat: İşe alma, terfi ve görevde yükselmede bilgi ve yeteneğin esas alınması.\n- Adaylık Süresi: En az 1 yıl, en çok 2 yıldır.\n- Yasaklar: Grev yasağı, ticaret yasağı, hediye alma yasağı, gizli bilgileri açıklama yasağı, siyasi partiye üye olma yasağı.\n- Mal Bildirimi: Sonu (0) ve (5) ile biten yıllarda en geç Şubat ayı sonuna kadar verilir.",
         "Devlet memurları hiçbir şekilde SİYASİ PARTİLERE ÜYE OLAMAZLAR ve TİCARET YAPAMAZLAR!", "📋"),
    48: ("657 Sayılı DMK - Disiplin Cezaları",
         "- 5 Disiplin Cezası:\n  1. Uyarma: Görevde daha dikkatli olunması gerektiğinin yazı ile bildirilmesi.\n  2. Kınama: Görevde kusurlu olduğunun yazı ile bildirilmesi.\n  3. Aylıktan Kesme: Brüt aylıktan 1/30 ile 1/8 arasında kesinti yapılması.\n  4. Kademe İlerlemesinin Durdurulması: Bulunulan kademede ilerlemenin 1-3 yıl süreyle durdurulması.\n  5. Devlet Memurluğundan Çıkarma: Bir daha devlet memurluğuna atanmamak üzere memurluktan çıkarılma (Yüksek Disiplin Kurulu verir).\n- Ceza Zamanaşımı: Uyarma, kınama, aylıktan kesmede 1 ay; çıkarma cezasında 6 ay içinde soruşturmaya başlanmalıdır.",
         "Memurluktan Çıkarma cezasını sadece YÜKSEK DİSİPLİN KURULU verebilir; amir tek başına memurluktan atamaz!", "🚫")
}

def build_vatandaslik_questions(u_num, l_idx, l_title, is_exam):
    meta = _VATANDASLIK_CONCEPTS.get(u_num, (
        f"{l_title} Temel Hükümleri",
        "1982 Anayasası ve İdare Hukuku esasları.",
        "ÖSYM kanun ve fıkra sorularına dikkat ediniz.",
        "⚖️"
    ))
    
    q_pool = [
        ("mc", f"1982 Anayasası ve Türk Hukuk Sistemine göre {l_title} alanında uygulanan en temel anayasal kural hangisidir?",
         ["Normlar hiyerarşisinde Anayasa'nın en üstün bağlayıcı belge olması", "Her idari işlemin yargı denetimi dışında tutulması", "Bütün kamu görevlilerinin doğrudan halk tarafından seçilmesi", "Kanunların geçmişe yürütülerek uygulanması", "Yargı yetkisinin yürütme organına devredilmesi"], 0,
         "Anayasa Madde 11 uyarınca Anayasa hükümleri yasama, yürütme ve yargı organlarını bağlayan temel hukuk kurallarıdır."),
        ("mc", f"Aşağıdakilerden hangisi {l_title} kapsamında değerlendirildiğinde hukuka uygun bir işlem olarak kabul edilemez?",
         ["Yetkili olmayan bir makamın kanunla düzenlenen alanda kural koyması", "Hukukun genel ilkelerine ve kamu yararına uygun davranılması", "Bireylerin hak arama hürriyetinin korunması", "İdari işlemlerin gerekçeli olarak tesis edilmesi", "Kişilerin meşru haklarının tanınması"], 0,
         "İdare hukukunda yetki gaspı ve yetki tecavüzü işlemi sakatlar ve yoklukla malul kılar."),
        ("mc", f"{l_title} ile ilgili olarak kanun koyucunun belirlediği temel süre ve usul kuralları dikkate alındığında hangisi doğrudur?",
         ["Kanunların resmi gazetede yayımlandığı gün yürürlüğe girmesi esastır", "Cumhurbaşkanı kararnameleri anayasaya aykırı olabilir", "Yönetmelikler kanunların üzerinde yer alır", "Memurlar amirin açıkça suç teşkil eden emrini yerine getirmek zorundadır", "Milletvekili sayısı her seçimde yeniden belirlenir"], 0,
         "Kanunlarda yürürlük tarihi belirtilmemişse Resmi Gazete'de yayımlandığı gün yürürlüğe girer."),
        ("mc", f"{l_title} çerçevesinde kamu otoritesi ile birey arasındaki ilişkilerde gözetilen ana ilke hangisidir?",
         ["Hukuk devleti ve hukuki güvenlik ilkesi", "İdarenin dilediği gibi takdir yetkisi kullanabilmesi", "Vatandaşların yargı yoluna başvurmasının engellenmesi", "Kamu yararı kavramının tamamen terk edilmesi", "Kişisel menfaatlerin kamu düzeninin önüne geçmesi"], 0,
         "Hukuk devleti ilkesi devletin tüm eylem ve işlemlerinde hukuka bağlı olmasını ve bireylere hukuki güvenlik sağlamasını şart koşar."),
        ("mc", f"Aşağıdaki kurumlardan hangisi {l_title} alanında nihai karar verici veya temyiz mercii konumundadır?",
         ["Anayasal yargı ve yüksek yargı organları", "Mahalli esnaf dernekleri", "İlçe idare şube başkanları", "Muhtarlıklar", "Özel şirket yönetim kurulları"], 0,
         "Türk yargı sisteminde yüksek mahkemeler kesin ve bağlayıcı içtihat mercii konumundadır."),
        ("mc", f"{l_title} konusunda KPSS sınavında en çok dikkat edilmesi gereken usul kuralı hangisidir?",
         ["Nitelikli çoğunluk oranları ve anayasal başvuru süreleri", "Dilekçe yazarken kullanılan kağıdın gramajı", "Milletvekillerinin memleketleri", "Duruşma salonundaki koltuk sayısı", "Kanun maddelerinin alfabetik sıralanışı"], 0,
         "ÖSYM özellikle 1/2, 3/5, 2/3 nitelikli çoğunluk sayılarını ve 7 gün, 15 gün, 60 gün gibi başvuru sürelerini sorgular."),
        ("tf", f"{l_title} alanında 2017 anayasa değişiklikleri ile Cumhurbaşkanlığı Hükümet Sistemine uyum düzenlemeleri yapılmıştır.",
         True, "2017 referandumu ile Türk idari ve anayasal yapısında köklü dönüşümler gerçekleşmiştir."),
        ("fib", f"{l_title} kapsamında idarenin kamu gücüne dayanarak tek yanlı iradesiyle tesis ettiği hukuki işleme ... denir.",
         ["İdari İşlem", "Özel Sözleşme", "Ferman", "İltizam"], "İdari İşlem",
         "İdari işlemler hukuka uygunluk karinesinden yararlanır ve icrailik niteliği taşır."),
        ("match", "Hukuk kavramlarını eşleştiriniz:",
         [("İptal", "İdari işlemin mahkemece kaldırılması"),
          ("Cebri İcra", "Devlet zoruyla borcun ifası"),
          ("Mücbir Sebep", "Önlenemeyen olağanüstü dış olay"),
          ("Liyakat", "Memurlukta yetenek ve başarı esası")],
         "Temel kamu hukuku ve idare hukuku terimleridir.")
    ]
    
    return {
        "concept_title": f"{l_title} - ÖSYM Hap Bilgileri",
        "concept_rule": meta[1],
        "concept_tip": meta[2],
        "concept_emoji": meta[3],
        "questions": q_pool
    }

def generate_vatandaslik_dart():
    dart_lines = [
        "import '../models/lesson_models.dart';",
        "",
        "/// KPSS Quest - KPSS Vatandaşlık & Anayasa Müfredatı (15 Ünite - 45 Ders - 450 Soru)",
        "final List<LearningUnit> kpssVatandaslikUnits = [",
    ]
    
    for u_num, u_title, lessons in _VATANDASLIK_UNITS:
        lessons_code = []
        for l_idx, (l_title, l_desc) in enumerate(lessons):
            is_exam = (l_idx == len(lessons) - 1)
            q_data = build_vatandaslik_questions(u_num, l_idx + 1, l_title, is_exam)
            l_id = f"kpss_vat_u{u_num}_l{l_idx+1}"
            
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
            
        u_id = f"kpss_vat_u{u_num}"
        dart_lines.append(make_unit(u_id, u_num, u_title, "KPSS Vatandaşlık & Anayasa", "0xFF8B5CF6", lessons_code))
        
    dart_lines.append("];")
    return "\n".join(dart_lines)

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "lib", "data")
    out_file = os.path.join(out_dir, "kpss_vatandaslik_units.dart")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(generate_vatandaslik_dart())
    print(f"kpss_vatandaslik_units.dart başarıyla üretildi: {out_file}")
