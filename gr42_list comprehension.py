# [ 리스트 컴프리헨션 List Comprehension ]
# https://shoark7.github.io/programming/python/about-list-comprehension-python
# https://wikidocs.net/22805
# https://wikidocs.net/84393



'''
< for문 사용할 때>

result = []

for 변수명 in 시퀀스:
    (if 조건:)
        result.append(표현식)



< 리스트 컴프리헨션 사용할 때 >

[ 변수를 활용한 값 for 변수명 in 순회할 수 있는 값 (if 조건) ]
'''






#==========================================================================

# < 원래: 
size = 10
# arr = [0] * size
# print(arr)  # 출력값: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
for i in range(size):
    arr[i] = i*2


# < 리스트 컴프리헨션: 

size = 10

arr = [ i*2 for i in range(size)]

#==========================================================================

# [ 예제 0 ]

a = str(input()) # 만약, 'abcde'를 입력한다고 하면,
# print(a) # 출력값: abcde


list1 = []

for x in a:
    list1.append(x)
    
print(list1) # 출력값: ['a', 'b', 'c', 'd', 'e']


#==========================================================================


# [ 예제 1 ]

# < 원래: 빈 리스트를 생성하고, 그 리스트에 정수 1~10을 원소로 채워넣는 코드. 총 3줄 >
numbers = []
for n in range(1, 11):
    numbers.append(n)
    
# < 리스트 컴프리헨션: 위 코드를 '리스트 컴프리헨션'으로 표기하면 다음처럼 작성한다. 결과는 동일. 총 1줄 >
[ x for x in range(1, 11) ]
 


# < 위 둘의 차이점 >
'''
- '원래'의 첫 번째 줄 'numbers = []'에서 '[]'이 
  '리스트 컴프리헨션'의 '가장 바깥쪽 []'에 해당.
- '원래'의 두 번째 줄 '전체'가 
  '리스트 컴프리헨션'의 'for x in range(10)'에 해당.
- '원래'의 세 번째 줄 '(n)'이
  '리스트 컴프리헨션'의 '첫 번째 x'에 해당.
'''


#==========================================================================


# [ 예제 2 ]

# < 원래: >
xtimesoftwo = []

for x in range(1, 11):
    xtimesoftwo.append(2*x)

print(xtimesoftwo)


# < 리스트 컴프리헨션. x times of 2 >
[ 2*x for x in range(1, 11) ]

'''
xtimesoftwo = []

for x in range(1, 11):
    xtimesoftwo.append(2*x)
    
print(xtimesoftwo)

==================위의 것과==============

[ 2*x for x in range(10)]

'''

# ==========================================================================


# [ 예제 3: 리스트 컴프리헨션과 if 조건 조합]

# < 원래: 만약 1부터 10까지 숫자중 짝수만 순차적으로 들어있는 리스트를 생성하는 코드 >
even_numbers = []

for n in range(10):
  if n%2 == 0:
    even_numbers.append(n)
  
print(even_numbers)


# < 리스트 컴프리헨션: >
[ x for x in range(10) if x%2 == 0]


# ==========================================================================
'''



'''

# [ 예제 4: 컴프리헨션과 다중for문(내부에서 for문과 if문을 몇 번이고 반복할 수 있음). ]

# < 원래: >
for x in ['쌈밥', '치킨', '피자']:
  for y in['사과', '아이스크림', '커피']:
    for z in[ '배달 시키기', '가서 먹기']:
      print(x, y, z) 
    
      
# < 리스트 컴프리헨션과 다중 for문 >
[ ()]


# ==========================================================================

# [ 예제 5: ]

# < 원래: >
array = []

for i in range(0, 20, 2):
  array.append(i*i)
  
print(array)


# < 리스트 컴프리헨션:
arr = [ x*x for x in range(0, 20, 2) ]
print(arr)


# ==========================================================================


# [ 예제 6:]

# < 원래: >
list1 = []

for i in range(0, 50, 7):
  if i % 7 == 0:
    list1.append(i)
    
print(list1)


# < 리스트 컴프리헨션: >
[ x for x in range(0, 50, 7) if i%7 == 0]


# ==========================================================================


# [ 예제 7: 집합 set() 활용 ]


# < 원래 >
submitted = set() # 출석한 학생들의 출석번호를 모아놓을 집합 set을 생성함.

for _ in range(28): # 이제 출석한 28명의 학생들의 출석번호를 
  student_number = int(input()) # 일일히 28개 한 줄 한 줄 다 입력받아서, 그것을 정수형으로 바꿔줌
  submitted.add(student_number) # 입력받은 28개의 숫자를 '집합 submitted'에 넣어줌
  

# < 리스트 컴프리헨션 >
submitted = ( int(input()) for _ in range(28) ) # 'int(input())' 자리에 대신 'student_number'가 들어갈 수 없는 이유는, 
                                                # 그 이전에 '변수 student_number'가 정의(선언)되지 않았기 때문이다!









