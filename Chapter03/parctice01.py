year_lists = [ 1980, 1981, 1982, 1983, 1984]
year_lists.sort()

print(year_lists[2])
print(year_lists[-1])

print()

things = [ 'mozzarella', 'cinderella', 'salmonella' ]
for name in things :
   print(name[0].upper() + name[1:])

print(things)

for name in things :
   print(name.upper())

del things[1]

print(things)

surprise = [ 'Groucho', 'Chico', 'Harpo' ]
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1][0].upper() + surprise[-1][1:]
print(surprise)