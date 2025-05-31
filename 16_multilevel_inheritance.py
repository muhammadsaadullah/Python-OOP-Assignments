class Grandparent:
    def say(self):
        print("I am the grandparent.")

class Parent(Grandparent):
    def say(self):
        super().say()
        print("I am the parent.")

class Child(Parent):
    def say(self):
        super().say()
        print("I am the child.")

c = Child()
c.say()