# [ pickle ]
'''
- 프로그램에서 우리가 사용하고 있는 데이터를 파일 형태로 저장해주는 것
  그리고, 그 데이터를 우리가 다시 가져와서 코드로 사용할 수 있음
'''

import pickle

profile_file = open("profile.pickle", "wb") # - wb: 쓰기 목적의 binary 파일. 또한, pickle에서는 따로 인코딩 설정할 필요 없음
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]} # 딕셔너리 형태

print(profile)

pickle.dump(profile, profile_file) # '딕셔너리 profile'의 정보(원소들)를 file에 저장.

profile_file.close()