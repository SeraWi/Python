#패키지 : 모듈을 모아둔것

#    패키지이름.파일이름(모듈)
# import travel.thailand
# from travel.vietnam import VietnamPackage

# #                       클래스바로 import 불가능
# #import travel.thailand.ThailandPackage()

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# #from 으로 import 하면 클래스도 import 가능
# from travel.thailand import ThailandPackage
# trip_to2 = ThailandPackage()
# trip_to2.detail()


# from travel import vietnam
# trip_to3 = vietnam.VietnamPackage()
# trip_to3.detail()


# __all__ 
# * travel 패키지에서 모든걸 import 하겠다
#  but !! __init__ 에서 __all__ 에 써줘야함
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()


import inspect
import random
# 어디서 임포트했는지 확인하기(위치 확인하기) :inspect.getfile()
print(inspect.getfile(random))
print(inspect.getfile(thailand)) #PythonBasic\travel\thailand.py
