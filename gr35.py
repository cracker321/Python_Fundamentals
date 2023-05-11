# [ 문자열 인덱싱과 문자열 슬라이싱 ]

'''

'''

# ex1) 문자열 인덱싱
a = "Life is too short, You need Python"

print(a[1]) # 출력값: i
print(a[4]) # 출력값: 공백
print(a[-1]) # 출력값: n. 음수 인덱싱은 맨 마지막에서부터 -1 시작함. 당연히 -0이 아님. 왜냐면, -0과 0은 동일화기 때문!


# [ 문자열 슬라이싱 ]
# - 세미콜론(:) 뒤의 끝 번호는 포함되지 않는다! 즉, 출력값은 끝 번호의 앞자리 인덱스번호까지만 출력되는 것이다.
a = "Life is too short, You need Python"

print(a)
print(a[0:3]) # 출력값: Lif. 출력 대상 인덱스는 0, 1, 2 이다! 즉, 3번 인덱스는 포함되지 않는다!
print(a[3:9]) # 출력값: e is t
print(a[9:]) # 출력값: short, You need Python. 9번 인덱스부터 끝까지 출력된다.
print(a[:11]) # 출력값: Life is too. 처음부터 10번 인덱스까지 출력된다.
print(a[:]) # 출력값: 전체가 다 출력됨. 시작부터 끝까지.
print(a[12:-1]) # 출력값: short, You need Pytho. -1 번째 인덱스인 'n'의 앞자리 인덱스번호까지만 출력된다!
print(a[::2]) # 출력값: Lf stosot o edPto 처음(0번 인덱스인 'L')부터 2 간격으로 출력하는 것. 즉, 0번 2번 4번 6번 .. 인덱스에 해당하는 문자를 추출하는 것
print(a[::-3]) # 출력값: nt eu rsoseL. 맨 끝의 처음(인덱스 -1번인 'n')부터 거꾸로 3 간격으로 출력하는 것.
print(a[3::7]) # 출력값: eo,eh. 인덱스 3번부터 7개의 간격으로 출력하는 것.
print(a[::-5]) # 출력값: nPn hte. 맨 끝의 처음(인덱스 -1번인 'n')부터 거꾸로 5 간격으로 출력하는 것.

# print(a[5, 10, 3]) # '문자열 String'에서는 왼쪽과 같은 슬라이싱을 하지 못한다. 이것은 오직 '숫자형 integer'일 때 가능함. 5번 인덱스부터 9번 인덱스까지 3개 간격으로 추출 출력함.


# 
