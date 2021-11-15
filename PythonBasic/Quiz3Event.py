# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 추천 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random모듈의 schuffle과 sample 를 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다--

#(활용 예제)
from random import *
lst =[1,2,3,4,5]
print(lst)
shuffle(lst) 
print(lst) #[4, 1, 2, 3, 5]
print(sample(lst,1))#list에서 무작위로 하나 뽑기


from random import *
#users =[1,2,3,4,...100]
users =range(1,21) #1 부터 20까지의 숫자를 생성
print(type(users)) #<class 'range'>
users= list(users) #list 타입으로 변환 (list 는 순서가 있다)<class 'list'>
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4) #1명은 치킨, 3명은 커피 sample(list, 뽑을 갯수)
print(winners) #[15, 6, 13, 18]

print("-- 당첨자 발표 --")
print("치킨 당첨자 {0}" . format(winners[0])) #15
print("커피 당첨자 {0}" . format(winners[1:])) #[6, 13, 18]
print("-- 축하합니다.")