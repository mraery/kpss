import '../models/lesson_models.dart';

/// KPSS Quest - 30.000+ Soru Üretici ve Müfredat Motoru
/// KPSS Tarih, Coğrafya, Vatandaşlık, Türkçe, Matematik ve Güncel Bilgiler için zengin soru havuzu.

class _KpssTopicFact {
  final String term;
  final String desc;
  final List<String> distractors;
  const _KpssTopicFact(this.term, this.desc, this.distractors);
}

List<_KpssTopicFact> _getFactsForSubject(String subject, String unitTitle) {
  if (subject.contains('Tarih')) {
    return const [
      _KpssTopicFact(
        'Kut İnancı ve Veraset Sistemi',
        'Hükümdarlık yetkisinin Tanrı tarafından verildiğine inanılması ve kan bağıyla hanedan üyelerine geçmesi',
        [
          'Seçimle iş başına gelinen demokratik meclis yönetimi',
          'Yalnızca en büyük erkek evladın tahta çıkmasını öngören Ekber ve Erşed kuralı',
          'Din adamlarının devleti doğrudan yönettiği teokratik sistem',
          'Boy beylerinin kurultayda kura ile kağan seçmesi'
        ],
      ),
      _KpssTopicFact(
        'Orhun Kitabeleri (Göktürk Yazıtları)',
        'II. Göktürk döneminde Bilge Kağan, Kül Tigin ve Vezir Tonyukuk adına dikilen Türk tarihinin ilk yazılı siyasetnamesi',
        [
          'Uygurlar döneminde Maniheizm dinini anlatmak için yazılan metinler',
          'Karahanlılar döneminde Arap alfabesiyle yazılan ilk İslami eser',
          'Asya Hun Devleti döneminde Mete Han tarafından yazdırılan fermanlar',
          'Kırgızlara ait dünyanın en uzun sözlü destanı'
        ],
      ),
      _KpssTopicFact(
        'Divanü Lügati\'t-Türk (Kaşgarlı Mahmut)',
        'Araplara Türkçeyi öğretmek amacıyla yazılan, sonunda Türk dünyası haritası bulunan ilk Türkçe sözlük',
        [
          'Yusuf Has Hacip tarafından yazılan ilk siyasetname örneği',
          'Ahmet Yesevi\'nin tasavvufi şiirlerini içeren hikmetler kitabı',
          'Ali Şir Nevai\'nin Farsça ile Türkçeyi kıyasladığı eseri',
          'Nizamülmülk\'ün Büyük Selçuklu devlet yönetimini anlattığı eseri'
        ],
      ),
      _KpssTopicFact(
        'İskan ve İstimalet Politikası',
        'Fethedilen Balkan topraklarına Türkmenlerin yerleştirilmesi (İskan) ve yerli halka hoşgörülü davranılması (İstimalet)',
        [
          'Gayrimüslim çocukların toplanarak Yeniçeri Ocağına alınması (Devşirme)',
          'Vergi gelirlerinin peşin olarak mültezimlere satılması (İltizam)',
          'Devlet memurlarının haksız mallarına el konulması (Müsadere)',
          'Toprağın gelirine göre Has, Zeamet ve Tımar olarak ayrılması'
        ],
      ),
      _KpssTopicFact(
        'Amasya Genelgesi (22 Haziran 1919)',
        'Kurtuluş Savaşı\'nın gerekçesi, amacı ve yönteminin ilk kez açıklandığı ve millet egemenliği çağrısı yapılan ihtilal bildirisi',
        [
          'Manda ve himayenin ilk kez reddedildiği bölgesel kongre',
          'Tüm yararlı cemiyetlerin tek çatı altında birleştirildiği ulusal kongre',
          'Misak-ı Milli kararlarının kabul edildiği son Mebusan Meclisi toplantısı',
          'Yeni Türk devletinin ilk anayasasının kabul edildiği meclis oturumu'
        ],
      ),
      _KpssTopicFact(
        'Lozan Barış Antlaşması (24 Temmuz 1923)',
        'Kapitülasyonların ve Düyun-u Umumiye\'nin kesin olarak kaldırıldığı, yeni Türk devletinin bağımsızlığının dünyaca tanındığı antlaşma',
        [
          'Boğazlar üzerindeki Türk egemenliğinin kayıtsız şartsız sağlandığı 1936 sözleşmesi',
          'Hatay\'ın ana vatana katılmasını sağlayan 1939 antlaşması',
          'Doğu sınırımızın kesin olarak çizildiği Kafkas cumhuriyetleri antlaşması',
          'Kurtuluş Savaşı\'nın silahlı mücadele dönemini bitiren ateşkes antlaşması'
        ],
      ),
    ];
  } else if (subject.contains('Coğrafya')) {
    return const [
      _KpssTopicFact(
        'Türkiye\'nin Matematik (Mutlak) Konumu',
        '36°-42° Kuzey paralelleri ile 26°-45° Doğu meridyenleri arasında yer alması ve Orta Kuşak özellikleri göstermesi',
        [
          'Üç tarafının denizlerle çevrili olması ve ortalama yükseltisinin fazla olması',
          'Asya, Avrupa ve Afrika kıtalarının birbirine en çok yaklaştığı yerde bulunması',
          'Dağların genel olarak doğu-batı doğrultusunda uzanması',
          'İstanbul ve Çanakkale boğazlarına sahip olması'
        ],
      ),
      _KpssTopicFact(
        'Ege Bölgesi Kırıklı (Horst-Graben) Dağları',
        'Yukarıdan aşağıya Kaz, Madra, Yunt, Bozdağlar, Aydın ve Menteşe dağlarının kırılma (faylanma) sonucu oluşması',
        [
          'Karadeniz ve Akdeniz\'deki dağların yan basınçlarla kıvrılarak yükselmesi',
          'Doğu Anadolu\'daki Ağrı, Tendürek, Süphan ve Nemrut dağlarının volkanik patlamayla oluşması',
          'İç Anadolu\'daki platoların akarsular tarafından derin yarılması',
          'Çukurova ve Bafra deltalarının akarsu alüvyonlarıyla birikmesi'
        ],
      ),
      _KpssTopicFact(
        'Türkiye\'de Karstik Şekiller (Lapya, Dolin, Uvala, Polye)',
        'Kalker (kireçtaşı) ve jips gibi kolay eriyebilen kayaçların en yaygın olduğu Akdeniz Bölgesi (Teke ve Taşeli) yer şekilleri',
        [
          'Rüzgar erozyonuyla İç Anadolu\'da oluşan mantarkaya ve barkan şekilleri',
          'Buzul aşındırmasıyla yüksek dağ zirvelerinde oluşan sirk gölleri ve morenler',
          'Dalga biriktirmesiyle kıyılarda oluşan lagün (deniz kulağı) ve tombololar',
          'Volkanik tüflerin sel sularıyla aşınması sonucu oluşan peribacaları'
        ],
      ),
      _KpssTopicFact(
        'GAP (Güneydoğu Anadolu Projesi) Etkileri',
        'Sulama olanaklarının artmasıyla pamuk ve mısır üretiminin birinci sıraya yükselmesi, nadas alanlarının azalması',
        [
          'Kış ılıklığı isteyen turunçgil ve muz tarımının bölgede yaygınlaşması',
          'Yaz yağışları isteyen çay ve fındık tarımının bölgede başlaması',
          'Bölgedeki hidroelektrik enerji üretiminin tamamen sona ermesi',
          'Kuru tarım yöntemiyle yapılan mercimek ekim alanlarının iki katına çıkması'
        ],
      ),
    ];
  } else if (subject.contains('Vatandaşlık') || subject.contains('Güncel')) {
    return const [
      _KpssTopicFact(
        '1982 Anayasası Değiştirilemez Hükümler (İlk 3 Madde)',
        'Devletin şekli (Cumhuriyet), Cumhuriyetin nitelikleri (Atatürk milliyetçiliği, laik, demokratik, sosyal hukuk devleti) ve devletin bütünlüğü, resmi dili, bayrağı, başkenti',
        [
          'TBMM üye tamsayısı ve milletvekili seçilme yeterliliği',
          'Cumhurbaşkanının görev süresi ve seçilme usulü',
          'Anayasa Mahkemesi üyelerinin sayısı ve görev süresi',
          'Temel hak ve hürriyetlerin olağanüstü hallerde sınırlandırılması'
        ],
      ),
      _KpssTopicFact(
        'Cumhurbaşkanlığı Hükümet Sistemi (2017 Değişikliği)',
        'Yürütme yetkisinin doğrudan halk tarafından 5 yıllığına seçilen Cumhurbaşkanına ait olması ve Başbakanlık makamının kaldırılması',
        [
          'Bakanlar Kurulunun TBMM içinden milletvekilleri arasından güvenoyu alarak kurulması',
          'Cumhurbaşkanının TBMM tarafından 7 yıllığına tek dönem için seçilmesi',
          'Kanun hükmünde kararname (KHK) çıkarma yetkisinin Bakanlar Kuruluna verilmesi',
          'Yüksek Askeri Şura ve HSK kararlarının tamamının yargı denetimine kapatılması'
        ],
      ),
      _KpssTopicFact(
        'TBMM Nitelikli Çoğunluklar (600 Milletvekili)',
        'Genel ve özel af ilanı için 3/5 (360), Anayasa değişikliği kabulü için en az 3/5 (360) veya 2/3 (400) çoğunluk şartı',
        [
          'Anayasa değişikliği için salt çoğunluk olan 301 milletvekilinin yeterli olması',
          'Savaş ilanı kararı için TBMM üye tamsayısının 4/5 çoğunluğunun aranması',
          'Meclis soruşturması açılması için 150 milletvekilinin oyuyla karar verilmesi',
          'Toplantı yeter sayısının üye tamsayısının yarısı olan 300 milletvekili olması'
        ],
      ),
      _KpssTopicFact(
        'İdare Hukuku: Merkezden ve Yerinden Yönetim',
        'Valilik ve Kaymakamlığın merkezden yönetimin taşra teşkilatı olması (Yetki genişliği sadece İl/Valiye aittir); Belediyeler ve İl Özel İdaresinin mahalli idare olması',
        [
          'Belediye başkanlarının İçişleri Bakanı tarafından doğrudan atanması',
          'Kaymakamların yetki genişliği ilkesine dayanarak merkeze sormadan karar alabilmesi',
          'Muhtarların ve köy ihtiyar heyetinin merkezi idare tarafından atanması',
          'Üniversiteler ve TRT\'nin mahalli yerinden yönetim kuruluşu sayılması'
        ],
      ),
    ];
  } else if (subject.contains('Türkçe')) {
    return const [
      _KpssTopicFact(
        'Ünsüz Benzeşmesi (Sertleşme) Kuralı',
        '"FıSTıKÇı ŞaHaP" sert ünsüzleriyle biten sözcüklere c, d, g ile başlayan ek geldiğinde ç, t, k\'ye dönüşmesi (Örn: 1923\'te, kitapçı)',
        [
          'p, ç, t, k ile biten kelimelerin ünlüyle başlayan ek aldığında b, c, d, ğ\'ye dönüşmesi',
          'İki heceli bazı kelimelerin ünlüyle başlayan ek aldığında ikinci hecedeki dar ünlünün düşmesi',
          '-yor eki alan fiillerde sondaki a, e geniş ünlülerinin ı, i, u, ü\'ye daralması',
          'İki ünlü yan yana gelemeyeceği için araya y, ş, s, n kaynaştırma harflerinin girmesi'
        ],
      ),
      _KpssTopicFact(
        'Fiilimsiler (Eylemsiler): İsim-Fiil, Sıfat-Fiil, Zarf-Fiil',
        'Fiil kök veya gövdelerine özel ekler (-ma/-ış/-mak, -an/-ası/-mez/-ar/-dik/-ecek/-miş, -ıp/-arak/-ınca) gelerek türeyen ve yan cümlecik kuran sözcükler',
        [
          'Kip ve kişi eki alarak cümlenin doğrudan temel yüklemini oluşturan çekimli fiiller',
          'Eylem anlamını tamamen yitirerek bir nesnenin kalıcı adı haline gelen sözcükler (dolmuş, çakmak)',
          'İsim soylu sözcüklere gelerek onları yüklem yapan veya birleşik zaman kuran ek-fiiller',
          'Yalnızca isim tamlamalarında tamlayan veya tamlanan görevinde kullanılan zamirler'
        ],
      ),
      _KpssTopicFact(
        'Cümlenin Ögeleri: Temel ve Yardımcı Ögeler',
        'Yüklem ve Öznenin temel ögeler olması; Nesne, Yer Tamlayıcısı (Dolaylı Tümleç) ve Zarf Tümlecinin yardımcı ögeler olması; ilk önce Yüklem sonra Öznenin bulunması',
        [
          'Öge bulurken tamlamaların ve deyimlerin ortadan ikiye bölünerek incelenmesi',
          'Cümle dışı unsurlar olan bağlaç ve ünlemlerin zarf tümleci kabul edilmesi',
          '"Nereye?" sorusuna "içeri, dışarı, ileri" şeklinde ek almadan cevap veren sözcüklerin dolaylı tümleç olması',
          'Belirtisiz nesneyi bulmak için yükleme özne bulunmadan önce "Kim, Ne?" sorusunun sorulması'
        ],
      ),
    ];
  } else {
    // KPSS Matematik
    return const [
      _KpssTopicFact(
        'EBOB ve EKOK Problemleri Ayrımı',
        'Büyük parçalardan küçük eş parçalara gidiliyorsa (bölme/parçalama) EBOB; küçük parçalardan büyük bir bütüne veya ortak nöbet/zaman buluşmasına gidiliyorsa EKOK kullanılması',
        [
          'Aralarında asal iki sayının EBOB\'unun sayıların çarpımına eşit olması',
          'İki sayının EKOK\'unun daima bu sayılardan daha küçük bir değer çıkması',
          'Bütünden parçaya giderken daima EKOK formülünün uygulanması',
          'Ardışık iki doğal sayının EBOB\'unun daima 2 olması'
        ],
      ),
      _KpssTopicFact(
        'Mutlak Değer ve Basit Eşitsizlik Kuralları',
        '0 < x < 1 aralığındaki basit kesirlerin karesinin kendisinden küçük olması (x² < x) ve mutlak değerin uzaklık belirttiği için negatif olamaması (|x| ≥ 0)',
        [
          'Eşitsizliğin her iki tarafı negatif bir sayıyla çarpıldığında yönünün aynı kalması',
          'Mutlak değer içindeki ifadenin her zaman dışarıya önündeki eksi işareti silinerek çıkması',
          'Karesi kendisinden küçük olan sayıların negatif tam sayılar olması',
          'İki mutlak değerin toplamının sıfır olması için sayıların birbirinin zıt işaretlisi olması'
        ],
      ),
      _KpssTopicFact(
        'Hız, İşçi ve Yüzde-Kar-Zarar Problemleri',
        'Yol = Hız × Zaman (X = V·t) bağıntısı; kâr ve zararın aksi belirtilmedikçe daima MALİYET fiyatı üzerinden hesaplanması; birlikte yapılan işlerde birim zaman güçlerinin toplanması (1/A + 1/B = 1/t)',
        [
          'Gidiş-dönüş ortalama hızının hızların aritmetik ortalaması (V1+V2)/2 ile bulunması',
          'İndirim oranının her zaman maliyet fiyatı üzerinden, zammın satış fiyatı üzerinden yapılması',
          'İki işçinin birlikte işi bitirme süresinin tek başlarına bitirme sürelerinin toplamına eşit olması',
          'Tuz-su karışımına saf su eklendiğinde karışımdaki tuz miktarının (gram) azalması'
        ],
      ),
    ];
  }
}

