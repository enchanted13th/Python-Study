periodic_table = { 'Hydrogen' : 1, 'Helium' : 2 }
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)

def no_idea() :
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

bestiary = defaultdict(lambda: 'Huh Huh?')
print(bestiary['E'])

from collections import defaultdict
food_counter = defaultdict(int)
for food in [ 'spam', 'spam', 'eggs', 'spam' ] :
    food_counter[food] += 1

for food, count in food_counter.items() : 
    print(food, count)

print()

# defaultdict 가 아닌 경우
dict_counter = {}
for food in [ 'spam', 'spam', 'eggs', 'spam' ] :
    if not food in dict_counter :
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items() :
    print(food, count)
