# [ 리스트 ]


my_list = [1, 2, 3]


# < 리스트에 원소 추가하기: append() >
my_list.append(6)
print(my_list)


# < 리스트의 특정 위치(인덱스)에 특정 원소 추가하기: insert() >
my_list.insert(1, 685) # 1번 인덱스에 '원소값 685'을 추가하기
print(my_list)


# < 리스트에 여러 개의 원소를 한 번에 추가하기: extend() >
my_list.extend([33, 44])
print(my_list)