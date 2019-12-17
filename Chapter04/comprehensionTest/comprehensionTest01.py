# List Comprehension
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)

print(number_list)

print()

number_list.clear()
for number in range(1, 6) :
    number_list.append(number)
print(number_list)

print()

number_list.clear()
number_list = list(range(1, 6))
print(number_list)

print()

number_list.clear()
number_list = [number for number in range(1,6)]
print(number_list)

print()

number_list.clear()
number_list = [number-1 for number in range(1,6)]
print(number_list)

print()

a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)

print()

a_list = []
for number in range(1,6) :
    if number % 2 == 1 :
        a_list.append(number)
print(a_list)

print()

rows = range(1, 4)
cols = range(1, 3)
for row in rows :
    for col in cols :
        print(row, col)

print()

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells :
    print(cell)

print()

for row, col in cells :
    print(row, col)