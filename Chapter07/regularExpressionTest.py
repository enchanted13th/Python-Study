import re
result = re.match('You', 'Young Frankenstein')
print(result)

youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
print(result)

source = 'Young Frankenstein'
# source 의 시작부터 패턴이 일치하는지 확인
m = re.match('You', source)
if m:
    print(m.group())

# source 가 패턴으로 시작하는지 확인
m = re.match('^You', source)
if m:
    print(m.group())

m = re.match('Frank', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

m = re.findall('n.', source)
print(m)

m = re.findall('n.?', source)
print(m)

m = re.split('n', source)
print(m)

# 일치하는 패턴 대체하기
m = re.sub('n', '?', source)
print(m)

import string
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s', printable))

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall('\w', x))

source = '''I wish I may, I wish I might
            Have a dish of fish tonight.'''
print(re.findall('wish', source))
print(re.findall('wish|fish', source))
print(re.findall('^wish', source))
print(re.findall('^I wish', source))
print(re.findall('fish$', source))
print(re.findall('fish tonight.$', source))

print(re.findall('[wf]ish', source))
print(re.findall('[wsh]+', source))
print(re.findall('ght\W', source))
print(re.findall('I (?=wish)', source))
print(re.findall('(?<=I) wish', source))
print(re.findall('\bfish', source))

m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))