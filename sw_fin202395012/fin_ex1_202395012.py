'''
202395012
김태환
문제분석
    p=3.14를 전역변수로 선언하여 원의 면적을 계산하는 함수 circleArea(r)과 원의 둘레를 계산하는 함수 circleCircumference(r)을 작성하기
    변수 반지름(r), 면적(area), 둘레(wide)
알고리즘
    circleArea(r), circleCircumference(r) 함수 지정
    반지름을 입력받기
    원 둘레 계산, 원 면적계산하는 함수 호출
'''
pi=3.14

def circleArea(r):
    return pi*r*r

def circleCircumference(r):
    return 2*pi*r

r=int(input("반지름 입력: "))

circleArea(r)
circleCircumference(r)


print("반지름이 {}인 원의 면적 : {}".format(r, circleArea(r)))
print("반지름이 {}인 원의 둘레 : {}".format(r, circleCircumference(r)))
