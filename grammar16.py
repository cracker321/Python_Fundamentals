# [ f-string ]

# f-string은 파이썬에서 문자열을 간단하게 다루기 위한 기능임. 이 기능을 사용하면 문자열 안에서 변수나 표현식을 쉽게 사용할 수 있음.

# < f-string과 문자열 사용 >
name = "Alice"
age = 10
print(f"My name is {name} and I am {age} years old")


# < f-string과 변수(표현식) 사용 >
a = 3
b = 4
print(f"{a}+{b}={a+b}")


# < f-string과 조건문 사용 >
num=3
print(f"The number is  {'even' if num % 2 == 0 else 'odd' }.")


