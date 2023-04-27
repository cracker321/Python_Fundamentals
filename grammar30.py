# [ 파일 입출력 ]grade_file

# < 파일 열기 >
'''
- 'open': 파일 열기
- 'score.txt': 임의의 파일 제목
- 'w': 파일 열기 모드를 '쓰기 모드(w)'로 설정함. 파일 열기 모드에는 w((덮어)쓰기), r(읽기), a(=append. 기존 파일의 내부 내용에 이어추가) 세 가지가 있음.
- 'encoding='utf8'': utf8로 인코딩 설정
- 'score.txt'파일은 왼쪽 탭에서 파이썬파일들 밑에 .txt파일로 생성된다.
'''

# < 파일 열기 모드: w((덮어)쓰기) >
score_file = open("score.txt", "w", encoding="utf8") # 'score.txt'라는 이름의 파일을 최초로 열기 위해서 최초로 만들고, 이것을 열기(open). 'score.txt'파일을 '파일객체 변수score_file'에 담은 것임.
print("수학: 0", file=score_file) # '인자값 file'을 통해 파일 객체를 전달할 수 있음. 
                                  # 여기서 'file=score.file'로 지정해주면, '출력문 print()함수'의 출력값(여기서는 '수학: 0')이 '파일객체 변수 score_file'에 입력된다(작성되어진다('w'))
print("영어: 50", file=score_file)
score_file.close() # 파일 작업 후 'score_file'파일을 닫기


# < 파일 열기 모드: a(기존 파일의 내부 내용에 이어 추가)>
score_file = open("score.txt", "a", encoding="utf-8") # 'score.txt'라는 이름의 파일을 만들고, 이것을 열기(open). 'score.txt'파일을 '파일객체 변수 score_file'에 담은 것임. 파일 추가 모드 'a' 사용함.
score_file.write("과학: 80") #  저~ 위에 먼저 생성한 'score.txt'파일 내부의 기존 내용에 이어서 추가 작성함.
score_file.write("\n코딩: 100") # 이거는 '출력문 print()'가 아니기 때문에, 자동으로 줄바꿈되지 않음. 따라서 이렇게 '\n을 넣어줘야 줄바꿈이 됨.
score_file.close()


# < 파일 열기 모드 & 파일 내부 전체 내용 한 번에 다 출력하기: r(읽기). 즉 해당 파일의 내부 내용을 여기 콘솔 창에 띄우는 것임 >
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()


# < 파일 열기 모드 & 파일 내부 내용을 '한 줄씩' 그리고 '한 줄 띄어서' 출력하기. readline() > 
score_file = open("score.txt", "r", encoding="utf=8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
# 만약, '한 줄 띄어서'를 없애고, 그냥 '한 줄씩' 그리고 '그 바로 다음 줄에' 출력하려면, 출력문 print()의 인자로 end="" 붙여주면 됨. 아래처럼.
print(score_file.readline(), end="")
score_file.close()


# <>
score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline() # 'score_file'에서 '한 줄씩 불러온 줄들'을 '변수 line'에 저장함. 
    if not line: # 만약, 읽어올 줄이 없으면,
        break # break가 작동하며 바로 반복문 탈출함
    print(line) # 만약,읽어올 줄이 있다면, 그냥 그 줄을 출력하는 것임.
score_file.close()

