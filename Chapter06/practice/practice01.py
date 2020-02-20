class Thing() :
    pass

class Thing2() :
    def __init__(self, letters):
        self.letters = letters

class Thing3() :
    def __init__(self, letters):
        self.letters = letters

example = Thing()

print('Thing() : ', Thing)
print('example : ', example)

example2 = Thing2('abc')
print('example2 : ', example2.letters)

print('Thing3() : ', Thing3('xyz').letters)