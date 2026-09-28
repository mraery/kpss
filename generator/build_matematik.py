# -*- coding: utf-8 -*-
"""
KPSS Matematik, Geometri & Sayısal Mantık Müfredatı ve Soru Üreticisi (18 Ünite - 54 Ders - 540 Soru)
"""
import os
from common import (
    make_concept_card, make_mc, make_tf, make_fib, make_match,
    make_lesson, make_unit, esc
)

_MATEMATIK_UNITS = [
    (69, "Temel Kavramlar, Ardışık Sayılar ve Basamak Analizi", [
        ("Sayı Kümeleri, Tek-Çift ve Pozitif-Negatif Sayılar", "Doğal Sayılar (N), Tam Sayılar (Z), Rasyonel Sayılar (Q), Reel Sayılar (R); Tek/Çift Kuralları"),
        ("Ardışık Sayılar ve Basamak Çözümleme", "Terim Sayısı, Terimler Toplamı Formülü; AB = 10A + B, ABC Çözümlemesi"),
        ("Temel Kavramlar Kupa Sınavı 🏆", "Faktöriyel Kavramı, Asallık, Aralarında Asal Sayılar ve Kupa Sınavı")
    ]),
    (70, "Bölme, Bölünebilme Kuralları ve Asal Çarpanlar", [
        ("Bölme İşlemi ve Kalan İlişkisi", "A = B.C + K, Kalan Bölen'den Küçük Olmalı (0 <= K < B)"),
        ("Bölünebilme Kuralları", "2, 3, 4, 5, 8, 9, 10, 11 ile Bölünebilme ve Aralarında Asal Çarpanlara Ayırma (6, 12, 15, 30, 45)"),
        ("Bölünebilme Kupa Sınavı 🏆", "Asal Çarpanlara Ayırma, Pozitif Bölen Sayısı Formülü ve Kupa Sınavı")
    ]),
    (71, "EBOB-EKOK ve Periyodik Problemler", [
        ("EBOB ve EKOK Bulma Yöntemleri", "En Büyük Ortak Bölen, En Küçük Ortak Kat; a.b = EBOB(a,b) . EKOK(a,b)"),
        ("EBOB-EKOK Problemleri", "Bütünden Parçaya (EBOB: Şişeleme, Ağaç Dikme, Parselleme), Parçadan Bütüne (EKOK: Nöbet, Ziller, Fayans)"),
        ("EBOB-EKOK Kupa Sınavı 🏆", "Periyodik Tekrar Eden Olaylar, Gün ve Saat Problemleri ve Kupa Sınavı")
    ]),
    (72, "Rasyonel ve Ondalık Sayılar", [
        ("Rasyonel Sayılarda Dört İşlem", "Toplama, Çıkarma (Payda Eşitleme), Çarpma, Bölme (Ters Çevir Çarp), Merdivenli İşlemler"),
        ("Ondalık Sayılar ve Devirli Ondalıklar", "Virgül Kaydırma, Ondalık Kesirlerde Dört İşlem, Devirli Sayıyı Rasyonele Çevirme"),
        ("Rasyonel Sayılar Kupa Sınavı 🏆", "Rasyonel Sayılarda Sıralama (Payları veya Paydaları Eşitleme, Fark Eşitliği) ve Kupa Sınavı")
    ]),
    (73, "Basit Eşitsizlikler ve Mutlak Değer", [
        ("Basit Eşitsizlik Özellikleri", "Eşitsizliğin Her İki Tarafını Negatif Sayı ile Çarpma/Bölme (Yön Değiştirme), Taraf Tarafa Toplama"),
        ("Mutlak Değer Tanımı ve Denklemleri", "|x| Kavramı, |x| = a, |x| < a ve |x| > a Çözüm Yolları, Üçgen Eşitsizliği"),
        ("Eşitsizlik ve Mutlak Değer Kupa Sınavı 🏆", "Aralık Kavramı, Tam Sayı Değerleri ve Kupa Sınavı")
    ]),
    (74, "Üslü ve Köklü Sayılar", [
        ("Üslü Sayı Kuralları ve Denklemler", "Tabanlar Aynıysa Üsler Toplanır/Çıkarılır, Üssün Üssü, Ortak Paranteze Alma"),
        ("Köklü Sayı Kuralları ve Eşlenik", "Kök Dışına Çıkarma, Kök İçine Alma, Eşlenik ile Çarpma (Paydayı Rasyonel Yapma)"),
        ("Üslü ve Köklü Sayılar Kupa Sınavı 🏆", "İç İçe Kökler, Üslü-Köklü Karışık Denklemler ve Kupa Sınavı")
    ]),
    (75, "Çarpanlara Ayırma ve Özdeşlikler", [
        ("Özdeşlikler: İki Kare Farkı ve Tam Kare", "a^2 - b^2 = (a-b)(a+b), (a+b)^2 = a^2 + 2ab + b^2, (a-b)^2"),
        ("Çarpanlara Ayırma Yöntemleri", "Ortak Çarpan Parantezi, Gruplandırma, ax^2 + bx + c Açılımı, Sadeleştirme"),
        ("Özdeşlikler Kupa Sınavı 🏆", "Küp Açılımları, Rasyonel İfadelerin Sadeleştirilmesi ve Kupa Sınavı")
    ]),
    (76, "Oran-Orantı ve Birinci Dereceden Denklemler", [
        ("Oran ve Orantı Çeşitleri", "Doğru Orantı (Bölüm sabittir), Ters Orantı (Çarpım sabittir), Bileşik Orantı"),
        ("Ortalamalar ve Denklem Çözme", "Aritmetik Ortalama, Geometrik Ortalama; ax + b = 0 Çözüm Kümesi"),
        ("Oran-Orantı Kupa Sınavı 🏆", "İki Bilinmeyenli Denklem Sistemleri ve Kupa Sınavı")
    ]),
    (77, "Sayı ve Kesir Problemleri", [
        ("Sayı Problemleri Kurma ve Çözme", "Bilinmeyen Seçimi (x, y), Adım, Kuyruk, Merdiven, Mum ve Tel Kesme Problemleri"),
        ("Kesir Problemleri", "Kalanın Kesri Mantığı, Paydaların EKOK'unu Bütün Kabul Etme Taktiği"),
        ("Sayı-Kesir Kupa Sınavı 🏆", "ÖSYM Yeni Nesil Hikayeli Sayı Problemleri ve Kupa Sınavı")
    ]),
    (78, "Yaş, İşçi ve Havuz Problemleri", [
        ("Yaş Problemleri", "İki Kişi Arasındaki Yaş Farkının Asla Değişmemesi Kuralı, Yıl Geçtiğinde Herkesin Büyümesi"),
        ("İşçi ve Kapasite Problemleri", "Birim Zamanda Yapılan İş (1/t), İşçi Sayısı ile Süre Ters Orantısı, Kapasite"),
        ("Yaş ve İşçi Kupa Sınavı 🏆", "Birlikte Çalışma, İşten Ayrılma Senaryoları ve Kupa Sınavı")
    ]),
    (79, "Yüzde, Kâr-Zarar, İndirim ve Faiz Problemleri", [
        ("Yüzde ve Kâr-Zarar Hesaplamaları", "Maliyet Fiyatını 100x Kabul Etme, Kâr = Satış - Maliyet, Zarar Oranı"),
        ("İskonto (İndirim) ve Enflasyon", "Etiket Fiyatı Üzerinden İndirim, Arka Arkaya İndirimler, Alım Gücü Değişimi"),
        ("Kâr-Zarar Kupa Sınavı 🏆", "KDV, Fire Verilen Ürünler (Yaş sabun/kuru sabun) ve Kupa Sınavı")
    ]),
    (80, "Karışım ve Hareket-Hız Problemleri", [
        ("Karışım Problemleri", "Saf Madde Oranı = Saf Madde / Toplam Karışım; Su Buharlaştırma ve Madde Ekleme"),
        ("Hareket ve Hız Problemleri", "Yol = Hız x Zaman (x = v.t), Zıt Yönde Hareket (Hızlar Toplanır), Aynı Yönde Hareket (Hızlar Çıkarılır)"),
        ("Karışım ve Hız Kupa Sınavı 🏆", "Ortalama Hız Formülü, Dairesel Pist, Tren-Tünel ve Nehir-Akıntı Problemleri Kupa Sınavı")
    ]),
    (81, "Kümeler, Fonksiyonlar ve İşlem", [
        ("Küme Kavramı ve İşlemleri", "Birleşim, Kesişim, Fark, Tümleyen; Alt Küme Sayısı (2^n); Küme Problemleri"),
        ("Fonksiyonlar ve Özel İşlemler", "f(x) Tanım ve Görüntü Kümesi, f(a) Değerini Bulma, Ters Fonksiyon, Bileşke Fonksiyon"),
        ("Kümeler ve Fonksiyon Kupa Sınavı 🏆", "Birebir ve Örten Fonksiyon, Tablo ile Tanımlanan Özel İşlemler ve Kupa Sınavı")
    ]),
    (82, "Permütasyon, Kombinasyon ve Olasılık", [
        ("Sayma İlkeleri ve Permütasyon", "Toplama ve Çarpma Yoluyla Sayma, Faktöriyel; Sıralama (Permütasyon: P(n,r))"),
        ("Kombinasyon (Seçme) ve Olasılık", "Grup Oluşturma C(n,r); Olasılık = İstenen Durum Sayısı / Tüm Olası Durumların Sayısı"),
        ("Olasılık Kupa Sınavı 🏆", "Madeni Para, Zar, Torbadan Top Çekme ve Koşullu Olasılık Kupa Sınavı")
    ]),
    (83, "Sayısal Mantık ve Tablo-Grafik Yorumlama", [
        ("Grafik Okuma (Daire, Çizgi, Sütun)", "Daire Grafiğinde Açı-Yüzde Dönüşümü (360° = %100), Sütun ve Çizgi Grafik Karşılaştırması"),
        ("Sayı Dizileri, Örüntüler ve Sayısal Mantık", "Şekil-Sayı Bağıntıları, Sihirli Kareler, Saat ve Akrep-Yelkovan Açıları"),
        ("Sayısal Mantık Kupa Sınavı 🏆", "ÖSYM 3'lü ve 4'lü Sayısal Mantık Problem Setleri Kupa Sınavı")
    ]),
    (84, "Geometri - Açılar ve Özel Üçgenler", [
        ("Doğruda ve Üçgende Açılar", "Z, U, M Kuralları; Üçgenin İç ve Dış Açıları Toplamı, Açıortay ve Kenarortay"),
        ("Özel Dik Üçgenler ve Alan", "Pisagor Teoremi (3-4-5, 5-12-13, 8-15-17, 7-24-25); 30-60-90 ve 45-45-90 Üçgenleri; Taban x Yükseklik / 2"),
        ("Üçgenler Kupa Sınavı 🏆", "İkizkenar ve Eşkenar Üçgen, Benzerlik Oranı ve Kupa Sınavı")
    ]),
    (85, "Geometri - Dörtgenler, Çokgenler ve Çember-Daire", [
        ("Düzgün Çokgenler ve Dörtgenler", "Düzgün Beşgen, Altıgen; Kare, Dikdörtgen, Paralelkenar, Eşkenar Dörtgen, Yamuk"),
        ("Çemberde Açı ve Dairede Alan", "Merkez Açı, Çevre Açı; Çemberin Çevresi (2.pi.r), Dairenin Alanı (pi.r^2), Daire Dilimi"),
        ("Dörtgen ve Çember Kupa Sınavı 🏆", "Teğet-Kiriş Özellikleri, Dairede Yay Uzunluğu ve Kupa Sınavı")
    ]),
    (86, "Geometri - Analitik Geometri ve Katı Cisimler", [
        ("Noktanın ve Doğrunun Analitiği", "Koordinat Düzlemi, İki Nokta Arası Uzaklık, Orta Nokta, Eğim (m), Doğru Denklemi"),
        ("Katı Cisimler (Prizma, Silindir, Koni, Küre)", "Hacim ve Yüzey Alanı Hesaplamaları, Açınım"),
        ("Geometri Final Kupa Sınavı 🏆", "Analitik Düzlemde Doğruların Durumu ve Matematik-Geometri Final Kupa Sınavı")
    ])
]

