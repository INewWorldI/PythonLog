# chapter02_01 파이썬 객체지향 프로그래밍(oop) 
# 코드의 재사용, 코드 중복 방지 
# 규모가 큰 프로젝트(프로그램) -> 함수 중심으로 코딩 -> 데이터 방대 -> 복잡해진다
# 클래스 중심 -> 데이터 중심 -> 객체로 관리


# 일반적인 코딩
# 차량1

car_company_1 = 'ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': '400'},
    {'price': '8000'}
]

#차량2
car_company_2 = 'bmw'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': '270'},
    {'price': '5000'}
]

#차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': '300'},
    {'price': '6000'}
]

# 리스트 구조
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': '400', 'price': '8000'},
    {'color': 'Black', 'horsepower': '270', 'price': '5000'},
    {'color': 'Silver', 'horsepower': '300', 'price': '6000'}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외처리 등

car_dict = [
    {'car_company': 'Ferrai', 'car_detail': {'color': 'white', 'horsepower': '400', 'price': '8000'}},
    {'car_company': 'BMW', 'car_detail': {'color': 'black', 'horsepower': '370', 'price': '8000'}},
    {'car_company': 'Audi', 'car_detail': {'color': 'silver', 'horsepower': '300', 'price': '8000'}}
]

del car_dict[1]
print(car_dict)

print()
print()

# 클래스 구조
# 구조 설계후 재사용성 증가 코드 반복 최소화 메소드 활용

class car():
    def __init__(self, company, detaills):
        self._company = company
        self._detaills = detaills

    def __str__(self):
        return 'str : {} {}'.format(self._company, self._detaills)

    def __repr__(self):
        return 'repr : {} {}'.format(self._company, self._detaills)



car1 = car('Ferrai', {'color': 'white', 'horsepower': '400', 'price': '8000'})
car2 = car('BMW', {'color': 'black', 'horsepower': '370', 'price': '8000'})
car3 = car('Audi', {'color': 'silver', 'horsepower': '300', 'price': '8000'})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()
print()

car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복문(__str__)
for x in car_list:
    #print(repr(x))
    print(x)
    