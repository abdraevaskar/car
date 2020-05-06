class Car:
    def __init__(self, make, model, year, odometer, fuel):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer = odometer
        self.__fuel = fuel
    
    def __add_distance(self, distance):
        if distance <= self.__fuel * 10:
            self.__odometer += distance
            

    
    def __subtract_fuel(self, distance):
        if distance <= self.__fuel * 10:
            self.__fuel -= distance / 10
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')


    def drive(self, distance):
        balance = self.__fuel * 10 / distance
        if balance >= 1:
            self.__subtract_fuel(distance)
        else:
            self.__subtract_fuel(distance)




car = Car('Mersedes', 'GT', '2020', 0, 70)

car.drive(10000)