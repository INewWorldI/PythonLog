# chapter02_03 파이썬 객체지향 프로그래밍(oop) 
# 코드의 재사용, 코드 중복 방지 
# 규모가 큰 프로젝트(프로그램) -> 함수 중심으로 코딩 -> 데이터 방대 -> 복잡해진다
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class car():
    """
    Car class
    Author: Kim
    Data: 2021.08.14
    Desccripton: Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0


    def __init__(self, company, details):
        self._company = company
        #self.car_count = 10
        self._details = details

    def __str__(self):
        return 'str : {} {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} {}'.format(self._company, self._details)

    # Instance Method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID: {} '.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))

    def get_price(self):
        return 'Befor Car price -> company : {}, price : {} '.format(self._company, self._details.get('price'))


    def get_price_culc(self):
        return 'After Car price -> company : {}, price : {} '.format(self._company, float(self._details.get('price')) * car.price_per_raise)

    # 클래스 메소드
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Plz enter 1 or more')
            return
        cls.price_per_raise = per
        print('Succes price increed')

    # 스테이틱 메소드
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'Ok This car is {}'.format(inst._company)
        return 'Sorry is not Bmw'

# self 의미
car1 = car('Ferrai', {'color': 'white', 'horsepower': '400', 'price': '8000'})
car2 = car('BMW', {'color': 'black', 'horsepower': '370', 'price': '5000'})


# 젼체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접접근)
print(car1._details.get('price'))
print(car2._details.get('price'))

# 가격 정보(인상전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상 (직접 설정)
car.price_per_raise = 1.4

# 가격 정보(인상후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상 (클래스 메소드 사용)
car.raise_price(1.6)

# 가격 정보(인상후)
print(car1.get_price_culc())
print(car2.get_price_culc())


# 스테이틱 메소드 (간접 호출)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 스테이틱 메소드 (직접호출)
print(car.is_bmw(car1))
print(car.is_bmw(car2))