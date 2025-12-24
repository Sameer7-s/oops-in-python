class Student:

    def study(self ,n_hours):
        print(f"the student studies for {n_hours} hours a day ")
        # print(f"self is : {self}")

    
    def sports(self,sports_name):
        print(f"The student plays : {sports_name}")


student1= Student()
# print(f"The object : {student1}")
student1.study(3)
student1.sports("Football")

print("************************************************************************")

student2 = Student()
# print(f"The object : {student2}")
student2.study(2)
student2.sports("Tennis")


