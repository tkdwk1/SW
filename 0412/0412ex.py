'''
2023-04-12
김태환
평점을 입력받아서 평점출력, 4.2 이상이면 "해외연수"
#문제분석
    변수-평점(score)
#알고리즘
    1.변수선언
        score에 평점 실수로 입력받기
    2.논리(선택)
        if score>=4.2:
'''

score=float(input("Enter your score: ")) #평점 실수로 입력

print("당신의 평점은: ",score) #평점출력
if score>=4.2: #조건
    print("해외연수") #조건이 참일때만 실행