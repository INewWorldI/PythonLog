# CSV 파일 읽기 및 쓰기

# CSV = MEME - text/csv

import csv

# 예제1

with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # header skip

    # 객체확인
    print(reader)

    # 타입 확인
    print(type(reader))

    # 속성확인
    print(dir(reader)) #__iter__
    print()

    for c in reader:
        #print(c)
        # 타입 확인 (리스트)
        # print(type(c))
        # list to str
        print(' : '.join(c))


# 예제 2

with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)

#예제 3

with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('-----------')

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

with open('./resource/write1.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt))
    # 타입 확인
    print(type(wt))
    for v in w:
        wt.writerow(v) 


# 예제 5

with open('./resource/write2.csv', 'w', encoding='UTF-8') as f:
    # 필드명
    fields = ['One','Two','Three']

    # Dict Write
    wt = csv.DictWriter(f, fieldnames=fields)
    # Header Writer
    wt.writeheader()

    for v in w:
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})


# 실습 코드 작성

InCode = [['갤럭시 S11', '안드로이드', '삼성전자', '엑시노스 APU'], ['아이폰 11 PRO', 'IOS', '애플', 'A11X'], ['V50', '안드로이드', 'LG전자', '스냅드래곤']]

with open('./resource/phone.csv', 'w', encoding='utf-8') as phone:
    fields = ['모델명', '운영체제', '제조사', '칩셋']

    wtphone = csv.DictWriter(phone, fieldnames=fields)
    wtphone.writeheader()

    for value in InCode:
        wtphone.writerow({'모델명' : value[0], '운영체제' : value[1], '제조사' : value[2], '칩셋' : value[3]})

    