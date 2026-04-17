class Student:
    def __init__(self):
        self.name = None
        self.class_no = None
        self.age = None
        self.semester = None
        self.department = None
        self.subjects = None
        self.gpa = None

    def store_data(self):
        self.name = input("Enter Student Name : ")
        self.class_no = input("Enter Class No : ")
        self.age = int(input("Enter age : "))
        self.semester = int(input("Enter Semester : "))
        self.subjects = input("Enter subject : ")
        self.department = input("Enter Department : ")
        self.gpa = float(input("Enter gpa : "))

    def show_data(self):
        print("----Student Information----")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Class No : {self.class_no}")
        print(f"Semester : {self.semester}")
        print(f"Subject : {self.subjects}")
        print(f"Department : {self.department}")
        print(f"GPA : {self.gpa}")




stu101 = Student()

stu101.