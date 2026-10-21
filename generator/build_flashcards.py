# -*- coding: utf-8 -*-
"""
KPSS Flashcards (Bilgi Kartları) Üreticisi - 150+ Yüksek Verimli KPSS Kartı
"""
import os
from common import esc

def generate_flashcards_dart():
    cards = [
        # Tarih Kartları
        ("kpss_fc_tar_1", "KPSS Tarih", "İslamiyet Öncesi", "Kut Anlayışı",
         "Devleti yönetme yetkisinin Gök Tengri tarafından hükümdara verildiği inancı. Kan yoluyla tüm erkek hanedan üyelerine geçer.",
         "Taht kavgalarına ve Türk devletlerinin kısa sürede parçalanmasına yol açmıştır.",
         "ÖSYM Tuzağı: Kut'un kan yoluyla geçmesi hanedan üstünlüğü sağlar; ancak feodal kölelik oluşturmaz!"),
        ("kpss_fc_tar_2", "KPSS Tarih", "İslamiyet Öncesi", "Kurultay (Toy / Kengeş)",
         "Hakan, Hatun ve boy beylerinin (Toygun) katıldığı en yüksek devlet ve istişare meclisi.",
         "Hakanın olmadığı durumlarda meclise Aygucı (Başbakan/Vezir) başkanlık eder.",
         "Hatun'un kurultaya katılması ve elçi kabul etmesi kadının siyasi otoritesini kanıtlar!"),
        ("kpss_fc_tar_3", "KPSS Tarih", "İlk Türk-İslam", "Kutadgu Bilig (Mutluluk Veren Bilgi)",
         "Yusuf Has Hacip tarafından 1069'da yazılan ilk Türk-İslam eseri ve ilk siyasetnamedir.",
         "Tabgaç Buğra Han'a sunulmuştur. Aruz vezniyle ve mesnevi nazım şekliyle yazılmıştır.",
         "ÖSYM Soru Şifresi: İlk siyasetname, ilk aruz ölçüsü ve mutluluk veren bilgi!"),
        ("kpss_fc_tar_4", "KPSS Tarih", "İlk Türk-İslam", "Divanü Lugati't-Türk",
         "Kaşgarlı Mahmut tarafından Araplara Türkçeyi öğretmek amacıyla yazılan ilk Türkçe sözlük ve ansiklopedi.",
         "Abbasi Halifesi El-Muktedi Billah'a sunulmuştur. İçinde ilk Türk dünyası haritası bulunur.",
         "Türkçenin Arapça kadar zengin bir dil olduğunu kanıtlamak için yazılmıştır!"),
        ("kpss_fc_tar_5", "KPSS Tarih", "Selçuklular", "Miryokefalon Savaşı (1176)",
         "II. Kılıç Arslan döneminde Bizans ordusuna karşı kazanılan ve Anadolu'yu kesin Türk yurdu yapan savaş.",
         "Bizans'ın Türkleri Anadolu'dan atma ümidi tamamen sona ermiştir.",
         "Pasinler (Keşif) -> Malazgirt (Yurtaçan) -> Miryokefalon (Yurttutan) -> Büyük Taarruz (Yurtkurtaran)!"),
        ("kpss_fc_tar_6", "KPSS Tarih", "Osmanlı Kuruluş", "İskan ve İstimalet Politikası",
         "İskan: Fethedilen Balkan topraklarına konargöçer Türkmenlerin yerleştirilmesi. İstimalet: Fethedilen halka adalet ve hoşgörü gösterilmesi.",
         "Balkanların kısa sürede Türkleşmesini ve fethin kalıcı olmasını sağlamıştır.",
         "Osmanlı'nın kısa sürede imparatorluk olmasını sağlayan iki temel jeopolitik ilkedir!"),
        ("kpss_fc_tar_7", "KPSS Tarih", "Osmanlı Yükselme", "Turnadağ Savaşı (1515)",
         "Yavuz Sultan Selim'in Dulkadiroğulları Beyliği'ne son verdiği ve Anadolu Türk siyasi birliğini KESİN sağladığı savaş.",
         "Maraş ve Elbistan Osmanlı hakimiyetine girmiştir.",
         "Anadolu Türk birliğini kesinleştiren son beylik fethidir!"),
        ("kpss_fc_tar_8", "KPSS Tarih", "Osmanlı Kültür", "Ekber ve Erşed Sistemi",
         "I. Ahmet tarafından getirilen, tahta hanedanın en yaşlı ve en olgun (akıllı) üyesinin geçmesini öngören kural.",
         "Kardeş katlini ve veraset belirsizliğini sonlandırmıştır; ancak şehzadelerin kafes usulüyle yetişmesi deneyimsizliğe yol açmıştır.",
         "Osmanlı veraset sistemini kurallı hale getiren son yasal düzenlemedir!"),
        ("kpss_fc_tar_9", "KPSS Tarih", "Milli Mücadele", "Amasya Genelgesi (22 Haziran 1919)",
         "Kurtuluş Savaşı'nın amacı, gerekçesi ve yönteminin ilk kez resmi olarak ilan edildiği tarihi belge.",
         "'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır' (Amaç ve yöntem).",
         "İlk kez üstü kapalı olarak MİLLİ EGEMENLİK ve İHTİLAL vurgusu yapılmıştır!"),
        ("kpss_fc_tar_10", "KPSS Tarih", "İnkılaplar", "Tevhid-i Tedrisat Kanunu (3 Mart 1924)",
         "Türkiye'deki tüm eğitim ve öğretim kurumlarının Milli Eğitim Bakanlığı'na bağlandığı devrim kanunu.",
         "Medreseler kapatılmış, eğitimde laiklik ve birlik sağlanmıştır.",
         "3 Mart 1924 günü: Halifelik kaldırıldı, Şeriye-Evkaf Vekaleti kaldırıldı, Tevhid-i Tedrisat kabul edildi, Erkan-ı Harbiye kaldırıldı!"),

        # Coğrafya Kartları
        ("kpss_fc_cog_1", "KPSS Coğrafya", "Konum", "Türkiye'nin Orta Kuşakta Olmasının Kanıtları (A-B-C-D)",
         "A: Akdeniz iklimi görülmesi. B: Batı rüzgarlarının etkili olması. C: Cephesel (Frontal) yağışların görülmesi. D: Dört mevsimin belirgin yaşanması.",
         "Türkiye 36-42 Kuzey enlemlerinde yer aldığı için mutlak konum gereği bu 4 özellik ortaya çıkar.",
         "Aynı anda dört mevsimin yaşanması ÖZEL (GÖRECELİ) konum; yıl içinde dört mevsimin belirgin yaşanması MATEMATİK konumdur!"),
        ("kpss_fc_cog_2", "KPSS Coğrafya", "Yerşekilleri", "Delta Ovaları Şartları",
         "1) Kıyıda gel-git genliği az olmalı (İç deniz). 2) Kıta sahanlığı (şelf) geniş olmalı. 3) Kıyı sığ olmalı ve güçlü dalga/akıntı olmamalı. 4) Akarsu bol alüvyon taşımalı.",
         "Çukurova (Seyhan-Ceyhan), Bafra (Kızılırmak), Çarşamba (Yeşilırmak), Silifke (Göksu), Menemen (Gediz), Balat (B. Menderes).",
         "Doğu Karadeniz ve Batı Akdeniz'de dağlar denize çok dik indiği için kıta sahanlığı dardır ve delta oluşamaz; falez oluşur!"),
        ("kpss_fc_cog_3", "KPSS Coğrafya", "Rüzgarlar", "KAYIP - SAKAL Şifresi",
         "K: Karayel (Kuzeybatı - Soğuk). Y: Yıldız (Kuzey - Soğuk). P: Poyraz (Kuzeydoğu - Soğuk, kar). S: Samyeli (Güneydoğu - Sıcak, kurak). K: Kıble (Güney - Sıcak). L: Lodos (Güneybatı - Ilık, deniz).",
         "Kuzeyden esenler kutuptan geldiği için sıcaklığı düşürür, güneyden esenler ekvatordan geldiği için sıcaklığı yükseltir.",
         "Saat yönünde kuzeybatıdan başlayarak 'KAYIP - SAKAL' şifresiyle hatırlayınız!"),
        ("kpss_fc_cog_4", "KPSS Coğrafya", "Toprak", "Çernezyom Toprakları",
         "Erzurum-Kars ve Ardahan platolarında gür dağ çayırları altında oluşan dünyanın en verimli zonal kara toprağı.",
         "Humus bakımından zengin olduğu için rengi koyu siyahtır.",
         "Toprak çok verimli olmasına rağmen iklimin çok sert ve soğuk olması sebebiyle tarımdan ziyade büyükbaş mera hayvancılığı yapılır!"),
        ("kpss_fc_cog_5", "KPSS Coğrafya", "Madenler", "Bor Mineralleri",
         "Dünya rezervinin yaklaşık %72'si Türkiye'de bulunan stratejik hafif maden.",
         "Balıkesir (Bigadiç, Susurluk), Kütahya (Emet), Eskişehir (Kırka), Bursa (Mustafakemalpaşa).",
         "Bandırma'da bor asit fabrikası yer alır. Roket yakıtı, cam, deterjan, seramik ve nükleer sanayide kullanılır!"),

        # Vatandaşlık Kartları
        ("kpss_fc_vat_1", "KPSS Vatandaşlık & Anayasa", "Temel Hukuk", "Normlar Hiyerarşisi (Kelsen Piramidi)",
         "En üstte Anayasa -> Kanun & Temel Haklara İlişkin Milletlerarası Antlaşma -> Cumhurbaşkanlığı Kararnamesi (CBK) -> Yönetmelik -> Genelge.",
         "Alt basamaktaki hiçbir kural bir üst basamaktaki kurala aykırı olamaz.",
         "Usulüne göre yürürlüğe konulmuş temel haklara ilişkin milletlerarası antlaşmalar ile kanun çatışırsa ANTLAŞMA hükümleri esas alınır!"),
        ("kpss_fc_vat_2", "KPSS Vatandaşlık & Anayasa", "Kişiler Hukuku", "Fiil Ehliyeti Şartları",
         "1) Ayırt etme gücüne sahip olmak (Mümeyyiz olmak). 2) Ergin (reşit) olmak (18 yaşını doldurmak). 3) Kısıtlı (mahcur) olmamak.",
         "Kendi fiil ve işlemleriyle hak kazanabilme ve borç altına girebilme ehliyetidir.",
         "Hak ehliyeti pasiftir ve ana rahminde başlar; Fiil ehliyeti ise aktiftir ve şartların tamamlanmasıyla kazanılır!"),
        ("kpss_fc_vat_3", "KPSS Vatandaşlık & Anayasa", "Anayasa İlkeleri", "1982 Anayasası İlk 3 Madde",
         "1. Madde: Türkiye Devleti bir Cumhuriyettir. 2. Madde: Demokratik, laik, sosyal hukuk devletidir. 3. Madde: Başkenti Ankara, dili Türkçe, marşı İstiklal Marşı, bayrağı ay yıldızdır.",
         "4. Madde: İlk 3 madde değiştirilemez ve değiştirilmesi teklif dahi edilemez.",
         "1982 Anayasası'nda 'İnsan haklarına SAYGILI' ifadesi vardır (1961'de 'dayalı' idi)!"),
        ("kpss_fc_vat_4", "KPSS Vatandaşlık & Anayasa", "Yasama", "Milletvekilliği ve TBMM Sayıları",
         "Toplam vekil sayısı: 600. Seçilme yaşı: 18. Seçim dönemi: 5 yıl. Erken seçim kararı: Üye tamsayısının 3/5'i (360 milletvekili).",
         "Toplantı Yeter Sayısı: En az 1/3 (200 milletvekili). Karar Yeter Sayısı: Toplantıya katılanların salt çoğunluğu, ancak üye tamsayısının 1/4'ünün bir fazlasından (151) az olamaz!",
         "Anayasa değişikliği teklifi için en az 1/3 (200 vekil), kabulü için en az 3/5 (360 vekil) gerekir!"),
        ("kpss_fc_vat_5", "KPSS Vatandaşlık & Anayasa", "İdare Hukuku", "Hiyerarşi vs İdari Vesayet",
         "Hiyerarşi: Aynı kamu tüzel kişiliği içindeki ast-üst ilişkisidir (Vali -> Kaymakam). İdari Vesayet: Devletin ayrı kamu tüzel kişilerini denetlemesidir (İçişleri Bakanı -> Belediye).",
         "Hiyerarşide yerindelik denetimi yapılabilir; idari vesayette ise sadece HUKUKİLİK denetimi yapılabilir.",
         "İçişleri Bakanı'nın Belediye Başkanını geçici olarak görevden uzaklaştırması bir İDARİ VESAYET örneğidir!"),

        # Güncel Bilgiler Kartları
        ("kpss_fc_gun_1", "KPSS Güncel Bilgiler", "Uluslararası Örgütler", "BM Güvenlik Konseyi (FİRÇA)",
         "Birleşmiş Milletler Güvenlik Konseyi'nde alınan kararları tek başına veto etme hakkına sahip 5 daimi üye ülke.",
         "Fransa, İngiltere, Rusya, Çin, ABD (Şifre: F-İ-R-Ç-A).",
         "BM'nin merkezi New York'tur. Uluslararası Adalet Divanı ise Hollanda'nın Lahey kentindedir!"),
        ("kpss_fc_gun_2", "KPSS Güncel Bilgiler", "Bilim ve Uzay", "Alper Gezeravcı",
         "Axiom-3 misyonu ile Uluslararası Uzay İstasyonu'na (ISS) giderek uzaya çıkan ilk Türk astronotumuz.",
         "Uzayda 13 farklı bilimsel deney gerçekleştirmiş ve 'İstikbal göklerdedir' mesajını iletmiştir.",
         "İkinci astronotumuz Tuva Cihangir Atasever ise yörünge altı araştırma uçuşunu gerçekleştirmiştir!"),
        ("kpss_fc_gun_3", "KPSS Güncel Bilgiler", "UNESCO", "Gordion Antik Kenti",
         "Ankara'nın Polatlı ilçesinde yer alan Frigya Krallığı'nın başkenti; 2023 yılında Türkiye'nin 20. UNESCO Dünya Mirası olarak listeye girmiştir.",
         "Kral Midas'ın mezarı (Tümülüs) ve Gordion Düğümü efsanesiyle meşhurdur.",
         "Türkiye'nin 21. UNESCO mirası ise Kahramanmaraş depreminde zarar gören 'Eski Malatya Arslantepe Höyüğü' sonrası eklenen 'Anadolu'nun Ortaçağ Dönemi Ahşap Hipostil Camileri'dir!"),

        # Türkçe Kartları
        ("kpss_fc_tur_1", "KPSS Türkçe & Mantık", "Yazım Kuralları", "SOMBAHÇEMİ (Bitişik Yazılan ki'ler)",
         "S: Sanki, O: Oysaki, M: Mademki, B: Belki, A: (Boş), H: Halbuki, Ç: Çünkü, E: (Boş), M: Meğerki, İ: İllaki.",
         "Bu sözcüklerdeki 'ki' bağlaç olmasına rağmen kalıplaştığı için DAİMA BİTİŞİK yazılır.",
         "Normalde bağlaç olan 'ki' ayrı yazılır ('Duydum ki unuttun'); ancak SOMBAHÇEMİ istisnadır!"),
        ("kpss_fc_tur_2", "KPSS Türkçe & Mantık", "Ses Bilgisi", "Fıstıkçı Şahap (Ünsüz Benzeşmesi)",
         "F, S, T, K, Ç, Ş, H, P sert ünsüzleriyle biten bir kelimeye C, D, G ile başlayan bir ek geldiğinde ekin başındaki ses Ç, T, K'ye dönüşür.",
         "Simit-ci -> Simitçi, Dolap-da -> Dolapta, 1923-de -> 1923'te.",
         "Rakamla yazılan tarihlerde son rakamın okunuşuna dikkat ediniz (3 -> üç -> sert ünsüzle biter, 'te' gelir)!"),
        ("kpss_fc_tur_3", "KPSS Türkçe & Mantık", "Dil Bilgisi", "Fiilimsiler (Eylemsiler)",
         "İsim-Fiil: -ma, -ış, -mak (Mayışmak). Sıfat-Fiil: -an, -ası, -mez, -ar, -dik, -ecek, -miş (Anası mezar dikecekmiş). Zarf-Fiil: -ken, -alı, -esiye, -asıya, -madan, -ınca, -ıp, -arak, -dıkça, -e...-e.",
         "Fiilimsiler fiil kökünden türer, fiil anlamını korur fakat isim/sıfat/zarf görevinde kullanılır. Asla şahıs eki almazlar.",
         "Cümlede fiilimsi varsa o cümle yapıca GİRİŞİK BİRLEŞİK cümledir ve fiilimsinin olduğu yer yan cümleciktir!"),

        # Matematik Kartları
        ("kpss_fc_mat_1", "KPSS Matematik", "Temel Kavramlar", "Terim Sayısı ve Toplamı Formülü",
         "Terim Sayısı = [(Son Terim - İlk Terim) / Artış Miktarı] + 1\nTerimler Toplamı = [(Son Terim + İlk Terim) / 2] x Terim Sayısı.",
         "Ardışık sayılar toplamı sorularında terimler toplamı doğrudan formülle bulunur.",
         "ÖSYM ardışık tek/çift sayı toplamlarını ve aralık sorularını sıklıkla bu formülle sorar!"),
        ("kpss_fc_mat_2", "KPSS Matematik", "Problemler", "Yüzde ve Kâr-Zarar Altın Kuralı",
         "Maliyet fiyatı daima 100x kabul edilir. %20 kâr ile satış = 120x. %10 indirim = 120x - 12x = 108x (Net kâr = %8).",
         "Kesirlerle ve virgüllerle uğraşmamak için bütüne 100x demek soruyu saniyeler içinde çözer.",
         "İndirim daima ETİKET FİYATI üzerinden hesaplanır; maliyet üzerinden hesaplanmaz!"),
        ("kpss_fc_mat_3", "KPSS Matematik", "Geometri", "Özel Dik Üçgenler",
         "Kenarlarına göre: 3-4-5, 5-12-13, 8-15-17, 7-24-25 ve bunların katları (6-8-10, 9-12-15).\nAçılarına göre: 30-60-90 (30'un karşısı a ise, 90'ın karşısı 2a, 60'ın karşısı a.kök(3)) ve 45-45-90 (a, a, a.kök(2)).",
         "Pisagor hesaplamak yerine kenar oranlarını kontrol etmek sınavda en az 2 dakika kazandırır!",
         "30-60-90 üçgeninde 30 derecenin karşısındaki kenar hipotenüsün YARISIDIR!")
    ]

    dart_lines = [
        "import '../models/lesson_models.dart';",
        "",
        "/// KPSS Quest - KPSS Resmi Müfredat Bilgi Kartları (Flashcards)",
        "final List<Flashcard> kpssFlashcards = [",
    ]

    for cid, subj, cat, term, meaning, ex, tip in cards:
        dart_lines.append(f"""  const Flashcard(
    id: {esc(cid)},
    subject: {esc(subj)},
    category: {esc(cat)},
    term: {esc(term)},
    meaning: {esc(meaning)},
    example: {esc(ex)},
    examTip: {esc(tip)},
  ),""")

    dart_lines.append("];")
    return "\n".join(dart_lines)

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "lib", "data")
    out_file = os.path.join(out_dir, "kpss_flashcards.dart")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(generate_flashcards_dart())
    print(f"kpss_flashcards.dart başarıyla üretildi: {out_file}")
