# Управление студентами
# У нас есть студенты с именами и оценками
# Нужно сделать возможность:
# - добавить студента в список
# - получить список студентов
# - получить среднюю оценку
# - получить лучшего студента
# - распечатать отчёт - средний бал и лучший студент


from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grade: float

@dataclass
class StudentRepository:
    students: list[Student]

    def add_student(self, student: Student):
        self.students.append(student)

    def get_students(self):
        return self.students

@dataclass
class StudentService:
    repository: StudentRepository

    def get_average_grade(self):
        students = self.repository.get_students()
        if not students:
            return 0
        total_grade = sum(student.grade for student in students)
        return total_grade / len(students)

    def get_best_student(self):
        students = self.repository.get_students()
        if not students:
            return None
        return max(students, key=lambda student: student.grade)

@dataclass
class ReportService:
    repository: StudentRepository
    student_service: StudentService

    def print_report(self):
        average_grade = self.student_service.get_average_grade()
        best_student = self.student_service.get_best_student()
        print(f"Average Grade: {average_grade:.2f}")
        if best_student:
            print(f"Best Student: {best_student.name} with grade {best_student.grade:.2f}")
        else:
            print("No students available.")

# Пример использования
repository = StudentRepository(students=[])
service = StudentService(repository)
report_service = ReportService(repository, service)
repository.add_student(Student("Alice", 85))
repository.add_student(Student("Bob", 90))
repository.add_student(Student("Charlie", 78))
report_service.print_report()