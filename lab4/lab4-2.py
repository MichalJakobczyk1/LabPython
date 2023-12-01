class Turtle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.__x = 0

    def say_name(self):
        print("Hello, I'm: " + self.name + " and my speed is: " + str(self.speed))

    def move(self, distance):
        self.__x += distance
        print(self.name + " moved " + str(distance) + " and now stays on position: " + str(self.__x))

    def get_position(self):
        return self.name + " is on postion: " + str(self.__x)


turtle = Turtle("John", 12)
turtle.say_name()
turtle.move(12)
turtle.move(12)
turtle.move(12)
print(turtle.get_position())
