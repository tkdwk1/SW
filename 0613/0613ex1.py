'''
2023-06-13
김태환
문제정의
    3개의 매개변수를 전달 받아서 자아 큰 값을 리턴하는 
    findmax(a,b,c)함수 구현
#알고리즘
    1.findmax(a,b,c)함수 선언
        1-1. a,b,c중 가장 큰 값 찾기
    2.num1,num2,num 점수 입력받기
    3.findmax(num1,num2,num3) 호출
    4.리턴 받은 가장 큰 값 출력
'''
def findmax(a,b,c): #함수 선언
    if a>b:
        biggiest=a
    else:
        biggiest=b
    if biggiest<c:
        biggiest=c

    return biggiest #가장 큰 값 반환
num1=int(input("num1: "))
num2=int(input("num2: "))
num3=int(input("num3: "))

biggiest_number=findmax(num1,num2,num3) #함수 호출

print("가장 큰 숫자는:",biggiest_number)
