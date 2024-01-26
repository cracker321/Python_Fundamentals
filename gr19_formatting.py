# [ 포맷팅 ]

name = 'Alice'
age = 5

greeting = "안녕, 나는 {}이고, {}살이야!".format(name, age) 
print(greeting)


# [ 인덱스 기반 포맷팅 ]
'''
파이썬 포맷팅 문법에서 '{}' 대신, '{0}', '{1}', '{2}.. 를 사용할 수 있다.
'인덱스'이기에 당연히 {0}부터 시작한다!
'''

fullName = '조유종'
firstName = '유종'
lastName = '조'
age = 32

greeting = '안녕, 내 성은 {1}이고, 이름은 {3}이야. 따라서, 내 풀네임은 {0} 이고, 나는 {2}살이야!'.format(fullName, lastName, age, firstName)
print(greeting)