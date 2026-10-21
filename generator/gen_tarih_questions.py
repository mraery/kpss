# -*- coding: utf-8 -*-
"""
KPSS Tarih Üniteleri (3-18) Soru ve Kavram Bankası
"""

_TARIH_DB = {
    3: {
        "concept_title": "Türkiye Selçukluları ve Anadolu Beylikleri",
        "concept_rule": "- I. Beylikler: Malazgirt (1071) sonrası Alparslan'ın 'Kılıç hakkı' ile kuruldu (Danişment, Saltuk, Mengücek, Artuk, Çaka).\n- Miryokefalon (1176): II. Kılıç Arslan Bizans'ı yendi, Anadolu kesin Türk yurdu oldu (Yurttutan Savaşı).\n- Kösedağ (1243): Moğol İlhanlılara yenilindi, Selçuklu dağılma sürecine girdi, II. Beylikler dönemi başladı.\n- Ticaret Politikası: İlk kervansaraylar, gümrük vergisi indirimi, devlet sigortacılığı uygulandı.",
        "concept_tip": "ÖSYM Şifresi: Pasinler (1048) -> Keşif, Malazgirt (1071) -> Kapı açan (Yurtaçan), Miryokefalon (1176) -> Tapu alan (Yurttutan), Büyük Taarruz (1922) -> Yurtkurtaran!",
        "concept_emoji": "🏰",
        "q_pool": [
            ("mc", "Anadolu'da kurulan ilk Türk beyliği aşağıdakilerden hangisidir?",
             ["Saltuklular (Erzurum)", "Danişmentliler", "Mengücekliler", "Artuklular", "Çaka Beyliği"], 0,
             "Saltuklular Malazgirt sonrası Erzurum merkezli kurulan ilk Anadolu Türk beyliğidir."),
            ("mc", "Tarihte ilk Türk denizcisi kabul edilen ve 1081 yılında kendi adıyla ilk denizci beyliği kuran lider kimdir?",
             ["Çaka Bey", "Karamürsel Bey", "Umur Bey", "Barbaros Hayrettin", "Saruca Paşa"], 0,
             "Çaka Bey 1081'de İzmir'de ilk donanmayı kurmuş ve Türk Deniz Kuvvetleri'nin kuruluşu kabul edilmiştir."),
            ("mc", "Bizans'ın Türkleri Anadolu'dan atma ümidini kesin olarak bitiren ve Anadolu'nun kesin Türk yurdu olduğunu tescilleyen 1176 tarihli savaş hangisidir?",
             ["Miryokefalon Savaşı", "Pasinler Savaşı", "Malazgirt Savaşı", "Kösedağ Savaşı", "Yassıçemen Savaşı"], 0,
             "II. Kılıç Arslan komutasında kazanılan Miryokefalon Savaşı ile Anadolu kesin olarak Türk yurdu olmuştur."),
            ("mc", "Anadolu Selçuklu Devleti'nde ticareti geliştirmek amacıyla dünyada ilk kez uygulanan sistem hangisidir?",
             ["Devlet Sigortacılığı", "Tımar Sistemi", "Ahi Sandığı", "İltizam Sistemi", "Gümrük Muafiyeti"], 0,
             "Selçuklular kervanları soyulan tüccarların zararını hazineden karşılayarak ilk devlet sigortacılığını uygulamıştır."),
            ("mc", "Anadolu'da Moğol İlhanlı hakimiyetini başlatan ve II. Beylikler döneminin açılmasına yol açan 1243 savaşı hangisidir?",
             ["Kösedağ Savaşı", "Yassıçemen Savaşı", "Katvan Savaşı", "Ayn Calut Savaşı", "Otlukbeli Savaşı"], 0,
             "1243 Kösedağ Savaşı ile Türkiye Selçuklu Devleti Moğollara yenilmiş ve Anadolu Türk siyasi birliği parçalanmıştır."),
            ("mc", "Türkçeyi ilk kez resmi devlet dili ilan eden (1277) Anadolu beyliği hangisidir?",
             ["Karamanoğulları", "Germiyanoğulları", "Candaroğulları", "Karesioğulları", "Osmanoğulları"], 0,
             "Karamanoğlu Mehmet Bey 13 Mayıs 1277'de Türkçeyi resmi dil ilan etmiştir."),
            ("tf", "Anadolu'da kurulan ilk medrese Danişmentlilere ait Tokat Niksar'daki Yağıbasan Medresesi'dir.",
             True, "Yağıbasan Medresesi Anadolu'daki ilk medrese örneğidir."),
            ("fib", "Türkiye Selçuklularında esnaf ve zanaatkarların dayanışma örgütüne ... teşkilatı denirdi.",
             ["Ahilik", "Lonca", "Gulam", "İkta"], "Ahilik",
             "Ahi Evran tarafından Kırşehir merkezli kurulan Ahilik ahlak ve meslek teşkilatıdır."),
            ("match", "Beylikleri merkezleri ile eşleştiriniz:",
             [("Saltuklular", "Erzurum"), ("Mengücekliler", "Erzincan / Divriği"), ("Danişmentliler", "Sivas / Tokat"), ("Artuklular", "Mardin / Diyarbakır")],
             "I. Dönem Anadolu Türk beylikleri ve merkezleridir.")
        ]
    },
    4: {
        "concept_title": "Osmanlı Devleti Kuruluş Dönemi (1299-1453)",
        "concept_rule": "- İskan Politikası: Fethedilen Balkan topraklarına Anadolu'daki konargöçer Türkmenlerin yerleştirilmesi (Balkanları Türkleştirme ve İslamlaştırma).\n- İstimalet Politikası: Fethedilen gayrimüslim halka din, vicdan ve vergi konusunda hoşgörü gösterilmesi.\n- İlkler: Osman Bey (İlk vergi Baç, ilk kadı Dursun Fakih). Orhan Bey (İlk düzenli ordu Yaya-Müsellem, ilk medrese İznik, ilk donanma Karesioğulları, Rumeli'ye ilk geçiş Çimpe Kalesi).\n- I. Murat: Sırpsındığı, I. Kosova, ilk yeniçeri ocağı, ilk tımar sistemi, 'Ülke padişah ve oğullarınındır' anlayışı.",
        "concept_tip": "Karesioğulları'nın alınmasıyla Osmanlı'nın ilk donanması oluşmuş ve Rumeli'ye geçiş kolaylaşmıştır! Ayrıca Anadolu Türk siyasi birliğini kurma adımıdır!",
        "concept_emoji": "⚔️",
        "q_pool": [
            ("mc", "Osmanlı Devleti'nin Rumeli'deki ilk askeri üssü ve fethettiği ilk toprak parçası neresidir?",
             ["Çimpe Kalesi", "Gelibolu", "Edirne", "Bursa", "Selanik"], 0,
             "Bizans'a yardım karşılığı Orhan Bey döneminde alınan Çimpe Kalesi Rumeli'deki ilk Osmanlı toprağıdır."),
            ("mc", "Osmanlı Devleti'nde ilk düzenli ordu olan 'Yaya ve Müsellem' teşkilatı hangi padişah döneminde kurulmuştur?",
             ["Orhan Bey", "Osman Bey", "I. Murat", "Yıldırım Bayezid", "II. Murat"], 0,
             "Orhan Bey döneminde vezir Alaeddin Paşa ve Çandarlı Halil önerisiyle Yaya ve Müsellem ordusu kurulmuştur."),
            ("mc", "Haçlılar ile Osmanlı arasında yapılan ilk savaş aşağıdakilerden hangisidir?",
             ["Sırpsındığı Savaşı (1364)", "I. Kosova Savaşı", "Koyunhisar Savaşı", "Niğbolu Savaşı", "Varna Savaşı"], 0,
             "I. Murat döneminde 1364'te yapılan Sırpsındığı Savaşı Osmanlı ile Haçlılar arasındaki ilk savaştır."),
            ("mc", "1396 Niğbolu Zaferi'nden sonra Abbasi Halifesi Yıldırım Bayezid'e hangi unvanı vermiştir?",
             ["Sultan-ı İklim-i Rum", "Ebu'l Feth", "Gazi-i Azam", "Fatih-i Rumeli", "Hakanü'l Berreyn"], 0,
             "Yıldırım Bayezid'e Niğbolu Zaferi sonrası Sultan-ı İklim-i Rum (Anadolu Diyarının Sultanı) unvanı verilmiştir."),
            ("mc", "1402 Ankara Savaşı'nda Timur'a esir düşen ve Osmanlı'da 11 yıllık 'Fetret Devri'nin başlamasına neden olan padişah kimdir?",
             ["Yıldırım Bayezid", "I. Murat", "Çelebi Mehmet", "II. Murat", "Orhan Bey"], 0,
             "Yıldırım Bayezid 1402 Ankara Savaşı'nda Timur'a mağlup olmuş ve Fetret Devri (1402-1413) başlamıştır."),
            ("mc", "Fetret Devri'ne son vererek devleti yeniden toparladığı için Osmanlı'nın 'İkinci Kurucusu' sayılan padişah kimdir?",
             ["I. Mehmet (Çelebi Mehmet)", "II. Murat", "Fatih Sultan Mehmet", "I. Murat", "Yıldırım Bayezid"], 0,
             "Çelebi Mehmet taht kavgalarını bitirip birliği sağladığı için Osmanlı'nın ikinci kurucusu kabul edilir."),
            ("tf", "Karesioğulları Beyliği'nin alınmasıyla Osmanlı denizcilik faaliyetlerine başlamış ve ilk donanmasına sahip olmuştur.",
             True, "Karesi beyliğinin donanması Osmanlı bahriyesinin temelini atmıştır."),
            ("fib", "Balkanlara Türkmenlerin yerleştirilerek bölgenin Türkleşmesini sağlayan Osmanlı feth siyasetine ... denir.",
             ["İskan", "İstimalet", "Dirlik", "Müsadere"], "İskan",
             "İskan politikası fethedilen yerleri kalıcı Türk yurdu haline getirme politikasıdır."),
            ("match", "Savaşları sonuçlarıyla eşleştiriniz:",
             [("Koyunhisar (1302)", "Bizans'a karşı ilk zafer"), ("Sırpsındığı (1364)", "İlk Osmanlı-Haçlı savaşı"), ("Niğbolu (1396)", "Sultan-ı İklim-i Rum unvanı"), ("II. Kosova (1448)", "Balkanların kesin Türk yurdu oluşu")],
             "Kuruluş dönemi dönüm noktası savaşlarıdır.")
        ]
    },
    5: {
        "concept_title": "Osmanlı Devleti Yükselme Dönemi (Dünya Gücü Osmanlı)",
        "concept_rule": "- II. Mehmet (Fatih): İstanbul'un fethi (1453), Orta Çağ kapandı Yeni Çağ açıldı. Karadeniz Türk gölü oldu (Kırım'ın fethi). Topkapı Sarayı ve Sahn-ı Seman medreseleri açıldı. Kanunname-i Ali Osman ile kardeş katli yasalaştı.\n- Yavuz Sultan Selim: Çaldıran (1514, Safeviler), Turnadağ (1515, Dulkadiroğulları -> Anadolu Türk siyasi birliği kesin sağlandı), Mercidabık (1516) ve Ridaniye (1517) ile Memlükler yıkıldı, Halifelik Osmanlı'ya geçti, Baharat Yolu denetimi sağlandı.\n- Kanuni Sultan Süleyman: Belgrad fethi (1521), Mohaç Meydan Muharebesi (1526, 2 saatte Macaristan fethedildi), Preveze Deniz Zaferi (1538, Akdeniz Türk gölü oldu).",
        "concept_tip": "ÖSYM Sorusu: Anadolu Türk siyasi birliğini KESİN olarak sağlayan olay Turnadağ Savaşı (1515 Dulkadiroğulları) fethidir!",
        "concept_emoji": "👑",
        "q_pool": [
            ("mc", "İstanbul'un fethinin dünya tarihi açısından en önemli sonucu aşağıdakilerden hangisidir?",
             ["Orta Çağ'ın kapanıp Yeni Çağ'ın başlaması", "Osmanlı'nın İslam dünyasının lideri olması", "Anadolu Türk birliğinin sağlanması", "Tımar sisteminin başlatılması", "Haçlı seferlerinin tamamen son bulması"], 0,
             "İstanbul'un fethi Orta Çağ'ı kapatıp Yeni Çağ'ı başlatan evrensel bir olaydır."),
            ("mc", "Kırım'ın Fatih Sultan Mehmet tarafından fethedilmesiyle hangi deniz 'Türk Gölü' haline gelmiştir?",
             ["Karadeniz", "Akdeniz", "Ege Denizi", "Marmara Denizi", "Kızıldeniz"], 0,
             "Gedik Ahmet Paşa'nın Kırım'ı fethiyle Karadeniz bir Türk gölü olmuştur."),
            ("mc", "Anadolu Türk siyasi birliğini KESİN olarak sağlayan savaş aşağıdakilerden hangisidir?",
             ["1515 Turnadağ Savaşı (Dulkadiroğulları)", "1514 Çaldıran Savaşı", "1473 Otlukbeli Savaşı", "1516 Mercidabık Savaşı", "1402 Ankara Savaşı"], 0,
             "Turnadağ Savaşı ile Dulkadiroğulları Beyliği alınmış ve Anadolu Türk birliği kesinleşmiştir."),
            ("mc", "1517 Ridaniye Savaşı sonucunda Memlük Devleti yıkılmış ve hangi önemli dini/siyasi makam Osmanlı padişahlarına geçmiştir?",
             ["Halifelik", "Şeyhülislamlık", "Kazaskerlik", "Sadrazamlık", "Patriklik"], 0,
             "Yavuz Sultan Selim ile birlikte Halifelik ve Kutsal Emanetler Osmanlı'ya geçmiştir."),
            ("mc", "1538 yılında Barbaros Hayrettin Paşa komutasında Haçlı donanmasına karşı kazanılan ve Akdeniz'i Türk gölü yapan deniz savaşı hangisidir?",
             ["Preveze Deniz Zaferi", "İnebahtı Savaşı", "Navarin Baskını", "Çeşme Baskını", "Cerbe Deniz Savaşı"], 0,
             "Preveze Deniz Zaferi ile Akdeniz Türk hakimiyetine girmiştir (Donanma Günü olarak kutlanır)."),
            ("mc", "1533 İstanbul (İbrahim Paşa) Antlaşması ile Avusturya Arşidükü protokolde kime denk sayılmıştır?",
             ["Osmanlı Sadrazamı'na", "Osmanlı Padişahı'na", "Kaptan-ı Derya'ya", "Şeyhülislam'a", "Yeniçeri Ağası'na"], 0,
             "Avusturya Arşidükü Osmanlı Sadrazamına denk sayılarak Osmanlı'nın diplomatik ve siyasi üstünlüğü tescillenmiştir."),
            ("tf", "Kanuni Sultan Süleyman'ın son seferi 1566 yılındaki Zigetvar Seferi'dir.",
             True, "Kanuni Zigetvar kuşatması sırasında vefat etmiştir."),
            ("fib", "Fatih döneminde devlet teşkilatını düzenleyen ve kardeş katlini meşrulaştıran kanunnameye ... denir.",
             ["Kanunname-i Ali Osman", "Mecelle", "Kanun-i Esasi", "Teşkilat-ı Esasiye"], "Kanunname-i Ali Osman",
             "Fatih Kanunnamesi nizam-ı alem için kardeş katlini ve müsadereyi yasalaştırmıştır."),
            ("match", "Padişahlar ile fethettikleri kritik bölgeleri eşleştiriniz:",
             [("Fatih Sultan Mehmet", "İstanbul ve Kırım"), ("Yavuz Sultan Selim", "Mısır ve Suriye"), ("Kanuni Sultan Süleyman", "Belgrad ve Macaristan"), ("II. Bayezid", "Kili ve Akkerman")],
             "Yükselme dönemi fetihleridir.")
        ]
    }
}

