def document_it(func) :
    def new_function(*args, **kwargs) :
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def square_it(func) :
    def new_function(*args, **kwargs) :
        result = func(*args, **kwargs)
        return result * result
    return new_function

def add_ints(a, b) :
    return a + b

print(add_ints(3, 5), '\n')

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)
print()

@document_it
def add_ints2(a, b) :
    return a + b

print(add_ints2(3, 5), '\n')

@document_it
@square_it
def add_ints3(a, b) :
    return a + b

print(add_ints3(3, 5), '\n')

@square_it
@document_it
def add_ints4(a, b) :
    return a + b

print(add_ints4(3, 5), '\n')