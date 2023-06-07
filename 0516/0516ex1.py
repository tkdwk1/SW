'''
2023-05-16
김태환
파일 입출력
'''
ft=open("C:/SW 프로그래밍 사고/test.txt","w") #파일 객체 ft생성

for i in range (1,11): #10번 반복
    ft.write("%d번째 줄입니다.\n"%i) #ft에 i 출력

ft.close() #파일종료