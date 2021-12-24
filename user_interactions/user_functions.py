from model.student import Student
from datetime import datetime,date 
import math

def createStudent():
    print("Creating a student .....")
    s_name = input("Enter name of the student.------>")
    s_email = input("Enter email of the student.------>")
    s_english_marks = input("Enter marks scored in english.------>")
    s_maths_marks = input("Enter marks scored in maths.------>")
    s_science_marks = input("Enter marks scored in science.------>")
    s_d_o_b = input("Enter Date of Birth of the student.------>")
    student = Student(s_name , s_email,s_english_marks,s_maths_marks,s_science_marks,s_d_o_b)
    if student:
        print(f"You have created a student \n{student}")
        student.save()
    else:
        print("Failed to create a user.")

def viewStudents():
    print("*"*20,' students ',"*"*20)
    students = Student.view_students()   
    for student in students:
        print(student)

def findStudentByName():
    print("*"*20,'find students ',"*"*20)
    print("Searching students by name..")
    search_name = input("Enter the name of a student ==>")
    students = Student.find_student_by_name(search_name)
    if students:
        for student in students:
            print(student)
    else:
        print("No Student found.")


def studentsAboveEighty():
    print("*"*20,' students abov 80 %',"*"*20)
    students = Student.view_students() 
    students_above_eighty = list(filter(lambda x :(int(x.s_english_marks) + int(x.s_maths_marks) + int(x.s_science_marks))/300 > 0.8 , students))
    if students_above_eighty:
        for student in students_above_eighty:
            print(student)
def deleteStudentByID():
    print("*"*20,'delete student ',"*"*20)
    print("Deleting students by ID..")
    id = input("Enter the ID of a student you want to remove ==>")
    Student.delete_student_by_id(id)
    


def studentAge():
    print("*"*20,'Calculate age of a student ',"*"*20)
    print("Calculating age of student ")
    id = input("Enter the ID of a student you want age ==>")
    # check for the student having the id
    students = Student.view_students()
    student_id = None
    # for s in students:
    #     if s.s_id == id:
    #         student_id = s
    #         break
    # print(s.s_id)
    student_id = list(filter (lambda x:x.s_id == id , students))
    
    if student_id:
        print(f"Correct student id is ----> {student_id[0]}")
    else:
        print(f" You have entered id {id}. This dosent exist")
        return
    # found the correct student now calculate the age of student
    print(f"Age of student with id {student_id[0].s_id} -----> date of birth  ---> {student_id[0].s_d_o_b}") 
    
    date_object = datetime.strptime(student_id[0].s_d_o_b.replace("\n",""), '%d-%m-%Y').date()
    # print(date_object)
    date.today()
    # print(date.today())
    total_days = date.today() - date_object
    print(f"Age of given Student is --->{math.trunc(total_days.days/365)} years")