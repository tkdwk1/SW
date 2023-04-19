'''
2023-04-19
김태환
입력받은 숫자가 양수, 0 음수인지 판단
#문제분석
    변수-정수(num)
    수식
        num>0 양수
        num<0 음수
#알고리즘
    1.변수 선언
        num에 정수입력 받기
    2.논리(선택)
        if num>0: 
            "양수"
        if num<0: 
            "음수"
        if num==0
            "0"
#알고리즘(다중 if)
    1.변수 선언
        num에 정수입력 받기
    2.논리(선택)
        if num>0: 
            "양수"
        elif num<0:
            "음수"
        else:
            "0"
'''
num=int(input('정수를 입력하세요:'))
if num>0: 
    print("양수")
if num<0: 
    print("음수")
if num==0:
    print("0")

num=int(input('정수를 입력하세요:'))
if num>0: 
    print("양수")
elif num<0:
    print("음수")
else:
    print("0")