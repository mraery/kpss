# -*- coding: utf-8 -*-
"""
KPSS Türkçe & Sözel Mantık Müfredatı ve Soru Üreticisi (14 Ünite - 42 Ders - 420 Soru)
"""
import os
from common import (
    make_concept_card, make_mc, make_tf, make_fib, make_match,
    make_lesson, make_unit, esc
)

_TURKCE_UNITS = [
    (55, "KPSS Dil Bilgisi ve Sözel Mantık", [
        ("Gerçek, Mecaz ve Terim Anlam", "Temel Anlam, Yan Anlam, Mecaz Anlam, Terim Anlam, Somutlaştırma ve Soyutlaştırma"),
        ("Söz Öbekleri ve Anlam Olayları", "Deyimler, Atasözleri, Dolaylama, Güzel Adlandırma, Ad Aktarması (Mecazımürsel)"),
        ("Sözcükte Anlam Kupa Sınavı 🏆", "İkilemeler, Yansıma Sözcükler ve Sözcükte Anlam Kupa Sınavı")
    ]),
    (56, "Cümlede Anlam, Kesin Yargı ve Örtülü Anlam", [
        ("Cümleler Arası Anlam İlişkileri", "Sebep-Sonuç (Neden), Amaç-Sonuç, Koşul-Sonuç (Şart), Karşılaştırma"),
        ("Cümle Yorumu ve Kesin Yargı Çıkarma", "Öznel ve Nesnel Anlatım, Doğrudan ve Dolaylı Anlatım, Örtülü Anlam, Çıkarım"),
        ("Cümlede Anlam Kupa Sınavı 🏆", "Aşamalı Durum, Olasılık, Varsayım, Eleştiri ve Cümlede Anlam Kupa Sınavı")
    ]),
    (57, "Paragrafta Ana Düşünce ve Konu", [
        ("Paragrafta Konu ve Başlık Belirleme", "Paragrafın Yazılış Amacı, Yazarın Üzerinde Durduğu Temel Duygu"),
        ("Paragrafta Ana Fikir ve Vurgulanan Yargı", "Ana Düşünce Cümlesi, İlk ve Son Cümle Analizi, Asıl Anlatılmak İstenen"),
        ("Ana Düşünce Kupa Sınavı 🏆", "ÖSYM Paragraf Taktikleri, Soru Kökü Analizi ve Kupa Sınavı")
    ]),
    (58, "Paragrafta Yardımcı Düşünceler ve Yapı", [
        ("Yardımcı Fikirler (Değinilmemiştir / Çıkarılamaz)", "Olumsuz Soru Kökleri, Şık Eleme Yöntemi ve Anahtar Sözcükler"),
        ("Paragrafta Yapı ve Akışı Bozan Cümle", "Paragrafı İkiye Bölme, Paragraf Tamamlama, Cümlelerin Yerini Değiştirme"),
        ("Paragrafta Yapı Kupa Sınavı 🏆", "Giriş-Gelişme-Sonuç Bağlantıları, Düşüncenin Akışı ve Kupa Sınavı")
    ]),
    (59, "Anlatım Biçimleri ve Düşünceyi Geliştirme Yolları", [
        ("4 Temel Anlatım Biçimi", "Öyküleme (Olay, kişi, zaman, mekan), Betimleme (Sözcüklerle resim yapma), Açıklama, Tartışma"),
        ("Düşünceyi Geliştirme Yolları", "Tanımlama, Karşılaştırma, Örnekleme, Tanık Gösterme, Sayısal Verilerden Yararlanma, Benzetme"),
        ("Anlatım Teknikleri Kupa Sınavı 🏆", "Anlatıcı Türleri (1. ve 3. Kişi), Bakış Açıları (İlahi, Kahraman, Gözlemci) ve Kupa Sınavı")
    ]),
    (60, "Ses Bilgisi ve Ses Olayları", [
        ("Ünlü Uyumları ve Ünlü Olayları", "Büyük ve Küçük Ünlü Uyumu, Ünlü Düşmesi, Ünlü Daralması, Ünlü Türemesi"),
        ("Ünsüz Olayları", "Ünsüz Yumuşaması (Değişimi), Ünsüz Benzeşmesi (Sertleşme), Ünsüz Türemesi, Kaynaştırma, Ulama"),
        ("Ses Bilgisi Kupa Sınavı 🏆", "Tüm Ses Olayları, Tuzak Kelimeler ve Ses Bilgisi Kupa Sınavı")
    ]),
    (61, "Yazım Kuralları ve TDK İpuçları", [
        ("Büyük Harfler, Ekler ve Kısaltmalar", "Büyük Harflerin Kullanımı, 'de/da' Bağlacı, 'ki' Bağlacı, 'mi' Soru Eki, Kısaltmalar"),
        ("Birleşik Sözcüklerin ve Sayıların Yazımı", "Bitişik ve Ayrı Yazılan Birleşik Kelimeler, Sayıların Yazımı, İkilemeler"),
        ("Yazım Kuralları Kupa Sınavı 🏆", "TDK Güncel Değişiklikleri, Sık Yapılan Hatalar ve Kupa Sınavı")
    ]),
    (62, "Noktalama İşaretleri ve Kullanım Yerleri", [
        ("Nokta, Virgül ve Noktalı Virgül", "Virgülün Kullanıldığı ve Kullanılmadığı Yerler, Noktalı Virgül Mantığı"),
        ("İki Nokta, Üç Nokta ve Diğer İşaretler", "İki Nokta, Üç Nokta, Soru ve Ünlem İşareti, Tırnak, Yay Ayraç, Kesme İşareti"),
        ("Noktalama İşaretleri Kupa Sınavı 🏆", "ÖSYM Noktalama Paragrafları ve Kupa Sınavı")
    ]),
    (63, "Sözcükte Yapı, Kökler ve Ekler", [
        ("Kök Türleri ve Yapım Ekleri", "İsim Kökü, Fiil Kökü, Sesteş Kök, Ortak Kök; İsimden İsim/Fiil, Fiilden İsim/Fiil Yapım Ekleri"),
        ("Çekim Ekleri ve Sözcüğün Yapısı", "İsim Çekim Ekleri (Çokluk, Durum, İyelik, İlgi); Basit, Türemiş ve Birleşik Sözcükler"),
        ("Sözcükte Yapı Kupa Sınavı 🏆", "İyelik Ekleri ile Belirtme Hali Ayrımı ve Yapı Kupa Sınavı")
    ]),
    (64, "Sözcük Türleri (İsim, Sıfat, Zamir, Zarf)", [
        ("İsimler (Adlar) ve Sıfatlar (Ön Adlar)", "Varlıklara Verilişine Göre İsimler; Niteleme ve Belirtme (İşaret, Sayı, Belgisiz, Soru) Sıfatları"),
        ("Zamirler (Adıllar) ve Zarflar (Belirteçler)", "Kişi, İşaret, Belgisiz, Soru Zamirleri; Durum, Zaman, Miktar, Yer-Yön, Soru Zarfları"),
        ("İsim Soylu Sözcükler Kupa Sınavı 🏆", "Edat (İlgeç), Bağlaç, Ünlem ve Sözcük Türleri Kupa Sınavı")
    ]),
    (65, "Fiiller, Ek Fiil, Fiilimsiler ve Fiilde Çatı", [
        ("Fiil Çekimi ve Ek Fiil (Ek Eylem)", "Haber ve Dilek Kipleri, Basit ve Birleşik Zamanlı Fiiller; Ek Fiilin 2 Görevi"),
        ("Fiilimsiler (Eylemsiler) ve Fiilde Çatı", "İsim-Fiil (Ma-Iş-Mak), Sıfat-Fiil (An-Ası-Mez-Ar-Dik-Ecek-Miş), Zarf-Fiil; Özne ve Nesnesine Göre Çatı"),
        ("Fiiller Kupa Sınavı 🏆", "Etken, Edilgen, Dönüşlü, İşteş; Geçişli, Geçişsiz, Oldurgan, Ettirgen Kupa Sınavı")
    ]),
    (66, "Cümlenin Ögeleri ve Cümle Türleri", [
        ("Temel ve Yardımcı Ögeler", "Yüklem, Özne; Nesne (Belirtili/Belirtisiz), Yer Tamlayıcısı (Dolaylı Tümleç), Zarf Tümleci"),
        ("Cümle Türleri ve Yapısı", "Yüklemin Türüne (İsim/Fiil), Yerine (Kurallı/Devrik), Anlamına (Olumlu/Olumsuz) ve Yapısına (Basit, Birleşik, Sıralı, Bağlı) Göre Cümleler"),
        ("Cümle Bilgisi Kupa Sınavı 🏆", "Öge Vurgusu, Ara Söz, Cümle Dışı Unsurlar ve Kupa Sınavı")
    ]),
    (67, "Anlatım Bozuklukları (Anlamsal ve Yapısal)", [
        ("Anlama Dayalı Anlatım Bozuklukları", "Gereksiz Sözcük Kullanımı, Sözcüğün Yanlış Anlamda Kullanımı, Anlamca Çelişen Sözcükler, Mantık Hatası"),
        ("Dil Bilgisine Dayalı Anlatım Bozuklukları", "Özne-Yüklem Uyumsuzluğu, Öge Eksikliği, Ek Fiil/Fiilimsi Uyuşmazlığı, Tamlama Yanlışları, Çatı Uyuşmazlığı"),
        ("Anlatım Bozukluğu Kupa Sınavı 🏆", "Tüm Anlatım Bozuklukları ve Kupa Sınavı")
    ]),
    # Unit 68
    (68, "Sözel Mantık ve Tablo Yorumlama", [
        ("Sözel Mantık Temel Kavramları ve Tablo Oluşturma", "Sabit ve Değişken Kriterler, Kişi-Sıra-Grup Tabloları Kurma"),
        ("Öncül Yorumlama ve İhtimal Hesapları", "Kesin Doğru, Kesin Yanlış ve İhtimal Yargılarını Belirleme"),
        ("Sözel Mantık Kupa Sınavı 🏆", "Çıkmış KPSS Formatında 4 Soruluk Mini Sözel Mantık Seti ve Kupa Sınavı")
    ])
]

