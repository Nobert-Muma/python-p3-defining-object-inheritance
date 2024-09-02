from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!" 
car_1=Car(2344, 12)
print(car_1.fill_up_tank())
print(car_1.wheel_number)
print(car_1.wheel_size)