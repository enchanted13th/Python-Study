marxes = ['Groucho', 'Chico', 'Harpo']

sorted_marxes = sorted(marxes)
print("marxes : " + ', '.join(marxes))
print("sorted_marxes : " + ', '.join(sorted_marxes))

print()

marxes.sort()
print("marxes : " + ', '.join(marxes))

numbers = [2, 1, 4.0, 3]
numbers.sort()
print("numbers : " + ', '.join(repr(numbers)[1:-1].split(', ')))

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print("numbers : " + ', '.join(repr(numbers)[1:-1].split(', ')))