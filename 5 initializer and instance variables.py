#__init__() method 
#is an instance method 
# is used to create and initialize the attributes during the object creation 



##early method 

# class Student:

#     def __init__(self):
#         print("calling the initalizer!")
       

#     def study(self ,n_hours):
#         print(f"the student studies for {n_hours} hours a day ")
#         # print(f"self is : {self}")

    
#     def sports(self,sports_name):
#         print(f"The student plays : {sports_name}")


# student1= Student()

# ##object_name.attribute_name = value 
# student1.name = "joht"


# student2 = Student 
# student2.name = "Carol"




class Student:

    def __init__(self,name,roll,dept ):
        self.name = name #student1.name = "john"  or student2.name = "harry" its stored the value from each attribues
        self.roll = roll
        self.department = dept

    def study(self ,n_hours):
        print(f"the student studies for {n_hours} hours a day ")
        # print(f"self is : {self}")

    
    def sports(self,sports_name):
        print(f"The student plays : {sports_name}")


student1= Student("John",1003,"BCA")
##object_name.attribute_name = value 

student2 = Student("Harry",1004,"BTECH")

print(student1.name , student1.roll,)
print(student2.name, student2.roll,student2.department)


"""
Instance variable/attributes are different for objects 
"""

## we can also update the values by previous methods 
student1.grade = "B"
print(student1.__dict__)
print(student2.__dict__)



## it's not include in the clas bcs its additional object which we created thats worng 
# student3 = Student("alice",1003,"Science")
# print(student3.__dict__)























