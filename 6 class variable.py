"""
class variable are defined at the class level 
same copy of the class variables are shared among the objects 

"""

class Student:


    college_name = "ABC college"
    departments = ["Arts","Commerce","Science"]

    def __init__(self,name,roll,dept ):
        self.name = name #student1.name = "john"  or student2.name = "harry" its stored the value from each attribues
        self.roll = roll
        self.department = dept


student1= Student("John",1003,"BCA")
# help(Student)
print(student1.__dict__)
# student2 = Student("Harry",1004,"BTECH")

# print(student1.name , student1.roll,)
# print(student2.name, student2.roll,student2.department)



# print(student1.department)
# print(student1.college_name)

# print(Student.departments)
# print(Student.college_name)


student2 = Student("carol",1005,"BCA")

print(student2.departments)
print(student2.college_name)

