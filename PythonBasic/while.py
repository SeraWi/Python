#while
customer ="토르"
index = 5
while index >=1:
    print("{0} 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
    index -=1
    if index ==0:
        print("커피는 폐기처분되었습니다.")

# 토르 커피가 준비 되었습니다. 5번 남았어요
# 토르 커피가 준비 되었습니다. 4번 남았어요
# 토르 커피가 준비 되었습니다. 3번 남았어요
# 토르 커피가 준비 되었습니다. 2번 남았어요
# 토르 커피가 준비 되었습니다. 1번 남았어요
# 커피는 폐기처분되었습니다.

#무한루프
# 무한루프 종료 ctrl c
# customer ="아이어맨"
# index =1
# while True:
#     print("{0} 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
#     index +=1


customer ="토르"
person ="Unknown"
# 이름에 맞는 손님 등장할때 while 종료
while  person != customer:
    print("{0} 커피가 준비 되었습니다" .format(customer))
    person = input("이름이 어떻게 되세요?")



