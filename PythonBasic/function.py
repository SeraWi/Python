# 함수 정의
# def 함수 이름() :
def open_account() :
    print("새로운 계좌가 생성되었습니다")

#함수 실행
open_account()


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은  {0} 원 입니다." .format(balance+ money))
    return balance + money

balance = 0 #잔액 0
balance = deposit(balance, 1000)
print(balance)


def withdraw(balance,money) : #출금
    if balance >= money : #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
    else: 
        print("출금 불가, 잔액은 {0}원입니다." .format(balance))
    return balance

balance = 0
balance = deposit(balance, 1000)
balacne = withdraw(balance, 500)

# 여러개의 값을 튜플로 반환
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission
balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance,500)
print("수수로{0} 원이며, 잔액은 {1}원입니다. " .format(commission, balance))

#기본값 설정하기

def profile(name, age, main_lang):
    print("이름 : {0} \t 나인: {1} \t 주 사용 언어: {2}" \
        .format(name, age, main_lang))


profile("유재석" ,20, "파이썬")
profile("김태호", 25, "자바")


#같은 학교, 같은 학년 같은 반 같은 수업
#즉 이름만 다르다
# 기본값 설정 : 매개변수 전달되지 않으면 기본값으로 들어감
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0} \t 나인: {1} \t 주 사용 언어: {2}" \
        .format(name, age, main_lang))
profile("유재석" )
profile("김태호")


print("-------------------------------------------------------")
#키워드값 이용한 함수 호출
#키워드 쓰며 순서 달라도상관 없어진다
def profile(name, age, main_lang):
    print(name,age,main_lang)

profile(name="유재석", main_lang= "자바", age=23)
profile(age= 30,main_lang ="파이썬", name="김태호")

# 가변인자
# * language
def profile(name,age,lang1,lang2,lang3,lang4,lang5):
    # end =" " 문장 이어서 출력
    print("이름 : {0} \t나이 :{1}\t" .format(name,age), end="")
    print(lang1,lang2,lang3,lang4,lang5)

profile("위세라", 20, "python","java", "c++","c#","C")
profile("위세라", 20, "kotlin","swift","","","")

print("-------------------------------------------------------")
def profile(name,age,*language):
    # end =" " 문장 이어서 출력
    print("이름 : {0} \t나이 :{1}\t" .format(name,age), end="")
    for lang in language:
        print(lang, end=" ")
    print()

profile("위세라", 20, "python","java", "c++","c#","C","Js")
profile("김태호", 20, "kotlin","swift")


print("-------------------------------------------------------")
# 지역변수와 전역변수
# 지역변수 : 함수내 변수
# 전역변수 : 모든 공간 전체 변수, 권장 되지 않는다. 

gun = 10

def checkpoint(soldiers) : #경계근무
    global gun # 전역 공간에 있는 gun을 사용 하겠다는 의미
    gun = gun- soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))

print("전체 총 :{0}" .format(gun))
checkpoint(2)
print("남은 총:{0}" .format(gun))



#방법2 파라미터로 보내기
def checkpoint_ret(gun, soldiers):
    gun = gun -soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun

print("전체 총 :{0}" .format(gun))
gun = checkpoint_ret(gun,2) # 함수 실행후 다시 넣기
print("남은 총:{0}" .format(gun))