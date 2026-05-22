class Vehicle:
    vehivles = []

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.vehivles.append(self)

    @classmethod
    def total_vehicles(cls):
        return len(cls.vehivles)

vehicle1 = Vehicle("Toyota", "Camry", 2020)
vehicle2 = Vehicle("Honda", "Civic", 2019)

print(f"Total vehicles: {Vehicle.total_vehicles()}")
