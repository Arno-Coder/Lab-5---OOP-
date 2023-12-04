class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Driver(Person):
    def __init__(self, first_name: str, last_name: str, exp: int):
        super().__init__(first_name, last_name)
        self.exp = exp

    def __str__(self):
        return f'Driver: {super().__str__()}, Experience: {self.exp}'

class Engine:
    def __init__(self, power: int, manufacturer: str):
        self.power = power
        self.manufacturer = manufacturer

    def __str__(self):
        return f'Motor: {self.power} horsepower, {self.manufacturer}'

class Car:

    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, motor: Engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.motor = motor

    def start(self) -> str:
        return "Go"

    def stop(self) -> str:
        return "Stop"

    def turnRight(self) -> str:
        return "Turn Right"

    def turnLeft(self) -> str:
        return "Turn Left"

    def __str__(self):
        return f'Brand: {self.brand}, Class: {self.car_class}, Weight: {self.weight}, Driver: {self.driver}, Motor: {self.motor}'


class Lorry(Car):
    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine, load_capacity: int):
        super().__init__(brand, car_class, weight, driver, engine)
        self.load_capacity = load_capacity

    def __str__(self):
        print()
        print("Info about lorry: ")
        return f'Lorry: {super().__str__()}, Load Capacity: {self.load_capacity}'

class SportCar(Car):
    def __init__(self, brand: str, car_class: str, weight: int, driver: Driver, engine: Engine, speed: int):
        super().__init__(brand, car_class, weight, driver, engine)
        self.speed = speed

    def __str__(self):
        print()
        print("Info about sport car: ")
        return f'Sport Car: {super().__str__()}, Speed: {self.speed}'


driver = Driver("Mark", "Evermind", 5)
engine = Engine(300, "Toyota")
car = Car("Toyota Camry", "Sedan", 1500, driver, engine)

lorry = Lorry("Honda", "Truck", 5000, driver, engine, 10000)

sport_car = SportCar("Ferrari", "Sports", 1200, driver, engine, 300)

print(car)

print(lorry)

print(sport_car)




