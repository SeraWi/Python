#continue 와 break

absent =[2,5] # 결석
no_book =[7] #책을 안가지고 온 학생
for student in range(1,11): # 10명의 학생
    if student in absent: #결석학생의 경우 빼고 책읽기 -> continue
        continue
    elif student in no_book: # 책 없는 경우 수업 종료 -> break
        print("오늘 수업 여기까지, {0}는 교무실로 따라와" .format(student))
        break
    print("{0}, 책을 읽어봐".format(student))


#한줄 for
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 ->101,102...

students =[1,2,3,4,5]
students =[i+100 for i in students]
print(students) #[101, 102, 103, 104, 105]


# 학생 이름을 길이로 변환
students =["Ironman", "Thor","I am groot"]
students= [len(i) for i in students]
print(students) #[7, 4, 10]

#학생이름을 대문자로 변환
students =["Ironman", "Thor","I am groot"]
students =[i.upper() for i in students]
print(students) #['IRONMAN', 'THOR', 'I AM GROOT']