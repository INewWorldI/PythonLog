# 파이썬 리스트
# 핵심은 순서 중복 수정 삭제가 가능한 자료형

# 선언

a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captin']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.1459]

# 인덱싱
print('>>>>>>>>>>>>>>>')
print('d - ', type(d), d)
print('d -', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e -', e[-1][1])
print('e -', list(e[-1][1]))

print('>>>>>>>>>>>>>>>')
# 슬라이싱

print('d - ', d[0:3])
print('d -', d[2:])
print('e -', e[-1][1:3])

# 리스트 연산
print('>>>>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print('Test + c[0]', 'Test' + str(c[0]))

# 값 비교
print('>>>>>>>>>>')
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정
print('>>>>>>>>>>>>>>>>>>>')

c[0] = 4
print('c - ', c)

c[1:2] = ['a', 'b', 'c']  # [['a', 'b', 'c']]
print('c', c)

c[1] = ['a', 'b', 'c']
print('c', c)

c[1:3] = []
print('c', c)

del c[2]
print('c -', c)

a = [5, 2, 3, 1, 4]
print('>>>>>>>>>>>>>>>>>>>>>>>')
print('a -', a)
a.append(10)
print('a -', a)
a.sort()
print('a -', a)
a.reverse()
print('a -', a)
print('a', a.index(3), a[3])
a.insert(2, 7)
print('a -', a)
a.reverse()
print('a -', a)
# del a[6] 예약어
# print('a -', a)
a.remove(10)
print('a -', a)

print('a -', a)
print('a -', a.pop())
print('a -', a)
print('a -', a.pop())
print('a -', a)
print('a', a.count(4))
print()
ex = [8, 9]
a.extend(ex)
print('a -', a)

# 삭제 : remove , pop, del

while a:
    data = a.pop()
    print(data)

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while list_num:
    num_data = list_num.pop()
    print('순차 출력:', num_data)
