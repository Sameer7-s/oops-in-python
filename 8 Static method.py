"""
Static method defined inside a class which is neither bound to object nor to the class
To create a static method ,we use static method decorator  
"""


class Student:


    college_name = "ABC college"
    departments = ["Arts","Commerce","Science"]

    def __init__(self,name,roll ):
        self.name = name                                   #student1.name = "john"  or student2.name = "harry" its stored the value from each attribues
        self.roll = roll
       

    def study(self ,n_hours):
        print(f"{self.name}  studies for {n_hours} hours a day ")
        
    
    def sports(self,sports_name):
        print(f"The student plays : {sports_name} in collage {self.college_name}")

        

    @staticmethod
    def greet():
        print(f"Welcome to the college")


    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.college_name} are : ")
        for department in cls.departments:
            print(department)



    
# help(Student)
student1 = Student("john",1002)
student1.study(3)
student1.get_departments()
student1.greet()

print("********************")

student2 = Student("Carol",1003)
student2.study(8)