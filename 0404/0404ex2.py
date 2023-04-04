'''
2023-04-04
김태환
표준출력(print) foramt()연습
'''

print('이름은 {}이고 나이는 {}입니다.'.format('김태환','20'))
print('이름 {name}, 나이 {age}, 주소 {adress}'.format(adress='Busan',name='김태환',age='20'))
print('the lucky number is ({:14})'.format(7777)) #숫자 기본 오른쪽 정렬
print('The lucky number is ({:<14})'.format(7777))