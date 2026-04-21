from person_package import Person

class Student(Person):
    _student_count = 0
    def __init__(self, student_id, name, age, email):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.__grades = {}
        Student._student_count += 1

    def get_role(self):
        return "Student"

    def add_grade(self, subject, grade):
        self.__grades[subject] = grade
        print("Subject Added!")
    
    def gpa(self):
        if self.__grades:
            avg = sum(self.__grades.values())/len(self.__grades.values())
            return avg/25
        else:
            return 0
        
    def get_summary(self):
        return f"Name : {self.name} | ID : {self.student_id} | Email : {self.email} | Grades {self.__grades}"
    

    def total(cls):
        return cls._student_count

