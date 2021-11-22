
import pygame
import random
#############################################################
# 기본 초기화 (반드시 해야 하는 것들)
# init 호출
pygame.init() 

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #t세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Sera Game") #게임 이름

# FPS
clock = pygame.time.Clock()

#############################################################
# 1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등 )
background = pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\background.png")
# 캐릭터 만들기
character = pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width /2 - character_width/2
charcter_y_pos= screen_height- character_height

#이동 위치
to_x = 0
character_speed = 10

#똥 만들기 
ddong = pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0,screen_width- ddong_width)
ddong_y_pos= 0
#스피드
ddong_speed = 10

# 이벤트 루프
running =True 
while(running) :
    dt = clock.tick(30) #게임화면의 초당 프레임수를 설정

    # 2 . 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            running = False 
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    
    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed
    # 똥이 아래로 떨어지고 나면 다시 위로 위치시키기
    if ddong_y_pos > screen_height:
        ddong_y_pos =0
        dding_x_pos = random.randint(0,screen_width- ddong_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = charcter_y_pos

    ddong_rect= ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    #충돌했는지
    if character_rect.colliderect(ddong_rect):
        print("충돌")
        running = False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,charcter_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    # 6. update ()반드시 호출
    pygame.display.update()
# pygame 종료
pygame.quit()

