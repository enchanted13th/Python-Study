class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
print(fowl.name)
print(fowl.get_name())

fowl.name = 'Daffy'
print(fowl.name)

fowl.set_name('Daffy')
print(fowl.name)

print()

class DecoDuck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = DecoDuck('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)

print()

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.diameter)
# c.diameter = 20

print()

class PrivateDuck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = PrivateDuck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
# print(fowl.__name)
print(fowl._PrivateDuck__name)