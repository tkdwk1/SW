'''
2023-05-09
김태환
#문제정의
    입력받은 숫자의 팩토리얼 값 계산하기
#문제분석
    변수 숫자(num1), 팩토리얼(fac)
#알고리즘
    1.변수 초기화
        num 변수에 정수입력
    2.프로그램 논리 (반복 for)
        for i in range(num,0,-1):
            fac=fac*i
'''
num=int(input("팩토리얼 숫자 입력:"))
fac=1
for i in range(num,0,-1):
    fac=fac * i
print("{}의 팩토리얼 값은: {}".format(num,fac))