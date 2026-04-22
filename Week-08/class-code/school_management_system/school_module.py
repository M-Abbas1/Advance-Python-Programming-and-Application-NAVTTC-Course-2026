from student_module import Student
from teacher_module import Teacher



class School:

    def __init__(self, name, location):
        self.school_name = name
        self.location = location
        self._students = []
        self._teachers = []

    
    def enroll_student(self, student):
        self._students.append(student)
        print("Student Enrolled")

    def hire_teacher(self, teacher):
        self._teachers.append(teacher)
        print("Teacher Hired!")

    def no_of_students(self):
        return self._students[0].total()
    
    def no_of_teachers(self):
        return len(self._teachers)
    

    def show_teacher_details(self):
        print("------Teachers Details------")
        for teacher in self._teachers:
            print(teacher.get_summary())

    def show_students_details(self):
        print("------Students Details-------")
        for student in self._students:
            print(student.get_summary())




    


    


    


