# -*- coding: utf-8 -*-
with open('lib/screens/flashcards_screen.dart', 'r', encoding='utf-8') as f:
    content = f.read()

target_str = "final List<Flashcard> defaultFlashcards = ["
class_str = "class FlashcardsScreen extends ConsumerStatefulWidget {"

idx1 = content.find(target_str)
idx2 = content.find(class_str)

if idx1 != -1 and idx2 != -1:
    header = content[:idx1] + "import '../data/kpss_flashcards.dart';\n\nfinal List<Flashcard> defaultFlashcards = kpssFlashcards;\n\n"
    body = content[idx2:]
    
    old_subjects = """  final List<String> _filterSubjects = const [
    'Tümü',
    'TYT Biyoloji',
    'TYT Türkçe',
    'TYT Matematik',
    'TYT Fizik',
    'TYT Kimya',
    'TYT Tarih',
    'TYT Coğrafya',
    'TYT Felsefe',
    'TYT Din Kültürü',
    'AYT Matematik',
    'AYT Edebiyat',
    'AYT Fizik',
    'AYT Kimya',
    'AYT Biyoloji',
  ];"""

    new_subjects = """  final List<String> _filterSubjects = const [
    'Tümü',
    'KPSS Tarih',
    'KPSS Coğrafya',
    'KPSS Vatandaşlık & Anayasa',
    'KPSS Güncel Bilgiler',
    'KPSS Türkçe & Mantık',
    'KPSS Matematik',
  ];"""

    body = body.replace(old_subjects, new_subjects)
    
    with open('lib/screens/flashcards_screen.dart', 'w', encoding='utf-8') as f:
        f.write(header + body)
    print("SUCCESS: flashcards_screen.dart updated with KPSS cards and filters!")
else:
    print("ERROR: could not find indices", idx1, idx2)
