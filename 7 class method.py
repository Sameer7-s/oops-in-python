"""
class methods are methods defined inside the class are bound to the class
To create a class method,we use a decorator -> classmethod
"""

class Student:


    college_name = "ABC college"
    departments = ["Arts","Commerce","Science"]

    def __init__(self,name,roll,dept ):
        self.name = name #student1.name = "john"  or student2.name = "harry" its stored the value from each attribues
        self.roll = roll
        self.departments = dept

    def study(self ,n_hours):
        print(f"the student studies for {n_hours} hours a day ")
        
    
    def sports(self,sports_name):
        print(f"The student plays : {sports_name} in collage {self.college_name}")

        

    @classmethod
    def greet(cls):
        print(f"Welcome to the {cls.college_name}")


    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.college_name} are : ")
        for department in cls.departments:
            print(department)


student1 = Student("John",1003,"BCA")
student1.study(5)
student1.greet()
student1.sports("Football")
student1.get_departments()



    
