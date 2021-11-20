# 내장함수 built -in- function
# 따로 import 하지 않아도 바로 사용 가능

# language = input("좋아하는 언어는 무엇입니까?")
# print("{0} 은 아주 좋은 언어 입니다." .format(language))

# #dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수 
# print(dir())
# import pickle
# print(dir())

# print(dir(random)) # 랜덤 함수 안에 있는 것들을 보여준다

# lst = [1,2,3]
# print(dir(lst))



# 외장 함수
#glob : 경로 내의 폴더/ 파일 목록 조회(윈도우 dir)
import glob
print(glob.glob("*.py")) #확장자가 py인 모든 파일 출력

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리 표시

folder ="sample_dir"
#폴더 있으면 구문 실행
if os.path.exists(folder) :
    print("이미 존재하는 폴더 입니다")
    #삭제하기
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else :
    #폴더 생성
    os.makedirs(folder)
    print(folder, "폴더를 생성합니다.")

print(os.listdir()) #glob 과 비슷

#시간 관련 외장함수
import time
print(time.localtime())
#원하는 형식으로 출력하기
print(time.strftime("%Y-%m-%d %H:%M:%S"))#2021-11-20 14:07:02

import datetime
print("오늘 날짜는" ,datetime.date.today())
#timedelta : 두날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) #100일 뒤를 저장
print("우리가 만난지 100일은 " ,today+td) #100일 후 알려주기 #우리가 만난지 100일은  2022-02-28

