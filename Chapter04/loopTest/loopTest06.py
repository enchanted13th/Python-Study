cheeses = []
for cheese in cheeses :
    print('This shop has some lovely', cheese)
    break
else :
    print('This is not much of a cheese shop, is it?')

print()

found_one = False
for cheese in cheeses :
    found_one = True
    print('This shop has some lovely', cheese)
    break
if not found_one :
    print('This is not much of a cheese shop, is it?')