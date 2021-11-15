# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사 입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님( 소요 시간 : 15 분)
# [ ] 2번째 손님( 소요 시간 : 50 분)
# [0] 3번째 손님( 소요 시간 : 5 분)
# ...
# [ ] 50번째 손님( 소요 시간 : 16 분)

# 총 탑승 승객 : 2분


# 내풀이

from random import *

index =0
for customer in range(1,51):
    time =randint(5,50)
    print("{0}번째 손님( 소요 시간 : {1} 분)" .format(customer,time))
    if  5<=time <=15 :
        index +=1

print( "총 탑승 승객 : {0}분" .format(index))


# 강의 풀이

cnt = 0 # 총 탑승 승객
for i in range(1,51): # 1~50 승객
    time = randrange(5,51) # 5~50 분 사이의 소요 시간 랜덤
    if 5 <= time <= 15: # 5분에서 15분 이내의 손님 -> 탑승승객수 증가
        print("[0] {0}번째 손님( 소요 시간 : {1} 분)" .format(i, time))
        cnt +=1
    else:
        print("[ ] {0}번째 손님( 소요 시간 : {1} 분)" .format(i, time))

print("총 탑승 승객 : {0} 분" .format(cnt))
