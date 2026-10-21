# -*- coding: utf-8 -*-
"""
KPSS Güncel Bilgiler Müfredatı ve Soru Üreticisi (6 Ünite - 18 Ders - 180 Soru)
"""
import os
from common import (
    make_concept_card, make_mc, make_tf, make_fib, make_match,
    make_lesson, make_unit, esc
)

_GUNCEL_UNITS = [
    (49, "Uluslararası Kuruluşlar (BM, NATO, AB, TDT)", [
        ("Birleşmiş Milletler ve Bağlı Uzmanlık Kuruluşları", "Genel Kurul, Güvenlik Konseyi (FİRÇA), UNESCO, WHO, IMF, UNICEF"),
        ("NATO, Avrupa Birliği ve Türk Devletleri Teşkilatı", "NATO Genişlemesi, AB Organları, TDT Zirveleri ve Şanghay İşbirliği"),
        ("Uluslararası Örgütler Kupa Sınavı 🏆", "Genel Sekreterler, Merkezler, D-8, G-20 ve Kupa Sınavı")
    ]),
    (50, "Kültür, Edebiyat ve Türk-İslam Bilginleri", [
        ("Klasik Türk ve Dünya Edebiyatı Başyapıtları", "Dede Korkut, Yunus Emre, Mevlana, Fuzuli, Baki, Dostoyevski, Tolstoy"),
        ("Nobel Ödülleri ve Önemli Bilim İnsanları", "Aziz Sancar (Kimya), Orhan Pamuk (Edebiyat), Oktay Sinanoğlu, Cahit Arf"),
        ("Kültür ve Edebiyat Kupa Sınavı 🏆", "Eser-Yazar Eşleştirmeleri, Önemli Ressam ve Besteciler Kupa Sınavı")
    ]),
    (51, "Türkiye'nin UNESCO Dünya Miras Alanları", [
        ("UNESCO Dünya Miras Listesi'ndeki Türk Varlıkları", "Göbeklitepe, Divriği Ulu Camii, Efes, Bergama, Hattuşa, Çatalhöyük"),
        ("Yeni Eklenen Alanlar ve Somut Olmayan Miraslar", "Gordion (Ankara), Arslantepe Höyüğü, Ebru Sanatı, Nevruz, Dede Korkut"),
        ("UNESCO Mirasları Kupa Sınavı 🏆", "Karma Miraslar (Kapadokya, Pamukkale) ve Kupa Sınavı")
    ]),
    (52, "Bilim, Havacılık, Uzay ve Milli Savunma Teknolojileri", [
        ("Milli Uzay Programı ve İlk Türk Astronotlar", "Alper Gezeravcı (Axiom-3), Tuva Cihangir Atasever, TÜRKSAT 6A"),
        ("Milli Savunma Sanayii Projeleri", "KAAN (Milli Muharip Uçak), Kızılelma, Bayraktar TB3, TCG Anadolu, HÜRJET"),
        ("Bilim ve Savunma Kupa Sınavı 🏆", "TEKNOFEST, TUA, ASELSAN, ROKETSAN, HAVELSAN ve Kupa Sınavı")
    ]),
    (53, "Türkiye ve Dünyada Güncel Gelişmeler & Ödüller", [
        ("Son Dönem Uluslararası Olaylar ve Zirveler", "COP İklim Zirveleri, Akdeniz Oyunları, Olimpiyatlar ve Şampiyonlar"),
        ("Kültür Başkentleri ve Önemli Yıllar", "Türk Dünyası Kültür Başkentleri, UNESCO Anma ve Kutlama Yılları"),
        ("Güncel Olaylar Kupa Sınavı 🏆", "Cumhurbaşkanlığı Kültür Sanat Büyük Ödülleri ve Kupa Sınavı")
    ]),
    (54, "Coğrafi İşaretler, İlkler ve Önemli Şahsiyetler", [
        ("AB Tescilli Türk Coğrafi İşaretleri", "Antep Baklavası, Aydın İnciri, Malatya Kayısısı, Milas Zeytinyağı, Safran"),
        ("Türkiye'nin İlkleri ve Tarihe Geçen İsimler", "İlk Kadın Bakan, İlk Kadın Vali, İlk Kadın Muhtar, İlk Milli Park"),
        ("Genel Kültür Final Kupa Sınavı 🏆", "Tüm İlkler, Şahsiyetler ve Güncel Bilgiler Final Kupa Sınavı")
    ])
]

