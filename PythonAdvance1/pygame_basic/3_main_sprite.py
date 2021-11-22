#캐릭터 추가하기

import pygame

pygame.init() #초기화하기 - 반드시 해야한다

#화면 크기 설정
screen_width = 480 #가로크기
screen_hegiht = 640 #새로크기
screen = pygame.display.set_mode((screen_width,screen_hegiht))


#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름


#배경 이미지 불러오기 : load(이미지경로)
background = pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\background.png") 

#스프라이트(캐릭터) 불러오기 ->캐릭터 계속 움직인다

character = pygame.image.load("C:\\Users\\wsr23\\OneDrive\\문서\\GitHub\\Python\\PythonAdvance1\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해온다
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width /2) - character_width/2  #화면 가로의 절반 크기에 해당하는 위치에 위치시키기
character_y_pos = screen_hegiht-character_height #화면 세로 크기 가장 아래에 위치시키기



# 이벤트 루프
running =True #게임이 진행중인가? (화면이 꺼지지 않도록!)
while(running) :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : #창을 끄는 버튼 x버튼을 누르면 이벤트 발생 -> 게임 종료
            running = False #게임이 진행중이 아님으로 바꾸기

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

