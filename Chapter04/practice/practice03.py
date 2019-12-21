def good() :
    harry_porter = [ 'Harry', 'Ron', 'Hermione' ]
    return harry_porter

print(good())

def get_odds(first = 0, last = 10, step = 1) :
    number = first
    while number < last :
        if number % 2 != 0 :
            yield number
        number += step

index = 0
for value in get_odds() :
    if index == 2 : print(value)
    index += 1

# Decorator
def test(func) :
    def new_func(*args, **kwargs) :
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

deco = test(good)
deco()