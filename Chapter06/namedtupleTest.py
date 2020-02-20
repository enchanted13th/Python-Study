from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

print('duck : ', duck)
print('duck.bill : ', duck.bill)
print('duck.tail : ', duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
# **parts : 키워드 인자
duck2 = Duck(**parts)
print('duck2 : ', duck2)

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print('duck3 : ', duck3)

duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print('duck_dict : ', duck_dict)

duck_dict['color'] = 'green'
print('duck_dict : ', duck_dict)