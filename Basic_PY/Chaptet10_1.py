# 행맨 미니 게임 제작
# 기본  프로그램 제작 및 테스트

import time

# 처음 인사

name = input("What is youre name?")

print("Hi , " + name, "Time to Play hangman game!")

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# 정답 언어
word = 'secret'

# 추측 단어
guesses = ''

# 기회
turn = 10

# 핵심 whille loop
# 찬스 카운트가 남아 있을 경우

while turn > 0:
    # 실패 횟수(단어 매치수)
    faild = 0 

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측단어 출력
            print(char, end=' ')
        else:
            #단어가 틀린경우 대시로 처리
            print("_", end=' ')
            faild += 1
    # 단어 추측이 성공한 경우 
    if faild == 0:
        print()
        print()
        print('Congratulations! The Guess is current')
        # whild 구문 중단k
        break
    print()

    # 추측단어 문자 단위 입력
    print()
    guess = input('guess a charater') 

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되지 않았으면

    if guess not in word:
        turn -= 1
        # 오류 메세지
        print('Ooops Wrong')
        # 남은 기회 출력
        print('You have', turn, 'More Guesses' )

        if turn == 0:
            # 실패 메세지
            print('You Faild Hangman Game Bye...')
    

