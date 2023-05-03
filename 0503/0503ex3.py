'''
2023-05-03
김태환
#문제정의
    1~입력받은 숫자끼리의 합계구하기
#문제분석
    변수 숫자(num)
#알고리즘
    num에 정수로 숫자 입력받기
    sum=0
    for i in range(1,num)
'''
num=int(input('숫자 입력:'))
sum=0
for i in range(1,num+1):
    sum=sum+i
print('1~{}까지의 합계:{}'.format(num,sum))

print()
num1=int(input('숫자 입력:'))
i=1 #반복 횟수 초기화
sum=0 #합계
while i<=num1: #반복 조건
    sum=sum+i #합계 저장
    i=i+1 #i 1증가
print('1~{}까지의 합계:{}'.format(num1,sum))