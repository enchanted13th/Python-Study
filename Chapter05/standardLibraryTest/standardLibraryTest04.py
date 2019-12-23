def palindrome(word) :
    from collections import deque
    dq = deque(word)
    while len(dq) > 1 :
        if dq.popleft() != dq.pop() :
            return False
    return True

print('a :', palindrome('a'))
print('racecar :', palindrome('racecar'))
print(' :', palindrome(''))
print('radar :', palindrome('radar'))
print('halibut :', palindrome('halibut'))

print()

def another_palindrome(word) :
    return word == word[::-1]
print('radar :', another_palindrome('radar'))
print('halibut :', another_palindrome('halibut'))
