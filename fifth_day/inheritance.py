class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
    
    def seating_capacity(self, capacity):
        return f"The seating capacity {self.name} {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=100):
        return super().seating_capacity(capacity=100)


School_bus = Bus("School bus", 180, 12)
print(School_bus.seating_capacity())