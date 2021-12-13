
import os
import random

class Student:
    filename = "students.csv"

    def __init__(self,s_name , s_email,s_english_marks,s_maths_marks,s_science_marks,s_d_o_b,s_id = None) -> None:
        self.s_name = s_name
        self.s_email = s_email
        self.s_english_marks = s_english_marks
        self.s_maths_marks = s_maths_marks
        self.s_science_marks = s_science_marks
        self.s_d_o_b = s_d_o_b
        if  not s_id:
            self.s_id = self.autogenerate_id()
        else:
            self.s_id = s_id
                

    def __repr__(self) -> str:
        return f"{self.s_id} ===>>> {self.s_name} mail me {self.s_email} ."

    @staticmethod
    def autogenerate_id():
        students = Student.view_students()
        ids = list(map(lambda x:int(x.s_id),students))
        
        while True:
            new_id = random.randint(100,999)
            if new_id not in ids:
                return new_id

    def save(self):
        line = f"\n{self.s_id},{self.s_name},{self.s_email},{self.s_english_marks},{self.s_maths_marks},{self.s_science_marks},{self.s_d_o_b}"
        with open(self.filename,'a') as f:
            f.write(line)

    @classmethod
    def view_students(cls):
        students =[]
        with open('students.csv','r')as f:
            lines = f.readlines()
            for line in lines:
                items = line.split(',')
                student = Student(*items[1:],items[0])
                students.append(student)

        return students
    @classmethod
    def find_student_by_name(cls,search_name):
        students =[]
        with open('students.csv','r')as f:
            lines = f.readlines()
            for line in lines:
                items = line.split(',')
                if items[1].strip().lower() == search_name.lower():
                    student = Student(*items[1:],items[0])
                    students.append(student)
        return students

    @classmethod
    def delete_student_by_id(cls,id):
        flag = 0
        with open('students.csv','r')as fr:  
            with open('temp.csv','w') as fw:
                lines = fr.readlines()
                for line in lines:
                    items = line.split(',')
                    if (items[0].strip()) != id:
                        flag = 1
                        fw.write(line)
                    else:    
                        print(f"Deleting {line} successfully")
                        
        if flag == 0:
            print("No student found")
            return 
        else:
            os.remove("students.csv")
            os.rename("temp.csv","students.csv")          