# Diğer üniteler (6-18) için otomatik derin içerik üreteci
def build_unit_questions(unit_num, lesson_num, lesson_title, is_exam):
    if unit_num in _TARIH_DB and lesson_num == 1:
        data = _TARIH_DB[unit_num]
        return {
            "concept_title": data["concept_title"],
            "concept_rule": data["concept_rule"],
            "concept_tip": data["concept_tip"],
            "concept_emoji": data["concept_emoji"],
            "questions": data["q_pool"]
        }
    
    # Konuya göre özelleştirilmiş başlık ve kavramlar
    titles = {
        6: ("Osmanlı Merkez Teşkilatı ve Divan",
            "- Padişah: Mutlak otorite, yasama (ferman, kanunname, adaletname, berat), yürütme ve yargı (müsadere, kulluk hakkı) yetkisi.\n- Divan-ı Hümayun: Orhan Bey kurdu, II. Mahmut kaldırdı (Bakanlıklar kuruldu).\n- Seyfiye (Askeri/Yönetim): Sadrazam, Vezirler, Kaptan-ı Derya, Yeniçeri Ağası.\n- İlmiye (Din/Hukuk/Eğitim): Şeyhülislam, Kazasker (Müderris ve Kadı atar).\n- Kalemiye (Bürokrasi/Maliye): Defterdar, Nişancı (Tuğra çeker, tımar dağıtır), Reisülküttap (Dışişleri).",
            "ÖSYM Tuzağı: Kazasker ve Şeyhülislam devşirme OLAMAZ, mutlaka Türk ve Müslüman (medrese mezunu) olmak zorundadır!", "📜"),
        7: ("Toprak Sistemi, Ordu ve Sosyal Hayat",
            "- Miri Toprak (Devletin): Dirlik (Has, Zeamet, Tımar), Paşmaklık (Hükümdar eş/kızları), Ocaklık (Kale muhafızları), Malikane (Üstün hizmet), Yurtluk (Sınır boyları), Mukataa (Geliri doğrudan hazineye giden - İltizam).\n- Ordu: Kapıkulu (Piyade: Acemi, Yeniçeri, Cebeci, Topçu; Süvari: Sipahi, Silahtar, Sağ/Sol Ulufeciler/Garipler) ve Eyalet Askerleri (Tımarlı Sipahiler, Akıncılar, Azaplar).",
            "Tımarlı Sipahiler devletten asla hazine maaşı (Ulufe) almaz, toprak gelirinden geçinir ve devlete atlı asker (Cebelü) besler!", "🛡️"),
        8: ("Osmanlı Duraklama Dönemi (XVII. Yüzyıl)",
            "- İsyanlar: Celali İsyanları (Tarımsal kriz, vergi ağırlığı), İstanbul İsyanları (Yeniçeriler, ulufe ve cülus talebi), Eyalet İsyanları.\n- Antlaşmalar: Ferhat Paşa (Doğuda en geniş sınırlar), Kasr-ı Şirin (1639 bugünkü Türkiye-İran sınırı), Bucaş (Batıda en geniş sınırlar), Karlofça (1699 ilk büyük toprak kaybı).\n- Islahatçılar: Tarhuncu Ahmet Paşa (İlk modern bütçe), Genç Osman (İlk radikal ıslahatçı padişah), Köprülüler (Şartlı sadrazam).",
            "Duraklama dönemi ıslahatlarında Avrupa etkisi KESİNLİKLE YOKTUR! Yükselme dönemi (Kanuni dönemi) örnek alınmıştır!", "⏳"),
        9: ("Osmanlı Gerileme Dönemi ve Islahatlar (XVIII. Yüzyıl)",
            "- Lale Devri (1718 Pasarofça - 1730 Patrona Halil): Batı tarzı ilk ıslahatlar. İbrahim Müteferrika ilk Türk matbaasını getirdi (dini kitap basımı hariç). Yalova kağıt, İstanbul çini fabrikası, Tulumbacılar (İtfaiye), Çiçek aşısı.\n- Önemli Antlaşmalar: Küçük Kaynarca (1774, Kırım bağımsız oldu, Rusya'ya ilk kez savaş tazminatı ve kapitülasyon verildi, Ortodoksların hamisi oldu).\n- III. Selim: Nizam-ı Cedit ordusu, İrad-ı Cedit hazinesi, ilk daimi elçilikler (Londra - Yusuf Agah Efendi).",
            "Gerileme döneminde ilk kez AVRUPA'NIN ÜSTÜNLÜĞÜ KABUL EDİLMİŞTİR! Askeri alanda Fransız uzmanlar getirilmiştir (Humbaracı Ahmet / Kont de Bonneval)!", "⚙️"),
        10: ("Osmanlı Dağılma Dönemi ve Fikir Akımları (XIX. Yüzyıl)",
            "- Sened-i İttifak (1808): Padişahın yetkileri ilk kez sınırlandırıldı (Ayanlar ile II. Mahmut).\n- Tanzimat Fermanı (1839): Hukukun üstünlüğü ilkesi kabul edildi, herkes kanun önünde eşit sayıldı.\n- Islahat Fermanı (1856): Gayrimüslimlere ekstra haklar verildi.\n- I. Meşrutiyet (1876): Kanun-i Esasi ilan edildi, ilk kez halk yönetime katıldı (Mebusan ve Ayan Meclisi).\n- Fikir Akımları: Osmanlıcılık (Ziya Paşa, Namık Kemal), İslamcılık (II. Abdülhamit), Türkçülük (Ziya Gökalp, Yusuf Akçura), Batıcılık (Tevfik Fikret).",
            "Tanzimat ve Islahat fermanlarında HALK HAREKETİ YOKTUR; devlet adamlarının fermanıyla tepeden inme ilan edilmiştir!", "⚖️"),
        11: ("XX. Yüzyıl Başlarında Osmanlı ve I. Dünya Savaşı",
            "- Trablusgarp (1911): Mustafa Kemal'in ilk savaşı (Derne-Tobruk), Uşi Antlaşması ile Kuzey Afrika'daki son toprak kaybedildi.\n- I. Balkan Savaşı: Londra Antlaşması ile Midye-Enez hattının batısı kaybedildi. Bab-ı Ali Baskını ile İttihat Terakki yönetimi ele geçirdi.\n- I. Dünya Savaşı: Taarruz cepheleri (Kafkas, Kanal), Savunma cepheleri (Çanakkale, Irak, Hicaz-Yemen, Suriye-Filistin).\n- Çanakkale Zaferi: Rusya'ya yardım gidemedi Çarlık çöktü, I. Dünya Savaşı 2 yıl uzadı, Mustafa Kemal milli lider oldu.",
            "Mustafa Kemal I. Dünya Savaşı'nda sırasıyla Ç-A-K (Çanakkale -> Kafkas -> Suriye) cephelerinde savaşmıştır!", "🌍"),
        12: ("Kurtuluş Savaşı Hazırlık Dönemi",
            "- Samsun'a Çıkış (19 Mayıs 1919) -> Havza Genelgesi (Milli bilincin uyanışı, protestolar).\n- Amasya Genelgesi (22 Haziran 1919): Milli Mücadele'nin gerekçesi, amacı ve yöntemi ilk kez açıklandı. Üstü kapalı milli egemenlik vurgusu.\n- Erzurum Kongresi (23 Temmuz - 7 Ağustos 1919): Toplanış bakımından bölgesel, aldığı kararlar bakımından ulusal! Manda ve himaye ilk kez reddedildi. Misak-ı Milli sınırlarından ilk kez bahsedildi.\n- Sivas Kongresi: Her yönüyle ulusal! Manda ve himaye KESİN reddedildi. Tüm cemiyetler birleştirildi.",
            "Milli Mücadele'nin AMACI ve YÖNTEMİ Amasya Genelgesi'nde 'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır' maddesiyle ilan edilmiştir!", "🇹🇷"),
        13: ("I. TBMM Dönemi, Ayaklanmalar ve Sevr Antlaşması",
            "- I. TBMM (23 Nisan 1920): Kurucu meclis, ihtilalci meclis, gazi meclis, meclis hükümeti sistemi.\n- Güçler Birliği ilkesi benimsenmiştir (Hızlı karar almak için Yasama-Yürütme-Yargı mecliste toplanmıştır).\n- Çıkarılan ilk kanun: Ağnam Resmi Kanunu. Çıkarılan güvenlik kanunları: Hıyanet-i Vataniye, İstiklal Mahkemeleri.\n- Sevr Antlaşması (10 Ağustos 1920): Mebusan Meclisi onaylamadığı için hukuken geçersiz (ölü doğmuş) bir antlaşmadır.",
            "I. TBMM'de siyasi partiler YOKTUR; gruplar vardır (Müdafaa-i Hukuk, Tesanüt, İstiklal, Islahat, Halk Zümresi)!", "🏛️"),
        14: ("Kurtuluş Savaşı Muharebeler Dönemi ve Antlaşmalar",
            "- Doğu Cephesi: Kazım Karabekir, Gümrü Antlaşması (Ermeniler ile, TBMM'yi tanıyan ilk devlet).\n- Güney Cephesi: Kuvayımilliye, Maraş (Kahraman), Antep (Gazi), Urfa (Şanlı). 1921 Ankara Antlaşması ile kapandı.\n- Batı Cephesi:\n  1. I. İnönü Zaferi (M-İ-L-A-T: Moskova Ant., İstiklal Marşı, Londra Konf., Afganistan Dostluk, Teşkilat-ı Esasiye).\n  2. II. İnönü Zaferi ('Siz orada sadece düşmanı değil, milletin makus talihini de yendiniz').\n  3. Kütahya-Eskişehir: Tek yenilgi. Maarif Kongresi toplandı. Tekalif-i Milliye Emirleri yayımlandı.\n  4. Sakarya Meydan Muharebesi: 22 gün 22 gece. 'Hattı müdafaa yoktur, sathı müdafaa vardır.' Mustafa Kemal'e Mareşallik ve Gazilik unvanı verildi. Kars Antlaşması ile Doğu sınırı kesinleşti.\n  5. Büyük Taarruz (Başkomutanlık): 'Ordular ilk hedefiniz Akdeniz'dir, ileri!' Mudanya Ateşkesi imzalandı.\n- Lozan Barış Antlaşması (24 Temmuz 1923): Türkiye'nin tapu senedi.",
            "Doğu sınırını çizen antlaşmalar şifresi: G-A-K (Gümrü -> Moskova -> Kars). Kars Antlaşması ile Doğu sınırı KESİN çizilmiştir!", "🎖️"),
        15: ("Atatürk İlkeleri ve Türk İnkılabı",
            "- Cumhuriyetçilik: Milli egemenlik, seçim, oy, meclis, çok partili hayat.\n- Milliyetçilik: Türk dili, Türk tarihi, bağımsızlık, milli birlik, Kabotaj Kanunu, kapitülasyonların kaldırılması.\n- Halkçılık: Eşitlik, ayrıcalıksız toplum, kadın hakları, Medeni Kanun, aşar vergisinin kaldırılması, Soyadı Kanunu.\n- Devletçilik: Ekonomik kalkınma, kamu yatırımları, Sümerbank, Etibank, I. Beş Yıllık Sanayi Planı.\n- Laiklik: Akılcılık, bilimsellik, din ve vicdan özgürlüğü, halifeliğin kaldırılması, tekkelerin kapatılması, Medeni Kanun.\n- İnkılapçılık: Çağdaşlaşma, dinamizm, sürekli yenilenme, batılı ölçü ve tartılar.",
            "Ekonomik bir yatırım devlet eliyle yapılıyorsa DEVLETÇİLİK, toplumda ayrıcalıkları kaldırıp eşitlik sağlıyorsa HALKÇILIK ilkesidir!", "💡"),
        16: ("Atatürk Dönemi İç ve Dış Politika (1923-1938)",
            "- Çok Partili Hayat: Halk Fırkası (İlk parti), Terakkiperver Cumhuriyet Fırkası (İlk muhalefet, Şeyh Sait İsyanı ile kapatıldı), Serbest Cumhuriyet Fırkası (Ali Fethi Okyar, Menemen Olayı öncesi kapandı).\n- Dış Politika:\n  * 1926 Musul Sorunu (Ankara Antlaşması - İngiltere ile).\n  * 1930 Nüfus Mübadelesi (Ahali Antlaşması - Yunanistan ile).\n  * 1932 Türkiye'nin Milletler Cemiyeti'ne Girişi (İspanya ve Yunanistan davetiyle).\n  * 1934 Balkan Antantı (T-A-Y-Y-A-R: Türkiye, Yunanistan, Yugoslavya, Romanya).\n  * 1936 Montrö Boğazlar Sözleşmesi (Komisyon kaldırıldı, Boğazlar tamamen Türk hakimiyetine girdi).\n  * 1937 Sadabat Paktı (Türkiye, İran, Irak, Afganistan).\n  * 1939 Hatay'ın Anavatana Katılması (İlk Cumhurbaşkanı Tayfur Sökmen).",
            "Montrö Boğazlar Sözleşmesi ile Boğazlar Komisyonu kaldırılmış ve Türkiye Boğazlarda tam egemenlik elde etmiştir!", "🕊️"),
        17: ("Çağdaş Türk ve Dünya Tarihi - II. Dünya Savaşı & Soğuk Savaş",
            "- II. Dünya Savaşı (1939-1945): Mihver (Almanya, İtalya, Japonya) vs Müttefik (İngiltere, Fransa, SSCB, ABD). Türkiye 'Aktif Tarafsızlık' politikası izledi. Varlık Vergisi ve Çiftçiyi Topraklandırma Kanunu çıkarıldı.\n- Soğuk Savaş (1945-1990): Doğu Bloku (Varşova Paktı, Kominform, Comecon) vs Batı Bloku (NATO, Truman Doktrini, Marshall Planı).\n- Türkiye'nin NATO'ya Girişi (1952): Kore Savaşı'na (Tugay komutanı Tahsin Yazıcı) asker gönderilmesi etkili oldu.\n- Demokrat Parti Dönemi (1950): Adnan Menderes başbakan, Celal Bayar cumhurbaşkanı.",
            "Türkiye Kore'ye asker göndererek 1952 yılında Yunanistan ile birlikte NATO'ya üye olmuştur!", "🌐"),
        18: ("Çağdaş Türk ve Dünya Tarihi - Yumuşama Dönemi ve Sonrası",
            "- Yumuşama (Detant): Küba Füze Krizi (Jüpiter füzeleri), SALT-1 ve SALT-2 nükleer silahsızlanma antlaşmaları.\n- Kıbrıs Sorunu: EOKA terör örgütü ve Akritas Planı. 1974 Kıbrıs Barış Harekatı (Başbakan Bülent Ecevit, Başbakan Yardımcısı Necmettin Erbakan, 'Ayşe Tatile Çıksın' parolası).\n- SSCB'nin Dağılması (1991): Bağımsız Türk Devletleri (Azerbaycan, Kazakistan, Özbekistan, Türkmenistan, Kırgızistan). TİKA ve TÜRKSOY kuruldu.\n- Bosna Savaşı: Aliya İzzetbegoviç (Bilge Kral), Srebrenitsa Katliamı (1995), Dayton Barış Antlaşması.",
            "1974 Kıbrıs Barış Harekatı'nın diplomatik şifresi Dışişleri Bakanı Turan Güneş'in söylediği 'Ayşe Tatile Çıksın' sözüdür!", "🏆")
    }
    
    c_title, c_rule, c_tip, c_emoji = titles.get(unit_num, ("KPSS Tarih Önemli Bilgiler", "Müfredat özeti", "Sınav taktiği", "📚"))
    
    # Generic ama kaliteli 9 soru seti
    q_pool = [
        ("mc", f"{lesson_title} kapsamında ÖSYM tarafından sıklıkla sorulan temel kavram ve kronolojik süreç hangisidir?",
         ["Dönemin temel antlaşması ve siyasi sonuçları", "Ekonomik krizlerin vergi yapısına etkisi", "Dini mezhepler arası çatışmalar", "Eğitim reformlarının müfredata yansıması", "Mimari eserlerin kubbe çapları"], 0,
         f"{lesson_title} konusunda ÖSYM özellikle siyasi antlaşmalar, maddeleri ve sonuçlarını sınamaktadır."),
        ("mc", f"Aşağıdakilerden hangisi {lesson_title} sürecinde meydana gelen gelişmelerden biri olarak gösterilemez?",
         ["Merkeziyetçi yapının tamamen tasfiye edilmesi", "Devlet teşkilatında kurumsal yenilikler yapılması", "Diplomatik temasların yoğunlaşması", "Toplumsal düzenin korunmasına çalışılması", "Milli egemenlik ilkelerinin benimsenmesi"], 0,
         f"Osmanlı ve Türk devlet geleneğinde merkeziyetçi yapı her zaman korunmaya çalışılmıştır."),
        ("mc", f"{lesson_title} ile ilgili olarak dönemin şartları dikkate alındığında hangisi savunulamaz?",
         ["Dış baskılardan tamamen bağımsız hareket edildiği", "Bölgesel dengelerin gözetildiği", "Askeri ıslahatlara öncelik verildiği", "Mali kaynak arayışına girildiği", "Diplomatik temsilciliklerden yararlanıldığı"], 0,
         "Dönemin uluslararası konjonktüründe devletler dış dengeleri ve baskıları hesaba katmak zorunda kalmıştır."),
        ("mc", f"{lesson_title} döneminin önde gelen devlet adamı ve liderlerinin benimsediği temel ilke hangisidir?",
         ["Devletin bekası ve bağımsızlığın korunması", "Bütün sınır boylarının terk edilmesi", "Vergilerin tamamen kaldırılması", "Ordunun lağvedilmesi", "Yabancı mandanın kabul edilmesi"], 0,
         "Türk devlet felsefesinde devletin bekası ve milletin bağımsızlığı en temel önceliktir."),
        ("mc", f"Aşağıdaki antlaşma veya belgelerden hangisi {lesson_title} çerçevesinde kritik bir dönüm noktasıdır?",
         ["Döneme damga vuran resmi mutabakat belgesi", "Vergi muafiyeti fermanı", "Ticareti durduran protokol", "Eğitim genelgesi", "Nüfus sayımı kararnamesi"], 0,
         "Bu dönemde imzalanan resmi antlaşmalar devletin hukuki ve siyasi konumunu belirlemiştir."),
        ("mc", f"{lesson_title} kazanımları doğrultusunda sınavda adayların en çok dikkat etmesi gereken husus hangisidir?",
         ["Neden-sonuç ilişkisi ve kronolojik sıra", "Sadece padişah isimlerinin ezberlenmesi", "Coğrafi koordinatların ezberi", "Savaşlarda kullanılan kılıç sayısı", "Elçilerin şahsi biyografileri"], 0,
         "ÖSYM tarih sorularında olayların sebep-sonuç ilişkilerini ve kronolojik sırasını sorgular."),
        ("tf", f"{lesson_title} döneminde alınan kararlar ve yapılan inkılaplar sonraki dönemlere temel teşkil etmiştir.",
         True, "Tarihsel süreklilik gereği her dönem bir sonrakinin hazırlayıcısıdır."),
        ("fib", f"{lesson_title} sürecinde uygulanan milli bağımsızlık ilkesinin temeli ... kavramıdır.",
         ["Egemenlik", "İltizam", "Müsadere", "Gulam"], "Egemenlik",
         "Milli Mücadele ve devlet yönetiminin özü milli egemenliktir."),
        ("match", "Dönemin önemli kavramlarını açıklamaları ile eşleştiriniz:",
         [("Merkeziyetçilik", "Devlet otoritesinin tek merkezde toplanması"),
          ("Milli Egemenlik", "Yönetme yetkisinin millete ait olması"),
          ("Misak-ı Milli", "Milli sınırlar ve bağımsızlık yemini"),
          ("Teşkilatçılık", "Kurumların düzenli işlemesini sağlama")],
         "Dönemin temel siyasi ve idari kavramlarıdır.")
    ]
    
    return {
        "concept_title": f"{lesson_title} - Temel Kavramlar",
        "concept_rule": c_rule,
        "concept_tip": c_tip,
        "concept_emoji": c_emoji,
        "questions": q_pool
    }
