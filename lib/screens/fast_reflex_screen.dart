import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/lesson_models.dart';
import '../providers/game_provider.dart';
import '../services/sound_service.dart';

class ReflexQuestion {
  final String prompt;
  final String triggerWord;
  final String correctAnswer;
  final List<String> wrongOptions;
  final String memoryCode;
  final String subject;

  const ReflexQuestion({
    required this.prompt,
    required this.triggerWord,
    required this.correctAnswer,
    required this.wrongOptions,
    required this.memoryCode,
    required this.subject,
  });
}

final List<ReflexQuestion> kpssReflexBank = [
  const ReflexQuestion(
    prompt: "İslamiyet öncesi Türk devletlerinde ilk kez yerleşik hayata geçen devlet hangisidir?",
    triggerWord: "Yerleşik Hayat & Maniheizm",
    correctAnswer: "Uygurlar",
    wrongOptions: ["Göktürkler", "Asya Hun Devleti", "Hazarlar"],
    memoryCode: "Bögü Kağan döneminde Maniheizm ile yerleşik hayata geçen ilk devlet UYGURLARDIR!",
    subject: "KPSS Tarih",
  ),
  const ReflexQuestion(
    prompt: "Türk adını resmi devlet adı olarak kullanan İLK Türk devleti hangisidir?",
    triggerWord: "Türk Adıyla İlk Devlet",
    correctAnswer: "Göktürkler (Kök Türkler)",
    wrongOptions: ["Asya Hunları", "Uygurlar", "Karahanlılar"],
    memoryCode: "Bumin Kağan liderliğinde kurulan GÖKTÜRKLER Türk adını kullanan ilk devlettir!",
    subject: "KPSS Tarih",
  ),
  const ReflexQuestion(
    prompt: "İslam dünyasında 'Sultan' unvanını kullanan İLK Türk hükümdarı kimdir?",
    triggerWord: "İlk Sultan Unvanı",
    correctAnswer: "Gazneli Mahmut",
    wrongOptions: ["Tuğrul Bey", "Sultan Alparslan", "Satuk Buğra Han"],
    memoryCode: "Abbasi halifesini koruduğu için Sultan unvanını ilk kullanan GAZNELİ MAHMUT'tur!",
    subject: "KPSS Tarih",
  ),
  const ReflexQuestion(
    prompt: "Anadolu'da kurulan ilk medrese olan Yağıbasan Medresesi hangi beyliğe aittir?",
    triggerWord: "Anadolu'da İlk Medrese",
    correctAnswer: "Danişmentliler (Tokat - Niksar)",
    wrongOptions: ["Artuklular", "Saltuklular", "Mengücekliler"],
    memoryCode: "Tokat Niksar Yağıbasan Medresesi = DANİŞMENTLİLER!",
    subject: "KPSS Tarih",
  ),
  const ReflexQuestion(
    prompt: "Osmanlı Devleti'ne katılan ve donanma gücünü başlatan İLK beylik hangisidir?",
    triggerWord: "Osmanlı'ya Katılan İlk Beylik",
    correctAnswer: "Karesioğulları Beyliği",
    wrongOptions: ["Karamanoğulları", "Germiyanoğulları", "Dulkadiroğulları"],
    memoryCode: "Orhan Bey döneminde alınan ilk beylik KARESİOĞULLARI (Balıkesir-Çanakkale)!",
    subject: "KPSS Tarih",
  ),
  const ReflexQuestion(
    prompt: "Kurtuluş Savaşı'nın amacı, gerekçesi ve yöntemi İLK KEZ nerede açıklanmıştır?",
    triggerWord: "Amaç, Gerekçe ve Yöntem",
    correctAnswer: "Amasya Genelgesi (22 Haziran 1919)",
    wrongOptions: ["Erzurum Kongresi", "Sivas Kongresi", "Havza Genelgesi"],
    memoryCode: "'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır' = AMASYA GENELGESİ!",
    subject: "KPSS Tarih",
  ),
  const ReflexQuestion(
    prompt: "Misak-ı Milli'den verilen İLK taviz neresidir ve hangi antlaşmayla verilmiştir?",
    triggerWord: "Misak-ı Milli İlk Taviz",
    correctAnswer: "Batum (1921 Moskova Antlaşması)",
    wrongOptions: ["Hatay (Ankara Antlaşması)", "Musul (Ankara Antlaşması)", "Boğazlar (Lozan)"],
    memoryCode: "İlk taviz BATUM (Moskova), ikinci taviz HATAY (1921 Ankara), üçüncü MUSUL (1926 Ankara)!",
    subject: "KPSS Tarih",
  ),
  const ReflexQuestion(
    prompt: "Türkiye'nin en uzun kara sınırına sahip olduğu komşusu hangisidir?",
    triggerWord: "En Uzun Kara Sınırı",
    correctAnswer: "Suriye (911 km)",
    wrongOptions: ["İran", "Irak", "Bulgaristan"],
    memoryCode: "En uzun sınır SURİYE, en kısa sınır NAHÇIVAN (Azerbaycan)!",
    subject: "KPSS Coğrafya",
  ),
  const ReflexQuestion(
    prompt: "Ege Bölgesi'ndeki kırıklı (Horst) dağların kuzeyden güneye doğru sıralaması nedir?",
    triggerWord: "Kırık Dağlar Şifresi",
    correctAnswer: "Kaz - Madra - Yunt - Bozdağlar - Aydın - Menteşe",
    wrongOptions: [
      "Küre - Canik - Giresun - Rize",
      "Ağrı - Tendürek - Süphan - Nemrut",
      "Erciyes - Melendiz - Hasandağı"
    ],
    memoryCode: "Şifre: Kırık At (Kaz, Madra, Yunt, Boz, Aydın, Menteşe)!",
    subject: "KPSS Coğrafya",
  ),
  const ReflexQuestion(
    prompt: "Türkiye'de karstik aşınım ve birikim şekillerinin (Lapya, Dolin, Polye, Traverten) en yaygın olduğu bölge?",
    triggerWord: "Karstik Arazi Merkezi",
    correctAnswer: "Akdeniz Bölgesi (Teke ve Taşeli Platosu)",
    wrongOptions: ["Karadeniz Bölgesi", "Doğu Anadolu Bölgesi", "Marmara Bölgesi"],
    memoryCode: "Kalker (Kireçtaşı) ve Karstik şekiller denince akla ilk AKDENİZ (Antalya-Mersin) gelir!",
    subject: "KPSS Coğrafya",
  ),
  const ReflexQuestion(
    prompt: "Sınırları tamamen Türkiye içinde doğup yine Türkiye kıyılarında denize dökülen EN UZUN akarsuyumuz?",
    triggerWord: "Sınırlarımız İçindeki En Uzun Akarsu",
    correctAnswer: "Kızılırmak (1355 km)",
    wrongOptions: ["Fırat Nehri", "Sakarya Nehri", "Yeşilırmak"],
    memoryCode: "Sınırlarımız içindeki en uzun nehir KIZILIRMAK (Bafra Deltası'nı oluşturur)!",
    subject: "KPSS Coğrafya",
  ),
  const ReflexQuestion(
    prompt: "1982 Anayasası'na göre TBMM üye tamsayısı kaçtır ve milletvekili seçilme yaşı kaçtır?",
    triggerWord: "TBMM Üye Sayısı & Yaş",
    correctAnswer: "600 Milletvekili — 18 Yaş",
    wrongOptions: ["550 Milletvekili — 25 Yaş", "600 Milletvekili — 30 Yaş", "450 Milletvekili — 18 Yaş"],
    memoryCode: "2017 değişikliğiyle TBMM 600 milletvekili, seçilme yaşı 18'dir!",
    subject: "KPSS Vatandaşlık",
  ),
  const ReflexQuestion(
    prompt: "1982 Anayasası'na göre TBMM'nin genel veya özel af ilan edebilmesi için gereken nitelikli çoğunluk?",
    triggerWord: "Genel ve Özel Af Çoğunluğu",
    correctAnswer: "Üye Tamsayısının 3/5 Çoğunluğu (En az 360 Milletvekili)",
    wrongOptions: [
      "Salt Çoğunluk (301 Milletvekili)",
      "Üye Tamsayısının 2/3 Çoğunluğu (400 Milletvekili)",
      "Toplantıya Katılanların Salt Çoğunluğu"
    ],
    memoryCode: "Genel ve Özel Af kararı için TBMM üye tamsayısının 3/5'i (360 MV) şarttır!",
    subject: "KPSS Vatandaşlık",
  ),
  const ReflexQuestion(
    prompt: "İdare hukukunda 'Yetki Genişliği' ilkesi yalnızca kime tanınmıştır?",
    triggerWord: "Yetki Genişliği İlkesi",
    correctAnswer: "Sadece İllerde VALİYE tanınmıştır",
    wrongOptions: ["Kaymakama", "Belediye Başkanına", "Bakan Yardımcısına"],
    memoryCode: "Merkeze danışmadan karar alabilme yetkisi (Yetki Genişliği) SADECE VALİYE aittir!",
    subject: "KPSS Vatandaşlık",
  ),
  const ReflexQuestion(
    prompt: "Anayasa Mahkemesi kaç üyeden oluşur ve üyeleri kimler seçer?",
    triggerWord: "Anayasa Mahkemesi Yapısı",
    correctAnswer: "15 Üye (12'sini Cumhurbaşkanı, 3'ünü TBMM seçer)",
    wrongOptions: [
      "17 Üye (Tamamını Cumhurbaşkanı seçer)",
      "13 Üye (HSK seçer)",
      "20 Üye (TBMM seçer)"
    ],
    memoryCode: "AYM = 15 Üye (12 Cumhurbaşkanı + 3 TBMM), görev süresi 12 yıldır!",
    subject: "KPSS Vatandaşlık",
  ),
  const ReflexQuestion(
    prompt: "Türkçede kurum, kuruluş ve kurul adlarına gelen ekler kesme işaretiyle ayrılır mı?",
    triggerWord: "Kurum Adlarına Gelen Ekler",
    correctAnswer: "KESİNLİKLE AYRILMAZ (İstisna: Avrupa Birliği'ne)",
    wrongOptions: [
      "Her zaman kesme işaretiyle ayrılır",
      "Sadece bakanlık adlarında ayrılır",
      "Sadece üniversite adlarında ayrılır"
    ],
    memoryCode: "Türk Dil Kurumuna, Türkiye Büyük Millet Meclisinde -> Kesme işareti YOK!",
    subject: "KPSS Türkçe",
  ),
  const ReflexQuestion(
    prompt: "Cümlede daha önce hiç virgül (,) kullanılmamışsa noktalı virgül (;) kullanılabilir mi?",
    triggerWord: "Noktalı Virgül Altın Şartı",
    correctAnswer: "Asla Kullanılamaz (Virgül yoksa noktalı virgül de yoktur)",
    wrongOptions: [
      "Özneden sonra her zaman kullanılır",
      "Uzun cümlelerde virgül olmadan kullanılır",
      "Yüklemden hemen önce kullanılır"
    ],
    memoryCode: "Virgülün olmadığı yerde NOKTALI VİRGÜL OLAMAZ!",
    subject: "KPSS Türkçe",
  ),
  const ReflexQuestion(
    prompt: "Bir doğal sayının 9 ile tam bölünebilmesi için hangi kural aranır?",
    triggerWord: "9 ile Bölünebilme",
    correctAnswer: "Rakamları Toplamı 9 veya 9'un Katı Olmalıdır",
    wrongOptions: [
      "Son iki basamağı 9'un katı olmalıdır",
      "Birler basamağı 9 olmalıdır",
      "Sayı tek sayı olmalıdır"
    ],
    memoryCode: "3 ve 9 ile bölünebilmede daima RAKAMLAR TOPLAMINA bakılır!",
    subject: "KPSS Matematik",
  ),
  const ReflexQuestion(
    prompt: "Bütünden küçük eş parçalara gidilen problemlerde (tarla bölme, çuval paylaştırma) hangisi kullanılır?",
    triggerWord: "Bütünden Parçaya",
    correctAnswer: "EBOB (En Büyük Ortak Bölen)",
    wrongOptions: [
      "EKOK (En Küçük Ortak Kat)",
      "Faktöriyel",
      "Aritmetik Ortalama"
    ],
    memoryCode: "Bütünden Parçaya = EBOB | Parçadan Bütüne (Nöbet, Küp yapma) = EKOK!",
    subject: "KPSS Matematik",
  ),
];

