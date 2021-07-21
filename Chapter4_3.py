# 파이썬 흐름제어문
# while <expr>:
#     <statemant(s)>

# 예제1

n = 5

while n > 0:
    print(n)
    n -= 1

print('>>>>>>>>>>>>>>')

# 예제2

a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

print('>>>>>>>>>>>>>>')

# if 중첩

# 예제3
# continue break

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Enable.')

print('>>>>>>>>>>>>>>')

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Enable.')

print('>>>>>>>>>>>>>>')

# 예제5

i = 1

while i <= 10:
    print('i :', i)
    if i == 6:
        break
    i += 1

print('>>>>>>>>>>>>>')

# 예제6

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')

print('>>>>>>>>>>')

# 예제7

a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        print('find it {:s}'.format(s))
        break
    i += 1
else:
    print('not found in list')

print('>>>>>>>>>>')

# 무한반복
# while True:
#     print('Foo')

while True:
    if not a:
        break
    print(a.pop())
