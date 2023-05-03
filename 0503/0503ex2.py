'''
2023-05-03
김태환
1~10까지 합계 구하기
'''

#while반복
i=1 #반복 횟수 초기화
sum=0 #합계
while i<=100: #반복 조건
    sum=sum+i #합계 저장
    i=i+1 #i 1증가
print('1~100까지의 합계:',sum)

#for 반복
sum=0
for i in range(1,101):
    sum=sum+i
print('1~100까지 합계:',sum)