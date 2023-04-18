'''
2023-04-18
김태환
'''

x=int(input("x의 값을 입력해주세요 :"))
y=int(input("y의 값을 입력해주세요 :"))
if x>y:
    if y!=0:
      print("{} // {} = {}".format(x,y,x//y))
    else:
        print("y의 값이 0입니다.")
elif x<y:
    print("{} + {} = {}".format(x,y,x+y))
else:
    print("{} * {} = {}".format(x,y,x*y))