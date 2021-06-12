# 파이썬 튜플
# 튜플 자료형 (순서O, 중복O, 수정X, 삭제X) 불변하는 자료

# 선언
a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱

print(">>>>>>>>>>>")
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1])
print('e -', e[-1][1])
print('e -', list(e[-1][1]))

# 수정 x
# d[0] = 1500

# 슬라이싱
print('>>>>>>>>>>')
print('d -', d[0:3])
print('d -', d[2:])
print('d -', d[2][1:3])

# 튜플 연산

print('>>>>')
print('c + d', c + d)
print('c * e', c * 3)

# 튜플 함수

a = (5, 2, 3, 1, 4)
print('a -', a)
print('a -', a.index(3))
print('a -', a.count(2))

# 팩킹과 언팩킹

# 팩킹

t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 패킹 & 언패킹

t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
