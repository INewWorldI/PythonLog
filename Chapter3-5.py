# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용

# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언

a = {'name': 'Kim', 'phone': '010-0000-0000', 'key': '870514'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)


# 딕셔너리  출력

print('a -', a['name'])  # 키가 존재하지 않으면 에러 출력
print('a -', a.get('name'))  # 키가 존재하지 않으면 none 로 출력

print('b -', b[0])
print('b -', b.get(0))

print('f -', f.get('City'))
print('f -', f.get('Age'))


# 딕셔너리 추가

a['Address'] = 'seoul'
print('a -', a)
a['rank'] = [1, 2, 3]
print('a -', a)

print(len(a))
print(len(b))
print(len(c))
print(len(d))

# dick_keys, dict_value, dict_items,

print('a -', a.keys())
print('b -', b.keys())
print('c -', c.keys())
print('d -', d.keys())

print('a -', list(a.keys()))
print('b -', list(b.keys()))

print()

print('a -', a.values())
print('b -', b.values())
print('c -', c.values())
print('d -', d.values())

print('a -', list(a.values()))
print('b -', list(b.values()))

print()

print('a -', a.items())
print('b -', b.items())
print('c -', c.items())
print('d -', d.items())

print('a -', list(a.items()))
print('b -', list(b.items()))

print()

print('a -', a.pop('name'))
print('a -', a)

print('c -', c.pop('arr'))
print('c -', c)

print()

print('f -', f.popitem())
print('f -', f)

print('f -', f.popitem())
print('f -', f)

print('f -', f.popitem())
print('f -', f)

print('f -', f.popitem())
print('f -', f)

print('f -', f.popitem())
print('f -', f)


print()

print('a -', 'birth' in a)
print('d -', 'City' in d)

# 수정

a['test'] = 'test_dict'
print('a -', a)

a['Address'] = 'dj'
print('a -', a)

a.update(birth=242414)
print('a -', a)

temp = {'address': 'busan'}
a.update(temp)
print('a -', a)
