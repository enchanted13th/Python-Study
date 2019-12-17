def do_nothing() :
    pass

do_nothing()

def make_a_sound() :
    print('quack')

make_a_sound()

def agree() :
    return True

if agree() :
    print('Splendid!')
else :
    print('That was unexpected.')

def echo(anything) :
    return anything + ' ' + anything

print(echo('Rumplestiltskin'))

def commentary(color) :
    if color == 'red' :
        return "It's a tomato."
    elif color == 'green' :
        return "It's a green pepper."
    elif color == 'bee purple' :
        return "I don't know what it is, but only bees can see it."
    else : return "I've never heard of the color " + color + "."

comment = commentary('blue')
print(comment)

comment = print(do_nothing())
print(type(comment))

thing = None
if thing :
    print("It's some thing")
else :
    print("It's no thing")

if thing is None :
    print("It's nothing")
else :
    print("It's something")

def is_none(thing) :
    if thing is None :
        print("It's None")
    elif thing :
        print("It's True")
    else :
        print("It's False")

is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())