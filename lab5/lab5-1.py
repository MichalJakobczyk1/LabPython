class Car():
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model,range):
        super().__init__(brand, model)
        self.range = range

class SportCar(Car):
    def __init__(self, brand, model, max_velocity):
        super().__init__(brand, model)
        self.max_velocity = max_velocity

class ElectricSportCar(ElectricCar, SportCar):
    def __init__(self, brand, model, range, max_velocity):
        ElectricCar.__init__(self, brand, model, range)
        SportCar.__init__(self, brand, model, max_velocity)

    def get_info(self):
        print(f"Brand: {self.brand} \n Model: {self.model} \n Range: {self.range} \n Max velocity: {self.max_velocity}")


car = ElectricSportCar("Tesla", "S Model", 1000, 300)
car.get_info()
