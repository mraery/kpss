import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/lesson_models.dart';
import '../providers/game_provider.dart';
import '../services/sound_service.dart';
import '../widgets/duo_button.dart';
import '../widgets/parrot_mascot_widget.dart';

import '../data/kpss_flashcards.dart';

final List<Flashcard> defaultFlashcards = kpssFlashcards;

class FlashcardsScreen extends ConsumerStatefulWidget {
  final List<Flashcard>? customDeck;

  const FlashcardsScreen({super.key, this.customDeck});

  @override
  ConsumerState<FlashcardsScreen> createState() => _FlashcardsScreenState();
}

class _FlashcardsScreenState extends ConsumerState<FlashcardsScreen>
    with SingleTickerProviderStateMixin {
  late List<Flashcard> _deck;
  int _currentIndex = 0;
  bool _isFlipped = false;
  final Set<String> _learnedCardIds = {};
  final Set<String> _reviewCardIds = {};

  // Branş Filtresi
  String _selectedFilterSubject = 'Tümü';
  final List<String> _filterSubjects = const [
    'Tümü',
    'KPSS Tarih',
    'KPSS Coğrafya',
    'KPSS Vatandaşlık & Anayasa',
    'KPSS Güncel Bilgiler',
    'KPSS Türkçe & Mantık',
    'KPSS Matematik',
  ];

  // 3D Flip Animasyonu
  late AnimationController _flipController;
  late Animation<double> _flipAnimation;

  // Drag & Swipe Durumu
  double _dragOffset = 0.0;
  bool _isFinished = false;

  void _onSelectFilterSubject(String subj) {
    setState(() {
      _selectedFilterSubject = subj;
      final base = (widget.customDeck ?? defaultFlashcards);
      if (subj == 'Tümü') {
        _deck = List.from(base)..shuffle();
      } else {
        _deck = base.where((c) => c.subject == subj).toList()..shuffle();
        if (_deck.isEmpty) {
          _deck = List.from(base)..shuffle();
        }
      }
      _currentIndex = 0;
      _isFlipped = false;
      _isFinished = false;
      _dragOffset = 0.0;
      _learnedCardIds.clear();
      _reviewCardIds.clear();
      _flipController.reset();
    });
  }

  @override
  void initState() {
    super.initState();
    _deck = List.from(widget.customDeck ?? defaultFlashcards)..shuffle();

    _flipController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 380),
    );

    _flipAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _flipController, curve: Curves.easeInOut),
    )..addListener(() {
        setState(() {});
      });
  }

  @override
  void dispose() {
    _flipController.dispose();
    super.dispose();
  }

  void _toggleFlip() {
    HapticFeedback.lightImpact();
    SoundService.playFlip();
    if (_isFlipped) {
      _flipController.reverse();
    } else {
      _flipController.forward();
    }
    _isFlipped = !_isFlipped;
  }

  void _onSwipe(bool isLearned) {
    if (_currentIndex >= _deck.length) return;

    final currentCard = _deck[_currentIndex];
    HapticFeedback.mediumImpact();

    if (isLearned) {
      SoundService.playCorrect();
    } else {
      SoundService.playIncorrect();
    }

    setState(() {
      if (isLearned) {
        _learnedCardIds.add(currentCard.id);
        _reviewCardIds.remove(currentCard.id);
      } else {
        _reviewCardIds.add(currentCard.id);
        _learnedCardIds.remove(currentCard.id);
      }

      // Animasyonu sıfırla
      if (_isFlipped) {
        _flipController.reset();
        _isFlipped = false;
      }
      _dragOffset = 0.0;

      if (_currentIndex + 1 >= _deck.length) {
        _isFinished = true;
        SoundService.playComplete();
        // Tamamlandı, ödül ver
        ref.read(userProfileProvider.notifier).recordLessonAttempt(
              Lesson(
                id: 'flashcards_complete_${DateTime.now().millisecondsSinceEpoch}',
                title: 'Kartlarla Pekiştir',
                description: 'Flaş kart tamamlama',
                xpReward: 35,
                gemReward: 12,
                questions: const [],
              ),
              100.0,
            );
      } else {
        _currentIndex++;
      }
    });
  }

  void _restartDeck({bool onlyReview = false}) {
    setState(() {
      final base = (widget.customDeck ?? defaultFlashcards);
      final filteredBase = _selectedFilterSubject == 'Tümü'
          ? base
          : base.where((c) => c.subject == _selectedFilterSubject).toList();
      if (onlyReview && _reviewCardIds.isNotEmpty) {
        _deck = filteredBase
            .where((fc) => _reviewCardIds.contains(fc.id))
            .toList()
          ..shuffle();
      } else {
        _deck = List.from(filteredBase.isEmpty ? base : filteredBase)..shuffle();
      }
      _currentIndex = 0;
      _isFlipped = false;
      _isFinished = false;
      _dragOffset = 0.0;
      _learnedCardIds.clear();
      _reviewCardIds.clear();
      _flipController.reset();
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_isFinished) {
      return _buildFinishedScreen();
    }

    final currentCard = _deck[_currentIndex];
    final progress = (_currentIndex + 1) / _deck.length;

    return Scaffold(
      backgroundColor: const Color(0xFFF9FAFB),
      appBar: AppBar(
        backgroundColor: Colors.white,
        elevation: 0,
        title: const Text(
          'Kartlarla Pekiştir 🎴',
          style: TextStyle(fontWeight: FontWeight.w900, fontSize: 19),
        ),
        leading: IconButton(
          icon: const Icon(Icons.close_rounded, color: Color(0xFF4B4B4B), size: 26),
          onPressed: () => Navigator.of(context).pop(),
        ),
        actions: [
          // Öğrenilen / Tekrar sayaçları
          Padding(
            padding: const EdgeInsets.only(right: 16),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: const Color(0xFFE8F5E9),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Row(
                    children: [
                      const Icon(Icons.check_circle_rounded, color: Color(0xFF2E7D32), size: 16),
                      const SizedBox(width: 4),
                      Text(
                        '${_learnedCardIds.length}',
                        style: const TextStyle(
                          color: Color(0xFF2E7D32),
                          fontWeight: FontWeight.w800,
                          fontSize: 13,
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 6),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: const Color(0xFFFFEBEE),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Row(
                    children: [
                      const Icon(Icons.replay_rounded, color: Color(0xFFC62828), size: 16),
                      const SizedBox(width: 4),
                      Text(
                        '${_reviewCardIds.length}',
                        style: const TextStyle(
                          color: Color(0xFFC62828),
                          fontWeight: FontWeight.w800,
                          fontSize: 13,
                        ),
                      ),
                    ],
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
            // Branş Filtreleme Çubuğu
            Container(
              height: 48,
              padding: const EdgeInsets.symmetric(vertical: 6),
              decoration: const BoxDecoration(
                color: Colors.white,
                border: Border(bottom: BorderSide(color: Color(0xFFF1ECE4), width: 1)),
              ),
              child: ListView.separated(
                scrollDirection: Axis.horizontal,
                padding: const EdgeInsets.symmetric(horizontal: 16),
                itemCount: _filterSubjects.length,
                separatorBuilder: (context, index) => const SizedBox(width: 8),
                itemBuilder: (context, index) {
                  final subj = _filterSubjects[index];
                  final isSelected = _selectedFilterSubject == subj;
                  return InkWell(
                    onTap: () => _onSelectFilterSubject(subj),
                    borderRadius: BorderRadius.circular(16),
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 180),
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: isSelected ? const Color(0xFF7C3AED) : const Color(0xFFF3F4F6),
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(
                          color: isSelected ? const Color(0xFF6D28D9) : const Color(0xFFE5E7EB),
                          width: 1,
                        ),
                      ),
                      child: Center(
                        child: Text(
                          subj,
                          style: TextStyle(
                            color: isSelected ? Colors.white : const Color(0xFF4B5563),
                            fontWeight: isSelected ? FontWeight.w800 : FontWeight.w600,
                            fontSize: 12,
                          ),
                        ),
                      ),
                    ),
                  );
                },
              ),
            ),

            // İlerleme Barı
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
              child: Row(
                children: [
                  Expanded(
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(8),
                      child: LinearProgressIndicator(
                        value: progress,
                        minHeight: 10,
                        backgroundColor: const Color(0xFFE5E7EB),
                        valueColor: const AlwaysStoppedAnimation<Color>(Color(0xFF7C3AED)),
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Text(
                    '${_currentIndex + 1} / ${_deck.length}',
                    style: const TextStyle(
                      fontWeight: FontWeight.w800,
                      color: Color(0xFF6B7280),
                      fontSize: 13,
                    ),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 8),

            // Kart Alanı (Swipeable & 3D Flip)
            Expanded(
              child: Center(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                  child: GestureDetector(
                    onHorizontalDragUpdate: (details) {
                      setState(() {
                        _dragOffset += details.primaryDelta!;
                      });
                    },
                    onHorizontalDragEnd: (details) {
                      if (_dragOffset > 90) {
                        // Sağa atıldı ➔ Öğrendim
                        _onSwipe(true);
                      } else if (_dragOffset < -90) {
                        // Sola atıldı ➔ Tekrar Çalış
                        _onSwipe(false);
                      } else {
                        // Merkeze geri dön
                        setState(() {
                          _dragOffset = 0.0;
                        });
                      }
                    },
                    onTap: _toggleFlip,
                    child: Transform.translate(
                      offset: Offset(_dragOffset, 0),
                      child: Transform.rotate(
                        angle: (_dragOffset / 300) * 0.15,
                        child: _buildFlipCard(currentCard),
                      ),
                    ),
                  ),
                ),
              ),
            ),

            // Alt Butonlar (Sola At & Sağa At)
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
              decoration: const BoxDecoration(
                color: Colors.white,
                border: Border(top: BorderSide(color: Color(0xFFE5E7EB), width: 1.5)),
              ),
              child: Row(
                children: [
                  // Sola At Butonu (Tekrar Çalış)
                  Expanded(
                    child: DuoButton(
                      text: '👈 TEKRAR ÇALIŞ',
                      color: DuoButtonColor.red,
                      height: 52,
                      onPressed: () => _onSwipe(false),
                    ),
                  ),
                  const SizedBox(width: 14),
                  // Sağa At Butonu (Öğrendim)
                  Expanded(
                    child: DuoButton(
                      text: 'ÖĞRENDİM 👉',
                      color: DuoButtonColor.green,
                      height: 52,
                      onPressed: () => _onSwipe(true),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildFlipCard(Flashcard card) {
    final angle = _flipAnimation.value * pi;
    final isBack = angle >= pi / 2;

    return Stack(
      children: [
        Transform(
          alignment: Alignment.center,
          transform: Matrix4.identity()
            ..setEntry(3, 2, 0.001)
            ..rotateY(angle),
          child: isBack
              ? Transform(
                  alignment: Alignment.center,
                  transform: Matrix4.identity()..rotateY(pi),
                  child: _buildCardBack(card),
                )
              : _buildCardFront(card),
        ),

        // Sola kaydırırken çıkan kırmızı "TEKRAR ET" rozeti
        if (_dragOffset < -20)
          Positioned(
            top: 24,
            right: 24,
            child: Opacity(
              opacity: min(1.0, (-_dragOffset / 120)),
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                decoration: BoxDecoration(
                  color: const Color(0xFFEF4444),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: Colors.white, width: 2),
                ),
                child: const Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.replay_rounded, color: Colors.white, size: 20),
                    SizedBox(width: 6),
                    Text(
                      'TEKRAR ÇALIŞ',
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.w900,
                        fontSize: 14,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),

        // Sağa kaydırırken çıkan yeşil "ÖĞRENDİM" rozeti
        if (_dragOffset > 20)
          Positioned(
            top: 24,
            left: 24,
            child: Opacity(
              opacity: min(1.0, (_dragOffset / 120)),
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                decoration: BoxDecoration(
                  color: const Color(0xFF10B981),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: Colors.white, width: 2),
                ),
                child: const Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.check_circle_rounded, color: Colors.white, size: 20),
                    SizedBox(width: 6),
                    Text(
                      'ÖĞRENDİM',
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.w900,
                        fontSize: 14,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
      ],
    );
  }

  // Kart Ön Yüzü (Kelime / Kavram)
  Widget _buildCardFront(Flashcard card) {
    Color subjectColor;
    if (card.subject.contains('Biyoloji')) {
      subjectColor = const Color(0xFF10B981);
    } else if (card.subject.contains('Matematik')) {
      subjectColor = const Color(0xFF1CB0F6);
    } else if (card.subject.contains('Fizik')) {
      subjectColor = const Color(0xFF7C3AED);
    } else if (card.subject.contains('Kimya')) {
      subjectColor = const Color(0xFFEC4899);
    } else if (card.subject.contains('Türkçe')) {
      subjectColor = const Color(0xFFEA580C);
    } else if (card.subject.contains('Edebiyat')) {
      subjectColor = const Color(0xFFB91C1C);
    } else if (card.subject.contains('Tarih')) {
      subjectColor = const Color(0xFFFF9600);
    } else if (card.subject.contains('Coğrafya')) {
      subjectColor = const Color(0xFF14B8A6);
    } else if (card.subject.contains('Felsefe')) {
      subjectColor = const Color(0xFF6366F1);
    } else if (card.subject.contains('Din')) {
      subjectColor = const Color(0xFF047857);
    } else {
      subjectColor = const Color(0xFF58CC02);
    }

    return Container(
      width: double.infinity,
      height: double.infinity,
      constraints: const BoxConstraints(maxHeight: 460),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: const Color(0xFFE5E7EB), width: 2),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.06),
            blurRadius: 16,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // Ders ve Kategori Rozeti
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
            decoration: BoxDecoration(
              color: subjectColor.withOpacity(0.12),
              borderRadius: BorderRadius.circular(20),
            ),
            child: Text(
              '${card.subject} • ${card.category ?? "YKS Temel"}',
              style: TextStyle(
                color: subjectColor,
                fontWeight: FontWeight.w900,
                fontSize: 13,
                letterSpacing: 0.5,
              ),
            ),
          ),

          const Spacer(),

          // Kart İkonu
          Container(
            width: 80,
            height: 80,
            decoration: BoxDecoration(
              color: subjectColor.withOpacity(0.1),
              shape: BoxShape.circle,
            ),
            child: Icon(
              Icons.style_rounded,
              size: 42,
              color: subjectColor,
            ),
          ),

          const SizedBox(height: 20),

          // Kelime / Kavram
          Text(
            card.term,
            textAlign: TextAlign.center,
            style: const TextStyle(
              fontSize: 28,
              fontWeight: FontWeight.w900,
              color: Color(0xFF1F2937),
              letterSpacing: -0.5,
            ),
          ),

          const Spacer(),

          // İpucu
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            decoration: BoxDecoration(
              color: const Color(0xFFF3F4F6),
              borderRadius: BorderRadius.circular(20),
            ),
            child: const Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(Icons.touch_app_rounded, size: 18, color: Color(0xFF6B7280)),
                SizedBox(width: 6),
                Text(
                  'Kartı çevirmek için dokun',
                  style: TextStyle(
                    fontSize: 13,
                    color: Color(0xFF6B7280),
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  // Kart Arka Yüzü (Anlam & Taktik)
  Widget _buildCardBack(Flashcard card) {
    return Container(
      width: double.infinity,
      height: double.infinity,
      constraints: const BoxConstraints(maxHeight: 460),
      padding: const EdgeInsets.all(22),
      decoration: BoxDecoration(
        color: const Color(0xFFFAF5FF), // Hafif Mor arka plan
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: const Color(0xFFD8B4FE), width: 2),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFF7C3AED).withOpacity(0.08),
            blurRadius: 16,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Üst Başlık & Çevir Simgesi
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  card.term,
                  style: const TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.w900,
                    color: Color(0xFF6B21A8),
                  ),
                ),
                Container(
                  padding: const EdgeInsets.all(6),
                  decoration: BoxDecoration(
                    color: const Color(0xFFEDE9FE),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: const Icon(
                    Icons.flip_camera_android_rounded,
                    size: 18,
                    color: Color(0xFF7C3AED),
                  ),
                ),
              ],
            ),

            const SizedBox(height: 12),
            const Divider(color: Color(0xFFE9D5FF), height: 1),
            const SizedBox(height: 12),

            // Anlam & Tanım
            const Text(
              'AÇIKLAMA / TANIM:',
              style: TextStyle(
                fontSize: 11,
                fontWeight: FontWeight.w900,
                color: Color(0xFF9333EA),
                letterSpacing: 0.8,
              ),
            ),
            const SizedBox(height: 6),
            Text(
              card.meaning,
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w600,
                color: Color(0xFF374151),
                height: 1.45,
              ),
            ),

            if (card.example != null) ...[
              const SizedBox(height: 14),
              const Text(
                'ÖRNEK:',
                style: TextStyle(
                  fontSize: 11,
                  fontWeight: FontWeight.w900,
                  color: Color(0xFF2563EB),
                  letterSpacing: 0.8,
                ),
              ),
              const SizedBox(height: 4),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: const Color(0xFFEFF6FF),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: const Color(0xFFBFDBFE)),
                ),
                child: Text(
                  card.example!,
                  style: const TextStyle(
                    fontSize: 13,
                    color: Color(0xFF1E40AF),
                    fontWeight: FontWeight.w600,
                    height: 1.35,
                  ),
                ),
              ),
            ],

            if (card.examTip != null) ...[
              const SizedBox(height: 12),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: const Color(0xFFFFFBEB),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: const Color(0xFFFDE68A)),
                ),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text('💡 ', style: TextStyle(fontSize: 16)),
                    Expanded(
                      child: Text(
                        card.examTip!,
                        style: const TextStyle(
                          fontSize: 12.5,
                          fontWeight: FontWeight.w700,
                          color: Color(0xFF92400E),
                          height: 1.35,
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
    );
  }

  // Deste Bittiğinde Kutlama Ekranı
  Widget _buildFinishedScreen() {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Spacer(),

              // Papağan Kutlama
              const ParrotMascotWidget(
                size: 130,
                mood: ParrotMood.happy,
                speechText: 'Harika iş çıkardın! Kartları pekiştirdin! 🎉',
              ),

              const SizedBox(height: 24),

              const Text(
                'Deste Tamamlandı!',
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.w900,
                  color: Color(0xFF10B981),
                ),
              ),

              const SizedBox(height: 8),

              Text(
                'Toplam ${_deck.length} kart üzerinden ${_learnedCardIds.length} tanesini öğrendin.',
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontSize: 15,
                  color: Color(0xFF6B7280),
                  fontWeight: FontWeight.w600,
                ),
              ),

              const SizedBox(height: 28),

              // Durum Kartları
              Row(
                children: [
                  Expanded(
                    child: Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: const Color(0xFFECFDF5),
                        borderRadius: BorderRadius.circular(18),
                        border: Border.all(color: const Color(0xFFA7F3D0)),
                      ),
                      child: Column(
                        children: [
                          const Icon(Icons.check_circle_rounded, color: Color(0xFF059669), size: 28),
                          const SizedBox(height: 6),
                          Text(
                            '${_learnedCardIds.length}',
                            style: const TextStyle(
                              fontSize: 24,
                              fontWeight: FontWeight.w900,
                              color: Color(0xFF059669),
                            ),
                          ),
                          const Text(
                            'ÖĞRENİLDİ',
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.w800,
                              color: Color(0xFF047857),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: const Color(0xFFFEF2F2),
                        borderRadius: BorderRadius.circular(18),
                        border: Border.all(color: const Color(0xFFFECACA)),
                      ),
                      child: Column(
                        children: [
                          const Icon(Icons.replay_rounded, color: Color(0xFFDC2626), size: 28),
                          const SizedBox(height: 6),
                          Text(
                            '${_reviewCardIds.length}',
                            style: const TextStyle(
                              fontSize: 24,
                              fontWeight: FontWeight.w900,
                              color: Color(0xFFDC2626),
                            ),
                          ),
                          const Text(
                            'TEKRAR EDİLECEK',
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.w800,
                              color: Color(0xFFB91C1C),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),

              const Spacer(),

              // Tekrar Çalış ve Çıkış Butonları
              if (_reviewCardIds.isNotEmpty) ...[
                DuoButton(
                  text: 'TEKRAR EDİLECEKLERİ ÇÖZ (${_reviewCardIds.length})',
                  color: DuoButtonColor.blue,
                  height: 52,
                  onPressed: () => _restartDeck(onlyReview: true),
                ),
                const SizedBox(height: 10),
              ],

              DuoButton(
                text: 'TÜMÜNÜ YENİDEN BAŞLAT',
                color: DuoButtonColor.green,
                height: 52,
                onPressed: () => _restartDeck(onlyReview: false),
              ),

              const SizedBox(height: 10),

              TextButton(
                onPressed: () => Navigator.of(context).pop(),
                child: const Text(
                  'Pratiğe Dön',
                  style: TextStyle(
                    fontWeight: FontWeight.w800,
                    color: Color(0xFF6B7280),
                    fontSize: 15,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
