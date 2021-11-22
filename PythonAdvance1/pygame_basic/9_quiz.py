# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐, x좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임이미지]
# 1. 배경 : 640 * 480(세로가로) -background.png
# 2. 캐릭터 : 70*70 - character.png
# 3. 똥 : 70*70 -enemy.png


from operator import pos
from os import execv
import pygame
from random import *
#############################################################
# 기본 초기화 (반드시 해야 하는 것들)
# init 호출
pygame.init() 

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #새로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Sera Game") #게임 이름

# FPS
clock = pygame.time.Clock()

#############################################################
# 1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등 )

# 배경 이미지 불러오기
background= pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\background.png")

#캐릭터 불러오기
character= pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

#캐릭터 이동 좌표

to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6


# 이벤트 루프
running =True 
while(running) :
    dt = clock.tick(30) #게임화면의 초당 프레임수를 설정

    #에너미 불러오기
    enemy_exist = False

    if enemy_exist ==False :
        enemy= pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\enemy.png")
        enemy_size = enemy.get_rect().size
        enemy_width = enemy_size[0]
        enemy_height = enemy_size[1]
        enemy_x_pos = randint(0, screen_width-enemy_width) #떨어지는  시작 위치 랜덤
        enemy_y_pos = 0 #가장 위에서 시작 

        #에너미 이동 좌표
        eto_x = 0
        eto_y = 0

        #에너미 속도
        enemy_speed = 0.2

        enemy_exist = True
    else: 
        pass
    


    # 2 . 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            running = False 

        #캐릭터 움직이기
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP :
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 to_x = 0

        
    #캐릭터 좌표 바꾸기 (이벤트 끝나면
    character_x_pos +=to_x *dt

    # 가로 경계값처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width- character_width


    # 3. 게임 캐릭터 위치 정의
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.right = enemy_y_pos

    # 4. 충돌 처리( 에너미랑 부딛히기 직전까지 에너미 계속 떨어지게 만든다)
    if character_rect.colliderect(enemy_rect):
            print("충돌") 
            running= False
    else:
        pass
            
        
    
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    # 6. update ()반드시 호출
    pygame.display.update()
# pygame 종료
pygame.quit()
