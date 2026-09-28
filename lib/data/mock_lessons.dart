import '../models/lesson_models.dart';
import '../models/exam_config.dart';
import 'kpss_streaming_units.dart';

export 'kpss_streaming_units.dart';
export 'kpss_flashcards.dart';

/// KPSS Quest Resmi Mufredati
final List<LearningUnit> mockUnits = kpssStreamingUnits;

List<LearningUnit> getUnitsForExam(ExamFranchise franchise) {
  return kpssStreamingUnits;
}
