# 파이썬 사용자 입력
# input 사용법 / 기본타입(str)

# 예제1

#name = input("Enter Youre Name: ")
#grade = input("Enter Youre Grade : ")
#company = input("Enter Youre Company : ")

#print(name, grade, company)

# 예제 2

#number = input("Enter numbers : ")
#name = input("Enter name : ")

#print('type number :', number * 3)
#print('type name:', name)

# 예제 3

#first_number = int(input('Enter numbers :'))
#secend_numbet = int(input('Enter numbers :'))

#total = first_number + secend_numbet
#print("총 합의 수는? :", total)

# 예제 4

float_number = float(input("Enter a float numbers : "))

print('input for number :', float_number)
print('type :', type(float_number))

# 예제 5

print('FirstName - {0}, LastName - {1}'.format(
    input("Enter a First Name : "), input("Enter a Secend Name : ")))
