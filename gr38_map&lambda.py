# [ map & lambda 예제 ]


# < 예제 1: map >

# map(함수, 리스트)
# 아래 두 리스트가 주어졌을 때, 다음 리스트를 만들고자 한다.
# 만들고자 하는 리스트: [5, 7, 9]

a = [1, 2, 3]
b = [4, 5, 6]

# 'c = [5, 7, 9]'가 되기 위해서는,  리스트 a와 리스트 b의 각 원소들을 서로 더해야 함.


# < 풀이 >
c = list(map(lambda x, y: x+y, a, b))

print(c)


# ==========================================================================


# < 예제 2: lambda >

# - 작성법
#   lambda 매개변수 : 함수내용(=return문)

def call_10_times(func):
    for i in range(10): # 0에서 시작해서 9까지, 총 10번 반복되는 것임.
        func(i)
        
call_10_times(lambda numbers : print(numbers+1)) # '함수 call_10_times의 인자값(매개변수 func에 들어갈 값)'으로 '람다함수 lambda numbers : numbers+1'을 넣음





