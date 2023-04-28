# [ f-string ]

# f-string은 파이썬에서 문자열을 간단하게 다루기 위한 기능임. 이 기능을 사용하면 문자열 안에서 변수나 표현식을 쉽게 사용할 수 있음.
# f-string은 '문자열들'을 따옴표(' 또는 ")로 감싸고, 그 감싸진 문자열들 안에 중괄호{}를 사용하여 그 중괄호 안에 변수, 표현식 등을 삽입함.




# 아래는 gpt 예제

# < ex1: f-string과 문자열 사용 >
name = "Alice"
age = 10
print(f"My name is {name} and I am {age} years old")


# < ex2: f-string과 변수(표현식) 사용 >
a = 3
b = 4
print(f"{a}+{b}={a+b}")


# < ex3: f-string과 조건문 사용 >
num=3
print(f"The number is  {'even' if num % 2 == 0 else 'odd' }.")


# < ex4: f-string과 숫자 형식 지정하기 >
for i in range(1, 106):
    print(f"{i:04}") # 1부터 105까지의 각각의 수가 4자리 형태로 출력됨. 그냥 이건 출력시켜보면 자연스럽게 이해됨.


# < ex5: >
person = {""}