'''
Спроектировать мини‑систему для школы, которая:
- хранит учеников, предметы и оценки (журнал);
- считает статистику по оценкам (средние баллы по предмету и ученику);
- отправляет уведомления (просто пишет в консоль) если средний бал по ученику становится < 3.5
Требования:
- Разделить ответственность (отдельно: журнал, статистика, уведомления, мониторинг).
- Возможность добавлять новые типы уведомлений и алгоритмы статистики без изменения существующего кода.
- Высокоуровневые сервисы зависят от абстракций, а не от конкретных классов.
'''

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict


# ── Domain ────────────────────────────────────────────────────────────────────

@dataclass
class Student:
    name: str
    grades: Dict[str, List[float]] = field(default_factory=dict)


@dataclass
class Subject:
    name: str


# ── GradeBook ─────────────────────────────────────────────────────────────────

@dataclass
class GradeBook:
    """Хранит учеников, предметы и оценки."""
    _students: Dict[str, Student] = field(default_factory=dict)
    _subjects: Dict[str, Subject] = field(default_factory=dict)

    def add_student(self, student: Student) -> None:
        self._students[student.name] = student

    def add_subject(self, subject: Subject) -> None:
        self._subjects[subject.name] = subject

    def add_grade(self, student_name: str, subject_name: str, grade: float) -> None:
        if student_name not in self._students:
            raise ValueError(f"Student '{student_name}' not found")
        if subject_name not in self._subjects:
            raise ValueError(f"Subject '{subject_name}' not found")
        student = self._students[student_name]
        student.grades.setdefault(subject_name, []).append(grade)

    @property
    def students(self) -> List[Student]:
        return list(self._students.values())

    @property
    def subjects(self) -> List[Subject]:
        return list(self._subjects.values())


# ── Statistics — два отдельных интерфейса ─────────────────────────────────────

class StudentAverageCalculator(ABC):
    """Считает средний балл по каждому ученику."""

    @abstractmethod
    def calculate(self, grade_book: GradeBook) -> Dict[str, float]:
        pass


class SubjectAverageCalculator(ABC):
    """Считает средний балл по каждому предмету."""

    @abstractmethod
    def calculate(self, grade_book: GradeBook) -> Dict[str, float]:
        pass


class SimpleStudentAverage(StudentAverageCalculator):
    def calculate(self, grade_book: GradeBook) -> Dict[str, float]:
        result: Dict[str, float] = {}
        for student in grade_book.students:
            all_grades = [g for grades in student.grades.values() for g in grades]
            result[student.name] = sum(all_grades) / len(all_grades) if all_grades else 0.0
        return result


class SimpleSubjectAverage(SubjectAverageCalculator):
    def calculate(self, grade_book: GradeBook) -> Dict[str, float]:
        result: Dict[str, float] = {}
        for subject in grade_book.subjects:
            all_grades = [
                g
                for student in grade_book.students
                for g in student.grades.get(subject.name, [])
            ]
            result[subject.name] = sum(all_grades) / len(all_grades) if all_grades else 0.0
        return result


# ── Notifications ─────────────────────────────────────────────────────────────

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class ConsoleNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[NOTIFICATION] {message}")


# ── Monitor ───────────────────────────────────────────────────────────────────

ALERT_THRESHOLD = 3.5

@dataclass
class Monitor:
    """Зависит только от абстракций — легко тестировать и расширять."""

    student_calc: StudentAverageCalculator
    subject_calc: SubjectAverageCalculator
    notifier: Notifier


    def check(self, grade_book: GradeBook) -> None:
        student_avgs = self.student_calc.calculate(grade_book)
        subject_avgs = self.subject_calc.calculate(grade_book)

        for name, avg in student_avgs.items():
            if avg < ALERT_THRESHOLD:
                self.notifier.send(
                    f"Ученик '{name}' имеет средний балл {avg:.2f} (ниже {ALERT_THRESHOLD})"
                )

        # subject_avgs доступны для будущих проверок или отчётов
        self._print_summary(student_avgs, subject_avgs)

    @staticmethod
    def _print_summary(
        student_avgs: Dict[str, float],
        subject_avgs: Dict[str, float],
    ) -> None:
        print("\n── Средние баллы по ученикам ──")
        for name, avg in student_avgs.items():
            print(f"  {name}: {avg:.2f}")
        print("── Средние баллы по предметам ──")
        for name, avg in subject_avgs.items():
            print(f"  {name}: {avg:.2f}")


# ── Demo ──────────────────────────────────────────────────────────────────────


book = GradeBook()
for name in ("Алия", "Данияр", "Жансая"):
    book.add_student(Student(name))
for name in ("Математика", "Физика", "История"):
    book.add_subject(Subject(name))
book.add_grade("Алия",    "Математика", 4.0)
book.add_grade("Алия",    "Физика",     3.0)
book.add_grade("Данияр",  "Математика", 2.5)
book.add_grade("Данияр",  "История",    3.0)
book.add_grade("Жансая",  "Математика", 5.0)
book.add_grade("Жансая",  "Физика",     4.5)
monitor = Monitor(
    student_calc=SimpleStudentAverage(),
    subject_calc=SimpleSubjectAverage(),
    notifier=ConsoleNotifier(),
)
monitor.check(book)
