'''
2023-05-10
김태환
#문제정의 
    입력받은 숫자가 소수인지 아닌지 판별하는 프로그램
#문제분석
    변수 수식(num)
알고리즘
    1.변수 초기화
        num에 정수입력
    2,논리 (반복안애 선택포함)
        for i in range (2,num+1):
            num%i==0
'''
num=int(input("소수 검증 숫자:"))
for i in range(2,num+1):
    if num%i==0:
        break
if num==1:
    print("{}는 소수".format(num))
else:
    print('{}는 소수아님'.format(i))