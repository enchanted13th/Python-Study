# Namespace & Scope
animal = 'fruitbat'
def print_global() :
    print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

# Error
# def change_and_print_global() :
#     print('inside change_and_print_global:', animal)
#     print('after the change:', animal)
#
# change_and_print_global()

def change_local() :
    animal = 'wombat'
    print('inside change_local', animal, id(animal))

change_local()
print(animal, id(animal))

def change_and_print_global() :
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

change_and_print_global()

def change_local() :
    animal = 'wombat'
    print('locals:', locals())

animal = 'fruitbat'

change_local()

print('globals:', globals())
print(animal)
