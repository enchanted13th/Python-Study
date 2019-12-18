def print_args(*args) :
    print('Positional argument tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

print()

def print_more(required1, required2, *args) :
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

print()

def print_kwargs(**kwargs) :
    print('Keywork arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
