from statistics import mean

class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def add_course(self, course):
    if course not in self.courses_in_progress:
      self.courses_in_progress.append(course)
    else:
      return f'{course} is list of courses already.'

  def rate_lecture(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

  def average_grade(self):
    sum_ = 0
    for course in self.grades.items():
      sum_ += mean(course[1])
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
    return (f'Name: {self.name}\nSurname: {self.surname}\nHomework average grade: {self.average_grade()}'
            f'\nCourses in progress: {", ".join(self.courses_in_progress)}'
            f'\nFinished courses: {", ".join(self.finished_courses)}')


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
    for course in self.grades.items():
      sum_ += mean(course[1])
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
    return f'Name: {self.name}\nSurname: {self.surname}\nLecture average grade: {self.average_grade()}'


class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += grade
      else:
        student.grades[course] = grade
    else:
      return 'Ошибка'

  def __str__(self):
    return f'Name: {self.name}\nSurname: {self.surname}\nChecks homework assignments on {", ".join(self.courses_attached)} courses.'

def average_course_grade(list_, course):    # функция средней оценки за курс
  sum_ = 0
  count_ = 0
  for person in list_:
    if course in person.grades.keys():
      sum_ += mean(person.grades[course])
      count_ += 1
  return f'The average grade on the course {course} is {sum_ / count_}'



# создаем студентов
student_1 = Student('Konstantin', 'Kanatev', 'man')
student_1.finished_courses.append('Induction')
student_2 = Student('Roma', 'Teslya', 'man')
student_2.finished_courses.append('API')
student_3 = Student('Elena', 'Davidova', 'woman')
student_3.finished_courses.append('API')
student_4 = Student('Nataliya', 'Voronova', 'man')
student_4.finished_courses.append('Kotlin')
student_5 = Student('Maxim', 'D\'yakov', 'man')
student_5.finished_courses.append('Lisp')
student_6 = Student('Petr', 'Ivanov', 'woman')
student_6.finished_courses.append('Induction')
student_7 = Student('Anna', 'Fedotova', 'woman')
student_7.finished_courses.append('Kotlin')
student_8 = Student('Rustam', 'Isaev', 'man')
student_8.finished_courses.append('Induction')

# присваиваем курсы
student_1.add_course('Python')
student_3.add_course('Python')
student_5.add_course('Python')
student_7.add_course('Python')

student_2.add_course('Git')
student_4.add_course('Git')
student_6.add_course('Git')
student_8.add_course('Git')

student_1.add_course('C++')
student_2.add_course('C++')
student_5.add_course('C++')
student_8.add_course('C++')

student_3.add_course('Django')
student_4.add_course('Django')
student_6.add_course('Django')
student_7.add_course('Django')

# создаем лекторов
lecturer_1 = Lecturer('Olga', 'Matveeva')
lecturer_1.courses_attached.append('Python')
lecturer_2 = Lecturer('Elena', 'Denisova')
lecturer_2.courses_attached.append('Git')
lecturer_3 = Lecturer('Ivan', 'Zakirov')
lecturer_3.courses_attached.append('C++')
lecturer_4 = Lecturer('Anna', 'Khabarova')
lecturer_4.courses_attached.append('Django')

# создаем проверяющих
reviewer_1 = Reviewer('Anna', 'Kazurova')
reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Django')
reviewer_2 = Reviewer('Oxana', 'Troickaya')
reviewer_2.courses_attached.append('Git')
reviewer_2.courses_attached.append('C++')

# выставляем оценки за курсы студентам
reviewer_1.rate_hw(student_1, 'Python', [3,3,5])
reviewer_1.rate_hw(student_3, 'Python', [5,3,5])
reviewer_1.rate_hw(student_5, 'Python', [3,4,5])
reviewer_1.rate_hw(student_7, 'Python', [4,3,5])

reviewer_2.rate_hw(student_2, 'Git', [3,5,5])
reviewer_2.rate_hw(student_4, 'Git', [4,4,5])
reviewer_2.rate_hw(student_6, 'Git', [5,3,5])
reviewer_2.rate_hw(student_8, 'Git', [4,5,5])

reviewer_2.rate_hw(student_1, 'C++', [5,5,5])
reviewer_2.rate_hw(student_2, 'C++', [3,2,5])
reviewer_2.rate_hw(student_5, 'C++', [2,4,5])
reviewer_2.rate_hw(student_8, 'C++', [2,5,5])

reviewer_1.rate_hw(student_3, 'Django', [5,2,5])
reviewer_1.rate_hw(student_4, 'Django', [2,4,5])
reviewer_1.rate_hw(student_6, 'Django', [5,2,5])
reviewer_1.rate_hw(student_7, 'Django', [4,5,5])

# выставляем оценки лекторам:
student_1.rate_lecture(lecturer_1, 'Python', 6)
student_3.rate_lecture(lecturer_1, 'Python', 4)
student_5.rate_lecture(lecturer_1, 'Python', 5)
student_7.rate_lecture(lecturer_1, 'Python', 5)

student_2.rate_lecture(lecturer_2, 'Git', 3)
student_4.rate_lecture(lecturer_2, 'Git', 4)
student_6.rate_lecture(lecturer_2, 'Git', 5)
student_8.rate_lecture(lecturer_2, 'Git', 5)

student_1.rate_lecture(lecturer_3, 'C++', 5)
student_2.rate_lecture(lecturer_3, 'C++', 4)
student_5.rate_lecture(lecturer_3, 'C++', 4)
student_8.rate_lecture(lecturer_3, 'C++', 4)

student_3.rate_lecture(lecturer_4, 'Django', 6)
student_4.rate_lecture(lecturer_4, 'Django', 7)
student_6.rate_lecture(lecturer_4, 'Django', 5)
student_7.rate_lecture(lecturer_4, 'Django', 5)

# print(student_7)
# print(lecturer_3)
# print(reviewer_1)

# создаем списоки для проверки методов:
students_list = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8]
lecturers_list = [lecturer_1, lecturer_2, lecturer_3, lecturer_4]

# выводим на экран лучшего и худшего студента группы:
# print(max(students_list))
# print(min(students_list))

# выводим на экран лучшего и худшего лектора:
# print(max(lecturers_list))
# print(min(lecturers_list))

# проверяем функцию средней оценки за курс:
# print(average_course_grade(students_list, 'C++'))
# print(average_course_grade(students_list, 'Python'))
# print(average_course_grade(lecturers_list, 'Git'))
# print(average_course_grade(lecturers_list, 'Django'))


