# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다

# 함수 정의 방법

# def function_name(parameter)
#       code

# 예제 1

def first_func(w):
    print("Hello", w)


word = 'GoodBoy'

first_func(word)

# 예제 2


def return_func(w1):
    value = "Hello, " + str(w1)
    return value


x = return_func('GoodBoy2')
print(x)

# 예제 3 (다중반환)


def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


x, y, z = func_mul(10)
print(x, y, z)


def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)


q = func_mul2(20)
print(type(q), q)


def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


p = func_mul3(20)
print(type(p), p, set(p))


def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}


l = func_mul4(30)
print(type(l), l, l.get('v2'), l.items(), l.keys())

# 중요
# *args,

# *args(언패킹)


def args_func(*args):  # 매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('------')


args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Kim', 'Park')

# kwargs(언패킹)


def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('------')


kwargs_func(names1='Lee')
kwargs_func(names1='Lee', name2='Kim')
kwargs_func(names1='Lee', names2='Kim', names3='Joe', sendSMS='False')

# 전체 혼합 예제


def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
    print('args_1 :', args_1)
    print('args_2 :', args_2)
    print('*args :', args)
    print('kwargs :', kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)

# 중첩함수


def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In Func')
    func_in_func(num + 100)


nested_func(100)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수 객체 생성 -> 리소스(메모리 할당)
# 람다는 즉시 실행 함수(Hoap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#    return x * y

#lambda x, y:x*y

# 일반적 함수 할당


def mul_func(x, y):
    return x * y


print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20, 50))


lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))


def func_final(x, y, func):
    print(x * y * func(100, 100))


func_final(10, 20, mul_func_var)
