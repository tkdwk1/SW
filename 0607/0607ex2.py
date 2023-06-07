'''
김태환
2023-06-07
#문제정의
    1~45사이의 난수 6개를 오름차순 정렬한 로또번호 생성하기
#문제분석
    변수-lotto
#알고리즘
    1.랜덤모듈 추가
    2.lotto(set변수) 생성
    3.반복(무한반복)
        while true:
            lotto=랜덤 수 6개 추가
            if len(lotto)==6
                break
    4.생성된 로또번호
    5.중복된 수 출력

'''
import random
lotto=set()

cnt=0
while True:
    lotto.add(random.randint(1,45))
    cnt=cnt+1
    if len(lotto)==6:
        break

print("이번주 로또 넘버:",sorted(lotto))
print("중복된 난수의 발생 횟수",cnt-6)