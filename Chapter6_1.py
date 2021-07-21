# 파이썬 클래스
# OOP 객체 지향 프로그래밍, self,  인스턴스, 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 접근 가능
# 인스턴스 변수: 객체마다 별도로 존재

# 예제 1

class Dog:  # objact 상속
    # 클래스 속성
    spacies = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성

print("{} is {} and {} is {}".format(a.name, a.age, b.name, b.age))

if a.spacies == 'firstdog':
    print("{0} is a {1}".format(a.name, a.spacies))

print(Dog.spacies)
print(a.spacies)
print(b.spacies)

# 예제 2
# self의 이해


class selftest:
    def func1():
        print('func1 calld')

    def func2(self):
        print(id(self))
        print('func2 calld')


f = selftest()

print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()
selftest.func1()

# selftest.func2() # 예외
selftest.func2(f)

# 예제 3
# 클래스 변수와 인스턴스 변수


class Warehouse:
    # 클래스 변수
    stock_num = 0  # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('After', Warehouse.__dict__)

# 예제 4


class Dog:  # objact 상속
    # 클래스 속성
    spacies = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speake(self, sound):
        return '{} says {}!'.format(self.name, sound)


# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Mary', 10)
# 메소드 호출
print(c.info())
# 메소드 호출
print(c.speake('Wal Wal'))
print(d.speake('Mang Mang'))


print('>>>>> 실습 구현 >>>>>')


class vocaloid():

    popularity_point = 0

    def __init__(self, name, enginver, birth, popularity):
        self.name = name
        self.enginver = enginver
        self.birth = birth
        self.popularity = popularity
        vocaloid.popularity_point += 1


miku = vocaloid("Hatsune Miku", "V2/V3/V4X/NT", "070831", "WORLD TOP")
lin = vocaloid("Kagamine Lin", "V2/V4X", "071227", "TOP")

print("보컬로이드명: {} \n 보컬로이드 엔진: {} \n 보컬로이드 출시일: {} \n 인기도: {}"
      .format(miku.name, miku.enginver, miku.birth, miku.popularity))

print(miku.popularity_point)
print(vocaloid.popularity_point)
