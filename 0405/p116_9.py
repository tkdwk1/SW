'''
2023-04-05
김태환
본봉과 수당을 정수로 입력 받아서 수령액 구하기
'''

as1=int(input('본봉: ')) #본봉 입력
allow=int(input('수당: ')) #수당 입력
total=as1+allow #총액 구하기
tax=total*0.2 #세금 구하기
sal=total-tax #수령액 구하기

print('본봉이 {}만원이고, 수당이 {}만원 일때, 이번달 수령액은 {}만원 입니다'.format(as1,allow,sal))