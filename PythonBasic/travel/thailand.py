class ThailandPackage :
    def detail(self):
        print("태국 패키지 3박 5일, 방콕 바타야 여행 , 야시장 투어, 가격 50만원sera")

if __name__ =="__main__" :
    print("Thailand모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행된다")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("Thailand 외부에서 모듈 호출")

# 이 모듈(파일)에서 호출하면 if 문 실행
# import 한 다른 파일에서 호출하면 else 문 실행