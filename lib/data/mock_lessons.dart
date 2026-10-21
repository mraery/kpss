import '../models/lesson_models.dart';
import '../models/exam_config.dart';
import 'kpss_units.dart';
import 'kpss_question_bank_builder.dart';

export 'kpss_streaming_units.dart';
export 'kpss_flashcards.dart';

/// KPSS Quest Resmi ÖSYM GY & GK Müfredatı (Genişletilmiş Soru Havuzu)
final List<LearningUnit> mockUnits = expandKpssUnitsWithQuestionBank(kpssUnits);

List<LearningUnit> getUnitsForExam(ExamFranchise franchise) {
  return mockUnits;
}
