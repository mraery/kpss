import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../services/sound_service.dart';
import '../widgets/duo_button.dart';
import 'fast_reflex_screen.dart';
import 'flashcards_screen.dart';

class SplashMascotScreen extends StatefulWidget {
  const SplashMascotScreen({super.key});

  static void show(BuildContext context) {
    Navigator.of(context).push(
      PageRouteBuilder(
        opaque: true,
        transitionDuration: const Duration(milliseconds: 350),
        pageBuilder: (context, anim, secAnim) => const SplashMascotScreen(),
        transitionsBuilder: (context, animation, secAnim, child) {
          return FadeTransition(opacity: animation, child: child);
        },
      ),
    );
  }

  @override
  State<SplashMascotScreen> createState() => _SplashMascotScreenState();
}

class _SplashMascotScreenState extends State<SplashMascotScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _bounceController;
  late Animation<double> _bounceAnimation;

  final List<String> _parrotTips = [
    'ÖSYM Şifresi: BM Güvenlik Konseyi veto ülkeleri -> FİRÇA! 💡',
    'Unutma: 1176 Miryokefalon Anadolu\'yu kesin Türk yurdu yaptı! ⚔️',
    'Taktik: Paragrafı ikiye bölme sorularında yeni düşüncenin başladığı cümleyi ara! 🎯',
    'Tarihte Türk adıyla kurulan ilk devlet Göktürklerdir! 🏹',
    'Rüzgarlar saat yönünde KAYIP - SAKAL şeklinde eser! 💨',
    'Cumhurbaşkanı seçilme yaşı 40, TBMM milletvekili yaşı 18\'dir! 🏛️',
    'Doğu sınırımızı sırasıyla çizen antlaşmalar: G-A-K! 🇹🇷',
  ];

  late String _currentQuote;

  @override
  void initState() {
    super.initState();
    _currentQuote = _parrotTips[Random().nextInt(_parrotTips.length)];

    _bounceController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1400),
    )..repeat(reverse: true);

    _bounceAnimation = Tween<double>(begin: -8.0, end: 8.0).animate(
      CurvedAnimation(parent: _bounceController, curve: Curves.easeInOut),
    );

    WidgetsBinding.instance.addPostFrameCallback((_) {
      SoundService.playCorrect();
    });
  }

  void _onParrotTap() {
    HapticFeedback.mediumImpact();
    SoundService.playFlip();
    setState(() {
      _currentQuote = _parrotTips[Random().nextInt(_parrotTips.length)];
    });
  }

  @override
  void dispose() {
    _bounceController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    return Scaffold(
      body: Container(
        width: double.infinity,
        height: double.infinity,
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [
              Color(0xFF0284C7), // KPSS Mavi
              Color(0xFF0369A1),
              Color(0xFF0C4A6E),
            ],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: Column(
            children: [
              // Üst Kapatma Butonu & Başlık
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.18),
                        borderRadius: BorderRadius.circular(16),
                      ),
                      child: const Row(
                        children: [
                          Icon(Icons.workspace_premium_rounded, color: Color(0xFFFBBF24), size: 20),
                          SizedBox(width: 6),
                          Text(
                            'KPSS QUEST RESMİ MASKOTU',
                            style: TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.w900,
                              fontSize: 11,
                              letterSpacing: 0.8,
                            ),
                          ),
                        ],
                      ),
                    ),
                    IconButton(
                      icon: const Icon(Icons.close_rounded, color: Colors.white, size: 28),
                      onPressed: () => Navigator.of(context).pop(),
                    ),
                  ],
                ),
              ),

              const Spacer(flex: 1),

              // Papağan Konuşma Balonu
              GestureDetector(
                onTap: _onParrotTap,
                child: Container(
                  margin: const EdgeInsets.symmetric(horizontal: 28),
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(24),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.20),
                        blurRadius: 16,
                        offset: const Offset(0, 6),
                      ),
                    ],
                  ),
                  child: Column(
                    children: [
                      const Text(
                        '🦜 ZEKI PAŞA DİYOR Kİ: (Dokun & Değiş)',
                        style: TextStyle(
                          color: Color(0xFF0284C7),
                          fontWeight: FontWeight.w900,
                          fontSize: 12,
                          letterSpacing: 0.5,
                        ),
                      ),
                      const SizedBox(height: 6),
                      Text(
                        _currentQuote,
                        textAlign: TextAlign.center,
                        style: const TextStyle(
                          color: Color(0xFF1E293B),
                          fontWeight: FontWeight.w800,
                          fontSize: 15,
                          height: 1.35,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              const SizedBox(height: 18),

              // TAM EKRAN RENKLİ PAPAĞAN MASKOTU (Hero)
              AnimatedBuilder(
                animation: _bounceAnimation,
                builder: (context, child) {
                  return Transform.translate(
                    offset: Offset(0, _bounceAnimation.value),
                    child: child,
                  );
                },
                child: GestureDetector(
                  onTap: _onParrotTap,
                  child: Container(
                    width: min(size.width * 0.72, 300),
                    height: min(size.width * 0.72, 300),
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      boxShadow: [
                        BoxShadow(
                          color: const Color(0xFF10B981).withOpacity(0.35),
                          blurRadius: 32,
                          spreadRadius: 6,
                          offset: const Offset(0, 8),
                        ),
                        BoxShadow(
                          color: const Color(0xFFF59E0B).withOpacity(0.25),
                          blurRadius: 20,
                          spreadRadius: 2,
                        ),
                      ],
                      border: Border.all(color: Colors.white.withOpacity(0.9), width: 4),
                    ),
                    child: ClipOval(
                      child: Image.asset(
                        'assets/images/mascot_parrot.jpg',
                        fit: BoxFit.cover,
                      ),
                    ),
                  ),
                ),
              ),

              const SizedBox(height: 16),

              // Başlık & Alt Bilgi
              const Text(
                'Zeki Paşa 🦜',
                style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.w900,
                  fontSize: 28,
                  letterSpacing: 0.5,
                ),
              ),
              const SizedBox(height: 4),
              const Text(
                '2.580+ ÖSYM Sorusu • 86 Ünite • Akıllı Şifreler',
                style: TextStyle(
                  color: Color(0xFFE0F2FE),
                  fontWeight: FontWeight.w700,
                  fontSize: 14,
                ),
              ),

              const Spacer(flex: 2),

              // Hızlı Başlat Butonları
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 24),
                child: Column(
                  children: [
                    DuoButton(
                      text: 'GÖRÜNCE YAPIŞTIR! OYNA ⚡',
                      color: DuoButtonColor.green,
                      onPressed: () {
                        Navigator.of(context).pushReplacement(
                          MaterialPageRoute(builder: (_) => const FastReflexScreen()),
                        );
                      },
                    ),
                    const SizedBox(height: 12),
                    Row(
                      children: [
                        Expanded(
                          child: DuoButton(
                            text: 'KARTLAR 🎴',
                            color: DuoButtonColor.purple,
                            onPressed: () {
                              Navigator.of(context).pushReplacement(
                                MaterialPageRoute(builder: (_) => const FlashcardsScreen()),
                              );
                            },
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: DuoButton(
                            text: 'DERSLER 📚',
                            color: DuoButtonColor.blue,
                            onPressed: () => Navigator.of(context).pop(),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),
            ],
          ),
        ),
      ),
    );
  }
}
