# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")


for waiting_no in [0,1,2,3,4]:
    print("대기 번호 : {0}".format(waiting_no))
# 대기 번호 : 0
# 대기 번호 : 1
# 대기 번호 : 2
# 대기 번호 : 3
# 대기 번호 : 4

for waiting_no in range(5): # 0,1,2,3,4
    print("대기 번호 : {0}".format(waiting_no))

for waiting_no in range(1,6): # 1,2,3,4,5
    print("대기 번호 : {0}".format(waiting_no))



starbucks =["아이언맨","토르","아이엠그루트"]

for customer in starbucks:
        print("{0} 커피가 준비되었습니다." .format(customer))



# 한줄 for

