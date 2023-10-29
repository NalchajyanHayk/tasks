from validations import Validations
from abc import ABC, abstractmethod

class SchoolOperations(ABC):
    @abstractmethod
    def create_course(self, course_name, max_students):
        pass

    @abstractmethod
    def view_students(self, course):
        pass



class SchoolMember(SchoolOperations):
    def __init__(self, name, contact_info):
        self._name = None
        self._contact_info = None
        self.name = name
        self.contact_info = contact_info

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self._name = value
        else:
            print("Invalid name format.")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if Validations.is_valid_email(value):
            self._contact_info = value
        else:
            print("Invalid email format.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Contact Info: {self.contact_info}")

    def create_course(self, course_name, max_students):
        pass

    def view_students(self, course):
        pass

class Student(SchoolMember):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)
        self._courses_enrolled = []

    @property
    def courses_enrolled(self):
        return self._courses_enrolled

    def enroll(self, course):
        if course not in self._courses_enrolled:
            self._courses_enrolled.append(course)
            course.add_student(self)
            print(f"{self.name} enrolled in {course.course_name}")

    def view_progress(self):
        print(f"Student: {self.name}")
        for course in self._courses_enrolled:
            course.display_progress(self)

    def display_info(self):
        super().display_info()

class Teacher(SchoolMember):
    def __init__(self, name, contact_info, subject_taught):
        super().__init__(name, contact_info)
        self._subject_taught = None
        self.subject_taught = subject_taught
        self._courses_taught = []

    @property
    def subject_taught(self):
        return self._subject_taught

    @subject_taught.setter
    def subject_taught(self, value):
        if Validations.is_valid_name(value):
            self._subject_taught = value
        else:
            print("Invalid subject format.")

    @property
    def courses_taught(self):
        return self._courses_taught

    def create_course(self, course_name, max_students):
        course = Course(course_name, self, max_students)
        self._courses_taught.append(course)
        print(f"Teacher {self.name} created a new course: {course.course_name}")

    def view_students(self, course):
        if course in self._courses_taught:
            students = course.get_students()
            print(f"Students enrolled in {course.course_name}:")
            for student in students:
                print(student.name)

    def display_info(self):
        super().display_info()
        print(f"Subject Taught: {self.subject_taught}")

class Course:
    def __init__(self, course_name, teacher, max_students):
        self._course_name = None
        self._teacher = None
        self._max_students = None
        self._enrolled_students = []

        self.course_name = course_name
        self.teacher = teacher
        self.max_students = max_students

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        if Validations.is_valid_name(value):
            self._course_name = value
        else:
            print("Invalid course name format.")

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if isinstance(value, Teacher):
            self._teacher = value
        else:
            print("Invalid teacher object.")

    @property
    def max_students(self):
        return self._max_students

    @max_students.setter
    def max_students(self, value):
        if isinstance(value, int) and value > 0:
            self._max_students = value
        else:
            print("Invalid max students value.")

    def add_student(self, student):
        if len(self._enrolled_students) < self.max_students:
            self._enrolled_students.append(student)

    def get_students(self):
        return self._enrolled_students

    def display_progress(self, student):
        print(f"{student.name}'s progress in {self.course_name} is displayed here.")



teacher_math = Teacher("Mr. Smith", "smith@example.com", "Math")
teacher_english = Teacher("Ms. Johnson", "johnson@example.com", "English")

student1 = Student("Alice", "alice@example.com")
student2 = Student("Bob", "bob@example.com")

# Teachers create courses
teacher_math.create_course("Math 101", max_students=10)
teacher_english.create_course("English 101", max_students=12)


# Students enroll in courses
student1.enroll(teacher_math.courses_taught[0])
student1.enroll(teacher_english.courses_taught[0])
student2.enroll(teacher_english.courses_taught[0])

# Display student progress
student1.view_progress()
student2.view_progress()

# Display teacher's students
teacher_math.view_students(teacher_math.courses_taught[0])
teacher_english.view_students(teacher_english.courses_taught[0])
