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

class Element2() :
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def symbol(self):
        return self.__symbol
    @symbol.setter
    def symbol(self, symbol):
        self.__symbol = symbol

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number):
        self.__number = number

    def __str__(self):
        return str({'name':self.__name, 'symbol':self.__symbol, 'number':self.__number})

elem2 = Element2('name2', 'n', 22)
print(elem2)

elem2.name = 'modifyName'
elem2.symbol = 'modifySymbol'
elem2.number = '0'
print(elem2)

