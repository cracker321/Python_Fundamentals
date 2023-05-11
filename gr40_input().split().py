# [ input().split() ]
# https://dojang.io/mod/page/view.php?id=2179
# https://dojang.io/mod/page/view.php?id=2286

'''
- 변수1, 변수2 = input().split()
- 변수1, 변수2 = input().split('기준문자열')
- 변수1, 변수2 = input('문자열').split()
- 변수1, 변수2 = input('문자열').split('기준문자열')
'''

# < ex1: '사용자가 입력할 문자열 3개(=input('문자열 세 개를 입력하세요))'를 '공백을 기준으로 분리(=split())' >
a, b, c = input('문자열 세 개를 입력하세요: ').split() # 입력받는 값을 공백을 기준으로 분리

print(a)
print(b)
print(c)


# < ex2: 두 숫자의 합 구하기 >

a, b = input('숫자 두 개를 입력하세요: ').split()

a = int(a)
b = int(b)

print(a+b)


# < ex3: map()을 사용하여 정수로 변환하기 >
'''
- 'input().split()'을 사용할 때 'map()'을 사용하면, 코드를 짧게 줄일 수 있다.
- 'ex2'에서 'input().split()'을 통해 입력받고 그 입력값을 분리한 값을, 매번 int로 변화하는 것은 귀찮음
  그 때, 이를 한 번에 손쉽게 해주는 것이 바로 map() 이다!
'''
a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) # 입력받는 값을 콤마를 기준으로 분리
print(a+b)