class FastReflexScreen extends ConsumerStatefulWidget {
  const FastReflexScreen({super.key});

  @override
  ConsumerState<FastReflexScreen> createState() => _FastReflexScreenState();
}

class _FastReflexScreenState extends ConsumerState<FastReflexScreen> {
  int _score = 0;
  int _combo = 0;
  int _currentIndex = 0;
  int _timeLeft = 7;
  Timer? _timer;
  bool _isAnswered = false;
  int? _selectedOptionIndex;
  late List<ReflexQuestion> _questions;
  late List<String> _currentShuffledOptions;

  @override
  void initState() {
    super.initState();
    _questions = List.from(kpssReflexBank)..shuffle();
    _prepareQuestion();
  }

  void _prepareQuestion() {
    if (_currentIndex >= _questions.length) {
      _questions.shuffle();
      _currentIndex = 0;
    }
    final q = _questions[_currentIndex];
    final allOps = [q.correctAnswer, ...q.wrongOptions];
    allOps.shuffle();
    _currentShuffledOptions = allOps;
    _isAnswered = false;
    _selectedOptionIndex = null;
    _timeLeft = 7;

    _timer?.cancel();
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (!mounted) return;
      setState(() {
        if (_timeLeft > 1) {
          _timeLeft--;
        } else {
          _onTimeOut();
        }
      });
    });
  }

  void _onTimeOut() {
    _timer?.cancel();
    _isAnswered = true;
    _combo = 0;
    SoundService.playIncorrect();
    HapticFeedback.heavyImpact();

    Future.delayed(const Duration(milliseconds: 1400), () {
      if (!mounted) return;
      setState(() {
        _currentIndex++;
        _prepareQuestion();
      });
    });
  }

  void _handleAnswer(int optionIndex) {
    if (_isAnswered) return;
    _timer?.cancel();
    _isAnswered = true;
    _selectedOptionIndex = optionIndex;

    final q = _questions[_currentIndex];
    final isCorrect = _currentShuffledOptions[optionIndex] == q.correctAnswer;

    if (isCorrect) {
      _combo++;
      final addedScore = 100 + (_combo * 20) + (_timeLeft * 10);
      _score += addedScore;
      SoundService.playCorrect();
      HapticFeedback.lightImpact();

      try {
        ref.read(userProfileProvider.notifier).recordLessonAttempt(
              Lesson(
                id: 'reflex_fast_kpss_${DateTime.now().millisecondsSinceEpoch}',
                title: 'KPSS Hızlı Refleks',
                description: 'Görünce Yapıştır Modu',
                questions: const [],
                xpReward: 15,
                gemReward: 3,
              ),
              100.0,
            );
      } catch (_) {}
    } else {
      _combo = 0;
      SoundService.playIncorrect();
      HapticFeedback.mediumImpact();
    }

    Future.delayed(const Duration(milliseconds: 1300), () {
      if (!mounted) return;
      setState(() {
        _currentIndex++;
        _prepareQuestion();
      });
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (_questions.isEmpty) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    final q = _questions[_currentIndex];

    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      appBar: AppBar(
        backgroundColor: const Color(0xFF1E293B),
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.close_rounded, color: Colors.white, size: 28),
          onPressed: () => Navigator.of(context).pop(),
        ),
        title: const Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(Icons.bolt_rounded, color: Color(0xFFF59E0B), size: 24),
            SizedBox(width: 6),
            Text(
              'KPSS GÖRÜNCE YAPIŞTIR! ⚡',
              style: TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.w900,
                fontSize: 15,
                letterSpacing: 0.5,
              ),
            ),
          ],
        ),
        actions: [
          Container(
            margin: const EdgeInsets.only(right: 16),
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
            decoration: BoxDecoration(
              color: const Color(0xFFDC2626).withOpacity(0.2),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: const Color(0xFFEF4444), width: 1.5),
            ),
            child: Row(
              children: [
                const Icon(Icons.local_fire_department_rounded, color: Color(0xFFF59E0B), size: 18),
                const SizedBox(width: 4),
                Text(
                  'x$_combo',
                  style: const TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.w900,
                    fontSize: 14,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 12, 16, 8),
              child: Row(
                children: [
                  Expanded(
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                      decoration: BoxDecoration(
                        color: const Color(0xFF1E293B),
                        borderRadius: BorderRadius.circular(14),
                      ),
                      child: Row(
                        children: [
                          const Icon(Icons.star_rounded, color: Color(0xFFFBBF24), size: 20),
                          const SizedBox(width: 6),
                          Text(
                            'Puan: $_score',
                            style: const TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.w800,
                              fontSize: 14,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                    decoration: BoxDecoration(
                      color: _timeLeft <= 2 ? const Color(0xFFEF4444) : const Color(0xFF0284C7),
                      borderRadius: BorderRadius.circular(14),
                    ),
                    child: Row(
                      children: [
                        const Icon(Icons.timer_rounded, color: Colors.white, size: 18),
                        const SizedBox(width: 6),
                        Text(
                          '$_timeLeft s',
                          style: const TextStyle(
                            color: Colors.white,
                            fontWeight: FontWeight.w900,
                            fontSize: 15,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              child: SingleChildScrollView(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                      decoration: BoxDecoration(
                        gradient: const LinearGradient(
                          colors: [Color(0xFFB91C1C), Color(0xFF7F1D1D)],
                        ),
                        borderRadius: BorderRadius.circular(16),
                        boxShadow: [
                          BoxShadow(
                            color: const Color(0xFFB91C1C).withOpacity(0.3),
                            blurRadius: 10,
                            offset: const Offset(0, 4),
                          ),
                        ],
                      ),
                      child: Column(
                        children: [
                          Text(
                            q.subject.toUpperCase(),
                            style: const TextStyle(
                              color: Color(0xFFFECACA),
                              fontWeight: FontWeight.w800,
                              fontSize: 11,
                              letterSpacing: 1.0,
                            ),
                          ),
                          const SizedBox(height: 4),
                          Text(
                            q.triggerWord,
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.w900,
                              fontSize: 20,
                              letterSpacing: 0.5,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: const Color(0xFF1E293B),
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: Colors.white.withOpacity(0.1)),
                      ),
                      child: Text(
                        q.prompt,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 16,
                          fontWeight: FontWeight.w700,
                          height: 1.35,
                        ),
                      ),
                    ),
                    const SizedBox(height: 20),
                    ...List.generate(_currentShuffledOptions.length, (idx) {
                      final option = _currentShuffledOptions[idx];
                      Color optBg = const Color(0xFF1E293B);
                      Color optBorder = Colors.white.withOpacity(0.12);

                      if (_isAnswered) {
                        if (option == q.correctAnswer) {
                          optBg = const Color(0xFF059669);
                          optBorder = const Color(0xFF10B981);
                        } else if (_selectedOptionIndex == idx) {
                          optBg = const Color(0xFFDC2626);
                          optBorder = const Color(0xFFEF4444);
                        }
                      }

                      return Padding(
                        padding: const EdgeInsets.only(bottom: 10),
                        child: Material(
                          color: Colors.transparent,
                          child: InkWell(
                            onTap: () => _handleAnswer(idx),
                            borderRadius: BorderRadius.circular(14),
                            child: AnimatedContainer(
                              duration: const Duration(milliseconds: 250),
                              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                              decoration: BoxDecoration(
                                color: optBg,
                                borderRadius: BorderRadius.circular(14),
                                border: Border.all(color: optBorder, width: 1.5),
                              ),
                              child: Row(
                                children: [
                                  Container(
                                    width: 28,
                                    height: 28,
                                    alignment: Alignment.center,
                                    decoration: BoxDecoration(
                                      color: Colors.white.withOpacity(0.1),
                                      shape: BoxShape.circle,
                                    ),
                                    child: Text(
                                      String.fromCharCode(65 + idx),
                                      style: const TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.w900,
                                        fontSize: 13,
                                      ),
                                    ),
                                  ),
                                  const SizedBox(width: 12),
                                  Expanded(
                                    child: Text(
                                      option,
                                      style: const TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.w700,
                                        fontSize: 14,
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),
                      );
                    }),
                    if (_isAnswered) ...[
                      const SizedBox(height: 10),
                      Container(
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: const Color(0xFFF59E0B).withOpacity(0.15),
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: const Color(0xFFF59E0B).withOpacity(0.4)),
                        ),
                        child: Row(
                          children: [
                            const Icon(Icons.lightbulb_rounded, color: Color(0xFFFBBF24), size: 20),
                            const SizedBox(width: 8),
                            Expanded(
                              child: Text(
                                q.memoryCode,
                                style: const TextStyle(
                                  color: Color(0xFFFEF3C7),
                                  fontSize: 13,
                                  fontWeight: FontWeight.w700,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
