number_list = [ 3, 2, 1, 0 ]
for value in number_list :
    print(value)

# List Comprehension
even_list = [ number for number in range(10) if number % 2 == 0]
print(even_list)

# Dictionary Comprehension
squares = { number : number * number for number in even_list }
print(squares)

# Set Comprehension
odd_set = { number for number in range(10) if number % 2 != 0 }
print(odd_set)

# Generator Comprehension
number_thing = ( number for number in range(10) )
for number in number_thing :
    print('Got', number)