from student_module import Student
from teacher_module import Teacher
from school_module import School



school = School("Hangu Institue of sceince and technology", "Hangu")


running = True

while running:
    print(school.school_name)
    print("1. Enroll Student")
    print("2. Hire Teacher")
    print("3. Show Students")
    print("4. Show Teachers")
    print("5. Total Students")
    print("6. Total Teachers")
    print("7. Exit")

    choice = input("What do you want : ")

    if choice == '1':
        print("-----Student Enrollment-----")
        id = int(input("Enter Student ID : "))
        name = input("Enter Student Name : ")
        age = int(input("Enter student age : "))
        email = input("Enter student email : ")
        stu = Student(id, name, age, email)
        school.enroll_student(stu)

        print("")

    elif choice == '2':
        print("------Hiring a Teacher-------")
        name = input("Enter Teacher Name ")
        age = int(input("Enter teacher age : "))
        email = input("enter teacher email : ")
        subject = input("Enter teacher subject : ")
        salary = float(input("Enter Teacher Salary : "))
        teacher = Teacher(name, age, email, subject, salary)
        school.hire_teacher(teacher)


    elif choice == '3':
        print(school.show_students_details())
        
    elif choice == '4':
        print(school.show_teacher_details())
        
    elif choice == '5':
        print(school.no_of_students())

    elif choice == '6':
        print(school.no_of_teachers())
        
    elif choice == '7':
        print("good bye")
        running = False
    else:
        print("Enter a valid option")



