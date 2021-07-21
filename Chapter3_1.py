# Chapter3-1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타임

import math
str1 = "Python"
bool = True
str2 = 'anaconda'
float_v = 10.0  # 10 == 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)
set = {7, 8, 9}

# 데이터 타입

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

"""
+
-
*
/
// : 몪
% : 나머지
abs(x) : 절대값
pow(x, y) : x ** y -> 2 ** 3 
"""

# 정수 선언

i = 77
i2 = -14
big_int = 777777777777777778888888888888888

# 정수 출력

print(i)
print(i2)
print(big_int)

# 실수 출력

f = 0.999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습

i1 = 39
i2 = 939
big_int1 = 324328043298904328904381904
big_int2 = 233381030912380123813
f1 = 1.234
f2 = 3.939

# 계산 실습

print('>>>>>+>>>>')
print("i1 + i2 =", i1 + i2)
print("f1 + f2 =", f1 + f2)
print('big_int1 + big_int2 =', big_int1 + big_int2)
print()

print('>>>>>->>>>')
print("i1 - i2 =", i1 - i2)
print("f1 - f2 =", f1 - f2)
print('big_int1 - big_int2 =', big_int1 - big_int2)
print()

print('>>>>>*>>>>')
print("i1 * i2 =", i1 * i2)
print("f1 * f2 =", f1 * f2)
print('big_int1 * big_int2 =', big_int1 * big_int2)
print()

print('>>>>>/>>>>')
print("i1 / i2 =", i1 / i2)
print("f1 / f2 =", f1 / f2)
print('big_int1 / big_int2 =', big_int1 / big_int2)
print()

print('>>>>>//>>>>')
print("i1 // i2 =", i1 // i2)
print("f1 // f2 =", f1 // f2)
print('big_int1 // big_int2 =', big_int1 // big_int2)
print()

# 형 변환

a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력

print(type(a), type(b), type(c), type(d))

# 형 변환

print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))
print(complex('3'))  # 복소수는 정수를 써야해서 문자열을 정수형으로 변환
print(complex(False))


# 수치 연산 함수

print(abs(-7))

x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3), 5 ** 3)

print(math.pi)
print(math.ceil(5.1))


# 추가 실습

str_11 = 35
float_11 = 35.2
big_int11 = 21401129840103781738923
tuple11 = ('Fire', 'Water', 'Eras', 'Wind')
dict11 = {
    "4대 원소": "4대 원소에 대한 설명",
    "불": "그냥 불",
    "불": "그냥 불",
    "불": "그냥 불",
    "불": "그냥 불"
}

print(type(str_11), type(float_11), type(
    big_int11), type(tuple11), type(dict11))

alpha = 50
beta = 50
bravo = 30
delta = 70
asset = 5
gamma = 34

print('사칙 연산 테스트')
print("alpha + beta =", alpha + beta)
print("beta - bravo =", beta - bravo)
print("delta * bravo =", delta * bravo)
print("beta / asset =", beta / asset)
print("gamma // asset", gamma // asset)

a = 7
b = 3.14
c = 4324.321314141
d = 3141412897973246325234586131
e = True

print('형 변환 테스트')
print(int(b))
print(float(e))
