pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Johns' : 'Terry',
    'Palin' : 'Michael',
}

# if 'Cleese' in pythons : print(pythons['Cleese'])
# else : print('Not a Python')

# if 'Marx' in pythons : print(pythons['Marx'])
# else : print('Not a Python')

print(pythons.get('Cleese'))
print(pythons.get('Marx', 'Not a Python'))