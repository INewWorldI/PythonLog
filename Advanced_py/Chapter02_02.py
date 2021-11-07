class car():
    """
    Car class
    Author: Kim
    Data: 2021.08.14
    """
    car_count = 0


    def __init__(self, company, details):
        self._company = company
        #self.car_count = 10
        self._details = details
        car.car_count += 1

    def __str__(self):
        return 'str : {} {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID: {} '.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))

    def __del__(self):
        car.car_count -= 1

# self 의미
car1 = car('Ferrai', {'color': 'white', 'horsepower': '400', 'price': '8000'})
car2 = car('BMW', {'color': 'black', 'horsepower': '370', 'price': '8000'})
car3 = car('Audi', {'color': 'silver', 'horsepower': '300', 'price': '8000'})


# ID 값
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(car1.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))

# 에러
#car.detail_info()
car.detail_info(car1)

# 공유확인
print(car1.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(car.car_count)

del car2
# 삭제확인
print(car1.car_count)
print(car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수)