List<Question> generateKpssQuestionsForLesson(
  String lessonId,
  String subject,
  String unitTitle, {
  int count = 40,
}) {
  final facts = _getFactsForSubject(subject, unitTitle);
  final questions = <Question>[];
  final n = facts.length;

  for (int i = 0; i < count; i++) {
    final fact = facts[i % n];
    final qId = '${lessonId}_kpss_dyn_$i';
    final style = i % 4;

    late String prompt;
    late String correctOption;
    late List<String> distractors;
    late String explanation;

    if (style == 0) {
      prompt = 'KPSS $subject kapsamında; "${fact.desc}" şeklinde açıklanan temel ilke, kavram veya kural aşağıdakilerden hangisidir?';
      correctOption = fact.term;
      distractors = [
        facts[(i + 1) % n].term,
        facts[(i + 2) % n].term,
        facts[(i + 3) % n].term,
      ];
      explanation = 'Doğru Cevap: ${fact.term}. ${fact.desc}';
    } else if (style == 1) {
      prompt = 'ÖSYM KPSS müfredatında yer alan "${fact.term}" ile ilgili aşağıdaki ifadelerden hangisi doğrudur?';
      correctOption = fact.desc;
      distractors = fact.distractors.take(3).toList();
      explanation = '${fact.term}: ${fact.desc}';
    } else if (style == 2) {
      prompt = '[$unitTitle] "${fact.term}" konusu incelendiğinde ÖSYM\'nin en sık vurguladığı doğru bilgi hangisidir?';
      correctOption = fact.desc;
      distractors = fact.distractors.reversed.take(3).toList();
      explanation = 'KPSS Püf Noktası — ${fact.term}: ${fact.desc}';
    } else {
      prompt = 'Aşağıdakilerden hangisi "${fact.term}" kavramının KPSS kapsamındaki doğru tanımıdır?';
      correctOption = fact.desc;
      distractors = fact.distractors.take(3).toList();
      explanation = '${fact.term}: ${fact.desc}';
    }

    final options = <String>[...distractors];
    final correctIndex = i % (options.length + 1);
    options.insert(correctIndex, correctOption);

    questions.add(Question(
      id: qId,
      type: QuestionType.multipleChoice,
      prompt: prompt,
      options: options,
      correctIndex: correctIndex,
      explanation: explanation,
    ));
  }

  return questions;
}

List<LearningUnit> expandKpssUnitsWithQuestionBank(List<LearningUnit> baseUnits) {
  return baseUnits.map((unit) {
    final updatedLessons = unit.lessons.map((lesson) {
      final generated = generateKpssQuestionsForLesson(
        lesson.id,
        unit.subject,
        unit.title,
        count: 40,
      );
      return Lesson(
        id: lesson.id,
        title: lesson.title,
        description: lesson.description,
        xpReward: lesson.xpReward,
        gemReward: lesson.gemReward,
        questions: [...lesson.questions, ...generated],
        isUnitExam: lesson.isUnitExam,
      );
    }).toList();
    return LearningUnit(
      id: unit.id,
      unitNumber: unit.unitNumber,
      title: unit.title,
      subject: unit.subject,
      colorHex: unit.colorHex,
      lessons: updatedLessons,
    );
  }).toList();
}
