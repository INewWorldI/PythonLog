# 파이썬 외장 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random

# 예제1
import sys
print(sys.argv)

# 예제2 (강제종료)
# sys.exit()

# 예제3
print(sys.path)

# pickle : 객체 파일 쓰기
import pickle

# 예제4
f = open("test.obj", 'wb')
obj = {1 : 'python', 2 : 'study', 3 : 'basic'}
pickle.dump(obj, f)
f.close()

# 예제5
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close

# os : 환경 변수, 디렉터리(파일) 처리 관련, 운영체제 작업 관련
# mkdir rmdir (비어 있으면 삭제), rename

# 예제6
import os
print(os.environ)
print(os.environ["USERNAME"])

# 예제7
print(os.getcwd())

# time : 시간 관련 처리
import time
# 예제8
print(time.time())

# 예제9
print(time.localtime(time.time()))

# 예제10
print(time.ctime())

# 예제11(형식표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', ))

# 예제12(시간간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random : 난수 리턴
import random

# 예제 13
print(random.random())

# 예제14
print(random.randint(1,45))
print(random.randrange(1,45))

# 예제15
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# 예제16
c = random.choice(d)
print(c)


# webbrowser : 본인 OS의 웹 브라우저 실행
import webbrowser

# 예제 17
webbrowser.open("http://naver.com")
webbrowser.open_new("http://google.com")