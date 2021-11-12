#문자열
sentence ='나는 소년입니다.'
print(sentence)

sentence2 ="파이썬은 쉬워요"
print(sentence2)

sentence3 ="""
나는 소년이고,
파이썬은 쉬워요
"""

print(sentence3)

#문자열 처리 함수

python ="Python is Amazing"
print(python.lower()) # 전체 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper()) #첫번째 글자가 대문자인지 반환 ->True
print(len(python)) #길이 반환
print(python.replace("Python", "Java")) # 파이썬을 자바로 바꾸기

index =python.index("n") #n의 위치 찾기
print(index) # 5
index= python.index("n", index+1) #현재 저장된 5+1=6 , index 6 뒤쪽으로 있는 n의 index
print(index) #15 Amazing의 n

print(python.find("n")) #포함된 위치 인덱스 반환
print(python.find("java")) #포한된 글자 없으면 -1반환
#print(python.index("java")) 포함된 글자없으면 에러 발생


print(python.count("n")) #n 이 총 몇번 나오는지 출력


#문자열 포맷 d, s, c
print("나는 %d살 입니다." %20) #%위치에 20 들어간다 d : 정수 값만
print("나는 %s을 좋아해요." %"파이썬") #s : 문자열
print("Apple 은 %c로 시작해요." %"A") #c : 한글자만
print("나는 %s살 입니다." %20) #s 에 정수값 넣어도 무관
print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

#방법2
print("나는 {}살 입니다." .format(20)) #format 괄호안쪽 숫자를 {}안으로 넣음
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))


#방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age=20 ))

#방법 4(v3.6 이상)
age= 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #f쓰고 문장쓰기


#탈출문자
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")


# \", \' : 문장내에서 따옴표
#저는 "나도코딩" 입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.") #저는  "나도코딩"입니다.

#\\ :문장 내에서 \
print("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonBasic")

#\r: 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple

#\b : 백스페이스(한 글자 삭제)
print("Redd\bApple")# RedApple , d 하나가 삭제된

#\t : 탭
print("red\tapple") #red     apple
