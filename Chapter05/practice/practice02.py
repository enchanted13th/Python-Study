plain = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    }
print(plain)

from collections import OrderedDict
fancy = OrderedDict([
    ( 'a', 1),
    ( 'b', 2),
    ( 'c', 3),
    ])
print(fancy)

from collections import defaultdict
def default_dict() :
    return 'None'
dict_of_lists = defaultdict(default_dict)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])
print(dict_of_lists['b'])
