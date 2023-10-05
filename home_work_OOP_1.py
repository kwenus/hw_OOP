from statistics import mean
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'
    def average_grade(self):
        sum_ = 0
        for el in self.grades.items():
            sum_ += mean(el[1])
        return round(sum_ / len(self.grades), 1)

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return (f'Name: {self.name}\nSurname: {self.surname}\nAverage grade: {self.average_grade()}'
                f'\nCourses in progress: {self.courses_in_progress}\nFinished courses: {self.finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        sum_ = 0
        for el in self.grades.items():
            sum_ += mean(el[1])
        return round(sum_ / len(self.grades), 1)

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):  # не равно
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):  # меньше, чем
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):  # больше, чем
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nAverage grade: {self.average_grade()}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}'

def average_student_grade(students):
    pass

def group(student_list, course):
    course_list = []
    for student in student_list:
        if course in student.courses_in_progress:
            course_list.append(student)
    return course_list


student_1 = Student('Kostya', 'Kanatev', 'm')
student_1.finished_courses += ['Git']    # правильно передавать список, а не строку
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Django']
student_1.grades['Git'] = [10, 8, 6, 5, 10]
student_1.grades['Python'] = [7, 10]

student_2 = Student('Anna', 'Fodotova', 'w')
student_2.finished_courses += ['Git']
student_2.courses_in_progress += ['API']
student_2.courses_in_progress += ['Python']
student_2.grades['Git'] = [7, 8, 4, 6, 8]
student_2.grades['Python'] = [7, 9]

student_3 = Student('Olga', 'Matveeva', 'w')
student_3.finished_courses += ['Git']
student_3.courses_in_progress += ['API']
student_3.courses_in_progress += ['Python']
student_3.grades['Git'] = [6, 6, 4, 3, 7]
student_3.grades['Python'] = [8, 10]

reviewer_1 = Reviewer('Ivan', 'Zaripov' )
reviewer_1.courses_attached += ['API']
reviewer_2 = Reviewer('Alla', 'Sabirova')
reviewer_2.courses_attached += ['Django']
reviewer_1.rate_hw(student_2, 'API', 10)
reviewer_2.rate_hw(student_1, 'Django', 8)

lecturer_1 = Lecturer('Roman', 'Rogov')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['API']
lecturer_2 = Lecturer('Sveta', 'Budina')
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['Django']

student_1.rate_lecture(lecturer_1, 'Python', 7)
student_2.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_2, 'Django', 8)
student_2.rate_lecture(lecturer_1, 'API', 10)

# print(student_1)
# print(student_2)
# print(student_3)
# print(reviewer_1)
# print(reviewer_2)
# print(lecturer_1)
# print(lecturer_2)
#
# print()
#
# print(max(student_1, student_2, student_3))
# print(min(lecturer_1, lecturer_2))


student_list = [student_1, student_2, student_3]

course = group(student_list, 'API')

for el in course:
    print(el)


