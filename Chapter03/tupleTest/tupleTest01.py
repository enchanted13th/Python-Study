empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

# Tuple Unpacking
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print("a : " + a, "b : " +  b, "c : " + c)

password = 'swordfish'
icecream = 'tuttifrutti'

password, icecream = icecream, password
print("password : " + password)
print("icecream : " + icecream)

marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))