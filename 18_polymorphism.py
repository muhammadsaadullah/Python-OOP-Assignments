class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches can't fly.")

obj = Bird()
obj.intro()
obj.flight()

obj2 = Ostrich()
obj2.intro()
obj2.flight()