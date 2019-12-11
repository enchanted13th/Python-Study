disaster = True
if disaster : print("Woe!")
else : print("Whee!")

furry = True
small = True
if furry :
    if small : print("It's a cat.")
    else : print("It's a bear")
else :
    if small : print("It's a skink!")
    else : print("It's a human. Or a hairless bear.")

color = "puce"
if color == "red" :
    print("It's a tomato")
elif color == "green" :
    print("It's a green pepper")
elif color == "bee purple" :
    print("I don't know what it is, but only bees can see it")
else :
    print("I've never heard of the color", color)

x = 7

print(x == 5)
print(x == 7)
print(5 < x)
print(x < 10)

print(5 < x and x < 10)
print((5 < x) and (x < 10))

print(5 < x or x < 10)
print(5 < x and x > 10)
print(5 < x and not x > 10)

print(5 < x < 10)
print(5 < x < 10 < 999)

some_list = []
if some_list :
    print("There's something in here")
else :
    print("Hey, it's empty!")