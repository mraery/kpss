import '../models/lesson_models.dart';
import 'kpss_tarih_units.dart';
import 'kpss_cografya_units.dart';
import 'kpss_vatandaslik_units.dart';
import 'kpss_guncel_units.dart';
import 'kpss_turkce_units.dart';
import 'kpss_matematik_units.dart';

export 'kpss_tarih_units.dart';
export 'kpss_cografya_units.dart';
export 'kpss_vatandaslik_units.dart';
export 'kpss_guncel_units.dart';
export 'kpss_turkce_units.dart';
export 'kpss_matematik_units.dart';
export 'kpss_flashcards.dart';

/// KPSS Quest - Genel Yetenek & Genel Kültür Resmi ÖSYM Müfredatı
/// Toplam: 86 Ünite, 258 Ders, 2580+ Soru
/// ÖSYM Kuralı: 4 Yanlış 1 Doğruyu Götürür (Net = Doğru - Yanlış / 4)
final List<LearningUnit> kpssUnits = [
  ...kpssTarihUnits,       // 18 Ünite (540 Soru) - Genel Kültür
  ...kpssCografyaUnits,    // 15 Ünite (450 Soru) - Genel Kültür
  ...kpssVatandaslikUnits, // 15 Ünite (450 Soru) - Genel Kültür
  ...kpssGuncelUnits,      // 6 Ünite (180 Soru) - Genel Kültür
  ...kpssTurkceUnits,      // 14 Ünite (420 Soru) - Genel Yetenek
  ...kpssMatematikUnits,   // 18 Ünite (540 Soru) - Genel Yetenek
];
