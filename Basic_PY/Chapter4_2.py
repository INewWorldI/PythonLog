# 파이썬 반복문
# for 실습

# for in <collection>
#         <loop body>

for v1 in range(10):
    print('v1 is', v1)

for v2 in range(1, 11):
    print('v2 is', v2)

for v3 in range(1, 11, 3):
    print('v3 is ', v3)

print()

sum1 = 0

for v in range(4, 1001, 4):
    sum1 += v

print('1 ~ 1000 Sum:', sum1)
print('1 ~ 1000 Sum:', sum(range(1, 1001)))
print('1 ~ 1000 4의 배수의 합:', sum(range(4, 1001, 4)))


# iterables
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterables 리턴함수 : range, reversed, enumerate, filter, map, zip

names = ['kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are :', n)

lotto_number = [11, 19, 21, 28, 36, 37]

for n in lotto_number:
    print('Current Numbers :', n)

word = 'butiful'

for n in word:
    print('word:', n)


my_info = {
    "name": "Lee",
    "age": 33,
    "city": "Seoul"
}

for key in my_info:
    print('key :', my_info[key])

for v in my_info.values():
    print('value :', v)

# 예제 5

name = 'FineAppLE'
n_name = ''

for n in name:
    if n.isupper():
        n_name += n
    else:
        n_name += n.upper()
print('전체 출력:', n_name)


# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34')
        break
    else:
        print('Not Found', num)

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("cureent type :", v, type(v))
    print("multiply by 2:", v * 3)


# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 3:
        print("Found  : 3")
        break
else:
    print('Not Found : 3')


# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print("{:4d}".format(i * j), end="")
    print()

# 변환 예제

name2 = 'Aceman'

print("Reversed", reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))
