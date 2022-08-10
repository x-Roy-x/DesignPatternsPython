import abc
from collections.abc import Iterable, Iterator


class Grades:

    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return float(sum(self.grades) / len(self.grades))

    def __str__(self):
        return str(self.grades)


class Student:

    def __init__(self, name):
        self.name = name
        self.grades = Grades()

    def add_grade(self, grade):
        self.grades.add_grade(grade)

    def __str__(self):
        return f"{self.name}: {self.grades}"


class StudentIterator(Iterator):

    def __init__(self, students):
        self._position = 0
        self._students = students

    @property
    def students_quantity(self):
        return len(self._students)

    @abc.abstractmethod
    def __next__(self):
        pass


class GradeStudentIterator(StudentIterator):

    def __init__(self, students):
        super().__init__(students)
        self._students = self.sort_by_grade()

    def sort_by_grade(self):
        students_sorted_by_grade = sorted(self._students, key=lambda student: student.grades.average_grade())
        return students_sorted_by_grade

    def __next__(self):
        student = None

        if self._position < self.students_quantity:
            student = self._students[self._position]
            self._position += 1
        else:
            raise StopIteration()

        return student


class RegisterCollection(Iterable):

    def __init__(self, students):
        self.students = students

    @abc.abstractmethod
    def __iter__(self):
        pass

    def add_new_student(self, student):
        self.students.append(student)


class GradeResisterCollection(RegisterCollection):

    def __iter__(self):
        return GradeStudentIterator(self.students)


if __name__ == '__main__':
    student1 = Student("Roi")
    student1.add_grade(10)
    student1.add_grade(2)

    student2 = Student("Bill")
    student2.add_grade(9)
    student2.add_grade(2)

    student3 = Student("Lu")
    student3.add_grade(8)
    student3.add_grade(2)

    grc = GradeResisterCollection([student1, student2, student3])

    for student in grc:
        print(student)





