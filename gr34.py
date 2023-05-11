# [ with ]

'''
- 'with 함수'는 파일 열기, 닫기, 수정 등이나 네트워크 연결과 같이 자원을 사용하는 경우에, '자동으로 자원을 해제하는 역할'을 함.
  이렇게 자동으로 자원을 해제(= 함수 close() )하면, 코드의 실수로 자원을 해제하지 않는 일을 방지할 수 있음.
- 기본 구조:
  with 자원객체명 as 변수명:
          코드작성블록


- with open('파일경로', '모드') as f: # '파일경로의 파일'을 '열어서(= open())', '변수'에 저장한 후,


'''


import pickle

# < >
with open("profile.pickle", "rb") as profile_file: # '파일 profile.pickle'을 '열어서(=open)', 그 내부 데이터를 '변수 profile_file'에 담은 후,
    print(pickle.load(profile_file)) # 그 '변수 profile_file'을 불러와서 출력하는 것임.
  
  
    
# < 파일 읽기 >
with open('example1.txt', 'r', encoding="utf-8") as f:
    data = f.read()

print(data)
    

# < 파일 (덮어)쓰기 1 >
with open('example1.txt', 'w', encoding="utf-8") as f: # 한글을 쓸 경우, encoding="utf-8" 넣어야 함. 그래야 해당 파일에서 글자가 안 깨짐
    f.write("Hallo Brother!")
    
# < 파일 (덮어)쓰기 2 >
with open('example2.txt', 'w') as f:
    f.write("What is up")
    
    
# < 여러 개의 파일 읽기 >
with open('example1.txt', 'r') as f1, open('example2.txt', 'r') as f2:
    data1 = f1.read()
    data2 = f2.read()
    
print(data1)
print(data2)