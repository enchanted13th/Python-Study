def menu(wine, entree, dessert='pudding') :
    return { 'wine' : wine, 'entree' : entree, 'dessert' : dessert }

print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'doughnut'))

def buggy(arg, result=[]) :
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

def works(arg) :
    result = []
    result.append(arg)
    return result

print(works('a'))
print(works('b'))

def nonbuggy(arg, result=None) :
    if result is None :
        result = []
    result.append(arg)
    print(result)

a_result = []
b_result = []

print(a_result, b_result)

nonbuggy('a', a_result)
nonbuggy('b', b_result)

print(a_result, b_result)