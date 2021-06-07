import sys
print('p', 't', 'h', 'o', sep='|')

print('010', '2052', '3071', sep='-')

print('python', 'google.com', sep='@')

print('welcom to', end=' ')
print('IT News', end=' ')
print('Web Site')

# File option


print('Learn Python', file=sys.stdout)
print()


# format 사용 (d:정수, s:문자열, f:실수)

print('%s %s' % ('own', 'two'))
print('{} {}'.format('own', 'two'))
print('{1} {0}'.format('one', 'two'))

print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('python study'))

print('{:10.5}'.format('pythonstudy'))

print('%d %d' % (1, 2))
print("{} {}".format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))

print('%f' % (3.1434343434343434343434))
print('{:f}'.format(3.14343434343434343434))
print('%06.2f' % (3.143434343434343434))
print('{:06.2f}'.format(3.1434343434343434343))

print('=====예제 테스트=====')

print('%5s' % ('nice'))
print('{:>5}'.format('nice'))

print('%-5s' % ('nice'))
print('{:<5}'.format('nice'))

print('%05.2f' % (365.21432423))
print('{:05.2f}'.format(365.21432423))
