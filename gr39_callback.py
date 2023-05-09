# [ Callback 함수 ]
'''
- '콜백'은 호출 방향이 반대라는 뜻
- 함수를 호출할 때, 그 함수의 인자값으로 함수 또는 람다를 넣어서 호출하는 것.


'''

# e.g 1) 콜백함수 
def call_10_times(func):
    for i in range(10): # 0~9 까지 반복. 즉, 10개(=번) 반복. 중요한 것은 어쨌든 range함수는 그 매개변수가 무엇이든지 마지막 것(여기서는 10)은 포함되지 않음!
        func()
        
        
def print_hello():
    print("안녕하세요")
    
call_10_times(print_hello)


# e.g 2)
def call_10_times2(func):
    for i in range(10):
        func(i)
        
        
def print_hello2(number):
    print("잘가세요", number)
    
call_10_times2(print_hello2)


