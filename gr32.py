# [ pickle ]
'''
- 프로그램에서 우리가 사용하고 있는 데이터를 파일 형태로 저장해주는 것
  그리고, 그 데이터를 우리가 다시 가져와서 코드로 사용할 수 있음
- with open('파일경로', '모드') as f:

'''

'''
아래에서
profile: 그냥 말 그대로 특정인의 프로필정보를 담고 있는 '리스트'임.
profile_list: '리스트 profile'과는 전혀 다른 '파일객체'임.
'''
import pickle


profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]} # '박명수'에 관한 프로필정보를 '딕셔너리 profile'에 담아 저장함.


# < '리스트 profile의 원소들'을 '파일객체 profile_list'에 '담기(쏟기)': pickle.dump(리스트명, 파일객체명) >
profile_file = open("profile.pickle", "wb") # wb: 쓰기 목적의 binary 파일 'profile_file'을 생성함. 또한, pickle에서는 따로 인코딩 설정할 필요 없음
                                            # 파일경로: profile.pickle / 모드: rb

print(profile)

pickle.dump(profile, profile_file) # '딕셔너리 profile'의 정보(원소들)를 '파일객체 profile_file'에 저장.
                                   # dump(q): dump(쏟다, 붓다) 뜻 그대로, 

profile_file.close()


#====================================================================================================================


# < '파일객체 profile_file의 데이터'를 '읽어와서(불러와서)' '리스트 profile에 담기': pickle.load(파일객체명) >
profile_file = open("profile.pickle", "rb") # 파일경로: profile.pickle / 모드: rb
profile = pickle.load(profile_file) # '파일객체 profile_file'의 데이터를 읽어와서(=불러와서), 이를 '리스트 profile'에 넣음.

print(profile)
profile_file.close()