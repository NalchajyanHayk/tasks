from abc import ABC, abstractmethod

class University_System:
    def __init__(self):
        self.courses = []
        self.students = []
        self.professors = []

    def add_course(self, course):
        if isinstance(course, Course):
            self.courses.append(course)
        else:
            raise ValueError("Invalid course object")

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise ValueError("Invalid student object")

    def add_professor(self, professor):
        if isinstance(professor, Professor):
            self.professors.append(professor)
        else:
            raise ValueError("Invalid professor object")

    def display_courses(self):
        for course in self.courses:
            print(f"Course: {course.name}, Instructor: {course.instructor}")

    def display_students(self):
        for student in self.students:
            print(f"Student: {student.name}")

    def display_professors(self):
        for professor in self.professors:
            print(f"Professor: {professor.name}")

class Course(ABC):
    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        self.content = []

    def add_content(self, content):
        self.content.append(content)

    @abstractmethod
    def get_course_type(self):
        pass

class Assignment(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def get_assignment_type(self):
        pass

class Student:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.enrolled_courses = []
        self.completed_assignments = []

    def enroll(self, course):
        if isinstance(course, Course):
            self.enrolled_courses.append(course)
        else:
            raise ValueError("Invalid course object")

    def complete_assignment(self, assignment):
        if isinstance(assignment, Assignment):
            self.completed_assignments.append(assignment)
        else:
            raise ValueError("Invalid assignment object")

    def view_progress(self):
        print(f"Student: {self.name}")
        print("Enrolled Courses:")
        for course in self.enrolled_courses:
            print(f"- {course.name} ({course.get_course_type()})")
        print("Completed Assignments:")
        for assignment in self.completed_assignments:
            print(f"- {assignment.name} ({assignment.get_assignment_type()})")

class Professor:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def create_course(self, name, instructor):
        new_course = Graduate_Course(name, instructor)  # Default is GraduateCourse
        self.add_content(new_course)
        return new_course

    def add_content(self, course):
        if isinstance(course, Course):
            course.instructor = self.name
            course.add_content("Syllabus")
            course.add_content("Lecture Notes")
        else:
            raise ValueError("Invalid course object")

class Undergraduate_Course(Course):
    def get_course_type(self):
        return "Undergraduate Course"

class Graduate_Course(Course):
    def get_course_type(self):
        return "Graduate Course"

class Homework_Assignment(Assignment):
    def get_assignment_type(self):
        return "Homework Assignment"

class Research_Assignment(Assignment):
    def get_assignment_type(self):
        return "Research Assignment"

# Instantiate the university system
university_system = University_System()

# Instantiate a professor
professor = Professor("Dr. Smith", "prof.smith@example.com")
university_system.add_professor(professor)

# Create a course
course = professor.create_course("Advanced Computer Science", professor.name)
university_system.add_course(course)

# Create assignments
homework = Homework_Assignment("Homework 1", "Complete exercises 1-5")
research = Research_Assignment("Research Project", "Submit a research paper")

# Enroll students
student1 = Student("Alice", "alice@example.com")
student2 = Student("Bob", "bob@example.com")
university_system.add_student(student1)
university_system.add_student(student2)

student1.enroll(course)
student2.enroll(course)

# Complete assignments
student1.complete_assignment(homework)
student2.complete_assignment(research)

# Display university system information
university_system.display_professors()
university_system.display_courses()
university_system.display_students()

# View student progress
student1.view_progress()
student2.view_progress()
