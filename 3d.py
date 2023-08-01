from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random

pygame.init()

# キャラクターの速度
CHARACTER_SPEED = 3
#木の座標
tree_x1 = random.randint(0,50)
tree_x2 = random.randint(100,150)
tree_x3 = random.randint(200,250)
tree_x4 = random.randint(300,350)
tree_x5 = random.randint(400,450)

# ゲームウィンドウの作成
screen = pygame.display.set_mode((500,100))
pygame.display.set_caption("ゲーム")

clock = pygame.time.Clock()
back = pygame.image.load("back.jpg")
blue = pygame.image.load("blue.png")
brown = pygame.image.load("brown.png")
red = pygame.image.load("red.png")
tree = pygame.image.load("tree.png")

def main():
    x = 0
    y = 70

    is_moving = False
    move_delay = 0
    move_delay_time = 10  # ディレイの時間（ミリ秒）

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()

        '''if keys[pygame.K_w]:
            if not is_moving:
                y -= CHARACTER_SPEED
                is_moving = True
                move_delay = pygame.time.get_ticks() + move_delay_time'''

        '''if keys[pygame.K_s]:
            if not is_moving:
                y += CHARACTER_SPEED
                is_moving = True
                move_delay = pygame.time.get_ticks() + move_delay_time'''

        if keys[pygame.K_a]:
            if not is_moving:
                x -= CHARACTER_SPEED
                is_moving = True
                move_delay = pygame.time.get_ticks() + move_delay_time

        if keys[pygame.K_d]:
            if not is_moving:
                x += CHARACTER_SPEED
                is_moving = True
                move_delay = pygame.time.get_ticks() + move_delay_time

        # ディレイを経過したら移動可能にする
        if is_moving and pygame.time.get_ticks() > move_delay:
            is_moving = False

        # キャラクターが画面外に出ないように制限
        x = max(0, min(x,500))
        y = max(0, min(y,100))

        # 画面をクリア
        screen.fill((0,0,0))
        
        '''if (x//100)%2 != 0:
            pygame.draw.rect(screen,(255,255,255),(x,y,20,20))
            for i in range(5):
                screen.blit(red,[i*100,0])
        else:
            for i in range(5):
                screen.blit(red,[i*100,0])
            pygame.draw.rect(screen,(255,255,255),(x,y,20,20))'''
        
        for i in range(5):
            screen.blit(red,[i*100,0])
        '''for i in range(5):
            if i%2 != 0:
                 screen.blit(tree,[100*i,30])
                 screen.blit(tree,[100*i+50,30])'''
        screen.blit(tree,[tree_x1,30])
        screen.blit(tree,[tree_x3,30])
        screen.blit(tree,[tree_x5,30])
        pygame.draw.rect(screen,(255,255,255),(x,y,20,20))
        screen.blit(tree,[tree_x2,30])
        screen.blit(tree,[tree_x4,30])

        # 画面を更新
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()


