import unicodedata as ud

mystery = '\U0001f4a9'
print(mystery)
print(ud.name(mystery))

pop_bytes = mystery.encode('UTF-8')
print(pop_bytes)

pop_string = pop_bytes.decode('UTF-8')
print(pop_string)