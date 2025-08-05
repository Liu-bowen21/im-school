class Vehicle:
    def __init__(self,color,wheels):
        self.color = color
        self.wheels = wheels

    def current_speed(self, speed):
        print(speed)

    def number_passegers(self,passegers):
        print(passegers)

    def play_number(self,number):
        print(number)


class Car(Vehicle):
    def __init__(self,color,wheels,plate):
        super().__init__(color,wheels)
        self.plate = plate


class Bike(Vehicle):
    def __init__(self, color, wheels):
        super().__init__(color, wheels)

car = Car('pink', 4, "ABCD")
car.current_speed(8)
car.play_number(10)