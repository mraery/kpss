# -*- coding: utf-8 -*-
"""
Ortak KPSS Soru & Ders Üretim Yardımcı Fonksiyonları
"""

def esc(s):
    if s is None:
        return "null"
    res = str(s).replace("\\", "\\\\").replace("'", "\\'").replace("$", "\\$")
    res = res.replace("\n", "\\n").replace("\r", "")
    return f"'{res}'"

def make_concept_card(q_id, title, rule, exam_tip, emoji="💡", examples=None):
    ex_str = ""
    if examples:
        ex_items = ", ".join(esc(e) for e in examples)
        ex_str = f"\n        examples: [{ex_items}],"
    return f"""      Question(
        id: {esc(q_id)},
        type: QuestionType.conceptCard,
        conceptTitle: {esc(title)},
        rule: {esc(rule)},{ex_str}
        examTip: {esc(exam_tip)},
        iconEmoji: {esc(emoji)},
      ),"""

def make_mc(q_id, prompt, options, correct_idx, explanation, passage=None):
    opt_str = ", ".join(esc(o) for o in options)
    passage_str = f"\n        passage: {esc(passage)}," if passage else ""
    return f"""      Question(
        id: {esc(q_id)},
        type: QuestionType.multipleChoice,{passage_str}
        prompt: {esc(prompt)},
        options: [{opt_str}],
        correctIndex: {correct_idx},
        explanation: {esc(explanation)},
      ),"""

def make_tf(q_id, prompt, is_true, explanation):
    return f"""      Question(
        id: {esc(q_id)},
        type: QuestionType.trueFalse,
        prompt: {esc(prompt)},
        isTrue: {str(is_true).lower()},
        explanation: {esc(explanation)},
      ),"""

def make_fib(q_id, prompt, blank_options, correct_answer, explanation):
    opt_str = ", ".join(esc(o) for o in blank_options)
    return f"""      Question(
        id: {esc(q_id)},
        type: QuestionType.fillInTheBlank,
        prompt: {esc(prompt)},
        blankOptions: [{opt_str}],
        correctBlankAnswer: {esc(correct_answer)},
        explanation: {esc(explanation)},
      ),"""

def make_match(q_id, prompt, pairs, explanation):
    pair_lines = []
    for l, r in pairs:
        pair_lines.append(f"MatchingPair(left: {esc(l)}, right: {esc(r)})")
    pairs_str = ", ".join(pair_lines)
    return f"""      Question(
        id: {esc(q_id)},
        type: QuestionType.matching,
        prompt: {esc(prompt)},
        matchingPairs: [{pairs_str}],
        explanation: {esc(explanation)},
      ),"""

def make_lesson(l_id, title, desc, questions, is_unit_exam=False):
    q_code = "\n".join(questions)
    exam_flag = "\n        isUnitExam: true," if is_unit_exam else ""
    return f"""    Lesson(
      id: {esc(l_id)},
      title: {esc(title)},
      description: {esc(desc)},{exam_flag}
      questions: [
{q_code}
      ],
    ),"""

def make_unit(u_id, unit_num, title, subject, color_hex, lessons):
    lessons_code = "\n".join(lessons)
    return f"""  LearningUnit(
    id: {esc(u_id)},
    unitNumber: {unit_num},
    title: {esc(title)},
    subject: {esc(subject)},
    colorHex: {color_hex},
    lessons: [
{lessons_code}
    ],
  ),"""
