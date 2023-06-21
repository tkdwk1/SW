'''
202395012
김태환
문제분석
    텍스트파일 data.txt에 한 줄에 한 개의 실숫값이 저장 되어 있다. 이 파일을 읽어서 합계와 평균을 계산한 후 out.txt 파일에 저장하는 프로그램 작성
알고리즘
    data.txt파일 읽기
    합계와 평균 계산하기
    out.txt 파일에 작성 후 저장
'''
data=[] #빈 리스트 변수생성
f=open("C:/data/data.txt","r") #읽기 모드의 파일 객체 생성
for i in range(5): #10명의 학생 점수 읽어 오기
    data.append(data.readline().split())