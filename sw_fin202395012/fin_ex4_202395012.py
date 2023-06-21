'''
김태환
202395012
문제분석
    주사위를 던져서 나오는 값들의 빈도를 계산하는 프로그램을 작성하시오 1,2,3,4,5,6의 값이 각각 몇번이나 나오는지를 계산
    변수 주사위 (dice)
알고리즘
    랜덤모듈 추가
    set변수 생성
    반복
    while True:
        dice.add(random.randint(1,6))
        
'''
import random
dice=set()
cnt=0
one=0
two=0
three=0
four=0
five=0
six=0
while True:
    dice.add(random.randint(1,6))
    cnt=cnt=1
    if cnt==1000:
        if dice==1:
            one=one+1
        elif dice==2:
            two=two+1
        elif dice==3:
            three=three+1
        elif dice==4:
            four=four+1
        elif dice==5:
            five=five+1
        else:
            six=six+1
        break
        
print("주사위가 1인 경우",one)
print("주사위가 2인 경우",two)
print("주사위가 3인 경우",three)
print("주사위가 4인 경우",four)
print("주사위가 5인 경우",five)
print("주사위가 6인 경우",six)