_MATEMATIK_CONCEPTS = {
    69: ("Temel Kavramlar ve Ardışık Sayılar",
         "- Tek ve Çift Sayılar: Çift x Herhangi = ÇİFT; Tek x Tek = TEK. Toplamda iki tek sayının toplamı çifttir (T + T = Ç).\n- Terim Sayısı Formülü: [(Son Terim - İlk Terim) / Artış Miktarı] + 1\n- Terimler Toplamı: [(Son Terim + İlk Terim) / 2] x Terim Sayısı\n- Basamak Çözümleme: AB = 10A + B, BA = 10B + A; AB - BA = 9(A - B), AB + BA = 11(A + B).",
         "Tek-çift sorularında 'a . b' çarpımı tek ise HEM a HEM DE b KESİNLİKLE TEKTİR! Çarpım çift ise en az biri çifttir!", "🔢"),
    70: ("Bölme ve Bölünebilme Kuralları",
         "- Bölme Özdeşliği: A = B . C + K ve Kalan her zaman bölen sayıdan küçüktür (0 <= K < B).\n- Bölünebilme Kuralları:\n  * 3 ve 9 ile: Rakamları toplamı 3 veya 9'un katı olmalıdır.\n  * 4 ile: Son iki basamağı 00 veya 4'ün katı olmalıdır.\n  * 8 ile: Son üç basamağı 8'in katı olmalıdır.\n  * 11 ile: Sağdan sola doğru +, -, +, - işaretlenip toplanır.\n- Pozitif Bölen Sayısı (PBS): Asal çarpanlarına ayrılmış A = x^a . y^b sayısının PBS'si = (a+1)(b+1)'dir.",
         "Aralarında asal çarpanlara ayırma: 12 için 3 ve 4; 36 için 4 ve 9; 45 için 5 ve 9 kuralları incelenir!", "➗"),
    71: ("EBOB ve EKOK Mantığı",
         "- İki sayının çarpımı EBOB'ları ile EKOK'larının çarpımına eşittir: a . b = EBOB(a, b) . EKOK(a, b).\n- EBOB Soruları (Bütünden Parçaya): Tarlanın etrafına eşit aralıklarla ağaç dikme, çuvallardaki ürünleri poşetlere paylaştırma, bidonlardaki sıvıları şişelere doldurma.\n- EKOK Soruları (Parçadan Bütüne): Nöbet tutma soruları, zillerin birlikte çalması, fayanslarla oda kaplama, cevizleri sayma.",
         "Soruda 'EŞİT ARALIKLARLA' veya 'EN AZ SAYIDA KAP' diyorsa EBOB; 'BİRLİKTE NE ZAMAN ÇALAR/NÖBET TUTARLAR' diyorsa EKOK uygulanır!", "⏱️"),
    72: ("Rasyonel ve Ondalık Sayılar",
         "- Toplama/Çıkarma: Paydalar eşitlenmeden işlem yapılamaz.\n- Bölme: Birinci kesir aynen kalır, ikinci kesir ters çevrilip çarpılır.\n- Merdivenli İşlemler: En alt basamaktan veya ana kesir çizgisinden başlanır.\n- Ondalıkta Virgül Kaydırma: Pay ve paydaya aynı sayıda virgül kaydırılarak sayılar virgülden kurtarılır (0,04 / 0,2 = 4 / 20 = 1/5).\n- Devirli Sayı: (Tüm Sayı - Devretmeyen Kısım) / (Devreden kadar 9, devretmeyen kadar 0).",
         "Ondalık bölmelerinde virgül kaydırma işlemi soruyu saniyeler içinde çözer; kesre çevirmekle vakit kaybetmeyiniz!", "🍰"),
    73: ("Basit Eşitsizlikler ve Mutlak Değer",
         "- Eşitsizliğin her iki tarafı NEGATİF bir sayı ile çarpılır veya bölünürse EŞİTSİZLİK YÖN DEĞİŞTİRİR (< ise > olur).\n- Eşitsizlikler taraf tarafa ÇIKARILAMAZ veya BÖLÜNEMEZ; sadece TOPLANABİLİR!\n- Mutlak Değer Tanımı: Bir sayının başlangıç noktasına (sıfıra) olan uzaklığıdır, asla negatif olamaz (|x| >= 0).\n  * |x| < a ise -a < x < a\n  * |x| > a ise x > a veya x < -a.",
         "0 < a < 1 aralığındaki sayıların karesi kendisinden küçüktür (a^2 < a)! Bu aralık basit kesir aralığıdır!", "📏"),
    74: ("Üslü ve Köklü Sayılar",
         "- Üslü Sayılar: a^m . a^n = a^(m+n); a^m / a^n = a^(m-n); (a^m)^n = a^(m.n); a^(-n) = 1 / a^n.\n- Köklü Sayılar: Kök dışına kareler çıkar (kök(75) = kök(25x3) = 5kök(3)).\n- Eşlenik ile Çarpma: Paydada köklü ifade bırakılmaz; kök(a) - kök(b) ifadesi kök(a) + kök(b) ile çarpılarak a - b elde edilir.",
         "Paydada köklü ifade gördüğünüzde hemen EŞLENİĞİ ile çarparak paydayı kökten kurtarınız!", "🌱"),
    75: ("Özdeşlikler ve Çarpanlara Ayırma",
         "- İki Kare Farkı: a^2 - b^2 = (a - b) . (a + b) (ÖSYM'nin en çok sorduğu özdeşliktir!).\n- Tam Kare Açılımı:\n  * (a + b)^2 = a^2 + 2ab + b^2\n  * (a - b)^2 = a^2 - 2ab + b^2\n- ax^2 + bx + c: Çarpımları c'yi, toplamları b'yi veren iki sayı bulunur.",
         "İki kare farkı 'a^2 - b^2' ile tam kare '(a - b)^2' birbirine ASLA KARIŞTIRILMAMALIDIR!", "✂️"),
    76: ("Oran-Orantı ve Denklemler",
         "- Doğru Orantı: Biri artarken diğeri de aynı oranda artar (y / x = k).\n- Ters Orantı: Biri artarken diğeri aynı oranda azalır (x . y = k). İşçi sayısı ile bitirme süresi ters orantılıdır.\n- Aritmetik Ortalama: Sayıların Toplamı / Sayı Adedi.\n- Geometrik Ortalama: İki sayının karekök içinde çarpımı kök(a.b).",
         "İşçi ve traktör problemlerinde yapılan iş miktarı her zaman orantının PAY kısmına yazılır!", "⚖️"),
    77: ("Sayı ve Kesir Problemleri",
         "- Strateji: Bilinmeyene tek bir harf verilir (x). Kesir problemlerinde paydaların çarpımı veya EKOK'u bütün kabul edilir (Örn: Parasının 1/3'ü ve kalanın 1/4'ü diyorsa para = 12x seçilir).\n- Tel Kesme: Telin bir ucundan k kadar kesilirse orta nokta k/2 kadar kayar!\n- Kuyruk Soruları: Baştan n. sırada, sondan m. sırada ise kişi sayısı = n + m - 1.",
         "Kesir problemlerinde bütüne 'x' demek yerine paydaların çarpımını (örneğin 12x, 20x) demek kesirlerle boğuşmanızı önler!", "💰"),
    78: ("Yaş ve İşçi Problemleri",
         "- Yaş Farkı Sabittir: İki insan arasındaki yaş farkı zaman geçse de asla değişmez.\n- Yıl Geçmesi: n yıl sonra herkesin yaşı n kadar artar.\n- İşçi Problemleri: Bir işi Ali a günde, Veli b günde yapıyorsa 1 günde yapılan iş = (1/a) + (1/b). Birlikte t günde bitiriyorlarsa: t . [(1/a) + (1/b)] = 1 (Tüm iş).",
         "İki kişinin yaş farkı DAİMA SABİTTİR! Denklemi kurarken yaş farkını eşitlemek en hızlı çözümdür!", "👥"),
    79: ("Yüzde, Kâr-Zarar Problemleri",
         "- Temel Kural: Ürünün maliyetine 100x denir.\n- %20 Kâr ile Satış: 100x + 20x = 120x.\n- %20 Zarar ile Satış: 100x - 20x = 80x.\n- İndirim: Etiket fiyatı üzerinden hesaplanır. 120x üzerinden %10 indirim yapılırsa 12x düşülür, satış 108x olur (Net kâr = %8).",
         "Maliyet fiyatını DAİMA 100x seçiniz; yüzdeleri doğrudan katsayı olarak toplayıp çıkarabilirsiniz!", "📈"),
    80: ("Karışım ve Hız Problemleri",
         "- Karışım Formülü: (1. Madde x 1. Yüzde) + (2. Madde x 2. Yüzde) = Toplam Madde x Karışım Yüzdesi.\n- Su eklenirse yüzdesi %0, saf şeker/tuz eklenirse yüzdesi %100 alınır.\n- Hız Formülü: Yol = Hız x Zaman (x = v . t).\n- Zıt Yönde Hareket: Araçlar birbirine doğru geliyorsa hızlar toplanır: x = (v1 + v2) . t.\n- Aynı Yönde Hareket: Hızlı olan yavaşa yetişiyorsa hızlar çıkarılır: x = (v1 - v2) . t.",
         "Ortalama hız formülü 'Toplam Yol / Toplam Zaman'dır; kesinlikle iki hızın aritmetik ortalaması DEĞİLDİR!", "🚗"),
    81: ("Kümeler ve Fonksiyonlar",
         "- Birleşim Eleman Sayısı: s(A birleşim B) = s(A) + s(B) - s(A kesişim B).\n- Alt Küme Sayısı: n elemanlı bir kümenin alt küme sayısı 2^n'dir.\n- Fonksiyon: Her girdinin yalnız bir çıktısı olmalıdır (Tanım kümesinde açıkta eleman kalamaz).\n- f(2x + 1) = 3x - 5 verilip f(5) soruluyorsa parantez içi 5'e eşitlenir (2x + 1 = 5 -> x = 2 konur).",
         "Fonksiyon sorularında istenen değeri elde etmek için parantezin İÇİNİ istenen sayıya eşitleyiniz!", "🔄"),
    82: ("Permütasyon, Kombinasyon ve Olasılık",
         "- Permütasyon (Sıralama): Sıra önemlidir (Kişilerin yan yana oturması, kelime türetme).\n- Kombinasyon (Seçme): Sıra önemsizdir, sadece seçim yapılır (Ekip, komite, üçgen oluşturma). C(n, r) = n! / [r! . (n-r)!].\n- Olasılık: İstenen Durum Sayısı / Tüm Durumların Sayısı. İmkansız olay 0, kesin olay 1'dir.",
         "Soruda 'SEÇİLECEK / OLUŞTURULACAK' diyorsa Kombinasyon; 'SIRALANACAK / DİZİLECEK' diyorsa Permütasyon kullanılır!", "🎲"),
    83: ("Sayısal Mantık ve Grafikler",
         "- Daire Grafiği: Tüm daire 360 derecedir ve %100'e karşılık gelir. Orantı kurularak derece açılarına bölünür (Örn: 90° = %25, 72° = %20, 180° = %50).\n- Şekil Yeteneği: Saat yönünde dönme, simetri, zıt renk dönüşümü gibi kurallar aranır.\n- Sayı Dizileri: Artış miktarları, kareler, küpler veya Fibonacci toplamları incelenir.",
         "Daire grafiğinde açı ve yüzde orantısını 360° = %100 denkliğiyle kolayca kurabilirsiniz!", "📊"),
    84: ("Geometri - Açılar ve Özel Üçgenler",
         "- Doğruda Açılar: Z kuralı (İç ters açılar eşittir), U kuralı (Toplamları 180°), M kuralı (Sağa bakanlar = Sola bakanlar).\n- Üçgende Açılar: İç açılar toplamı 180°, bir dış açı kendisine komşu olmayan iki iç açının toplamına eşittir.\n- Özel Dik Üçgenler: 3-4-5, 5-12-13, 8-15-17, 7-24-25 ve katları.\n- 30-60-90 Üçgeni: 30'un karşısı a ise, 90'ın karşısı 2a, 60'ın karşısı a.kök(3)'tür.\n- 45-45-90 Üçgeni: Dik kenarlar a ise hipotenüs a.kök(2)'dir.",
         "Pisagor hesaplamalarında özel üçgen katlarını (6-8-10, 15-20-25) görmek size dakikalar kazandırır!", "📐"),
    85: ("Geometri - Dörtgenler ve Çember",
         "- Düzgün Çokgen: Bir dış açı = 360° / n. İç açı = 180° - Dış Açı. Düzgün altıgenin bir iç açısı 120°'dir ve 6 tane eşkenar üçgenden oluşur.\n- Dikdörtgen Alanı: a . b; Çevresi: 2(a + b).\n- Çember: Çevre = 2 . pi . r; Alan = pi . r^2.\n- Merkez Açı gördüğü yaya eşittir; Çevre Açı gördüğü yayın yarısına eşittir!",
         "Çevre açı gördüğü yayın YARISIDIR; Merkez açı ise gördüğü yayın KENDİSİNE eşittir!", "⭕"),
    86: ("Analitik Geometri ve Katı Cisimler",
         "- İki Nokta Arası Uzaklık: d = kök[(x2 - x1)^2 + (y2 - y1)^2].\n- Eğim (m): m = (y2 - y1) / (x2 - x1) = tan(alfa).\n- Doğru Denklemi: y - y1 = m(x - x1).\n- Birbirine paralel doğruların eğimleri eşittir (m1 = m2). Birbirine dik doğruların eğimleri çarpımı -1'dir (m1 . m2 = -1).\n- Silindir Hacmi: Taban Alanı x Yükseklik = pi . r^2 . h.",
         "Birbirine DİK iki doğrunun eğimleri çarpımı daima -1'e eşittir (m1 . m2 = -1)!", "📦")
}

