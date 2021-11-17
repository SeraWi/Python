import pickle

# with : 파일 입출력을 쉽게 할 수 있음
# close 할 필요 없음


#pickle읽어오기
#profile.prickle의 파일을 열어서 내용을  profile_file변수에 저장
with open("profile.pickle","rb") as profile_file :
    print(pickle.load(profile_file))

# close 할 필요가 없다


#일반적 파일을 with로 쓰기
# with open("study.txt", "w", encoding="utf") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")


# 파일 읽어오기
with open("study.txt" ,"r",encoding ="utf8") as study_file:
    print(study_file.read())