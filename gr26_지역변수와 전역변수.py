# [ 지역변수와 전역변수 ]

gun = 10 # 여기서의 '변수 gun'은 전역공간에서 선언되었지만, 개별 함수 내부에서 'global gun'을 선언하기 전에는
         # 이 '변수 gun'이 개별 함수 내부에 마치 지역변수와 같이 영향을 주지 못한다!

def checkpoint(soldiers):
    global gun # 3번 줄 전역공간에서 최초 선언된 gun의 값을 여기서 'global gun'으로 선언함으로써
               # 이제서야 드디어 '변수 gun'을 '전역변수 gun'으로 '받아들이게 된다!' 함수 내에서 '전역변수 gun'을 사용하겠다는 뜻.
               # cf) 그런데, '전역선언 global'을 자주 쓰면, 코드 관리가 어려워지기 때문에, 이렇게 하는 건 지양해야 함. 
    gun = gun - soldiers # 중요!!) 저 아래 어딘가에서 '함수 checkpoint'를 호출하면, 
                         # '그 지점부터'는 '변수 gun'이 사용될 때는 '전역변수 gun'이 아닌 '함수 checkpoint의 결과인 gun의 값 8'이 사용된다! 
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun)) # 3번 줄에서 최초 선언된 gun의 값 10 그대로 
checkpoint(2) # 2명이 경계근무 나감. 함수 checkpoint 호출. 3번 줄에서 최초 선언된 gun은 전역공간에 있지만, '함수 checkpoint'에는 영향을 주지 못함.
              # '함수 checkpoint' 내부에서 '3번 줄에서 최초 선언된 gun'을 사용하려면, 'gun=20'과 같은 것이 아니라, 별개로 'global gun'을 선언해줘야 함
              # '함수 checkpoint' 호출 결과, gun의 값은 이제 8이 되었음. 그리고, 그 8이 이 아래부터 gun=8 로 적용되어 시작함.
print("남은 총: {0}".format(gun)) # 3번 줄에서 최초 선언된 gun의 값 10이 함수 checkpoint 내부로 들어가서 


# ====================================================================================================================


# []

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

checkpoint_ret(gun, 20) # 여기서 인자값으로 적용되는 gun의 값은 8이다.
    