# < while 반복문을 통해 파일객체의 내용을 출력하기 >
score_file = open("score.txt", "r", encoding="utf-8")

while True:
    line = score_file.readline() # 'score_file'에서 '한 줄씩 불러온 줄들'을 '변수 line'에 저장함. 
    if not line: # 만약, 읽어올 줄이 없으면,
        break # break가 작동하며 바로 반복문 탈출함
    print(line, end="") # 만약,읽어올 줄이 있다면, 그냥 그 줄을 출력하는 것임.
                        # 또한, 줄바꿈을 원하지 않으면, end="" 키워드를 추가하면 됨.
                        # 원래는 한 줄 띄어 한 줄 이렇게 출력되는데, end=""를 추가하면, 그 한 줄 띄어지는 것이 사라짐으로써 공백이 사라짐.
score_file.close()


# < 리스트에 값을 넣어 파일객체의 내용을 출력하기 >
score_file = open("score.txt", "r", encoding="utf-8")

lines = score_file.readlines() # 리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

