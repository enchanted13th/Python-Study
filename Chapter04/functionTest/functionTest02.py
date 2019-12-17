def menu(wine, entree, dessert) :
    return { 'wine' : wine, 'entree' : entree, 'dessert' : dessert }

print(menu('chardonnay', 'chicken', 'cake'))
print(menu('beef', 'bagel', 'bordeaux'))

print()

print(menu(entree = 'beef', dessert = 'bagel', wine = 'bordeaux'))
print(menu('frontenac', dessert = 'flan', entree = 'fish'))