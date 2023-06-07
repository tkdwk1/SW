'''
2023-05-16
김태환
파일 입출력 - 읽기 (read() - 천체 내용을 하나의 문자열로 반환)
'''

f=open("C:/SW 프로그래밍 사고/test.txt","r") #파일 객체 생성(읽기)


txts=f.read() #파일 전체 내용 txts에 하나의 문자열로 반환

print(txts) #읽은 내용 출력

f.close