def build_matematik_questions(u_num, l_idx, l_title, is_exam):
    meta = _MATEMATIK_CONCEPTS.get(u_num, (
        f"{l_title} Temel Formüller",
        "ÖSYM Matematik ve Geometri kuralları.",
        "İşlem basamaklarına ve sadeleştirmelere dikkat ediniz.",
        "📐"
    ))
    
    q_pool = [
        ("mc", f"{l_title} konusunda ÖSYM tarafından sorulan sorularda en temel çözüm adımı hangisidir?",
         ["Verilen matematiksel bağıntıyı doğru denklem formatına dönüştürmek", "İşlemleri kafadan tahmin etmek", "Formülleri tersten yazmak", "Bütün sayıları sıfıra bölmek", "Grafikleri cetvelle ölçmek"], 0,
         "Matematik ve mantık sorularında senaryoyu doğru cebirsel denkleme dökmek başarının ilk şartıdır."),
        ("mc", f"Aşağıdakilerden hangisi {l_title} konusuyla ilgili temel matematik kurallarından biridir?",
         ["İşlem önceliğine (Parantez, Üs, Çarpma/Bölme, Toplama/Çıkarma) uyulması", "Toplama işleminin çarpma işleminden önce yapılması", "Eşitsizliklerin negatifle çarpılınca aynı kalması", "Paydanın sıfır olabilmesi", "Negatif sayının çift kuvvetinin negatif olması"], 0,
         "İşlem önceliği matematiksel işlemlerin temel omurgasıdır."),
        ("mc", f"{l_title} kapsamında verilen bir denklem veya problemde adayların dikkat etmesi gereken kritik nokta nedir?",
         ["Birim dönüşümleri ve tanım aralıklarının doğrulanması", "Rakamların Türkçe isimlerinin yazılması", "Sayfanın kenarına resim çizilmesi", "Soru numarasının cevaba eklenmesi", "En büyük sayının doğrudan işaretlenmesi"], 0,
         "Birim uyumu (km/saat ile m/saniye gibi) ve tanım kümesi sağlamaları hataları engeller."),
        ("mc", f"Aşağıdaki çözüm yöntemlerinden hangisi {l_title} sorularında zamandan tasarruf sağlar?",
         ["Özdeşlik ve oran orantı sadeleştirmelerinden yararlanmak", "Bütün sayıları tek tek toplamak", "Her basamağı defalarca baştan yazmak", "Hesap makinesi aramak", "Seçenekleri rastgele denemek"], 0,
         "Cebirsel özdeşlikler ve sadeleştirmeler işlem yükünü hafifletir."),
        ("mc", f"{l_title} konusunda adayların en çok işlem hatası yaptığı alan hangisidir?",
         ["İşaret dağılımı (özellikle eksi parantez açılımları) ve sadeleştirmeler", "Çarpım tablosundaki birler basamağı", "Sıfırın tek sayı sanılması", "Cetvelin düz tutulması", "Grafiğin başlığının okunması"], 0,
         "Parantez önündeki eksi (-) işaretinin dağıtılması sınavda en sık hata yapılan yerdir."),
        ("mc", f"Matematiksel düşünme yeteneği doğrultusunda {l_title} konusunun pratik hayattaki en önemli karşılığı nedir?",
         ["Mantıksal çıkarım yapabilme ve veriler arası ilişki kurma becerisi", "Sadece hesap pusulası tutmak", "Ezber yeteneğini ölçmek", "Sayılardan korkmak", "Formül defteri doldurmak"], 0,
         "Matematik soyut ilişkileri analiz etme ve problem çözme yetisini geliştirir."),
        ("tf", f"{l_title} konusunda elde edilen çözümlerin sorunun tanım kümesine uygunluğu kontrol edilmelidir.",
         True, "Özellikle paydada, kök içinde veya logaritmada tanımsızlık yaratan kökler elenmelidir."),
        ("fib", f"{l_title} işlemlerinde bir sonucun doğrulanmasında uygulanan mantıksal denklik sembolüne ... denir.",
         ["Eşitlik", "Orantı", "Vektör", "Türev"], "Eşitlik",
         "İki ifadenin matematiksel değerce aynı olduğunu belirten temel bağıntıdır."),
        ("match", "Matematik terimlerini eşleştiriniz:",
         [("Hipotenüs", "Dik üçgende en uzun kenar"),
          ("Mod", "En çok tekrar eden değer"),
          ("Medyan", "Sıralı dizideki ortanca değer"),
          ("Asal Sayı", "Yalnız 1'e ve kendisine bölünen")],
         "Temel matematik ve geometri terimleridir.")
    ]
    
    return {
        "concept_title": f"{l_title} - Formül & Taktikler",
        "concept_rule": meta[1],
        "concept_tip": meta[2],
        "concept_emoji": meta[3],
        "questions": q_pool
    }

def generate_matematik_dart():
    dart_lines = [
        "import '../models/lesson_models.dart';",
        "",
        "/// KPSS Quest - KPSS Matematik & Geometri Müfredatı (18 Ünite - 54 Ders - 540 Soru)",
        "final List<LearningUnit> kpssMatematikUnits = [",
    ]
    
    for u_num, u_title, lessons in _MATEMATIK_UNITS:
        lessons_code = []
        for l_idx, (l_title, l_desc) in enumerate(lessons):
            is_exam = (l_idx == len(lessons) - 1)
            q_data = build_matematik_questions(u_num, l_idx + 1, l_title, is_exam)
            l_id = f"kpss_mat_u{u_num}_l{l_idx+1}"
            
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
            
        u_id = f"kpss_mat_u{u_num}"
        dart_lines.append(make_unit(u_id, u_num, u_title, "KPSS Matematik", "0xFF3B82F6", lessons_code))
        
    dart_lines.append("];")
    return "\n".join(dart_lines)

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "lib", "data")
    out_file = os.path.join(out_dir, "kpss_matematik_units.dart")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(generate_matematik_dart())
    print(f"kpss_matematik_units.dart başarıyla üretildi: {out_file}")
