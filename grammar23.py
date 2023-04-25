# [ 기본값 ]

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용언어: {2}"\
#         .format(name, age, main_lang)) # 역슬래시(\)는 두 줄을 한 줄로 연결시켜주는 역할!
#                                        # 역슬래시 사용하고, 그 줄 끝에서 공백이 있으면 에러 발생한다! 
      
# profile("유재석", 20, "파이썬")
# profile("조유종", 32, "자바")    
    
    
# < 만약, 같은 학교, 같은 학년, 같은 나이, 같은 사용 언어 반 수업 이라면? 이 때 바로 '기본값'을 사용한다! >
# 아래에서는 나이=17살, 주 사용 언어 반="파이썬" 으로 고정하여 기본값 지정함.


def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t 주 사용언어:{2}"\
        .format(name, age, main_lang))

profile("유재석")
profile("조유종")
profile("이석진")



# [ 키워드값 ]
# - 함수를 호출할 때, 매개변수의 값(=인자값)을 직접 입력하는 경우, '호출할 때의 매개변수 입력값 순서'를 '실제 원래 함수의 매개변수 입력값 순서'와 다르게 입력해도
#   아래처럼 매개변수의 값을 지정하여 입력하면, 자동으로 알아서 '실제 원래 함수의 매개변수 입력값 순서'에 맞게 출력해준다!

def self_introduction(name, age, main_lang):
    print(name, age, main_lang)
    
self_introduction(main_lang="파이썬", name="조유종", age=32) # 출력값: 조유종 32 파이썬
self_introduction(age=21, main_lang="자바", name="메렁") # 출력값: 메렁 21 자바
self_introduction(name="네넵", main_lang="자바스크립트", age=26) # 출력값: 네넵 26 자바스크립트


# [ 탭 \t ]
# - 수평 방향으로 일정한 간격만큼 띄어쓰기 하는 역할

print("이름\t나이\t학년")
print("홍길동\t15\t2")
print("조유종\t30\t4")