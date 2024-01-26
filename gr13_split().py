# [ 문자열 나누기 split() ]

'''

- '문자열'을 특정 구분자(delimter)를 기준으로 분리하여 '리스트'로 반환하는 문자열 메소드.
  즉, split() ---> '문자열'을 구분자 기분으로 분리하여 '리스트'로 반환
'''

# < '공백'을 기준으로 문자열 나누기 >

# e.g 1)
a = 'Life is too short'

print(a.split())  # 출력값: [ 'Life', 'is', 'too', 'short']


# e.g 2)
text = "Hello World!"
words = text.split()
print(words)  # 출력값: [ 'Hello', 'World!' ]


# < ':'를 기준으로 문자열 나누기 >
b = "a : b : c : d"

print(b.split(':'))  # 출력값: [ 'a', 'b', 'c', 'd']

c = "a : b : c : d"
d = c.split(':')
print(d)
