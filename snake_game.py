import pygame
import time
import random

# 初始化 pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 165, 0)

# 设置游戏窗口
width = 600
height = 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('刺激的贪吃蛇游戏')

# 设置游戏时钟
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# 字体样式
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

def score_display(score):
    value = score_font.render("Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def generate_food():
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    return (food_x, food_y)

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = generate_food()
    start_time = time.time()
    time_limit = 30  # 30秒时间限制

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("你输了! 按 C 继续或 Q 退出", red)
            score_display(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  # 动态背景
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        score_display(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            Length_of_snake += 1
            foodx, foody = generate_food()  # 生成新的食物

        # 检查时间限制
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
