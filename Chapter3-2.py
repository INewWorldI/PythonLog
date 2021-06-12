# 파이썬 문자열

str1 = "i am python"
str2 = 'Python'
str3 = '''How are yoy'''
str4 = """ Thank you """

print(type(str1), type(str2), type(str3), type(str4))

str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용

print("I'm Boy")
print('I\'m boy')

print('a \t b')
print('a \n b')
print(' a \" \" b ')


escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = "What\'s on Tv"
print(escape_str2)

t_s1 = "Click \t Start"
t_s2 = "New Line\n Check"
print(t_s1)
print(t_s2)

row_s1 = r'D:\python\test'
print(row_s1)

# 멀티 라인 입력

multi_str = \
    """
문자열
멀티라인 입력
테스트
"""
print(multi_str)

# 문자열 연산

str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환

print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수

print("Capitalize", str_o1.capitalize())
print("endswith", str_o2.endswith("e"))
print("replace", str_o1.replace("thon", "Good"))
print("sorted", sorted(str_o1))
print("split", str_o4.split(' '))

# 반복 시퀀스

im_str = "Goob Boy!"

print(dir(im_str))  # __iter__

for i in im_str:
    print(i)

# 슬라이싱

str_sl = "Nice Python"

# 슬라이싱 연습

print(str_sl[0:3])
print(str_sl[5:])
print(str_sl[:len(str_sl)])
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])

# 아스키 코드 or 유니코드

a = 'z'
print(ord(a))
print(chr(122))
