# 파이선 예외 처리의 이해
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로 예외는 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리해야한다
# 2. 로그는 반드시 남긴다
# 3. 예외는 던져진다
# 4. 예외 무시

# SyantaxError

# 문법오류
#print('error)
#print('error'))
#if True
#     pass

#NameError
#a = 10
#b = 15
#print(c)

#ZeroDivisionError
#print(100 / 0)

# IndexError

x = [50, 70, 90]
#print(x[1])
#print(x[4])
#print(x.pop())
#print(x.pop())
#print(x.pop())
#print(x.pop())

# KeyError
#dic = {'name' : 'Lee', 'Age' : 41, 'City' : 'Busan'}
#print(dic['hobby'])
#print(dic.get('hobby'))

# 예외 없는것을 가정하고 프로그램 작성 -> 런타임 예외 발생시 예외 처리 권장(EAPP)

# AttuributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
#print(time.time2())

# ValueError 
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError

# f = open('text.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행하는 경우
x = [1, 3]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y))

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try : 블럭의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['kim', 'lee', 'park']

# 예제1

# try: 
#     z = 'cho'
#     x = name.index(z)
#     print('{} Found it! {}'.format(z, x + 1))
# except ValueError:
#     print('Not Found it - Occurred ValueError!')
# else:
#     print('Ok Else')

# print()

# print('pass')

# 예제2

# try: 
#     z = 'cho'
#     x = name.index(z)
#     print('{} Found it! {}'.format(z, x + 1))
# except Exception:
#     print('Not Found it - Occurred ValueError!')
# else:
#     print('Ok Else')

# print()

# print('pass')

# 예제3

# try: 
#     z = 'kim'
#     x = name.index(z)
#     print('{} Found it! {}'.format(z, x + 1))
# except Exception as e:
#     print(e)
#     print('Not Found it - Occurred ValueError!')
# else:
#     print('Ok Else')
# finally:
#     print('Ok! Finally')

# print()

# print('pass')

# 예제 4

try:
    a = 'Paek'
    if a == 'Kim':
        print('Ok Pass!')
    else:
        raise ValueError
except ValueError:
    print('Value Error')
else:
    print('Ok Else!')
