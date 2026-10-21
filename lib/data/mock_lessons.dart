import '../models/lesson_models.dart';
import '../models/exam_config.dart';
import 'kpss_units.dart';
import 'kpss_question_bank_builder.dart';

export 'kpss_units.dart';

/// KPSS Quest Resmi ÖSYM GY & GK Müfredatı (Genişletilmiş Soru Havuzu)
final List<LearningUnit> mockUnits = expandKpssUnitsWithQuestionBank(kpssUnits);

/// Aktif Quest sınavına göre müfredat ünitelerini döndürür
List<LearningUnit> getUnitsForExam(ExamFranchise franchise) {
  return mockUnits;
}