_TURKCE_CONCEPTS = {
    55: ("Sözcükte Anlam İlişkileri",
         "- Gerçek Anlam: Sözcüğün akla gelen ilk ve temel anlamıdır.\n- Mecaz Anlam: Sözcüğün gerçek anlamından tamamen uzaklaşarak kazandığı yeni soyut anlamdır.\n- Terim Anlam: Bilim, sanat, spor veya meslek dalına özgü özel kavramlardır.\n- Ad Aktarması (Mecazımürsel): Benzetme amacı gütmeden bir sözcüğün başka bir sözcük yerine kullanılmasıdır ('Sobayı yaktık' -> Odunları, 'Marmara'da gemiler battı').\n- Somutlaştırma: Soyut bir kavramın somut bir varlıkla anlatılmasıdır ('Fikirleri çok sivriydi').",
         "Deyimler ve atasözleri genellikle MECAZ anlamlıdır; ancak 'Dost ile ye, iç; alışveriş etme' gibi tamamen GERÇEK anlamlı atasözleri de vardır!", "📖"),
    56: ("Cümlede Anlam ve Kesin Yargı",
         "- Sebep-Sonuç: Eylem gerekçesiyle birlikte verilir ('Kar yağdığı için yollar kapandı' -> İkisi de gerçekleşmiştir).\n- Amaç-Sonuç: Ulaşılmak istenen bir hedef vardır ('Sınavı kazanmak amacıyla gece gündüz çalıştı' -> Hedef henüz gerçekleşmemiştir).\n- Koşul-Sonuç: Bir durumun gerçekleşmesi başka bir şarta bağlıdır ('Düzenli tekrar yaparsan konuları unutmazsın').\n- Kesin Yargı: Parçada verilen bilgilerden yüzde yüz çıkarılabilen, hiçbir yoruma veya tahmine dayanmayan nesnel sonuçtur.",
         "ÖSYM'nin 'Kesin olarak çıkarılabilir' sorularında parçada geçmeyen hiçbir yorum şıkka dahil edilemez; birebir örtüşen yargı aranır!", "🎯"),
    57: ("Paragrafta Ana Düşünce",
         "- Paragrafın Konusu: Parçada 'Neden bahsediliyor?' sorusunun cevabıdır.\n- Paragrafın Ana Düşüncesi: Yazarın okuyucuya vermek istediği 'ASIL MESAJ'dır. 'Bana ne anlatmak istiyor?' sorusunun cevabıdır.\n- Ana düşünce genellikle 'Özetle, oysa, asıl mesele, demek ki, kısacası, sonuç olarak' gibi bağlaçlardan sonra gelir.\n- Başlık paragrafın hem konusunu hem ana fikrini kapsayan en özlü ifadedir.",
         "Ana fikir sorularında ilk ve son cümlelere özellikle dikkat edilmelidir; tümdengelim paragraflarında başta, tümevarım paragraflarında sonda yer alır!", "💡"),
    58: ("Paragrafta Yapı ve Akış",
         "- Akışı Bozan Cümle: Paragrafın genelinde anlatılan konudan farklı bir boyuta geçen, düşüncenin yönünü değiştiren cümledir.\n- Paragrafı İkiye Bölme: Yazarın konunun farklı bir yönüne geçtiği cümleden itibaren ikinci paragraf başlar.\n- Giriş Cümlesi Özellikleri: Kendisinden önce bir cümle varmış hissi uyandırmaz ('Çünkü, nitekim, bundan dolayı, bu yüzden' ile başlayamaz).",
         "Paragrafı ikiye bölme sorularında yeni düşüncenin veya konunun farklı bir yönünün başladığı cümle tespit edilmelidir!", "✂️"),
    59: ("Anlatım Biçimleri ve Teknikleri",
         "- Öyküleme: Olay, kişi, zaman ve mekan unsurları vardır; hareket ve akış (video kamera gibi) esastır.\n- Betimleme: Varlıkların niteleyici özellikleriyle göz önünde canlandırılmasıdır (Fotoğraf karesi gibi durağandır).\n- Açıklama: Bilgi vermek, öğretmek amacıyla yazılır; nesneldir.\n- Tartışma: Okuyucunun fikrini değiştirmek, bir görüşü çürütmek amacıyla yazılır ('Oysa bana göre, bence, sanıldığı gibi değil' ifadeleri yer alır).",
         "Betimlemede 'Sözcüklerle resim çizme' vardır, zaman akmaz; Öykülemede ise 'Olay akışı ve hareket' vardır, zaman akar!", "🎨"),
    60: ("Ses Olayları",
         "- Ünlü Düşmesi: Burun-u -> Burnu, Şehir-e -> Şehre, Akıl-ı -> Aklı.\n- Ünlü Daralması: 'a, e' ile biten fiillere '-yor' eki geldiğinde 'ı, i, u, ü'ye dönüşmesi (Başla-yor -> Başlıyor, De-yor -> Diyor, Ye-yor -> Yiyor).\n- Ünsüz Yumuşaması: P-Ç-T-K ile biten sözcüklerin ünlüyle başlayan ek aldığında B-C-D-G-Ğ'ye dönüşmesi (Kitap-ı -> Kitabı, Ağaç-ı -> Ağacı).\n- Ünsüz Benzeşmesi (Sertleşme): F-S-T-K-Ç-Ş-H-P (Fıstıkçı Şahap) ile biten sözcüğe C-D-G ile başlayan ek geldiğinde Ç-T-K'ye dönüşmesi (Sınıf-da -> Sınıfta, 1923-de -> 1923'te).",
         "'Diyor' ve 'Yiyor' sözcüklerinde ünlü daralması vardır! Ancak 'Geliyor, Seviyor' sözcüklerinde daralma YOKTUR, aradaki ünlü yardımcı ünlüdür!", "🗣️"),
    61: ("Yazım Kuralları",
         "- 'de / da': Cümleden çıkarıldığında anlam bozulmuyorsa BAĞLAÇTIR ve ayrı yazılır ('Sen de gel'). Anlam bozuluyorsa BULUNMA HAL EKİDİR ve bitişik yazılır ('Evde bekliyorum').\n- 'ki': Şüpheye düşüldüğünde sonuna '-ler' getirilir. Anlamlı oluyorsa bitişik ('Evdekiler'), anlamsız oluyorsa ayrıdır ('Duydum ki'). İstisna şifresi: SOMBAHÇEMİ (Sanki, Oysaki, Mademki, Belki, Halbuki, Çünkü, Meğerki, İllaki).\n- 'mi' soru edatı her zaman ayrı yazılır ve kendisinden sonraki ekler bitişir ('Gelecek misin?').",
         "İkilemeler DAİMA AYRI YAZILIR ('El ele, art arda, yan yana, peş peşe')! 'Art arda' ve 'Yan yana' yazımına özellikle dikkat!", "✍️"),
    62: ("Noktalama İşaretleri",
         "- Virgül (,) Konulmayacak Yerler:\n  * Şart ekinden (-se, -sa) sonra virgül konmaz.\n  * Zarf-fiil ekinden (-ıp, -arak, -ınca) sonra tek başına ise virgül konmaz.\n  * 'Ve, veya, yahut, hem... hem, ne... ne' bağlaçlarından önce veya sonra virgül konmaz.\n  * Tamlamalarda tamlayan ile tamlanan arasına virgül girmez.\n- Noktalı Virgül (;): Cümle içinde virgüllerle ayrılmış tür veya takımları birbirinden ayırmak veya ögeleri arasında virgül bulunan sıralı cümleleri ayırmak için kullanılır (Noktalı virgül olması için cümlede en az bir virgül bulunması şarttır!).",
         "Cümlede hiç virgül (,) yoksa kesinlikle NOKTALI VİRGÜL (;) KULLANILAMAZ!", "✒️"),
    63: ("Sözcükte Yapı",
         "- Kök: Sözcüğün anlamlı en küçük parçasıdır (İsim veya Fiil kökü).\n- Yapım Ekleri: Sözcüğün anlamını veya türünü değiştiren eklerdir (Türemiş sözcük yapar: Göz-lük, Sev-gi, Su-la-).\n- Çekim Ekleri: Sözcüğün anlamını değiştirmeyen, cümledeki görevini belirleyen eklerdir (Çokluk, Hal, İyelik ekleri).\n- İyelik Eki vs Belirtme Hali: Sözcüğün başına 'Onun' getirilir; uyuyorsa İYELİK EKİ, 'Neyi/Kimi' sorusuna cevap veriyorsa BELİRTME HAL EKİDİR ('Evi çok güzel' -> Onun evi = İyelik; 'Evi temizledi' -> Neyi temizledi? = Belirtme).",
         "Sözcüğün başına 'ONUN' tamlayanı getirildiğinde anlamlı oluyorsa o ek İYELİK (AİTLİK) EKİDİR!", "🧩"),
    64: ("Sözcük Türleri",
         "- Sıfat (Ön Ad): İsmi niteler veya belirtir ('Güzel ev', 'Üç kişi', 'Bu yol').\n- Zamir (Adıl): İsmin yerini tutar ('O geldi', 'Bunu aldım', 'Herkes gördü', 'Kim aradı?').\n- Zarf (Belirteç): Fiili, fiilimsiyi, sıfatı veya başka bir zarfı durum, zaman, miktar veya yer-yön bakımından belirtir ('Hızlı koştu', 'Dün geldi', 'Çok çalıştı', 'İçeri girdi').\n- Edat (İlgeç): Tek başına anlamı olmayan, cümledeki sözcükler arasında anlam ilgisi kuran sözcüklerdir ('Gibi, kadar, için, göre, doğru').",
         "'İçeri, dışarı, aşağı, yukarı, ileri, geri' sözcükleri yalın halde fiili nitelerse ZARF; hal eki alırsa İSİM olur ('İçeri girdi' -> Zarf, 'İçeriye girdi' -> İsim)!", "🏷️"),
    65: ("Fiiller, Ek Fiil ve Çatı",
         "- Ek Fiil (İ-mek): 1) İsim soylu sözcüklere gelerek onları yüklem yapar ('O iyi bir doktordu'). 2) Basit zamanlı fiillere gelerek onları birleşik zamanlı yapar ('Gel-iyor-du' -> Şimdiki zamanın hikayesi).\n- Fiilimsiler: Fiil kökünden türer, fiil anlamını korur ama isim, sıfat veya zarf görevinde kullanılır. Asla şahıs eki almazlar.\n- Çatı Özellikleri: İsim cümlelerinde çatı özelliği KESİNLİKLE ARANMAZ!\n  * Geçişli Fiil: Nesne alabilen fiildir (Başına 'Onu' gelir: 'Onu okudu').\n  * Geçişsiz Fiil: Nesne alamayan fiildir (Başına 'Onu' gelmez: 'Onu uyudu' X).",
         "Yüklemi İSİM olan cümlelerde ÇATI ÖZELLİĞİ ARANMAZ! Önce yüklemin türüne bakınız!", "⚡"),
    66: ("Cümlenin Ögeleri ve Cümle Türleri",
         "- Öge Bulma Sırası: Y-Ö-N-T (Yüklem -> Özne -> Nesne -> Tümleç).\n- Tamlamalar, deyimler, birleşik fiiller ve ikilemeler ASLA BÖLÜNMEZ, tek bir öge kabul edilir.\n- Cümle Türleri:\n  * Basit Cümle: Tek bir yüklemi olan ve içinde fiilimsi bulunmayan cümle.\n  * Birleşik Cümle: Tek yüklemi olan ve içinde FİİLİMSİ (girişik birleşik) bulunan cümle.\n  * Sıralı Cümle: Virgül veya noktalı virgülle ayrılmış birden fazla yüklemi olan cümle.\n  * Bağlı Cümle: 'Ve, ama, fakat' gibi bağlaçlarla bağlanan birden fazla yüklemi olan cümle.",
         "İçinde FİİLİMSİ bulunan ve tek yüklemi olan cümleler GİRİŞİK BİRLEŞİK CÜMLEDİR!", "📐"),
    67: ("Anlatım Bozuklukları",
         "- Anlamsal Bozukluklar:\n  * Gereksiz Sözcük: Eş anlamlı sözcüklerin bir arada kullanılması ('Yaşlı ihtiyar', 'Hala henüz').\n  * Sözcüğün Yanlış Anlamda Kullanımı: Benzer sesli ama farklı anlamlı kelimeler ('Fiyat/Ücret', 'Öğretim/Öğrenim', 'Çekimser/Çekingen').\n  * Çelişen Sözcükler: 'Kuşkusuz gelebilir, galiba'.\n- Yapısal Bozukluklar:\n  * Özne-Yüklem Uyumsuzluğu: Özne insan dışı çoğulsa yüklem tekil olur ('Kuşlar uçuyorlar' X -> 'Kuşlar uçuyor' √).\n  * Çatı Uyuşmazlığı: Cümledeki fiil ve fiilimsilerin ikisi de ya etken ya edilgen olmalıdır.",
         "Özne çoğul insan dışı bir varlıksa yüklem DAİMA TEKİL OLMALIDIR ('Ağaçlar yapraklarını döktüler' YANLIŞ, 'döktü' DOĞRU)!", "⚠️"),
    68: ("Sözel Mantık Çözüm Taktikleri",
         "- Sabit Kriter Seçimi: Günler, katlar, sıralar gibi değişmeyen unsurlar tablonun üst sütunlarına yazılır.\n- Değişken Kriterler: Kişiler veya nesneler tablonun altına not edilir.\n- Kesin Bilgiler: Tabloya doğrudan yerleştirilir ve üzeri çizilir.\n- İhtimaller: Oklar, parantezler veya alternatif tablolar ile gösterilir.\n- 'Sadece, kesinlikle, hemen ardında, aralarında bir kişi vardır' gibi anahtar ifadelere harfiyen uyulur.",
         "Sözel mantıkta soru köklerine çok dikkat edilmelidir: 'Kesinlikle doğrudur' ile 'Doğru olabilir' sorularının mantığı tamamen farklıdır!", "🧠")
}

