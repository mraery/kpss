import 'package:flutter_test/flutter_test.dart';
import 'package:kpss_quest/data/mock_lessons.dart';
import 'package:kpss_quest/models/lesson_models.dart';
import 'package:kpss_quest/screens/fast_reflex_screen.dart';

void main() {
  group('KPSS Quest Data Integrity & Question Validation', () {
    test('All questions across all 86 units have valid options and correct indices', () {
      final seenQuestionIds = <String>{};
      int totalValidated = 0;

      for (final unit in mockUnits) {
        expect(unit.id.isNotEmpty, isTrue, reason: 'Unit id cannot be empty');
        expect(unit.title.isNotEmpty, isTrue, reason: 'Unit title cannot be empty: ${unit.id}');

        for (final lesson in unit.lessons) {
          expect(lesson.id.isNotEmpty, isTrue, reason: 'Lesson id cannot be empty: ${lesson.title}');
          expect(lesson.title.isNotEmpty, isTrue, reason: 'Lesson title cannot be empty');

          for (final q in lesson.questions) {
            totalValidated++;
            // Check unique IDs
            expect(seenQuestionIds.contains(q.id), isFalse, reason: 'Duplicate question ID: ${q.id}');
            seenQuestionIds.add(q.id);

            // Validate based on question type
            if (q.type == QuestionType.multipleChoice) {
              expect(q.prompt.isNotEmpty, isTrue, reason: 'Empty prompt in ${q.id}');
              expect(q.options, isNotNull, reason: 'Options null for ${q.id}');
              expect(q.options!.length, greaterThanOrEqualTo(2), reason: 'Options < 2 for ${q.id}');
              for (final opt in q.options!) {
                expect(opt.trim().isNotEmpty, isTrue, reason: 'Empty option string in ${q.id}');
              }
              expect(q.correctIndex, isNotNull, reason: 'correctIndex null for ${q.id}');
              expect(q.correctIndex! >= 0 && q.correctIndex! < q.options!.length, isTrue,
                  reason: 'correctIndex out of bounds for ${q.id}: ${q.correctIndex} >= ${q.options!.length}');
              expect(q.options![q.correctIndex!].trim().isNotEmpty, isTrue,
                  reason: 'Empty correct option in ${q.id}');
            } else if (q.type == QuestionType.fillInTheBlank) {
              expect(q.prompt.isNotEmpty, isTrue, reason: 'Empty prompt in fillInTheBlank ${q.id}');
              expect(q.blankOptions != null && q.blankOptions!.isNotEmpty, isTrue,
                  reason: 'blankOptions null or empty for ${q.id}');
              expect(q.correctBlankAnswer != null && q.correctBlankAnswer!.isNotEmpty, isTrue,
                  reason: 'correctBlankAnswer null or empty for ${q.id}');
              expect(q.blankOptions!.contains(q.correctBlankAnswer), isTrue,
                  reason: 'correctBlankAnswer "${q.correctBlankAnswer}" not in blankOptions for ${q.id}');
            } else if (q.type == QuestionType.trueFalse) {
              expect(q.prompt.isNotEmpty, isTrue, reason: 'Empty prompt in trueFalse ${q.id}');
              expect(q.isTrue, isNotNull, reason: 'isTrue null for ${q.id}');
            } else if (q.type == QuestionType.matching) {
              expect(q.matchingPairs != null && q.matchingPairs!.isNotEmpty, isTrue,
                  reason: 'Matching pairs missing for ${q.id}');
              for (final pair in q.matchingPairs!) {
                expect(pair.left.isNotEmpty, isTrue, reason: 'Empty matching left in ${q.id}');
                expect(pair.right.isNotEmpty, isTrue, reason: 'Empty matching right in ${q.id}');
              }
            } else if (q.type == QuestionType.conceptCard) {
              expect(q.conceptTitle != null && q.conceptTitle!.isNotEmpty, isTrue,
                  reason: 'conceptTitle empty for concept card ${q.id}');
              expect(q.rule != null && q.rule!.isNotEmpty, isTrue,
                  reason: 'rule empty for concept card ${q.id}');
            }
          }
        }
      }

      expect(totalValidated, greaterThanOrEqualTo(2500));
    });

    test('All flashcards have valid term, meaning, subject, and unique IDs', () {
      final seenCardIds = <String>{};
      for (final card in kpssFlashcards) {
        expect(seenCardIds.contains(card.id), isFalse, reason: 'Duplicate flashcard ID: ${card.id}');
        seenCardIds.add(card.id);

        expect(card.term.isNotEmpty, isTrue, reason: 'Empty term in ${card.id}');
        expect(card.meaning.isNotEmpty, isTrue, reason: 'Empty meaning in ${card.id}');
        expect(card.subject.isNotEmpty, isTrue, reason: 'Empty subject in ${card.id}');
      }
      expect(kpssFlashcards.length, greaterThanOrEqualTo(100));
    });

    test('All reflex questions have valid trigger words, correct answers, and distinct wrong options', () {
      expect(kpssReflexBank.length, greaterThanOrEqualTo(30));
      for (final rq in kpssReflexBank) {
        expect(rq.prompt.isNotEmpty, isTrue, reason: 'Empty prompt in reflex question');
        expect(rq.triggerWord.isNotEmpty, isTrue, reason: 'Empty triggerWord');
        expect(rq.correctAnswer.isNotEmpty, isTrue, reason: 'Empty correctAnswer');
        expect(rq.memoryCode.isNotEmpty, isTrue, reason: 'Empty memoryCode');
        expect(rq.wrongOptions.length, greaterThanOrEqualTo(3), reason: 'Less than 3 wrong options for ${rq.prompt}');
        expect(rq.wrongOptions.contains(rq.correctAnswer), isFalse,
            reason: 'wrongOptions contains correctAnswer for ${rq.prompt}');
      }
    });
  });
}
