# Dziedziczenie jako realizacja zasady DRY - Don't Repeat Yourself
# Inheritance (IS-A) relacja typu jest, dziedziczenie
class Animal:
    def say_hi(self):
        print("Hi")


# Krowa i koń dziedziczą po rodzicu metodę say_hi
class Cow(Animal):
    pass


class Horse(Animal):
    pass


# Żólw nadpisuje metodę rodzica say_hi
class Turtle(Animal):
    def say_hi(self):
        print("Hello!")


# Kurczak rozbudowuje metodę rodzica say_hi
class Chicken(Animal):
    def say_hi(self):
        super().say_hi()
        print("No i hello!")


################################################

cow1 = Cow()
cow1.say_hi()

horse1 = Horse()
horse1.say_hi()

turtle1 = Turtle()
turtle1.say_hi()

chicken1 = Chicken()
chicken1.say_hi()
