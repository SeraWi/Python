# 내장함수 built -in- function
# 따로 import 하지 않아도 바로 사용 가능

language = input("좋아하는 언어는 무엇입니까?")
print("{0} 은 아주 좋은 언어 입니다." .format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수 
print(dir())
import pickle
print(dir())

print(dir(random)) # 랜덤 함수 안에 있는 것들을 보여준다

lst = [1,2,3]
print(dir(lst))