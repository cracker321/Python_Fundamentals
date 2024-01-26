# [ 가변인자를 사용한 함수 호출 ]

def profile1(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)
    
profile1("조유종",32, "Python", "Java", "C", "C++", "C#") # cf) 함수의 매개변수 개수 만큼 이에 해당하는 인자값을 반드시 끝까지 다 채워 넣어줘야 함
profile1("김태호", 25, "Kotlin", "Swift", "", "", "") # cf) 이렇게 일단 '비어있는 값(괄호)'으로라도 채워넣어야 함


# ------------------------------------------------------------------------------------------------------------

# [ 가변인자 '*args']
'''
- 어떤 함수를 호출할 때, 호출할 함수의 특정 매개변수에 에 대해 개수가 정해지지 않은 인자를 넣을 때 사용됨. 

'''
def profile2(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
        
        
profile2("이석진", 31, "자바", "스프링", "파썬", "자스", "리액트", "넥스트") 
'''
출력값에서 '이석진'과 '나이'는 일단 첫 번째 print문에 의해 출력되고,
그 뒤에 이어 나오는 '자바', '스프링', '파썬', ... 는 '매개변수 *language'로 들어가서, 이제 아래로 내려와 for문의 language에 들어가게 된다.
그리고, for문의 변수 lang이 language의 요소들이 되는 '자바', '스프링', '파썬', ... 등등을 하나씩 차례로 꺼내서 그 아래 print문에 따라 출력하는 것이다.
'''


# ex1)
def greet_users(age, *names):
    for name in names: 
        print(age, name, end=" ")
        
greet_users(25, '조유종', '이석진', '김성현', '허두현')

