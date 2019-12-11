e2f = { 'dog' : 'chien',
        'cat' : 'chat',
        'walrus' : 'morse',
      }

print(e2f)
print(e2f['walrus'])

e2f_list = list(e2f.items())
f2e = {}

for eng, france in e2f_list :
    f2e[france] = eng

print(f2e['chien'])

print(e2f.keys())

life = { 'animals' : { 'cats' : 'Henri',
                       'octopi' : 'Grumpy',
                       'emus' : 'Lucy',
                     },
         'plants' : {},
         'other' : {},
       }

print(life.keys())
print(life.get('animals').keys())
print(life['animals']['cats'])
