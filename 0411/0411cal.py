'''
정수 2개와 연산자 1개(+,-,*,/)를 입력 받아
사칙연산을 수행하는 프로그램 작성
'''

num1=int(input('첫번째 숫자: '))
op=input('연산자: ')
num2=int(input('두번째 숫자: '))
if op=="+":
    print(num1+num2)
if op=="-":
    print(num1-num2)
if op=="*":
    print(num1*num2)
else:
    print(num1/num2)
print()
