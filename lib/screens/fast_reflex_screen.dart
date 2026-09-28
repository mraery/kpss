import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../providers/game_provider.dart';
import '../services/sound_service.dart';
import '../widgets/duo_button.dart';

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
    prompt: 'BM Güvenlik Konseyi daimi veto hakkına sahip 5 ülke?',
    triggerWord: 'F - İ - R - Ç - A',
    correctAnswer: 'Fransa, İngiltere, Rusya, Çin, ABD',
    wrongOptions: [
      'Fransa, İtalya, Rusya, Çin, Almanya',
      'Finlandiya, İngiltere, Romanya, Çin, ABD',
      'Fransa, İspanya, Rusya, Çekya, ABD'
    ],
    memoryCode: 'Şifre: FİRÇA (Fransa, İngiltere, Rusya, Çin, ABD)',
    subject: 'KPSS Güncel Bilgiler',
  ),
  const ReflexQuestion(
    prompt: 'Türkiye\'nin Orta Kuşakta bulunmasının kanıtları?',
    triggerWord: 'A - B - C - D',
    correctAnswer: 'Akdeniz İklimi, Batı Rüzgarları, Cephe Yağışı, Dört Mevsim',
    wrongOptions: [
      'Alüvyal Toprak, Bozkır, Çölleşme, Dağlar',
      'Akarsu Rejimi, Buzullar, Çukurova, Deltalar',
      'Aşınım, Birikim, Çernezyom, Depremler'
    ],
    memoryCode: 'Şifre: A-B-C-D (Akdeniz iklimi, Batı rüzgarları, Cephesel yağış, Dört mevsim)',
    subject: 'KPSS Coğrafya',
  ),
  const ReflexQuestion(
    prompt: 'Türkiye\'yi etkileyen yerel rüzgarların yönleri?',
    triggerWord: 'KAYIP - SAKAL',
    correctAnswer: 'Karayel, Yıldız, Poyraz / Samyeli, Kıble, Lodos',
    wrongOptions: [
      'Kıble, Ayaz, Yıldız, Poyraz / Samyeli, Karayel',
      'Karayel, Asor, Poyraz / Sibirya, Kıble, Lodos',
      'Kuzey, Ayaz, Poyraz / Samyeli, Keşişleme, Lodos'
    ],
    memoryCode: 'Şifre: Saat yönünde KAYIP (Kuzeyden soğuk) - SAKAL (Güneyden sıcak)',
    subject: 'KPSS Coğrafya',
  ),
  const ReflexQuestion(
    prompt: 'Türkçede kalıplaştığı için bitişik yazılan bağlaç ki\'ler?',
    triggerWord: 'S O M B A H Ç E M İ',
    correctAnswer: 'Sanki, Oysaki, Mademki, Belki, Halbuki, Çünkü, Meğerki, İllaki',
    wrongOptions: [
      'Sanki, Olur ki, Mademki, Belli ki, Hatta, Çünkü, Meğerki, İllaki',
      'Sonraki, Oysaki, Mademki, Belki, Halbuki, Çokça, Meğerki, İlle de',
      'Sanki, Oysaki, Mademki, Bence, Halbuki, Çünkü, Madem, İllaki'
    ],
    memoryCode: 'Şifre: SOMBAHÇEMİ sözcüklerindeki ki\'ler daima bitişik yazılır!',
    subject: 'KPSS Türkçe & Mantık',
  ),
  const ReflexQuestion(
    prompt: 'Sert ünsüz benzeşmesi (sertleşme) harfleri?',
    triggerWord: 'Fıstıkçı Şahap',
    correctAnswer: 'F, S, T, K, Ç, Ş, H, P',
    wrongOptions: [
      'B, C, D, G, Ğ, J, L, M',
      'F, S, T, R, Ç, Ş, N, P',
      'A, E, I, İ, O, Ö, U, Ü'
    ],
    memoryCode: 'Fıstıkçı Şahap sert ünsüzleriyle biten sözcüğe gelen c,d,g -> ç,t,k olur!',
    subject: 'KPSS Türkçe & Mantık',
  ),
  const ReflexQuestion(
    prompt: 'Tarihte Türk adıyla kurulan ilk devlet ve milli alfabe?',
    triggerWord: 'Türk Adıyla İlk Devlet',
    correctAnswer: 'Göktürkler (Kök Türkler)',
    wrongOptions: ['Asya Hun Devleti', 'Uygurlar', 'Avarlar'],
    memoryCode: 'Bumin Kağan kurdu, 38 harfli Orhun alfabesini kullandı!',
    subject: 'KPSS Tarih',
  ),
  const ReflexQuestion(
    prompt: 'Tarihte Sultan unvanını kullanan ilk Türk hükümdarı?',
    triggerWord: 'İlk Sultan',
    correctAnswer: 'Gazneli Mahmut',
    wrongOptions: ['Tuğrul Bey', 'Sultan Alparslan', 'Yıldırım Bayezid'],
    memoryCode: 'Abbaso Halifesi Şii Büveyhoğullarına karşı koruduğu için vermiştir.',
    subject: 'KPSS Tarih',
  ),
  const ReflexQuestion(
    prompt: 'Anadolu\'yu kesin Türk yurdu yapan 1176 zaferi?',
    triggerWord: 'Yurttutan Savaşı',
    correctAnswer: 'Miryokefalon Savaşı (II. Kılıç Arslan)',
    wrongOptions: ['Malazgirt Savaşı', 'Pasinler Savaşı', 'Kösedağ Savaşı'],
    memoryCode: 'Pasinler (Keşif) -> Malazgirt (Yurtaçan) -> Miryokefalon (Yurttutan)!',
    subject: 'KPSS Tarih',
  ),
  const ReflexQuestion(
    prompt: 'Anadolu Türk siyasi birliğini KESİN sağlayan savaş?',
    triggerWord: '1515 Turnadağ',
    correctAnswer: 'Dulkadiroğulları Beyliği\'nin Alınması',
    wrongOptions: ['Karesioğulları\'nın Alınması', 'Otlukbeli Savaşı', 'Çaldıran Savaşı'],
    memoryCode: 'Yavuz Sultan Selim Turnadağ ile Dulkadiroğullarını sonlandırıp birliği kesinleştirdi.',
    subject: 'KPSS Tarih',
  ),
  const ReflexQuestion(
    prompt: 'I. İnönü Zaferi\'nin iç ve dış sonuçları şifresi?',
    triggerWord: 'M - İ - L - A - T',
    correctAnswer: 'Moskova Ant., İstiklal Marşı, Londra Konf., Afganistan Dostluk, Teşkilat-ı Esasiye',
    wrongOptions: [
      'Mudanya, İttifak, Lozan, Ankara, Teşkilat',
      'Moskova, İzmir İktisat, Lozan, Askeri Birlik, Türkiye',
      'Mondros, İntikam, Londra, Amasya, Tamim'
    ],
    memoryCode: 'Şifre: M-İ-L-A-T (I. İnönü sonrası yaşanan 5 büyük gelişme)',
    subject: 'KPSS Tarih',
  ),
  const ReflexQuestion(
    prompt: 'Doğu sınırımızı sırasıyla çizen 3 antlaşma?',
    triggerWord: 'G - A - K',
    correctAnswer: 'Gümrü -> Moskova -> Kars Antlaşması',
    wrongOptions: [
      'Gümrü -> Ankara -> Kasr-ı Şirin',
      'Girit -> Atina -> Kars',
      'Gence -> Amasya -> Kars'
    ],
    memoryCode: 'G-A-K şifresi! Kars Antlaşması ile Doğu sınırımız KESİN çizilmiştir.',
    subject: 'KPSS Tarih',
  ),
  const ReflexQuestion(
    prompt: 'Balkan Antantı\'na (1934) katılan devletler şifresi?',
    triggerWord: 'T - A - Y - Y - A - R',
    correctAnswer: 'Türkiye, Yunanistan, Yugoslavya, Romanya',
    wrongOptions: [
      'Türkiye, Arnavutluk, Yugoslavya, Rusya',
      'Türkiye, Avusturya, Yunanistan, Romanya',
      'Türkiye, Almanya, Yemen, Rusya'
    ],
    memoryCode: 'Şifre: TAYYAR (Arnavutluk ve Bulgaristan katılmamıştır!)',
    subject: 'KPSS Tarih',
  ),
  const ReflexQuestion(
    prompt: 'Normlar Hiyerarşisinde (Kelsen Piramidi) en üstün belge?',
    triggerWord: 'Kelsen Piramidi Zirvesi',
    correctAnswer: 'Anayasa',
    wrongOptions: ['Kanun', 'Cumhurbaşkanlığı Kararnamesi', 'Milletlerarası Antlaşma'],
    memoryCode: 'Anayasa en üstündür; hiçbir kanun, CBK veya yönetmelik Anayasaya aykırı olamaz!',
    subject: 'KPSS Vatandaşlık & Anayasa',
  ),
  const ReflexQuestion(
    prompt: '1982 Anayasası\'na göre TBMM üye tam sayısı kaçtır?',
    triggerWord: 'TBMM Vekil Sayısı',
    correctAnswer: '600 Milletvekili',
    wrongOptions: ['550 Milletvekili', '450 Milletvekili', '650 Milletvekili'],
    memoryCode: '2017 değişikliği ile milletvekili sayısı 550\'den 600\'e çıkarılmıştır.',
    subject: 'KPSS Vatandaşlık & Anayasa',
  ),
  const ReflexQuestion(
    prompt: 'Cumhurbaşkanı seçilme yaşı ve görev süresi?',
    triggerWord: 'Cumhurbaşkanı Şartları',
    correctAnswer: '40 Yaşını Doldurmuş - 5 Yıl (En çok 2 Dönem)',
    wrongOptions: [
      '30 Yaş - 7 Yıl (Tek Dönem)',
      '35 Yaş - 4 Yıl (Sınırsız)',
      '18 Yaş - 5 Yıl (En çok 3 Dönem)'
    ],
    memoryCode: '40 yaş + yükseköğrenim + 5 yıl + en fazla 2 kez!',
    subject: 'KPSS Vatandaşlık & Anayasa',
  ),
  const ReflexQuestion(
    prompt: 'Türkiye\'nin ilk uzaya çıkan astronotu kimdir?',
    triggerWord: 'İlk Türk Astronot',
    correctAnswer: 'Alper Gezeravcı (Axiom-3)',
    wrongOptions: ['Tuva Cihangir Atasever', 'Vecihi Hürkuş', 'Nuri Demirağ'],
    memoryCode: 'Alper Gezeravcı ISS\'de 13 deney yaptı: "İstikbal göklerdedir!"',
    subject: 'KPSS Güncel Bilgiler',
  ),
  const ReflexQuestion(
    prompt: 'Dünya rezervinin %72\'sine sahip olduğumuz stratejik maden?',
    triggerWord: 'Bor Madeni',
    correctAnswer: 'Balıkesir, Kütahya, Eskişehir, Bursa',
    wrongOptions: [
      'Zonguldak, Karabük, Kastamonu',
      'Artvin, Elazığ, Rize',
      'Muğla, Batman, Adıyaman'
    ],
    memoryCode: 'Bor madeninde dünyada 1. sıradayız; roket yakıtı ve cam sanayiinde kullanılır.',
    subject: 'KPSS Coğrafya',
  ),
  const ReflexQuestion(
    prompt: 'Mimar Sinan\'ın "Ustalık Eserim" dediği ve UNESCO listesindeki cami?',
    triggerWord: 'Ustalık Eseri',
    correctAnswer: 'Edirne Selimiye Camii',
    wrongOptions: [
      'İstanbul Süleymaniye Camii (Kalfalık)',
      'İstanbul Şehzade Camii (Çıraklık)',
      'Sultanahmet Camii (Sedefkar Mehmet Ağa)'
    ],
    memoryCode: 'Çıraklık: Şehzade, Kalfalık: Süleymaniye, Ustalık: Edirne Selimiye!',
    subject: 'KPSS Güncel Bilgiler',
  ),
  const ReflexQuestion(
    prompt: 'Matematikte iki insan arasındaki yaş farkı zaman geçtikçe ne olur?',
    triggerWord: 'Yaş Problemleri Sırrı',
    correctAnswer: 'Asla Değişmez (Daima Sabittir)',
    wrongOptions: [
      'Yıl geçtikçe yaş farkı artar',
      'Yaş farkı ikiye katlanır',
      'Büyüğün lehine azalır'
    ],
    memoryCode: 'İki kişi arasındaki yaş farkı DAİMA SABİTTİR!',
    subject: 'KPSS Matematik',
  ),
  const ReflexQuestion(
    prompt: '0 < a < 1 aralığındaki basit kesir sayılarda karesi ile kendisi kıyası?',
    triggerWord: 'a² < a Kuralı',
    correctAnswer: 'Karesi Kendisinden Küçüktür (a² < a)',
    wrongOptions: [
      'Karesi kendisinden büyüktür (a² > a)',
      'Karesi her zaman 1\'e eşittir',
      'Karesi negatif olur'
    ],
    memoryCode: 'Örnek: a = 1/2 ise a² = 1/4 olur; 1/4 < 1/2!',
    subject: 'KPSS Matematik',
  ),
];

