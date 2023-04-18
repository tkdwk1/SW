'''
2023-04-28
김태환
'''
num1=int(input("첫번째 숫자를 입력해주세요 :"))
num2=int(input("두번째 숫자를 입력해주세요 :"))

if num1%num2==0:
    print("{}는 {}의 약수입니다.".format(num2,num1))
else:
    print("{}는 {}의 약수가 아닙니다.".format(num2,num1))