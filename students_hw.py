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

  def __str__(self):
    return f'Name: {self.name}\nSurname: {self.surname}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}

  def __str__(self):
    return f'Name: {self.name}\nSurname: {self.surname}'


class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'

  def __str__(self):
    return f'Name: {self.name}\nSurname: {self.surname}\nChecks homework assignments on {", ".join(self.courses_attached)} courses.'

def average_course_grade(students_list, course):     # функция средней оценки за курс
    pass
    # course_list = []
    # for student in students_list:
    #     if course in student.courses_in_progress:
    #         course_list.append(student)
    # return course_list

# создаем студентов
student_1 = Student('Konstantin', 'Kanatev', 'man')
student_2 = Student('Roma', 'Teslya', 'man')
student_3 = Student('Elena', 'Davidova', 'woman')
student_4 = Student('Nataliya', 'Voronova', 'man')
student_5 = Student('Maxim', 'D\'yakov', 'man')
student_6 = Student('Petr', 'Ivanov', 'woman')
student_7 = Student('Anna', 'Fedotova', 'woman')
student_8 = Student('Rustam', 'Isaev', 'man')

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
lecturer_1.courses_attached.append('Git')

lecturer_2 = Lecturer('Ivan', 'Zakirov')
lecturer_2.courses_attached.append('C++')
lecturer_2.courses_attached.append('Django')

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

students_list = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8]

# выставляем оценки лекторам
student_1.rate_lecture(lecturer_1, 'Python', 6)
student_3.rate_lecture(lecturer_1, 'Python', 4)
student_5.rate_lecture(lecturer_1, 'Python', 5)
student_7.rate_lecture(lecturer_1, 'Python', 5)

student_2.rate_lecture(lecturer_1, 'Git', 3)
student_4.rate_lecture(lecturer_1, 'Git', 4)
student_6.rate_lecture(lecturer_1, 'Git', 5)
student_8.rate_lecture(lecturer_1, 'Git', 5)

student_1.rate_lecture(lecturer_2, 'C++', 5)
student_2.rate_lecture(lecturer_2, 'C++', 4)
student_5.rate_lecture(lecturer_2, 'C++', 4)
student_8.rate_lecture(lecturer_2, 'C++', 4)

student_3.rate_lecture(lecturer_2, 'Django', 6)
student_4.rate_lecture(lecturer_2, 'Django', 7)
student_6.rate_lecture(lecturer_2, 'Django', 5)
student_7.rate_lecture(lecturer_2, 'Django', 5)

print(lecturer_2.grades)