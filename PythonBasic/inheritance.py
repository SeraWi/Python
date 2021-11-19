# 상속
# 매딕: 의무병, 체력 회복시켜주는 역할

#일반 유닛
class Unit :
    def __init__(self,name,hp,speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self,location):
        print("[지상유닛이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
             . format(self.name, location, self.speed))


#공격 유닛이 일반 유닛 상속 받아서 사용
class AttackUnit(Unit) :
    def __init__(self, name, hp ,speed, damage) :
        # 상속 받은 init
        Unit.__init__(self, name, hp, speed)
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


# 다중 상속 (부모 클래스를 2개이상을 상속 받는다)
# 자바는 다중 상속 불가능, 오직 단일 상속만 허용

#드랍쉽 : 공중 유닛, 수송기, 마린/ 파이어뱃/탱크 등을 수송, 공격 기능이 없다

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2} ]" \
            .format(name, location,self.flying_speed))


# 공중 공격 유닛 클래스 (공격 유닛 생속, 날수 있는 유닛 상속)
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        #멤버 변수 초기화
        AttackUnit.__init__(self,name,hp,0,damage)  #지상 스피드는 0으로 처리
        Flyable.__init__(self,flying_speed)
    def move(self, location) :
        print("[공중유닛이동]")
        self.fly(self.name, location)



# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200,60,5)
valkyrie.fly(valkyrie.name,"3시")


#오버로딩 : 상속관계에서 메서드 재정의

#벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌처" , 80,10,20)
#배틀크루저 : 공중 유닛, 체력, 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루져",500,25,3)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name,"3시")

battlecruiser.move("3시")

#pass

#건물
# class BulidingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass 
    # pass 완성되지 않았지만 pass시킴

# 서플라이 디폿 : 건물임, 1개 건물 = 8유닛을
#supply_depot = BulidingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")

# def game_over():
#     pass

# game_start()
# game_over()


#super

class BulidingUnit(Unit):
    def __init__(self, name, hp, location):
       # Unit.__init__(self.name,hp,0)
       super().__init__(name,hp,0) # 상속받는 부모 init 쓰기
       self.location = location
