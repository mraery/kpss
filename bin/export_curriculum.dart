// ignore_for_file: avoid_relative_lib_imports, avoid_print
import 'dart:convert';
import 'dart:io';
import '../lib/data/kpss_units.dart';

void main() {
  final dir = Directory('curriculum');
  if (!dir.existsSync()) dir.createSync(recursive: true);

  for (final unit in kpssUnits) {
    final file = File('curriculum/${unit.id}.json');
    file.writeAsStringSync(jsonEncode(unit.toJson()));
  }
  print('Exported ${kpssUnits.length} KPSS units to curriculum/*.json');
}
