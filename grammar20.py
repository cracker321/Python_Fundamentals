# [ 함수 ]

# 파이썬에서 텍스트 치환 단축키: ctrl + H
# ctrl + H로 텍스트상자에 입력한 후, 현재 페이지 전체에 해당 텍스트 치환 진행하려면, ctrl + alt + enter 누름

def open_account(): # 함수 생성
    print("새로운 계좌가 생성되었습니다.")
    
open_account() # 함수 호출

# ========================================================================================================

def deposit(balance, withdrawl_amount): # 함수 생성, 매개변수 입력
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance + withdrawl_amount))
    return balance + withdrawl_amount # 여기에서, 이 리턴문('return balance + withdrawl_amount')을 제거하더라도, 저~ 아래에서 deposit()함수를 호출할 때,
                           # '입금이 완료되었습니다. 잔액은 ~원 입니다'가 출력되는 이유는, 바로 위에 'print 출력문'이 여전히 실행되기 때문이다.
                           # 다만, 리턴값을 활용하고자 할 때는, 'return문'이 필요하기 때문에, 반환값을 활용하고자 하는 경우, 'return balance + withdrawl_amount'를 유지해야 함.
deposit(40, 5000)    

# ========================================================================================================

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)

# ========================================================================================================

def withdrawl(balance, withdrawl_withdrawl_amount):
    if balance > withdrawl_amount:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - withdrawl_amount))
        return balance - withdrawl_amount
    else:
        print("잔액부족으로 출금되지 않습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance
    
# ========================================================================================================

def withdrawl_night(balance, withdrawl_amount):
    fee = 100 # 수수료 100원
    return fee, balance - withdrawl_amount 
    
    
