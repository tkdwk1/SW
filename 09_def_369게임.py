'''
사용자로부터 정수를 입력 받아 1부터 입력받은 수 까지
369게임을 진행합니다
3,6,9 에서는 '짝'을
10,20,30... 10의 배수 자리에는 '만세'를 출력하는 부분은 함수로 작성하시오
'''

def game(num):
    for i in range(1,num+1):
        if i%10==3 or i%1==6 or i%10==9:
            print("짝",end=', ')
        elif i%10==0:
            print("만세",end=', ')
        else:
            print(i,end=', ')
print("<< 369 게임 >>")
num=int(input("정수 입력:"))
game(num)