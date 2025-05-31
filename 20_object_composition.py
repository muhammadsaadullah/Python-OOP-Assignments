class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

class Phone:
    def __init__(self, model, battery_capacity):
        self.model = model
        self.battery = Battery(battery_capacity)

p = Phone("Model X", 4000)
print(f"{p.model} with battery {p.battery.capacity}mAh")