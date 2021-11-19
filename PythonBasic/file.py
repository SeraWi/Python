#파일 입출력
# 파일 열고 , 파일 이름, 쓰겠다 : W
score_file = open("score.txt","w", encoding="utf8")

print("수학 : 0", file= score_file)
print("영어 : 50" , file= score_file)
# 파일 닫기
score_file.close()

# a : 존재하는 파일에 이어서 쓰기
# w : 파일 덮어 쓰기
# score_file.write() :줄바꿈 자동으로 안됨
score_file = open("score.txt" ,"a", encoding ="utf8")
score_file.write("과학 : 80")
score_file.write("\n 코딩 : 100")
score_file.close()

# 파일을 읽어오기
score_file = open("score.txt", "r", encoding ="utf8")
print(score_file.read()) # 한번에 전체 내용읽어오기 -> 콘솔에 찍힌다
score_file.close()

score_file = open("score.txt","r", encoding="utf8")
print(score_file.readline(), end="") # 한줄만 읽어오기 수행, 한줄 읽고나서 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()


# 파일에 몇줄인지 모를때 처리 -> 반복문
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    # 읽어올 내용이 없으면 반복문 탈출 
    if not line:
        break
    print(line, end="")
score_file.close()

# 리스트에 넣어서 처리하기
score_file = open("score.txt", "r",encoding="utf8")
lines = score_file.readlines() # 모든 라인을 리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