def build_turkce_questions(u_num, l_idx, l_title, is_exam):
    meta = _TURKCE_CONCEPTS.get(u_num, (
        f"{l_title} Temel Kurallar",
        "TDK ve ÖSYM Türkçe müfredatı kuralları.",
        "ÖSYM soru kalıplarına ve örneklerine dikkat ediniz.",
        "📚"
    ))
    
    q_pool = [
        ("mc", f"{l_title} konusunda ÖSYM tarafından hazırlanan sorularda en çok ölçülen dil yetisi hangisidir?",
         ["Dilin kurallarını doğru uygulama ve anlamsal kavrayış derinliği", "Sözcüklerin kaç harften oluştuğunun sayılması", "Metinlerin hece vezniyle yazılması", "Yazarların doğum yerlerinin ezberlenmesi", "Noktalama işaretlerinin toplam sayısı"], 0,
         "KPSS Türkçe sorularında dil kurallarının işlevsel kullanımı ve okuduğunu anlama becerisi ölçülür."),
        ("mc", f"Aşağıdakilerden hangisi {l_title} bakımından dil kurallarına aykırı bir kullanım örneğidir?",
         ["Kurala ve bağlama uymayan hatalı kullanım", "Cümle yapısına uygun düşen bağlaçlar", "Anlamı pekiştiren ikilemeler", "Yerinde kullanılan noktalama işaretleri", "Ses olaylarına uygun türetilmiş sözcükler"], 0,
         "Dil kurallarına aykırılıklar yazım yanlışı, anlatım bozukluğu veya ses olayı ihlallerine yol açar."),
        ("mc", f"{l_title} kapsamında verilen bir metinde adayların ilk olarak dikkat etmesi gereken strateji hangisidir?",
         ["Soru kökünü olumlu veya olumsuz yönden dikkatle okumak", "Sadece son seçeneğe bakarak karar vermek", "Paragrafı hiç okumadan işaretleme yapmak", "Uzun cümleleri doğrudan atlamak", "Tüm seçeneklerin aynı olduğunu varsaymak"], 0,
         "Soru kökünün olumsuz (değinilmemiştir, çıkarılamaz) veya olumlu (vurgulanmıştır, asıl anlatılmak istenen) olduğunu belirlemek ilk adımdır."),
        ("mc", f"Aşağıdaki cümlelerin hangisinde {l_title} ile ilgili tipik bir kural örneklendirilmiştir?",
         ["Kuralın gereklerini kusursuz yansıtan örnek cümle", "Tamamen anlamsız söz dizimi", "Devrik ve bozuk yapı", "Hiçbir yüklemi bulunmayan eksiltili yapı", "Yabancı kökenli uydurma terimler"], 0,
         "Örnek cümle konunun kural ve yapısını net biçimde somutlaştırmaktadır."),
        ("mc", f"{l_title} ile ilgili sorularda seçenekler elenirken en güvenilir yöntem hangisidir?",
         ["Metindeki anahtar sözcüklerle seçenekleri adım adım karşılaştırmak", "Şıkların uzunluğuna göre eleme yapmak", "En kısa seçeneği işaretlemek", "Zar atarak şık seçmek", "Yalnızca A şıkkına odaklanmak"], 0,
         "Anahtar sözcük eşleştirmesi ve bağlam analizi paragraf ve dil bilgisi sorularının temel çözüm yöntemidir."),
        ("mc", f"Türkçenin yapısal ve anlamsal zenginliği dikkate alındığında {l_title} konusunun önemi nedir?",
         ["Düşüncelerin açık, duru ve etkili bir biçimde ifade edilmesini sağlamak", "Yabancı sözcük sayısını artırmak", "Cümleleri anlaşılmaz hale getirmek", "Yazım kurallarını ortadan kaldırmak", "Noktalama işaretlerini gereksiz kılmak"], 0,
         "Türkçe dil bilgisi kuralları anlatımda açıklık, duruluk ve akıcılığı temin eder."),
        ("tf", f"{l_title} kuralları TDK Yazım Kılavuzu ve Güncel Türkçe Sözlük standartlarına dayanır.",
         True, "ÖSYM Türkçe sorularında TDK'nin güncel kural ve kılavuzlarını esas alır."),
        ("fib", f"{l_title} sürecinde anlatımın hiçbir engele takılmadan kolayca okunabilmesi özelliğine ... denir.",
         ["Akıcılık", "Özgünlük", "Açıklık", "Duruluk"], "Akıcılık",
         "Akıcılık metnin dil ve ses yönünden rahatça okunabilmesidir."),
        ("match", "Türkçe kavramlarını eşleştiriniz:",
         [("Duruluk", "Gereksiz sözcük bulunmaması"),
          ("Açıklık", "Tek bir anlamın anlaşılması"),
          ("Yalınlık", "Süsten ve sanattan uzaklık"),
          ("Özgünlük", "Başkasına benzememe, farklı olma")],
         "Metinlerin temel anlatım ilkeleridir.")
    ]
    
    return {
        "concept_title": f"{l_title} - Püf Noktalar",
        "concept_rule": meta[1],
        "concept_tip": meta[2],
        "concept_emoji": meta[3],
        "questions": q_pool
    }

def generate_turkce_dart():
    dart_lines = [
        "import '../models/lesson_models.dart';",
        "",
        "/// KPSS Quest - KPSS Türkçe & Sözel Mantık Müfredatı (14 Ünite - 42 Ders - 420 Soru)",
        "final List<LearningUnit> kpssTurkceUnits = [",
    ]
    
    for u_num, u_title, lessons in _TURKCE_UNITS:
        lessons_code = []
        for l_idx, (l_title, l_desc) in enumerate(lessons):
            is_exam = (l_idx == len(lessons) - 1)
            q_data = build_turkce_questions(u_num, l_idx + 1, l_title, is_exam)
            l_id = f"kpss_tur_u{u_num}_l{l_idx+1}"
            
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
            
        u_id = f"kpss_tur_u{u_num}"
        dart_lines.append(make_unit(u_id, u_num, u_title, "KPSS Türkçe & Mantık", "0xFFEC4899", lessons_code))
        
    dart_lines.append("];")
    return "\n".join(dart_lines)

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "lib", "data")
    out_file = os.path.join(out_dir, "kpss_turkce_units.dart")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(generate_turkce_dart())
    print(f"kpss_turkce_units.dart başarıyla üretildi: {out_file}")
