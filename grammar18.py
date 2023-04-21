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
# 키: 'apple'
# 값: '사과'
my_dict = {"apple":"사과"}


# < dictionary에서 '밸류값'을 꺼내는 방법 >
# 대괄호 안에 밸류값에 해당하는 '키'를 넣는다. 
print(my_dict["apple"]) # 출력값: '사과'


# < dictionary에 새로운 키와 값을 넣는 방법 >
# 리스트에 해당하는 새로운 '키'를 추가한다.
my_dict['banana'] = '바나나'
print(my_dict)


# < dictionary의 모든 키와 값 쌍을 깔끔하게 확인하는 방법: items() >
for key, value in my_dict.items():
    print(key, value) 
    
# < dictionary에서 특정 키(그 키에 해당하는 '값'도 당연히 같이 삭제됨)를 삭제하기: del >
del my_dict['banana']
print(my_dict)

