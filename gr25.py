# [ print()함수에서의 'end 파라미터' ]
'''
- 'print()함수'에서의 'end 인수'는 출력후 다음 줄로 넘어가는(줄바꿈) 대신에 무엇으로 끝날지를 결정하는 파라미터.
  일반적으로 print()함수는 한 줄을 출력한 후, 자동으로 다음 줄로 이동함. 이것이 줄바꿈임.
  그런데, 'end 파라미터'를 사용하면, 줄바꿈 대신에 무엇으로 끝날지를 설정할 수 있음.
'''

# ex1) 'end 파라미터를 이용하여 줄바꿈 대신 특정 문자 출력하기'
print("나는 {0}살이고, 내 친구는 {1}살이야".format(32, 31), end=". 그래서 어쩌라구") # 출력값: 나는 32살이고, 내 친구는 31살이야. 그래서 어쩌라구


# ex2) 'end 파라미터를 이용하여 줄바꿈 없애고 같은 줄에 출력하기'
name = "조유종"
age = 32
print("나의 이름은 {0}이고, 나이는 {1}살 입니다.".format(name, age), end=" ")
print("만나서 반갑습니다!")  # 출력값: 나의 이름은 조유종이고, 나이는 32살 입니다. 만나서 반갑습니다!


# ex3) 'end 파라미터를 이용하여 출력 시 각 열을 구분하기'
name = ["김철수", "조유종", "이석진"]
age = [30, 32, 31]
job = ["디자이너", "개발자", "기술지원"]

 
# [ 포맷코드 ':< 숫자' ]
'''
중괄호 안의 ':<10'는 '포맷 코드 중 하나'로, 콜론(:) 다음에 숫자를 적어주면, '해당 칸의 폭'을 설정 할 수 있음
'<'기호는 '왼쪽 정렬'을 의미하며, '숫자 10'은 '출력될 문자열의 폭'을 의미함.
만약, 출력될 문자열의 길이가 10보다 짧다면, 남는 공간은 공백으로 채워짐.
따라서, 아래 코드는 "이름", "나이", "직업"을 각각 10자리의 공간 안에서 왼쪽 정렬하게 출력하게 됨.
예를 들어, "이름"이 5글자라면, 뒤에 5자리의 공백이 채워져 "이름"이 출력됨.
'''
print("{0:<10}{1:<10}{2:<10}".format("이름", "나이", "직업")) # 'format()'안에 꼭 '변수'가 아닌 '상수'가 들어가도 상관없다!
for i in range(len(name)):
    print("{0:<10}{1:<10}{2:<10}".format(name[i], age[i], job[i]), end=" ")
    
    
    # ':' : 
    # '<' : 왼쪽 정렬 을 의미
    # '숫자': 출력될 문자열의 폭
print("{0:<10}, {1:<60}, {2:<20}".format("엄마","아빠","사랑해요"))
for i in range(len(name)):
  print("{0:<30}{1:<15}{2:<20}".format(name[i], age[i], job[i]))