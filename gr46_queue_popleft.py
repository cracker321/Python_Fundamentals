# [ 큐 queue ]

from collections import deque

# 빈 dequeue 생성
my_queue = deque()

# 원소 추가
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)


# 첫 번째로 들어간 맨 앞 원소 제거를 제거하고, 그 제거한 원소를 반환함
first_element = my_queue.popleft() 
print(first_element) # 출력값: 1
