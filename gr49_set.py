# [ 집합 set ]
# https://aigong.tistory.com/30
# 

'''
- 중복을 허용하지 않는다는 특징 때문에, 집합 set은 '원소들 간 중복을 제거'할 때 유용하게 사용됨.
  for문을 돌면서 어떤 값을 얻었을 때, set에 계속 집어넣고 마지막에 최대, 최소, 합 등을 구하고자 할 때 많이 사용하는 것 같음
- 집합 set() 을 사용할 때는, '중괄호 {}'를 사용하는 것이 맞는 듯..? 엥 아닌 것 같은데..
'''

# ======================================================================================        

s0 = set({2, 2, 3, 3, 3, 1, 4, 4, 4, 4, 5, 5, 5, 5, 5})
print(s0) # 출력값: {1, 2, 3, 4, 5}
          # 즉, 중복되는 원소들이 모두 제거된다!
 
 
s00 = set({'a', 1, 2, 2, 3, 3, 3, ('a', 'b'), ('b', 'a'), ('a', 'b'), ('a')})         
print(s00) # 출력값: {'a', 1, 2, 3, ('a', 'b'), ('b', 'a'), ('a')}    
           # -출력값의 원소 순서는 매 출력 때마다 매번 달라진다!
           # -중복값이었던 
           # 'a'와 ('a'), 2, 3, ('a', 'b') 총 4개 종류가 중복 제거되었음. 
           # -특이한 것은 
           # 'a'와 튜플('a')는 같은 것으로 인식되고, 
           # 튜플 ('a', 'b')와 ('b', 'a')는 다른 것으로 인식된다는 점.



# ======================================================================================        

# cf) '리스트'는 최초 선언할 때 e.g: 'numbers = []' 선언 생성하지만, '집합 set'은 아래처럼 'submitted = set()' 이렇게 선언 생성한다!

s1 = set() # '집합 set'을 최초 선언 및 초기화함.


s1 = set({1, 2, 3}) # '집합 set'을 변수에 넣어줄 때는 반드시 set() 안에 '리스트 []' 형태로 넣어줘야 한다!!!
print(s1) # 출력값: {1, 2, 3}


s2 = set('Hello')
print(s2) # 출력값: {'l', 'e', 'H', 'o'} 또는 {'o', 'e', 'H', 'l'} 또는 {'H', 'l', 'o', 'e'} 등등 
          # -'집합 set'은 원소의 중복을 허용하지 않기 때문에, 원래 있던 'l', 'l'의 총 2개가 총 1개로 줄어서 집합 set에 입력된다!
          # -'집합 set의 원소들 간'에는 순서가 없기 때문에, 그때그때 출력되는 원소 순서는 무작위로 달라진다!


# ======================================================================================        


# < 생성하기 >
my_set = {1, 2, 3}



# < 값 추가하기: add(n) >
# -여기서 n은, '하나의 숫자', '하나의 글자', '문장', '튜플'만 가능하다!

my_set.add(4) # '하나의 숫자'인 '새로운 원소 4'를 추가하기
print(my_set) # 출력값: {1, 2, 3, 4}. 단, 이 원소들 간의 순서는 매 출력마다 바뀐다!

my_set.add('오라버니 안녕하세요') # '하나의 글자 or 문장'인 
print(my_set) # 출력값: {'오라버니 안녕하세요', 1, 2, 3, 4'}. 단, 이 원소들 간의 순서는 매 출력마다 바뀐다!



# < 값 제거하기: remove(n) >
my_set.remove(3) # '기존의 원소 3'을 제거하기. 만약, remove(n)에서 입력한 원소 n이 집합 내부에 없으면 에러 메시지 출력함.
print(my_set) # 출력값:   단, 이 원소들 간의 순서는 매 출력마다 바뀐다!
 


# < 여러 값 한 번에 추가하기: update(n) >
# -여러 값을 추가할 때는 원소들을 '중괄호 {}' 또는 '리스트 [] 형태'에 담아 추가할 수 있음.
my_set.update({5, 6, 7, 8}) 
print(my_set) # 출력값: 단, 이 원소들 간의 순서는 매 출력마다 바뀐다!



# < 집합의 얕은 복사: copy() >
s5 = set({'맞아유', '하하하', '메렁', '그런가요?', '유재석', '조유종'})

s6 = s5.copy()
print(s6) # 출력값: {'맞아유', '하하하', '메렁'}. 단, 이 원소들 간의 순서는 매 출력마다 바뀐다!
 
 
 
# < 특정 값이 내부에 있는지 여부 확인: if ... in ...: >
if '메렁' in s5:
  print('맞습니다 맞고요')
  
  
# < 집합 내부의 임의의 값을 리턴한 후, 그 값을 현재 집합에서 삭제: pop() >
print(s5.pop())


# < 전혀 다른 '리스트 자료형인 리스트'를 '집합 자료형으로 변환'시키기 >
s7 = set(['집합으로 변환시키기 전', '기존 리스트 자료형', '입니다'])

# < 집합의 모든 원소를 삭제: clear() >. 즉, 기존 집합을 '공집합으로 변환'시키는 것임.
print(s7.clear()) # 출력값: None

