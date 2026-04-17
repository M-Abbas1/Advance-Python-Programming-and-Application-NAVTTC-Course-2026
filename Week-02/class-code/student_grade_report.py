
print("----- Student Grade Calculator---------")


student_name = input("Enter Student Name : ")
mid_term = float(input("Enter Mid Term Marks : "))
final_term = float(input("Enter Final Term Marks : "))
assignment = float(input("Enter Assignment Marks : "))

mid_term_w = mid_term * 0.30
final_term_w = final_term * 0.40
assignment_w = assignment * 0.30

total_percentange = mid_term_w + final_term_w + assignment_w

letter_grade = None
gpa = None
if total_percentange >= 90:
    letter_grade = "A+"
    gpa = 4.0
elif total_percentange >= 85:
    letter_grade = "A"
    gpa = 3.7
elif total_percentange >= 80:
    letter_grade = "B+"
    gpa = 3.3
elif total_percentange >= 75:
    letter_grade = "B"
    gpa = 3.0
elif total_percentange >= 70:
    letter_grade = "B-"
    gpa = 2.7
elif total_percentange >= 65:
    letter_grade = "C"
    gpa = 2.5
else:
    letter_grade = "F"
    gpa = 2.0

status = None
if total_percentange >= 60:
    status = "PASS"
else:
    status = "FAIL"

dean_list = None
if gpa >= 3.5 and mid_term >= 80 and final_term >= 80 and assignment>=80:
    dean_list = "Yes"
else:
    dean_list = "No"

feedback = None
if total_percentange >= 90:
    feedback = "Outstanding work"
elif total_percentange >= 80:
    feedback = "Excellent"
elif total_percentange >= 70:
    feedback = "Good, keep it up"
else:
    feedback = "you need to work harder"

print()
print("="*11, "GRADE REPORT", "="*11)
print(f"Student : {student_name}")
print("-"*36)

print("Score Breakdown : ")
print(f"  Mid Term (30%): \t{mid_term} -> {mid_term_w}")
print(f"  Final Term (40%): \t{final_term} -> {final_term_w}")
print(f"  Assignment (30%): \t{assignment} -> {assignment_w}")
print("-"*36)

print(f"Total Percentange : {total_percentange:.2f}%")
print(f"Letter Grade : {letter_grade}")
print(f"GPA : {gpa:.2f}")
print(f"Status : {status}")
print(f"Dean's List : {dean_list}")
print("-"*36)
print(f"Performance: {feedback}")
print("="*36)
