"""
Inheritance 
"""
class vehicle:
    company  = "XYZ Motors"
    
    def __init__(self,n_wheels,n_seats,milage):
        print("init of vehicle")
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.milage = milage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels ,which has {self.n_seats} seats and it provide {self.milage} milage on the road  "

v1 = vehicle(4,7,45)
print(v1.get_details())

class Car(vehicle):
        model = "ABC1 motors!!!"
        def __init__(self,car_type,drive_type,wheels,seats,mileage):
            print("init of car")
            self.car_type = car_type
            self.drive_type = drive_type
            vehicle.__init__(self ,4,7,45)
            super().__init__(4,7,45)
          

c1 = Car("SUV","Manual",4,8,49)
print(c1.model)
print(c1.company)
print(c1.milage) ## inherited from the vehicle class '
print(c1.n_seats) ## inherited from the vehicle class 
print(c1.get_details())
print(c1.__dict__)
# print(c1.milage)   ### this shows eror bcs we can not call directly parent class of instance method
"""when car has own init so it doesn't call the  init of vehicle we have to explicitily call the init of vehicle in the car class 
inside the init of class  """



