# [ 내장함수 map() ]
'''
- 리스트와 같이 여러 원소들이 들어 있는 객체를 대상으로 함
- 리스트 안의 원소들을 하나씩 꺼내서 동일한 작업을 가해줌. 
  그리고, 그것들을 다시 하나로 묶어줌. 이 때는, 리스트객체가 아닌 '맵 객체'로 묶임.
  그리고, 이것을 다시 리스트객체로 바꿔줌.


'''

# ========================== < 함수 map()을 사용하기 전의 복잡하게 처리해야 되는 예제 경우들 > ============================================

# < ex1: '문자열 리스트 time_list'의 '문자열 원소들'을 '정수형'으로 '바꿔서' '정수형 리스트 int_time_list'에 넣은 후, 이것을 다시 time_list에 넣기 >
# 즉, 여기에서 사용된 map() 기능의 핵심은, '최초 입력된 문자열 원소들 리스트'를 변환시켜서 '정수형 원소들 리스트'로 탈바꿈시키는 것이다!
time_list = ["1", "2", "3", "4", "5", "6"]

int_time_list = []

for t in time_list: # time_list의 원소들을 하나씩 꺼내서 
    int_time_list.append(int(t)) # 그 원소들을 int형을 형변환시킨 후, int_time_list에 삽입하는 것
    
time_list = int_time_list # 기존의 time_list에 정수형 리스트 int_time_list를 넣어서 time_list를 바뀐 것으로 정의하기

print(time_list) # 원소들이 정수형으로 바뀐 time_list의 원소들 다 출력하기 


# < ex2: 위에서 새롭게 정의된 정수형이 된 time_list의 각 원소들의 값을 1씩 추가시키기 >

time_list2 = []

for t in time_list:
    time_list2.append(t+1)
    
print(time_list2)

# =============================================================================================================================================


'''
1. map(for문에서 최초 리스트의 원소들을 꺼내 어떤 작업을 해줄 때 사용되는 함수(위에서는 int함수) , map 객체로 변환시킬 최초의 대상 리스트 or 튜플 객체(위에서는 time_list))
   즉, map(int, time_list)가 되는 것임. 이제 이것은 map 객체가 되는 것임
2. 그리고, 이 map 객체를 다시 리스트객체로 변환시켜야 하기 때문에,
   list(map(int, time_list)) 로 해준다.
'''

# < ex3: map 객체를 사용하여, 저 위의 'ex1 과정'을 재작성함 >
time_list = ["1", "2", "3", "4", "5", "6"]

time_list2 = list(map(int, time_list))

print(time_list2)


# < ex4: 함수를 사용하여 'ex2 과정'을 재작성함 >
def plus1(x):
    return x+1

time_list = list(map(plus1, time_list2))

print(time_list)



# < 람다 lambda >
# - 'lambda 매개변수 : 함수내용' 
# 바로 위에 '함수 def plus1(x): return x+1'을 이렇게 람다로 간단히 표현 가능. 함수명 plus1은 이제 필요 없음.
# 즉, 'lambda 매개변수 : 함수내용' 형식으로 사용하는 것이다.
lambda x : x+1


# < ex5: 'ex4 과정'을 재작성함 >

time_list = list(map(lambda x:x+1, time_list2))
print(time_list)

