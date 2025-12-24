"""Instancre method
defined inside a class which is bound to/associated with the instance/object """

# class Student:
#     """this is a class student to manage info and activities """

#     def study():
#         return "the student studies for 3 hours a day "
    
# student1= Student()
# print(student1)
# student1.study()


## by passing the arguements 

class Student:

    def study(self ):
        print("the student studies for 3 hours a day ")
        print(f"self is : {self}")

student1= Student()
print(f"The object : {student1}")


student1.study()

"""when we call an instance method using the object/instance if the class , python passes the object 
itself as the first arguments to that method 
That first arguement is by standard is self
 """