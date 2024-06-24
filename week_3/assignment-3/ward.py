'''
Câu 2: Một Ward (phường) gồm có name (string) và danh sách của mọi người trong Ward.
Một người person có thể là student, doctor, hoặc teacher. Một student gồm có name,
yob (int) (năm sinh), và grade (string). Một teacher gồm có name, yob, và subject
(string). Một doctor gồm có name, yob, và specialist (string). Lưu ý cần sử dụng a
list để chứa danh sách của mọi người trong Ward.
'''

from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        raise NotImplementedError


class Student(Person):

    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print("Student - Name: {} - YoB: {} - Grade: {}".format(self._name,
              self._yob, self._grade))


class Teacher(Person):

    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print("Teacher - Name: {} - YoB: {} - Subject: {}".format(self._name,
              self._yob, self._subject))


class Doctor(Person):

    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print("Doctor - Name: {} - YoB: {} - Speacialist: {}".format(self._name,
              self._yob, self._specialist))


class Ward():

    def __init__(self, name: str):
        self._name = name
        self.people_list = []

    def add_person(self, person: Person):
        self.people_list.append(person)

    def describe(self):
        print("Ward: {}".format(self._name))
        for p in self.people_list:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.people_list:
            if isinstance(p, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people_list.sort(reverse=True, key=lambda n: n.yob)

    def compute_average(self):
        teacher_list = []
        s = 0
        for p in self.people_list:
            if isinstance(p, Teacher):
                teacher_list.append(p)
                s += p.yob
        return s / len(teacher_list)
