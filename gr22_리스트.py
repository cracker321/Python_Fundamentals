# [ 리스트 ]

'''
리스트
순서가 있음. 리스트의 각 원소는 특정 순서. 인덱스를 통해 접근하 룻 ㅣㅇㅆ음.
리스트의 원소는 생성된 후에도 변경할 수 있ㅇ므.
리스트는 다양한 데이터타입의 원소를 저장할 수 있음.
my_list = [1, 2, 3]
pritn(my_list[0]) 첫 번째 요소 출력
my_list[1]=20
첫 번째 원소를 20으로 변경
my_list.append(4) --> 리스트 끝에 4 추가
my_list.pop(1) ---> 두 번째 원소 삭제
튜플: 변경 불가능. () 사용
Set: 순서가 없고 중복을 허용X
Dictionary: 키-값 쌍으로 순서가 없음.

'''
my_list = [1, 2, 3, 4, 5]


# < 리스트에 원소 추가하기: append() >
my_list.append('유종')
print(my_list)


# < 리스트의 특정 위치(인덱스)에 특정 원소 추가하기: insert() >
my_list.insert(1, '안느융')  # 1번 인덱스에 '원소값 685'을 추가하기
print(my_list)


# < 리스트에 여러 개의 원소를 한 번에 추가하기: extend() >
my_list.extend([33, '큐큐', 44])
print(my_list)


# < 리스트의 특정 인덱스에 해당하는 원소를 출력하고, 그 원소를 그 리스트에서 삭제하기: pop() >
print(my_list.pop(2))  # 리스트에서 2번 인덱스에 해당하는 원소를 출력하고, 그 원소를 그 리스트에서 삭제하기
print(my_list)  # 2번 인덱스에 해당하는 원소가 삭제된 리스트가 출력됨
'''

my_list = [1, 2, 3, 4, 5, 6]

my_list.append('유종')
print(my_list)

my_list.insert(2, '안녕하세용')
print(my_list)

my_list.extend(['그러신가용?', '아넵넵', 4353, 11])
print(my_list)

'''
