class Robot:
    """Represents a robot, with a name."""
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot. Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(myclassObj):
        """Prints the current population."""
        print("We have {:d} robots.".format(myclassObj.population))


# class end here

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many() #classmethod usage
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()#classmethod usage
print("Robots can do some work here.")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()#classmethod usage


