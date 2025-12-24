class Student:
    pass

student1 = Student()
student2 = Student()

student1.name = "Johnny"
student2.roll = 15255

print(student1.name)
print(student2.roll)

help(Student)

print(student1.__dict__)
print(student2.__dict__)