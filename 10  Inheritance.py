"""
Inheritance 
"""
class vehicle:
    company  = "XYZ Motors"
    

    def __init__(self,n_wheels,n_seats,milage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.milage = milage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels ,which has {self.n_seats} seats and it provide {self.milage} milage on the road  "

v1 = vehicle(4,7,45)
print(v1.get_details())