class FastReflexScreen extends ConsumerStatefulWidget {
  const FastReflexScreen({super.key});

  @override
  ConsumerState<FastReflexScreen> createState() => _FastReflexScreenState();
}

class _FastReflexScreenState extends ConsumerState<FastReflexScreen>
    with SingleTickerProviderStateMixin {
  late List<ReflexQuestion> _questions;
  int _currentIndex = 0;
  int _score = 0;
  int _combo = 0;
  int _maxCombo = 0;
  bool _isAnswered = false;
  String? _selectedOption;
  bool _isCorrect = false;

  Timer? _countdownTimer;
  double _timeLeft = 10.0;
  static const double _maxTime = 10.0;

  late List<String> _currentShuffledOptions;

  @override
  void initState() {
    super.initState();
    _questions = List.from(kpssReflexBank)..shuffle();
    _loadCurrentQuestion();
  }

  void _loadCurrentQuestion() {
    final q = _questions[_currentIndex];
    final allOpts = [q.correctAnswer, ...q.wrongOptions];
    allOpts.shuffle();
    _currentShuffledOptions = allOpts;
    _isAnswered = false;
    _selectedOption = null;
    _timeLeft = _maxTime;
    _startTimer();
  }

  void _startTimer() {
    _countdownTimer?.cancel();
    _countdownTimer = Timer.periodic(const Duration(milliseconds: 100), (timer) {
      if (!mounted) return;
      setState(() {
        _timeLeft -= 0.1;
        if (_timeLeft <= 0.0) {
          _timeLeft = 0.0;
          _onTimeUp();
        }
      });
    });
  }

  void _onTimeUp() {
    _countdownTimer?.cancel();
    HapticFeedback.heavyImpact();
    SoundService.playIncorrect();
    setState(() {
      _isAnswered = true;
      _isCorrect = false;
      _combo = 0;
    });
  }

  void _onOptionSelected(String opt) {
    if (_isAnswered) return;
    _countdownTimer?.cancel();

    final q = _questions[_currentIndex];
    final isRight = (opt == q.correctAnswer);

    if (isRight) {
      HapticFeedback.mediumImpact();
      SoundService.playCorrect();
      _combo++;
      if (_combo > _maxCombo) _maxCombo = _combo;
      final speedBonus = (_timeLeft * 10).toInt();
      _score += 100 + (_combo * 20) + speedBonus;
      ref.read(userProfileProvider.notifier).addGems(2);
    } else {
      HapticFeedback.heavyImpact();
      SoundService.playIncorrect();
      _combo = 0;
    }

    setState(() {
      _isAnswered = true;
      _selectedOption = opt;
      _isCorrect = isRight;
    });
  }

  void _nextQuestion() {
    if (_currentIndex < _questions.length - 1) {
      setState(() {
        _currentIndex++;
      });
      _loadCurrentQuestion();
    } else {
      _showGameOverModal();
    }
  }

  void _showGameOverModal() {
    _countdownTimer?.cancel();
    SoundService.playComplete();

    // Pratik ödülü olarak +1 Can kazandır
    ref.read(userProfileProvider.notifier).gainHeart();
    ref.read(userProfileProvider.notifier).addGems(15);

    showModalBottomSheet(
      context: context,
      isDismissible: false,
      enableDrag: false,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
      ),
      builder: (ctx) => Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text(
              '🎉 TEBRİKLER ŞAMPİYON! 🎉',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: Color(0xFF10B981)),
            ),
            const SizedBox(height: 12),
            Text(
              'Görünce Yapıştır refleks serisini tamamladın!\nToplam Skor: $_score\nMaksimum Kombo: $_maxCombo 🔥',
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w600, color: Color(0xFF4B4B4B)),
            ),
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: const Color(0xFFDCFCE7),
                borderRadius: BorderRadius.circular(16),
              ),
              child: const Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(Icons.favorite_rounded, color: Color(0xFFFF4B4B), size: 28),
                  SizedBox(width: 8),
                  Text(
                    '+1 Can ve +15 Elmas Kazandın!',
                    style: TextStyle(fontWeight: FontWeight.w900, color: Color(0xFF15803D)),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            DuoButton(
              text: 'ANA SAYFAYA DÖN',
              color: DuoButtonColor.green,
              onPressed: () {
                Navigator.of(ctx).pop();
                Navigator.of(context).pop();
              },
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _countdownTimer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final q = _questions[_currentIndex];
    final progressRatio = _timeLeft / _maxTime;

    return Scaffold(
      backgroundColor: const Color(0xFF0F172A), // Gece modunda odaklanma zemini
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.close_rounded, color: Colors.white, size: 28),
          onPressed: () => Navigator.of(context).pop(),
        ),
        title: Row(
          children: [
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
              decoration: BoxDecoration(
                color: const Color(0xFFF59E0B),
                borderRadius: BorderRadius.circular(12),
              ),
              child: const Row(
                children: [
                  Icon(Icons.bolt_rounded, color: Colors.white, size: 18),
                  SizedBox(width: 4),
                  Text(
                    'GÖRÜNCE YAPIŞTIR! ⚡',
                    style: TextStyle(color: Colors.white, fontWeight: FontWeight.w900, fontSize: 13),
                  ),
                ],
              ),
            ),
            const Spacer(),
            if (_combo > 1)
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  gradient: const LinearGradient(colors: [Color(0xFFEF4444), Color(0xFFF97316)]),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Text(
                  '🔥 ${_combo}x KOMBO',
                  style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900, fontSize: 12),
                ),
              ),
          ],
        ),
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // Geri Sayım Barı
              ClipRRect(
                borderRadius: BorderRadius.circular(8),
                child: SizedBox(
                  height: 10,
                  child: LinearProgressIndicator(
                    value: progressRatio,
                    backgroundColor: Colors.white.withOpacity(0.15),
                    valueColor: AlwaysStoppedAnimation<Color>(
                      progressRatio > 0.4
                          ? const Color(0xFF10B981)
                          : (progressRatio > 0.2 ? const Color(0xFFF59E0B) : const Color(0xFFEF4444)),
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 14),

              // Branş & Soru No
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    q.subject.toUpperCase(),
                    style: const TextStyle(
                      color: Color(0xFF94A3B8),
                      fontWeight: FontWeight.w800,
                      fontSize: 12,
                      letterSpacing: 0.8,
                    ),
                  ),
                  Text(
                    'Skor: $_score',
                    style: const TextStyle(
                      color: Color(0xFF38BDF8),
                      fontWeight: FontWeight.w900,
                      fontSize: 15,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),

              // Tetikleyici Şifre / Anahtar Kelime Kartı
              Container(
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  gradient: const LinearGradient(
                    colors: [Color(0xFF1E293B), Color(0xFF334155)],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(24),
                  border: Border.all(color: const Color(0xFF475569), width: 1.5),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.3),
                      blurRadius: 12,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Column(
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                      decoration: BoxDecoration(
                        color: const Color(0xFFE2E8F0).withOpacity(0.12),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Text(
                        '🔑 TETİKLEYİCİ ŞİFRE: "${q.triggerWord}"',
                        style: const TextStyle(
                          color: Color(0xFFFCD34D),
                          fontWeight: FontWeight.w900,
                          fontSize: 14,
                        ),
                      ),
                    ),
                    const SizedBox(height: 14),
                    Text(
                      q.prompt,
                      textAlign: TextAlign.center,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 18,
                        fontWeight: FontWeight.w900,
                        height: 1.35,
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 20),

              // Seçenek Butonları (Yıldırım Refleksi)
              Expanded(
                child: ListView.separated(
                  physics: const BouncingScrollPhysics(),
                  itemCount: _currentShuffledOptions.length,
                  separatorBuilder: (context, index) => const SizedBox(height: 10),
                  itemBuilder: (ctx, idx) {
                    final opt = _currentShuffledOptions[idx];
                    Color btnColor = const Color(0xFF1E293B);
                    Color borderColor = const Color(0xFF475569);
                    Color textColor = Colors.white;

                    if (_isAnswered) {
                      if (opt == q.correctAnswer) {
                        btnColor = const Color(0xFF059669);
                        borderColor = const Color(0xFF34D399);
                      } else if (opt == _selectedOption) {
                        btnColor = const Color(0xFFDC2626);
                        borderColor = const Color(0xFFF87171);
                      }
                    }

                    return InkWell(
                      onTap: _isAnswered ? null : () => _onOptionSelected(opt),
                      borderRadius: BorderRadius.circular(18),
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 200),
                        padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 16),
                        decoration: BoxDecoration(
                          color: btnColor,
                          borderRadius: BorderRadius.circular(18),
                          border: Border.all(color: borderColor, width: 2),
                          boxShadow: [
                            BoxShadow(
                              color: btnColor.withOpacity(0.3),
                              blurRadius: 6,
                              offset: const Offset(0, 3),
                            ),
                          ],
                        ),
                        child: Row(
                          children: [
                            Container(
                              width: 28,
                              height: 28,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                color: Colors.white.withOpacity(0.12),
                              ),
                              alignment: Alignment.center,
                              child: Text(
                                String.fromCharCode(65 + idx),
                                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900),
                              ),
                            ),
                            const SizedBox(width: 14),
                            Expanded(
                              child: Text(
                                opt,
                                style: TextStyle(
                                  color: textColor,
                                  fontSize: 15,
                                  fontWeight: FontWeight.w800,
                                ),
                              ),
                            ),
                            if (_isAnswered && opt == q.correctAnswer)
                              const Icon(Icons.check_circle_rounded, color: Colors.white, size: 24),
                            if (_isAnswered && opt == _selectedOption && !_isCorrect)
                              const Icon(Icons.cancel_rounded, color: Colors.white, size: 24),
                          ],
                        ),
                      ),
                    );
                  },
                ),
              ),

              // Geri Bildirim ve Hafıza Şifresi Alanı
              if (_isAnswered) ...[
                Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    color: _isCorrect ? const Color(0xFF065F46) : const Color(0xFF7F1D1D),
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Row(
                    children: [
                      Icon(
                        _isCorrect ? Icons.emoji_events_rounded : Icons.lightbulb_rounded,
                        color: const Color(0xFFFDE047),
                        size: 26,
                      ),
                      const SizedBox(width: 10),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              _isCorrect ? 'HARİKA REFLEKS! 🎯' : 'ÖSYM HAFIZA ŞİFRESİ 💡',
                              style: const TextStyle(
                                color: Colors.white,
                                fontWeight: FontWeight.w900,
                                fontSize: 13,
                              ),
                            ),
                            const SizedBox(height: 2),
                            Text(
                              q.memoryCode,
                              style: const TextStyle(
                                color: Color(0xFFF1F5F9),
                                fontSize: 12.5,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 12),
                DuoButton(
                  text: (_currentIndex < _questions.length - 1) ? 'SIRADAKİ ŞİFREYE GEÇ ⚡' : 'SONUÇLARI GÖR 🏆',
                  color: DuoButtonColor.green,
                  onPressed: _nextQuestion,
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}
