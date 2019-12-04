a = [1, 2, 3]

print("a : " + ", ".join(repr(a)[1:-1].split(", ")))

b = a

print("b : " + ", ".join(repr(b)[1:-1].split(", ")))

a[0] = 'surprise'

print("a : " + ", ".join(repr(a)[1:-1].split(", ")))
print("b : " + ", ".join(repr(b)[1:-1].split(", ")))

b[0] = 'I hate surprises'

print("a : " + ", ".join(repr(a)[1:-1].split(", ")))
print("b : " + ", ".join(repr(b)[1:-1].split(", ")))

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'integer lists are boring'
b[0] = 'I am b'

print("a : " + ", ".join(repr(a)[1:-1].split(", ")))
print("b : " + ", ".join(repr(b)[1:-1].split(", ")))
print("c : " + ", ".join(repr(c)[1:-1].split(", ")))
print("d : " + ", ".join(repr(d)[1:-1].split(", ")))