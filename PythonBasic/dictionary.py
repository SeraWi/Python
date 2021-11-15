#dictionary 자료형 / 사전
# key 와 value
# key는 중복 불가능
# {}

cabinet = {3:"유재석", 100:"김태호", "A" : "유재석"}
print(cabinet[3]) #유재석
print(cabinet[100]) #김태호

print(cabinet.get(3)) #유재석
#print(cabinet[5]) key 값 없으면 오류 발생
print(cabinet.get(5)) #key 값 없으면 None 출력
print(cabinet.get(5,"사용가능")) # key =5 가 있으면 value 반환, 없으면 사용가능 반환

print(3 in cabinet) # key값이 존재하는지 반환 True
print(5 in cabinet) # False

print(cabinet["A"]) #key 값 string 도 가능


#새 손님
cabinet ={"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet)
cabinet["c-20"] = "조세호"
print(cabinet) #{'A-3': '유재석', 'B-100': '김태호', 'c-20': '조세호'}

cabinet["A-3"] ="김종국"  #같은 키값 쓰면 덮어쓰기 된다
print(cabinet) #{'A-3': '김종국', 'B-100': '김태호', 'c-20': '조세호'}

#값 지우기
del cabinet["A-3"]
print(cabinet) #{'B-100': '김태호', 'c-20': '조세호'}

# key들만 출력
print(cabinet.keys()) #dict_keys(['B-100', 'c-20'])

# value들만 출력
print(cabinet.values()) #dict_values(['김태호', '조세호'])

#key, value쌍으로 출력
print(cabinet.items()) #dict_items([('B-100', '김태호'), ('c-20', '조세호')])

#cabinet 비우기
cabinet.clear() #{}
print(cabinet)