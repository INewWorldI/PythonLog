# 파일 읽기 및 쓰기

# 읽기모드 : r , 쓰기모드 : w , 추가모드 : a , 텍스트모드 : t , 바이너리모드 : b
# 상대경로 ('../, ./') 절대경로('.C:path/path/parh..')

# 파일 읽기
# 예제 1

f = open('./resource/it_news.txt', 'r', encoding='utf-8')

# 속성확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 확인
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 종료
f.close()

# 예제 2

with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제 3
# read() : 전체 읽기, read(10) : 10 Byte 읽기

with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()


# 예제 4
# readline() 한줄 한줄 읽어오는 함수

with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

    print()

# 예제 5
# readlines : 전체를 읽은 후 라인 단위로 텍스트를 저장

with open('./resource/it_news.txt', 'r', encoding='utf-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

    print()


# 파일 쓰기 (Write)

# 예제1

with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2

with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')

# 예제3
# writelines : 리스트 -> 파일

with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제4

with open('./resource/contents2.txt', 'w') as f:
    print('Test Text Write1', file=f)
    print('Test Text Write1', file=f)
    print('Test Text Write1', file=f)

# 실습 코드

with open('./resource/vocaloid.txt', 'w', encoding='EUC-KR') as vc:
    input_text = ['하츠네 미쿠\n', '카가미네 린\n', '카가미네 렌\n', '메구리네 루카\n', '이아\n', '루오 티엔이\n'] 
    vc.writelines(input_text)

