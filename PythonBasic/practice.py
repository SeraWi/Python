# 숫자
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(5*3)
print(3*(3+1))

# 문자 '', "" 가능
print('풍선')
print("나비")
print("zzzzzzzz")
print("ㅋ"*9)

#boorlan 참/거짓
print(5>10) #false
print(5<10)
print(True)
print(not True) #false
print(not False) 

# 애완동물을 소개해 주세요
#변수 : 값 저장 공간
animal ="강아지"
name ="연탄이"
age = 4
hobby ="산책"
is_adult = age>=3

# 정수형 출력할 떄 str(숫자)

print("우리집 "+ animal+"의 이름은 "+name+"에요")
hobby ="공놀이"
#print(name+"는 "+ str(age)+"살이며, "+hobby+"을 아주 좋아해요")
print(name,"는 ", age,"살이며, ",hobby, "을 아주 좋아해요")
print(name+"는 어른일까요? "+str(is_adult))


#주석22: 27
'''
이렇게 여러
문장이 
주석처리 
된다
'''
#ctrl + / 

#연산자
print(1+1) 
print(3-1)
print(5*2)
print(6/3)


print(2**3) # 2^3 =8
print(5%3) # 나머지 구하기2
print(5//3) # 몫 구하기

print(10>3) #true
print(4>=7) #false
print(10<3)
print(10==3) #false
print(3+4==7)

print(1 != 3)
print(not (1!=3))
print((3>0) and (3<5)) #true
print((3>0) & (3<5)) #true and &

print((3>0) or (3 >5))  #true
print((3>0) | (3 >5))  #or |

print(5>4>3) #true
print(5>4>7) #false

print(2+3 *4) #14
print((2+3)*4) #20
number = 2+3 *4
print(number) #14
number = number +2
print(number) #16
number+=2#18
print(number) 
number*=2 #36
print(number)
number/=2 #18
print(number)
number-=2 #16
print(number)
number%=2 #0
print(number)

