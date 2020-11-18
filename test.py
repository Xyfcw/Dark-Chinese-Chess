import pygame
from pygame.locals import *
from sys import exit
'''
pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:

    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[-screen_size[1]//font_height:]

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))
    
    y = screen_size[1] - font_height

    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 255, 0)), (0, y))

        y -= font_height

    pygame.display.update()
'''
'''
background_image_filename = 'black_cannon.jpg'
 
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
 
x, y = 0, 0
move_x, move_y = 0, 0
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           exit()
        if event.type == KEYDOWN:
            #键盘有按下？
            if event.key == K_LEFT:
                #按下的是左方向键的话，把x坐标减一
                move_x = -1
            elif event.key == K_RIGHT:
                #右方向键则加一
                move_x = 1
            elif event.key == K_UP:
                #类似了
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            #如果用户放开了键盘，图就不要动了
            move_x = 0
            move_y = 0
 
        #计算出新的坐标
    x+= move_x
    y+= move_y

    screen.fill((0,0,0))
    screen.blit(background, (x,y))
    #在新的位置上画图
    pygame.display.update()
'''

'''
background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
#指定图像文件名称

pygame.init()
#初始化pygame,为使用硬件做准备
 
screen = pygame.display.set_mode((640, 480), 0, 32)
# screen = pygame.display.set_mode((800, 500), 0, 32)
#创建了一个窗口
pygame.display.set_caption("Hello, World!")
#设置窗口标题
 
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像
 
while True:
#游戏主循环
 
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
 
    screen.blit(background, (0,0))
    #将背景图画上去
 
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    # x-= mouse_cursor.get_width() / 2
    # x-= mouse_cursor.get_width() 
    # y-= mouse_cursor.get_height() / 2
    # y-= mouse_cursor.get_height()
    #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去
 
    pygame.display.update()
    #刷新一下画面
'''


a = Rect(1, 3, 2, 4)
print(a.size)