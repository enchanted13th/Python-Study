class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

print(Bear().eats())
print(Rabbit().eats())
print(Octothorpe().eats())

class Robot():
    def does(self):
        pass

class Laser(Robot):
    def does(self):
        return 'disintegrate'

class Claw(Robot):
    def does(self):
        return 'crush'

class SmartPhone(Robot):
    def does(self):
        return 'ring'

robot = Laser()
print(robot.does())

robot = Claw()
print(robot.does())

robot = SmartPhone()
print(robot.does())