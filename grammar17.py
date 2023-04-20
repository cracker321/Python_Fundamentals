# [ 삼항연산자 ]
# : < 값1 if 조건식 else 값2 >


# 아래 예제들은 다 gpt임.
# < ex1: 짝수와 홀수 >
# - 입력된 숫자가 짝수인지 홀수인지 출력하는 코드. 삼항연산자를 사용하여 간단하게 작성할 수 있음
num = int(input("숫자를 입력하세요: "))
result = "짝수" if num % 2==0 else "홀수"
print(result)


# 아래는 그냥 내가 임의로 간단히 만들어 본 것일 뿐임.
stringstring =str(input("문자열만 입력하셈여:"))
resulttt="문자열아니구요" if stringstring != "문자열노노" else "문자열아니구요"
print(resulttt)


# < ex2: 절댓값 >
# - 입력된 숫자를 절댓값을 변환해줌
num = int(input("아무숫자나 입력해봐. 절댓값으로 바꾸는 로직이야 이거: "))
result = num if num >= 0 else -num
print(result)


# < ex3: 최댓값 >
# - 입력된 두 수 중 큰 숫자를 출력하는 코드. 
num1 = int(input("첫 번째 숫자 입력해봐: "))
num2 = int(input("두 번재 숫자 입력해봐: "))
result = num1 if num1 > num2 else num2
print(result)

