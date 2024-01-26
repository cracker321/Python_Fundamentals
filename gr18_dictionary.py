# [ Dictionary 딕셔너리 자료형 ]
''' (또는 """)
- 딕셔너리는 '한국어-영어' 사전과 같이 'Key-Value'를 '한 쌍으로 갖는 자료형'임.
- 중괄호{}로 묶인 키와 밸류(값)의 한 쌍으로 이루어져 있으며, 각각의 키와 값 쌍은 콜론: 으로 구분됨
'''


"""
챗gpt에 물어본 질문
파이썬의 딕셔너리 문법에 대해 아주 상세히 개념, 예제 5개 과정 단계 별로 상세히 설명해줘 like i'm 5 years old
"""


# < dictionary의 기본 형식 >
my_dict = {"apple" : "사과"}
my_dict = {"orange": '오렌지'}


# < dictionary의 기본 형식 >
# 키: 'apple'
# 값: '사과'
my_dict = {"apple":"사과"}


# < dictionary에서 '값'을 꺼내는 방법 >
# '대괄호' 안에 '값'에 해당하는 '키'를 넣는다. 
print(my_dict["apple"]) # 출력값: '사과'


# < dictionary에 새로운 '한 쌍의 키와 값'을 넣는 방법 >
# 아래 형식처럼 새로운 '키'와 '값'를 추가한다.
my_dict['banana'] = '바나나'
print(my_dict)

'''
즉)
- 딕셔너리에서 '키(cnumber)'와 '값(clocation)' 중에서 '값(clocation)'을 '꺼내는' 방법
  : cows[cnumber]
  
- 기존의 딕셔너리에 새로운 '키(cnumber)'와 '값(clocation)'을 '추가'하는 방법
  : cows[cnumber] = clocation
'''

 
# < dictionary의 모든 키와 값 쌍을 깔끔하게 확인하는 방법: items() >

# - 아래의 key, value는 고정된 변수명이 아니라, 그냥 '키'와 '값'을 의미
#   예를 들어, '변수 key'를 '변수 fruit', '변수 value''를 '변수 species'로 해도 된다!
#   즉, 아래를 'for fruit, species in my_dict.items():
#                   print(fruit, species)' 로 해도 됨.어차피, for문 안에서만 잠깐 사용된는 일시적 변수명들 key, value, fruit, species이기 때문임.
for key, value in my_dict.items():
    print(key, value) 
    
    
# < 현재 딕셔너리의 모든 키와 값 쌍을 깔끔하게 확인하는 방법: items() >

for key, value in my_dict.items():
    print(key, value)

    
# < dictionary에서 특정 키(그 키에 해당하는 '값'도 당연히 같이 삭제됨)를 삭제하기: del >
del my_dict['banana']
print(my_dict)



# < dictinary에서 키와 값을 반복문을 통해 출력하기 > 

teams_record = { 
                'Team A': [10, 15, 12],
                'Team B': [8, 9, 7],
                'Team C': [13, 11, 9]
                }

for team, score_list in teams_record.items(): # 하나의 반복에서, 한 쌍의 키-값은 동시에 반복이 진행됨.
  print(team)
  print(score_list)
  
# 출력값:  Team A
#         [10, 15, 12],
#         Team B
#         [8, 9, 7],
#         Team C
#         [13, 11, 9]
