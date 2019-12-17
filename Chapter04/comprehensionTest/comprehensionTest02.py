# Dictionary Comprehension
word = 'letters'
letter_counts = { letter : word.count(letter) for letter in word }
print(letter_counts)

print()

# Set Comprehension
a_set = { number for number in range(1,6) if number % 3 == 1 }
print(a_set)

print()

# Generator Comprehension
number_thing = ( number for number in range(1,6) )
print(type(number_thing))
for number in number_thing :
   print(number)

print()

number_thing = ( number for number in range(1,6) )
number_list = list(number_thing)
print(number_list)

print()

try_again = list(number_thing)
print(try_again)