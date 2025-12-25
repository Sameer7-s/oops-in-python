class Vehicle:
    def __init__(self,n_wheels,n_seats,n_mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.n_mileage = n_mileage

    def get_details(self):
        return f"The vehicle has  {self.n_wheels} wheels and {self.n_seats} seats and mileage of {self.n_mileage}"
    



class Car(Vehicle):
    model = "ABC111"
    def __init__(self , car_type , drive_type ,wheels, seats,mileage):
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(wheels,seats,mileage)

    def display_info(self):
        print(f"Car type : {self.car_type} Drive type {self._drive_type}")

class Electric_car(Car):
    def __init__(self , car_type , drive_type,wheels, seats,mileage,battery_capacity,distance_range):
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
        super().__init__(car_type,drive_type,wheels,seats,mileage)
    

    def charge(self):
        print(f"Charging to battery {self.battery_capacity}")



ec1 = Electric_car("Sedaan","manual",4,2,10,34,"4hr")
print(ec1.__dict__)