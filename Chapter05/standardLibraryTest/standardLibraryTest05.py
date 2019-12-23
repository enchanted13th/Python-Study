import itertools

for item in itertools.chain([ 1, 2 ], [ 'a', 'b' ]) :
    print(item)

print()

# Loop
# for item in itertools.cycle([ 1, 2 ]) :
#     print(item)

for item in itertools.accumulate([ 1, 2, 3, 4 ]) :
    print(item)

print()

def multiply(a, b) :
    return a * b

for item in itertools.accumulate([ 1, 2, 3, 4 ], multiply) :
    print(item)
