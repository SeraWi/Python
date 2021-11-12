# 집합(세트)
#  중복이 안됨, 순서 없음
# {}


my_set ={1,2,3,3,3}
print(my_set) #{1, 2, 3}

java ={"유재석","김태호","양세형"}
python =set(["유재석","박명수"])

#교집합구하기
print(java & python) #{'유재석'}
print(java.intersection(python)) #{'유재석'}

#합집합 구하기
print(java | python) #{'유재석', '김태호', '양세형', '박명수'}
print(java.union(python))

# 차집합(자바는 할 줄 알지만 파이썬은 몰라)
print(java-python) #{'김태호', '양세형'}
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")  #값 추가하기
print(python) #{'유재석', '박명수', '김태호'}
# dictionary에서 추가할떄는 cabinet["c-20"] = "조세호"식으로 추가 key, value


#java 에서 값 빼기 remove
java.remove("김태호")
print(java)