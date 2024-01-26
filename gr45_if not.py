# [ if not 문 ]
# https://sikaleo.tistory.com/100

# < not 0 >
if not 0: # 원래 '0 자체가 boolean의 False'를 의미하기 때문에, 'not 0'은 'boolean의 True'가 된다. 
          # 따라서, if문 실행조건인 boolean의 True에 해당되므로, 바로 아래 print('참')이 실행된다.
   print('참')
else: # 정수형
    print('거짓') # 출력값: 참
  
    
# < not None >
if not None: # 원래 'None 자체가 boolean의 False'를 의미하기 때문에, 'not None'은 당연히 'boolean의 True'가 된다.
             # 따라서, if문 실행조건인 boolean의 True에 해당되므로, 바로 아래 print('참')이 실행된다.
    print('참')
else:
    print('거짓') # 출력값: 참
    

# < not '' >
if not '': # 원래 ' '' 자체가 boolean의 False'를 의미하기 때문에, 'not '' '은 당연히 'boolean의 True'가 된다.
           # 따라서, if문 실행조건인 boolean의 True에 해당되므로, 바로 아래 print('참')이 실행된다.
    print('참')
else:
    print('거짓') # 출력값: 참
    
    