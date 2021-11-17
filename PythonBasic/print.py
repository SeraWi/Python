# 표준 입출력
print("Python", "Java") #Python Java
print("Python", "Java", sep= ",") #Python,Java
print("Python", "Java", sep= " ")
print("Python", "Java", sep= " vs ")
print("Python", "Java", "Javascript", sep= " vs ")

# print 한줄로 하기
# end : 문장 끝을  ?로 하고 다음줄 붙이기
print("Python", "Java", sep= ",", end ="?")
print("무엇이 더 재밌을까요?") #Python,Java?무엇이 더 재밌을까요?

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java",file=sys.stderr) #에러 처리

print("----------------------------------------")
#시험성적
scores = {"수학":0, "영어" :50, "코딩" :100}
for subject, score in scores.items():
   # print(subject,score)
   #ljust() : 왼쪽 정렬 rjust(): 오른쪽 정렬
    print(subject.ljust(8),str(score).rjust(4), sep =":")
#수학      :   0
#영어      :  50
#코딩      : 100

print("----------------------------------------")
#은행 대기순번표
#001 , 002, 003...
#zfil() :0으로 채우기
#zfill(3) : 3자리를 기본으로 하고 남는 자리에 0채우기
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3))

# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# 대기번호 : 004



print("----------------------------------------")
# 표준입력
answer = input("아무 값이나 입력하세요 : ") #문자열형태로 저장된다
print(type(answer)) # 숫자나 문자 다 string 으로 바뀐다
print("입력하신 값은 " +answer  +"입니다") # answer가 숫자여도 잘 출력된다str 안해도!


