class Student:
    def __init__(self,student_id,name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
        
    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False

    def view_student_info(self):
        en_status=''
        if self.__is_enrolled:
            en_status = 'Enrolled'
        else:
            en_status='Not Enrolled'
        return f"ID: {self.__student_id}, Name: {self.__name}, Dept: {self.__department}, Enrolled: {en_status}"
    
    def is_enrolled(self):
        return self.__is_enrolled
    def get_id(self):
        return self.__student_id


class StudentDatabase:
    student_list = []
    def __init__(self):
        pass
    @classmethod
    def add_student(self,student):
        self.student_list.append(student)

    @classmethod
    def is_available(self, studn_id):
        for student in self.student_list:
            if student.get_id() == studn_id:
                return student
        return None
    
    @classmethod
    def all_student(self):
        for student in self.student_list:
            print(student.view_student_info())


s1 = Student(201, "Nayeem Hasan", "CSE")
s2 = Student(202, "Maliha Jahan", "BBA")
s3 = Student(203, "Sajid Rahman", "EEE")
s4 = Student(204, "Farzana Akter", "LAW")
s5 = Student(205, "Tariqul Islam", "CSE")
s6 = Student(206, "Shamima Nasrin", "ENG")
s7 = Student(207, "Tanvir Ahmed", "BBA" )
s8 = Student(208, "Rafiq Hasan", "EEE")
s9 = Student(209, "Lubaba Hossain", "LAW")
s10 = Student(210, "Kazi Arif", "CSE")



def menu():
    print("""

1. View All Students
2. Enroll Student
3. Drop Student
4. Exit

""")

while True:
    menu()
    options = int(input("select 1-4 :"))

    if options == 1:
        StudentDatabase.all_student()
    elif options == 2:
        try:
            std_id = int(input("ID for enrollment : "))
            found = StudentDatabase.is_available(std_id)

            if found:
                if not found.is_enrolled():
                    found.enroll_student() 
                    print("Enrollment successFull")
                    
                else:
                    print("Alrady Enrolled")
            else:
                print("Student Not found")
        except ValueError:
            print("Invalid Student ID")


    elif options == 3:
        try:        
            std_id = int(input("ID for enrollment : "))
            found = StudentDatabase.is_available(std_id)

            if found:
                if found.is_enrolled():
                    found.drop_student()
                    print("Student Dropped succefully")
                else:
                    print("Studlent Already Dropped")
            else:
                print("Student not found")
        except ValueError:
            print("Invalid Student ID")
    elif options == 4:
        break