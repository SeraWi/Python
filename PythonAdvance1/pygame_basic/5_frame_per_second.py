#FPS : frame per second

import pygame

pygame.init() #초기화하기 - 반드시 해야한다

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #새로크기
screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기 : load(이미지경로)
background = pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\background.png") 

#스프라이트(캐릭터) 불러오기 ->캐릭터 계속 움직인다

character = pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해온다
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width /2) - character_width/2  #화면 가로의 절반 크기에 해당하는 위치에 위치시키기
character_y_pos = screen_height-character_height #화면 세로 크기 가장 아래에 위치시키기

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6


# 이벤트 루프
running =True #게임이 진행중인가? (화면이 꺼지지 않도록!)
while(running) :
    dt = clock.tick(30) #게임화면의 초당 프레임수를 설정
    #fps 높으면 빠르고 부드럽게 움직임

    #캐릭터가 100만큼 이동을 해야함
    #10fps : 1초 동안에 10번 동작 ->1번에 몇만큼 이동?10만큼 -> 10 *10 = 100
    #20fps : 1초 동안에 20번 동작  -> 1번에 5만큼 이동 -> 5*20 =100
    #print("fps : " +str(clock.get_fps()))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : #창을 끄는 버튼 x버튼을 누르면 이벤트 발생 -> 게임 종료
            running = False #게임이 진행중이 아님으로 바꾸기

        #사용자가 키보드를 눌렀을 때 ->캐릭터의 좌표를 바꿔주면 된다
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :  # 캐릭터를 왼쪽으로 
                to_x -=character_speed
            elif event.key == pygame.K_RIGHT : #캐릭터를 오른쪽으로
                to_x +=character_speed
            elif event.key == pygame.K_UP: #캐릭터를 위로
                to_y -=character_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로
                to_y +=character_speed

        if event.type == pygame.KEYUP : #방향기를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    #캐릭터 좌표 바꾸기
    character_x_pos +=to_x *dt
    character_y_pos +=to_y *dt

    #캐릭터가 화면 밖으로 나가지 않도록 1) 가로 경계값 처리
    if character_x_pos <0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width : #스크린 오른쪽끝에 붙어있을때
        character_x_pos = screen_width-character_width
    
    #세로 경계값 처리
    if character_y_pos <0:
        character_y_pos =0
    elif character_y_pos > screen_height - character_height : #스크린 오른쪽끝에 붙어있을때
        character_y_pos = screen_height-character_height

    # 스크린에 배경이미지를 0,0 좌표에 넣기 (왼쪽 가장 위치가 0,0 )
    screen.blit(background,(0,0))

    #캐릭터 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) 

    # 다른방법 2) 백그라운드 이미지 쓰지 않고 바로 색을 넣는 방법 : fill(rgb색)
    #screen.fill((0,0,255))
    
    #while 안에 돌때 게임 화면을 계속해서 다시 그리기(반드시 호출이 계속되어야 한다)
    pygame.display.update()


# pygame 종료
pygame.quit()