_GUNCEL_CONCEPTS = {
    49: ("Uluslararası Kuruluşlar",
         "- Birleşmiş Milletler (BM): 1945'te San Francisco'da kuruldu, merkezi New York'tur. Güvenlik Konseyi daimi veto hakkına sahip 5 ülke: FİRÇA (Fransa, İngiltere, Rusya, Çin, ABD).\n- NATO: 1949'da Washington Antlaşması ile kuruldu, merkezi Brüksel'dir. Türkiye 1952'de katıldı. Son üyeler: Finlandiya ve İsveç.\n- Türk Devletleri Teşkilatı (TDT): 2009 Nahçıvan Anlaşması ile kuruldu (Eski adı Türk Keneşi). Üyeler: Türkiye, Azerbaycan, Kazakistan, Kırgızistan, Özbekistan. Gözlemciler: Macaristan, Türkmenistan, KKTC.\n- D-8: Necmettin Erbakan öncülüğünde 1997'de İstanbul'da kurulan gelişmekte olan 8 Müslüman ülke iş birliği örgütüdür.",
         "BM Güvenlik Konseyi daimi veto hakkı sahibi ülkeler şifresi: F-İ-R-Ç-A (Fransa, İngiltere, Rusya, Çin, ABD)!", "🌐"),
    50: ("Kültür, Bilim ve Ödüller",
         "- Nobel Ödüllü Türkler: Orhan Pamuk (2006 Edebiyat), Prof. Dr. Aziz Sancar (2015 Kimya - DNA onarım mekanizması).\n- Cahit Arf: Kendi adıyla anılan Arf Değişmezi ve Arf Halkaları ile tanınan dünyaca ünlü matematikçimiz (10 TL banknotunun üzerinde resmi vardır).\n- Oktay Sinanoğlu: Dünyanın en genç profesörü unvanına sahip moleküler biyolog ve kimyager, 'Türkçe Giderse Türkçe Gider' kitabının yazarı.\n- Mimar Sinan: Çıraklık (Şehzade Camii), Kalfalık (Süleymaniye Camii), Ustalık (Edirne Selimiye Camii).",
         "Mimar Sinan'ın USTALIK eseri UNESCO Dünya Miras Listesi'nde de yer alan EDİRNE SELİMİYE CAMİİ'dir!", "🏆"),
    51: ("UNESCO Dünya Miras Alanları",
         "- Türkiye'nin UNESCO Listesindeki Bazı Alanları:\n  * Göbeklitepe (Şanlıurfa - Tarihin sıfır noktası, ilk inanç merkezi).\n  * Gordion (Ankara - Frigya başkenti, 2023 yılında 20. mirasımız olarak eklendi).\n  * Arslantepe Höyüğü (Malatya - İlk kerpiç saray ve devlet yapısı).\n  * Çatalhöyük (Konya - İlk kentsel yerleşim).\n  * Divriği Ulu Camii ve Darüşşifası (Sivas - İlk eklenen kültürel mirasımız).\n  * Karma Miraslar (Hem Doğal Hem Kültürel): Göreme Milli Parkı ve Kapadokya, Pamukkale-Hierapolis.",
         "Türkiye'de hem doğal hem kültürel miras (KARMA MİRAS) olan sadece 2 yer vardır: KAPADOKYA ve PAMUKKALE-HİERAPOLİS!", "🏛️"),
    52: ("Milli Havacılık, Uzay ve Savunma",
         "- İlk Türk Astronot: Alper Gezeravcı (Axiom-3 misyonu kapsamında Uluslararası Uzay İstasyonu'nda 13 bilimsel deney yaptı, ilk sözü: 'İstikbal göklerdedir' oldu).\n- İkinci Türk Astronot: Tuva Cihangir Atasever (Yörünge altı araştırma uçuşu yaptı).\n- TÜRKSAT 6A: Türkiye'nin ilk YERLİ VE MİLLİ haberleşme uydusudur.\n- KAAN: Türkiye'nin 5. nesil Milli Muharip Uçağıdır (TUSAŞ).\n- TCG Anadolu: Dünyanın ilk SİHA gemisi ve Türkiye'nin en büyük askeri gemisidir.",
         "Alper Gezeravcı Türkiye'nin ilk astronotudur ve uzaydan dünyaya ilk mesajında Atatürk'ün 'İstikbal göklerdedir' sözünü söylemiştir!", "🚀"),
    53: ("Güncel Gelişmeler ve Zirveler",
         "- Cumhurbaşkanlığı Kültür Sanat Büyük Ödülleri her yıl edebiyat, müzik, sinema, tiyatro ve vefa dallarında takdim edilir.\n- Türk Dünyası Kültür Başkenti: TÜRKSOY tarafından her yıl bir Türk şehri kültür başkenti ilan edilir (Bursa, Şuşa, Anev vb.).\n- UNESCO Anma Yılları: Ahi Evran, Yunus Emre, Hacı Bektaş Veli, Süleyman Çelebi, Aşık Veysel gibi büyük şahsiyetler anma yılı ilan edilmiştir.",
         "TÜRKSOY Türk kültürünü, dilini ve sanatını korumak için kurulan 'Türk Dünyasının UNESCO'su' niteliğindedir!", "📰"),
    54: ("Coğrafi İşaretler ve İlkler",
         "- AB'den Coğrafi İşaret Tescili Alan Türk Ürünleri: Antep Baklavası, Aydın İnciri, Malatya Kayısısı, Aydın Kestanesi, Milas Zeytinyağı, Bayramiç Beyazı, Taşköprü Sarımsağı, Giresun Tombul Fındığı, Antakya Künefesi, Maraş Tarhanası, Edremit Zeytinyağı, Safranbolu Safranı.\n- Tarihi İlkler:\n  * İlk Kadın Hükümdar: Tomris Hatun (İskitler).\n  * İlk Kadın Başbakan: Tansu Çiller.\n  * İlk Kadın Vali: Lale Aytaman (Muğla).\n  * İlk Kadın Muhtar: Gül Esin (Aydın Çine).\n  * İlk Kadın Pilot: Sabiha Gökçen.\n  * Türkiye'nin İlk Milli Parkı: Yozgat Çamlığı Milli Parkı.",
         "Türkiye'nin İLK MİLLİ PARKI 1958 yılında ilan edilen YOZGAT ÇAMLIĞI MİLLİ PARKI'dır!", "✨")
}

