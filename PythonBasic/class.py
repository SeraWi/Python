# #클래스
# #마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" #유닛의 이름 
# hp =40 # 유닛의 체력
# damage =5 #유닛의 공격력

# print("{} 유닛이 생성되었습니다." .format(name))
# print("체력{0}, 공격력{1} \n" .format(hp, damage))

# #탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드

# tank_name ="탱크"
# tank_hp =150
# tank_damage =35

# print("{} 유닛이 생성되었습니다." .format(tank_name))
# print("체력{0}, 공격력{1} \n" .format(tank_hp, tank_damage))

# def attack(name,location,damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]" .format(\
#     name, location, damage))

# attack(name,"1시", damage)
# attack(tank_name,"1시", tank_damage)


class Unit :
    def __init__(self,name,hp, damage) :
        self.name = name
        self.hp = hp
        self.damage =damage
        print("{}유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))
    


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


# __init__ : 파이썬 생성자임
# 멤버 변수 : 클래스내에서 정의된 변수

#레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("빼앗은레이스", 80, 5)
#                                           멤버변수 쓰기
print("유닛이름 : {0}, 공격력 :{1}" .format(wraith1.name, wraith1.damage))

# 마인트 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("레이스", 80,5)

# clocking 이라는 변수는 클래스 내에는 없음 
#파이썬은 추가로 변수를 할당할 수 없음
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


# 메서드 
class AttackUnit :
    def __init__(self, name, hp , damage) :
        self.name = name
        self.hp =hp
        self.damage = damage

    def attack (self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]" \
            .format(self.name,location, self.damage) )

    def damaged(self,damage) :
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다." .format(self.name))


# 파이어뱃 :공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)

