class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")
s1 = Student("Alice", 20, "S12345")
s2 = Student("Bob", 22, "S67890")
s1.display_info()
s2.display_info()
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")
t1 = Teacher("Mr. Smith", 45, "Mathematics")
t2 = Teacher("Ms. Johnson", 38, "Physics")
t1.display_info()
t2.display_info()
class Course:
    def __init__(self, title, code):
        self.title = title
        self.code = code
    def display_info(self):
        print(f"Course Title: {self.title}, Course Code: {self.code}")
c1 = Course("Introduction to Python", "CS101")
c2 = Course("Data Structures", "CS102")
c1.display_info()
c2.display_info()