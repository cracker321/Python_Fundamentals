# [ range() 함수 ]
'''
- 숫자의 시퀀스(리스트 등)을 만들 때 사용됨. 시작 숫자, 끝 숫자, 간격 등을 지정할 수 있음
- 시퀀스는 '시작 값'부터 '끝 값 바로 직전의 값'까지 포함됨.
'''

# ex1) 1부터 5까지의 숫자 가져오기
my_range = range(1, 6)
print(my_range) # 출력값: range(1, 6). 이거는 해당 숫자 시퀀스를 불러오는 것이 아니다.
for i in my_range:
    print(i) # 출력값: 1~5까지 출력됨. 이렇게 for문을 사용해야 해당 숫자 시퀀스의 원소들을 불러오는 것이다.
    
    
# ex2) 1부터 10까지의 홀수 가져오기 
my_range = range(1, 11, 2)
for i in range(1, 11, 2):
    print(i) # 출력값: 1~10 사이의 홀수가 출력됨.
    
    
# ex3) 10부터 0까지 거꾸로 숫자 가져오기
my_range = range(10, -1, -1)
for i in my_range:
    print(i)
    

# ex4) 0부터 10까지 중 2의 배수를 가져오기
my_range = range(0, 11, 2)
for i in my_range:
    print(i)