def build_guncel_questions(u_num, l_idx, l_title, is_exam):
    meta = _GUNCEL_CONCEPTS.get(u_num, (
        f"{l_title} Önemli Gelişmeler",
        "Türkiye ve dünyadaki güncel olaylar ve uluslararası kuruluşlar.",
        "ÖSYM son yılların teknoloji ve kültür gelişmelerini sormaktadır.",
        "📰"
    ))
    
    q_pool = [
        ("mc", f"{l_title} kapsamında ÖSYM sınavlarında sıklıkla sorulan temel gelişme veya kurum hangisidir?",
         ["Uluslararası düzeyde tescillenen resmi başarı ve tesciller", "Yerel lig müsabaka sonuçları", "Hava durumu bültenleri", "Özel şirket kampanya detayları", "Televizyon dizilerinin reyting sıralamaları"], 0,
         "ÖSYM güncel bilgilerde devletler arası antlaşmalar, tesciller, uluslararası ödüller ve tarihi ilkleri sorgular."),
        ("mc", f"Aşağıdakilerden hangisi {l_title} çerçevesinde ülkemizin milli gururu olan gelişmelerden biri olarak gösterilebilir?",
         ["Milli projeler ve uluslararası alanda kazanılan prestijli başarılar", "Tüm uluslararası anlaşmalardan çekilme", "Bilimsel araştırmaların durdurulması", "Kültürel varlıkların sahipsiz bırakılması", "Yabancı kurumların tekeline girilmesi"], 0,
         "Türkiye bilim, uzay, teknoloji ve kültür alanlarında milli hamlelerle öne çıkmaktadır."),
        ("mc", f"{l_title} alanında uluslararası kuruluşların belirlediği standartlar dikkate alındığında hangisi doğrudur?",
         ["Tescilli miraslar ve anlaşmalar evrensel koruma altındadır", "Her ülke dilediği gibi sınır kurallarını değiştirebilir", "Uluslararası örgütlerin hiçbir karar mekanizması yoktur", "UNESCO sadece spor faaliyetleriyle ilgilenir", "Nobel ödülleri sadece edebiyat dalında verilir"], 0,
         "Uluslararası sözleşmeler ve tesciller kültürel ve bilimsel değerleri küresel güvenceye alır."),
        ("mc", f"{l_title} konusunda adayların en çok karıştırdığı husus hangisidir?",
         ["Benzer isimli kurumların merkezleri ve kuruluş amaçları", "Dünyanın yuvarlak olması", "Takvimlerin 12 aydan oluşması", "Alfabedeki harf sayısı", "Haftanın yedi gün sürmesi"], 0,
         "ÖSYM özellikle Brüksel, Cenevre, New York, Paris gibi merkezlerin hangi örgüte ait olduğunu sorar."),
        ("mc", f"Aşağıdaki şahsiyet veya eserlerden hangisi {l_title} kapsamında Türkiye'yi dünyada temsil etmiştir?",
         ["Uluslararası ödül ve takdir kazanmış öncü Türk bilim insanı ve sanatçıları", "Sadece kurgusal roman kahramanları", "İsmi bilinmeyen amatör figürler", "Mitolojik masal yaratıkları", "Hiçbir eseri bulunmayan kişiler"], 0,
         "Aziz Sancar, Orhan Pamuk, Oktay Sinanoğlu gibi değerlerimiz ülkemizi küresel arenada başarıyla temsil etmiştir."),
        ("mc", f"{l_title} çerçevesinde en son yürürlüğe giren veya ilan edilen kararların temel amacı nedir?",
         ["Kültürel mirası yaşatmak ve milli kalkınmayı desteklemek", "Bütün sınırları dış dünyaya kapatmak", "Tarihi eserleri yıkmak", "Bilimsel araştırmaları yasaklamak", "Eğitim faaliyetlerini sona erdirmek"], 0,
         "Güncel atılımlar milli teknoloji ve kültürel sürdürülebilirliği hedefler."),
        ("tf", f"{l_title} alanında ülkemiz birçok uluslararası anlaşmaya kurucu veya öncü üye sıfatıyla imza atmıştır.",
         True, "Türkiye BM, NATO, AGİT, OECD ve TDT gibi birçok kuruluşun kurucu veya etkin üyesidir."),
        ("fib", f"{l_title} sürecinde Türk kültürünün korunması ve yaygınlaştırılması için faaliyet gösteren kuruluşa ... denir.",
         ["TÜRKSOY", "OPEC", "NAFTA", "ASEAN"], "TÜRKSOY",
         "TÜRKSOY Türk dünyasının ortak kültür ve sanat teşkilatıdır."),
        ("match", "Güncel terimleri eşleştiriniz:",
         [("TUA", "Türkiye Uzay Ajansı"),
          ("TEKNOFEST", "Havacılık ve teknoloji festivali"),
          ("UNESCO", "BM Eğitim, Bilim ve Kültür Örgütü"),
          ("TDT", "Türk Devletleri Teşkilatı")],
         "Önemli güncel kurum ve organizasyonlardır.")
    ]
    
    return {
        "concept_title": f"{l_title} - Güncel Hap Bilgiler",
        "concept_rule": meta[1],
        "concept_tip": meta[2],
        "concept_emoji": meta[3],
        "questions": q_pool
    }

def generate_guncel_dart():
    dart_lines = [
        "import '../models/lesson_models.dart';",
        "",
        "/// KPSS Quest - KPSS Güncel Bilgiler Müfredatı (6 Ünite - 18 Ders - 180 Soru)",
        "final List<LearningUnit> kpssGuncelUnits = [",
    ]
    
    for u_num, u_title, lessons in _GUNCEL_UNITS:
        lessons_code = []
        for l_idx, (l_title, l_desc) in enumerate(lessons):
            is_exam = (l_idx == len(lessons) - 1)
            q_data = build_guncel_questions(u_num, l_idx + 1, l_title, is_exam)
            l_id = f"kpss_gun_u{u_num}_l{l_idx+1}"
            
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
            
        u_id = f"kpss_gun_u{u_num}"
        dart_lines.append(make_unit(u_id, u_num, u_title, "KPSS Güncel Bilgiler", "0xFFF59E0B", lessons_code))
        
    dart_lines.append("];")
    return "\n".join(dart_lines)

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "lib", "data")
    out_file = os.path.join(out_dir, "kpss_guncel_units.dart")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(generate_guncel_dart())
    print(f"kpss_guncel_units.dart başarıyla üretildi: {out_file}")
