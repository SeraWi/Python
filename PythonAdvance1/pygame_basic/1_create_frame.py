import pygame

pygame.init() #초기화하기 - 반드시 해야한다

#화면 크기 설정
screen_width = 480 #가로크기
screen_hegiht = 640 #새로크기
screen = pygame.display.set_mode((screen_width,screen_hegiht))


#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 이벤트 루프
running =True #게임이 진행중인가? (화면이 꺼지지 않도록!)
while(running) :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : #창을 끄는 버튼 x버튼을 누르면 이벤트 발생 -> 게임 종료
            running = False #게임이 진행중이 아님으로 바꾸기


# pygame 종료
pygame.quit()

