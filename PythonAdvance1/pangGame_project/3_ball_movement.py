# 3. 공 움직이기

import os
import pygame
#############################################################
# 기본 초기화 (반드시 해야 하는 것들)
# init 호출
pygame.init() 

#화면 크기 설정
screen_width = 640 #가로크기
screen_height = 480 #새로크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Sera Pang") #게임 이름

# FPS
clock = pygame.time.Clock()

#############################################################
# 1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등 )
current_path = os.path.dirname(__file__) #현재 파일 위치 반환
image_path = os.path.join(current_path, "images") #images 폴더 위치 반환

#배경만들기
background = pygame.image.load(os.path.join(image_path,"background.png"))
#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character= pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height- stage_height #스테이지 위에 위치

#캐릭터 이동방향
character_to_x = 0

#캐릭터 이동 속도
character_speed = 5

#무기 만들기
weapon =pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] #가로만 필요, 세로 필요 X

#무기는 한번에 여러발 발사 가능
weapons = [] #리스트로 관리, 무기의 x,y자표가 묶음으로 들어감

#무기 이동 속도
weapon_speed = 10

#공 만들기(4개 크기에 대해 따로 처리)
ball_images =[
    pygame.image.load(os.path.join(image_path,"balloon1.png")),
    pygame.image.load(os.path.join(image_path,"balloon2.png")),
    pygame.image.load(os.path.join(image_path,"balloon3.png")),
    pygame.image.load(os.path.join(image_path,"balloon4.png"))
]
# 공 크기에 따른 최초 스피드
ball_speed_y= [-18,-15,-12,-9] #index 0,1,2,3에 해당하는 값, 바닥에 튕기면 스피드 줄어든다

# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, # 공의 x좌표
    "pos_y" : 50 , # 공의 y좌표
    "img_idx" : 0, # 공의 이미지 idx
    "to_x" : 3, #공의 x축 이동 방향 -3이면 왼쪽으로 3이면 오른쪽으로
    "to_y" : -6, # 공의 y축 이동 방향
    "init_spe_y" : ball_speed_y[0]  #y 최초 속도
})




# 이벤트 루프
running =True 
while(running) :
    dt = clock.tick(30) #게임화면의 초당 프레임수를 설정

    # 2 . 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            running = False 
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:#캐릭터 왼쪽 이동
                character_to_x -=character_speed 
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽 이동
                character_to_x +=character_speed
            elif event.key== pygame.K_SPACE: #무기 발사
                #무기의 위치 : 현재 캐릭터 위치의 중앙 (캐릭터 왼쪽 좌표 + 캐릭터 절반 크기 -무기 절반 크기 )
                weapon_x_pos = character_x_pos +(character_width/2)-weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos]) #x,y좌표 넣기


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x =0




    # 3. 게임 캐릭터 위치 정의

    character_x_pos += character_to_x

    #경계값 처리 (캐릭터)
    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos >screen_width- character_width :
        character_x_pos = screen_width- character_width

    #무기 위치 조정
    #            현재 x좌표, y좌표 -스피드
    #               x좌표는 그대로 y는 줄어들어서 올라가는 효과
    weapons = [[w[0],w[1]- weapon_speed] for w in weapons] #무기 위치를 위로 올린다

    #천장에 닿은 무기 없애기
    weapons =[[w[0],w[1]] for w in weapons if w[1]> 0] # y좌표가 0보다큰것만!!천장에 닿지 닿은것만 저장

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls) :
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx=ball_val["img_idx"]

        ball_size= ball_images[ball_img_idx].get_rect().size #idx에 해당하는 image가져오기
        ball_width= ball_size[0]
        ball_height =ball_size[1]

        # 볼 경계값 처리, 벽에 닿으면 튕겨서 위치 이동시키기
        if ball_pos_x <0 or ball_pos_x >screen_width - ball_width:
           #튕겨서 반대 방향으로 움직이기
           ball_val["to_x"] = ball_val["to_x"] *-1 # 3->-3, -3->3

        #세로위치 ->스테이지에 닿으면 튕겨서 올라감
        if ball_pos_y >= screen_height - stage_height - ball_height :
            ball_val["to_y"] =ball_val["init_spe_y"]
        else:
            #그외의 모든 경우에는 속도를 증가
            #튕겨서 올라가는 속도를 줄어들도록(포물선)
            ball_val["to_y"] +=0.5
        
        ball_val["pos_x"] +=ball_val["to_x"]
        ball_val["pos_y"] +=ball_val["to_y"]




        

    # 4. 충돌 처리
    # 5. 화면에 그리기(순서대로 그린다)
    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx,val in enumerate(balls) :
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx= val["img_idx"]
        #                       idx 에 해당하는 볼 크기 이미지 가져오기
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))


    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))




    # 6. update ()반드시 호출
    pygame.display.update()
# pygame 종료
pygame.quit()

