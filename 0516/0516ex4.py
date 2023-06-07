'''
2023-05-16
김태환
파일 입출력 -seek(o):파일의 처음으로 포인트 이동
            -read(int n):지정한 갯수만큼 파일 읽어오기
'''
f=open("C:/SW 프로그래밍 사고/test.txt","r") #파일 객체 생성(읽기)

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.seek(0)

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.close()