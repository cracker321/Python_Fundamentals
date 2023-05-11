# [ 리스트 ]


my_list = [1, 2, 3, 4, 5]


# < 리스트에 원소 추가하기: append() >
my_list.append('유종')
print(my_list)


# < 리스트의 특정 위치(인덱스)에 특정 원소 추가하기: insert() >
my_list.insert(1, '안느융') # 1번 인덱스에 '원소값 685'을 추가하기
print(my_list)


# < 리스트에 여러 개의 원소를 한 번에 추가하기: extend() >
my_list.extend([33, '큐큐', 44])
print(my_list)


'''

my_list = [1, 2, 3, 4, 5, 6]

my_list.append('유종')
print(my_list)

my_list.insert(2, '안녕하세용')
print(my_list)

my_list.extend(['그러신가용?', '아넵넵', 4353, 11])
print(my_list)

'''