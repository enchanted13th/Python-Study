class Element() :
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return str({'name':self.name, 'symbol':self.symbol, 'number':self.number})
    def dump(self):
        print('name : ', self.name, ', symbol : ', self.symbol, ', number : ', self.number)



elem = Element('Hydrogen', 'H', 1)
print('elem : ', elem)

elem_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
elem2 = Element(**elem_dict)
print('elem2 : ', elem2)

hydrogen = Element('Hydrogen', 'H', 1)
print('dump() : ', end='')
hydrogen.dump()
print('__str__ : ', hydrogen)