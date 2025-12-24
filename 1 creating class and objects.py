"""
Docstring for creating class and objects
object => A container
 => data -> attributes 
 =>functionality -> methods/behaviour

"""

fruits = ["mango","apple","orrange"]
print(type(fruits))


#fruits is an object of a class 
fruits.append("grapes") #.append is a method of class for adding the fruit
print(fruits)
"""

car1 
=> brand = "bmw",model = "XYZ655" ,year = 2020
=> accelerate,brake 


dot notation(.)

car1.brand => "Bmw"
car1.accelerated(10)

"""

#creating objects => we need classes 

#classes => templates/blueprints/design used for creating object 
##also called as type 


##objected are created using the class
#also known as instance of a class


##creating a class

class MyClass:
    pass

#creating an object 

obj1 = MyClass()
obj2 = MyClass()

## obj1 and obj2 are objects of class MyClass

l1 = [10,20,30]
print(type(l1))

print(type(obj1))
print(type(obj2))


## calling methods using objects
##obj1.method(arg1,arg2....)

class Student:
    """
    Docstring for  student this is a class to manage student information and activities
    """
s1 = Student()
s2 = Student()


## docstrins => __doc__
print(Student.__doc__)
print(help(Student))














