'''
2023-04-04
김태환
표준입력(input())함수 연습
'''

name=input('이름: ') #키보드로 이름을 입력 받아서 name 변수에 저장
#키보드로 국어 점수 입력 받아서 score1변수에 저장
score1=input('국어점수: ')
#키보드로 수학 점수 입력 받아서 score2변수에 저장
score2=input('수학점수: ')

print('{}의 점수 합계는 {}이다.'.format(name,score1+score2))

print('\n') #한줄 띄우기

name1=input('이름: ') #키보드로 이름을 입력 받아서 name1 변수에 저장
#키보드로 국어 점수 입력 받아서 jumsu1변수에 저장
jumsu1=int(input('국어점수: '))
#키보드로 수학 점수 입력 받아서 jumsu2변수에 저장
jumsu2=int(input('수학점수: '))

print('{}의 점수 합계는 {}이다.'.format(name1,jumsu1+jumsu2))