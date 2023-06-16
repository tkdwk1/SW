'''
사이렌 오더를 통해 음료를 미리 예약하는 프로그램을 만드시오
메뉴는 
1.아메리카노 2500원
2.카페라떼 3000원
3.바닐라 라떼 3000원
메뉴번호를 선택하면 해당 메뉴와 가격을 출력해주는 부분을 함수로 작성하시오

선택한 메뉴는 인수로 전달되어 가격이 결과 값으로 반환되는 함수로 작성하시오.

사용자가 음료를 선택하면 음료의 가격을 알려주는 프로그램
'''



def price(menu):
    if menu == 1:
        return 2500
    elif menu == 2 or menu == 3:
        return 3000
    else:
        return 0
print("메뉴를 선택하세요:")
print("1. 아메리카노 - 2500원")
print("2. 카페라떼 - 3000원")
print("3. 바닐라 라떼 - 3000원")

select = int(input("메뉴 번호를 입력하세요: "))

price = price(select)

if price == 0:
    print("잘못된 메뉴 번호입니다.")
else:
    print(f"선택한 음료의 가격은 {price}원 입니다.")

# num=int(input("1. 아메리카노\n2. 카페라떼\n3. 바닐라 라떼\n메뉴를 선택하세요:"))
# menu(num)
