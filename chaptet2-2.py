# chapter 2-2 파이썬 기초 > 변수

# 기본 선언

n = 700

print(n)
print(type(n))

# 동시 선언

x = y = z = 700
print(x, y, z)

# 선언
var = 75

# 재선언
var = 'change value'

# 출력
print(var)
print(type(var))

m = 800
n = 600

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800
z = 800
i = 800

print(id(m))
print(id(n))
print(id(m) == id(n) == id(z) == id(i))
print()

# 다양한 변수 선언
# Camel case : numberOfCallgeGradutes

age = 1

Age = 2

aGe = 3

AGE = 4

a_g_e = 5

_age = 6

_AGE_ = 7

# 예약어는 변수로 선언 불가능 if for class 등
