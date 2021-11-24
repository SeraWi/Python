balls=[1,2,3,4]
weapons= [11,22,3,44]

for ball_idx, ball_val in enumerate(balls):
    print("ball :" , ball_val)
    for weapon_dix, weapon_val in enumerate(weapons) :
        print("weapons :" , weapon_val)
        if ball_val == weapon_val :
            print("공과 무기가 충돌")
            break
    else:
        # for에 더이상 값이 없으면 바깥쪽 for문 동작
        continue

    #안쪽 for문 break되면 아래쪽 실행
    print("바깥 for 문 break")
    break

# ball : 1
# weapons : 11
# weapons : 22
# weapons : 3
# weapons : 44
# ball : 2
# weapons : 11
# weapons : 22
# weapons : 3
# weapons : 44
# ball : 3
# weapons : 11
# weapons : 22
# weapons : 3
# 공과 무기가 충돌
# ball : 4
# weapons : 11
# weapons : 22
# weapons : 3
# weapons : 44

# for 바깥 조건:
#     동작
#     for 안쪽 조건 :
#         동작
#         if 충돌 :
#             break
#     else:
#         continue
#     break