'''
2023-05-10
김태환
#문제분석
    변수 숫자(num)
#알고리즘
    1.변수 초기화
        num변수에 정수 입력
    2.논리(중첩 반복)
        (반복) for i in range(1,num+1): #줄 반복
            (반복) for i in range(1,i+1): #별 찍기
'''
num=int(input("정수 입력:"))
for i in range(1,num+1):
    for i in range(1,i+1):
        print("*",end="")
