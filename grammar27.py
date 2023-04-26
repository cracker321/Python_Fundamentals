# [ 표준입출력 ]
'''
# sep는 separate의 약자
# end는 

'''

# < sep= >

print("Python", "Java") # 출력값: Python Java
print("Python", "Java", sep=" 그리고 ") # 출력값: Python 그리고 Java
print("Python", "Java", "JavaScript", sep=" 그리고 ") # 출력값: Python 그리고 Java 그리고 Javascript
print("Python", "Java", "JavaScript", sep=" 그리고 ", end="?") # 출력값: Python 그리고 Java 그리고 JavaScript?
print(" 중에서 무엇이 가장 재밌을까요?") # 출력값: Python 그리고 Java 그리고 JavaScript? 중에서 무엇이 가장 재밌을까요?


#================================================================================================


import sys

print("Python", "Java", file=sys.stdout) # '표준출력'으로 출력하라 라는 뜻. 보통은 생략되는 코드임. 그냥 자동으로 표준출력 해주는 문구임. 너무 당연.
print("Python", "Java", file=sys.stderr) # '표준에러' 출력장치. 

# < 과목(키)별 시험 성적(값) 딕셔너리 >
scores = {"수학":0, "영어":50, "코딩":100}

# 딕셔너리 내부의 모든 키, 값 출력하기
for subject, score in scores.items():
    print(subject.ljust(12), str(score).rjust(15), sep=(":")) # - .ljust(n): n칸 만큼의 공간을 오른쪽에 확보한 후 '왼쪽 정렬'. 
                                                              #              즉, 'subject(키)' 출력 후 오른쪽으로 n칸만큼 띄운 후 'score(값)'이 출력됨. 그냥, 출력문 확인하면 된다.
                                                              # - .rjust(n): n칸 만큼의 공간을 왼쪽 확보한 후 '오른쪽 정렬'. 단, 반드시 int형이 아니라 문자열형(=str형)이어야 한다! 
                                                              #              따라서, 여기서 int형인 score값들을 str형으로 형변환시켜줌. 그냥, 출력문 확인하면 된다.
                                                              
                                                              
# < 문자열 str 앞을 0으로 채우기: zfill(n) >
# ex1) 은행 대기순번표: 001, 002, 003 ... 처럼 앞에 00x, 0xx 와 같은 형식으로 출력하고자 할 때.

for num in range(1, 21):
    print("대기번호: "+str(num).zfill(3)+" 입니다.")
    
    
# < 표준 입력 input(q) >
answer = input("아무 값이나 입력하세용용: ")
print("입력하신 값은 {0} 입니다".format(answer))

print(type(answer)) # 'answer'의 타입을 확인하여 출력하기
                    # 'input(q)'을 통해 입력될 때는, 입력되는 텍스트가 무엇이든지 간에, 그 텍스트는 무조건 문자열 str형으로 인식된다!