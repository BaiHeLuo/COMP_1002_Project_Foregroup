import math
import pygame
import sys
import random
import time

pygame.init()

# 设置屏幕
size = width, height = 400, 200
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Text Input")

input_box = pygame.Rect(50, 50, 300, 50)

# 设置文本框的颜色和文本颜色
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

# 设置文本框的字体
font = pygame.font.Font(None, 32)

# 初始化输入文本
text = ''
text_surface = font.render(text, True, color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # 检查鼠标点击是否在文本框内
            if input_box.collidepoint(event.pos):
                color = color_active
            else:
                color = color_inactive

        if event.type == pygame.KEYDOWN:
            # 处理键盘按下事件
            if color == color_active:
                if event.key == pygame.K_RETURN:
                    # 处理回车键按下事件
                    print(text)
                    break
                elif event.key == pygame.K_BACKSPACE:
                    # 处理退格键按下事件，删除最后一个字符
                    text = text[:-1]
                else:
                    # 处理其他键按下事件，将字符添加到文本中
                    text += event.unicode


            text_surface = font.render(text, True, color)

        # 绘制屏幕
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color, input_box, 2)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    pygame.display.flip()

pygame.quit()

user_name = text



#游戏部分
pygame.init()

# 设置颜色
WHITE = pygame.color.Color(255, 255, 255)
BLACK = pygame.color.Color(0, 0, 0)
RED = '#FF0000'

# 屏幕大小
size = width, height = (200, 400)
pygame.display.set_caption('Run with Numbers')
screen = pygame.display.set_mode(size)

# 难度
dif = 0

# 定义血量
player_life = 1


# 生成合适数字
def makeup(play_life):
    char_list = '+-*/'
    test = 0
    while 1 > 0:
        char = random.choice(char_list)
        num = random.randint(1, 9)
        if char == '+':
            test = player_life + num
        if char == '-':
            test = player_life - num
        if char == '*':
            test = player_life * num
        if char == '/':
            test = player_life / num
        if test >= 1 and test % 1 == 0 and test < 100:
            return char, num, test


# 设置计算方法
def comp(ans, char, num):
    if char == '+':
        return ans + num
    if char == '-':
        return ans - num
    if char == '*':
        return ans * num
    if char == '/':
        return ans / num


# 定义player
class Player():

    def __init__(self):
        x, y = (width / 2, height - 30)
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        # 运动函数
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x += 5
        if pressed_key[pygame.K_LEFT]:
            self.rect.x -= 5
        if self.rect.x <= -30:
            self.rect.x = -30
        if self.rect.x > 130:
            self.rect.x = 130


class road_line():

    def __init__(self):
        x, y = (width / 2, -400)
        self.image = pygame.image.load('lines.png')
        self.image = pygame.transform.scale(self.image, (10, 800))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        self.rect.y += 2

        if self.rect.y == 0:
            self.rect.y = -380


# 定义other
class Other1():

    def __init__(self):
        x, y = (width / 4, 0)
        self.image = pygame.image.load('blue.png')
        self.image = pygame.transform.scale(self.image, (100, 10))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        # 运动
        self.rect.y += 2

    def up(self):
        # 重置
        self.rect.y = 0


# 定义第二个other
class Other2():

    def __init__(self):
        x, y = (width * 3 / 4, 0)
        self.image = pygame.image.load('red.png')
        self.image = pygame.transform.scale(self.image, (100, 10))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        self.rect.y += 2

    def up(self):
        self.rect.y = 0


# 定义boss
class Boss():
    def __init__(self):
        x, y = (width / 2, 0)
        self.image = pygame.image.load('boss.png')
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        self.rect.y += 2


player = Player()
other1 = Other1()
other2 = Other2()
boss = Boss()
road_line = road_line()

# 各种计数器
ans = 1
counter = 0
counter1 = 0
counter2 = 0
counter_dif = 0

# 初始值
a1, a2, a3 = makeup(player_life)
b1, b2, b3 = makeup(player_life)
ans1 = 0
ans2 = 0

# 设置刷新速率
FPS = 60
clock = pygame.time.Clock()
running=True
while running:
    if counter_dif != 2:
        font = pygame.font.SysFont('微软雅黑', 25)
        difficult1 = font.render('use your keyboard ', True, BLACK)
        difficult2 = font.render('to choose num 1,2,3', True, BLACK)
        difficult3 = font.render('to select your difficult', True, BLACK)
        screen.fill(WHITE)
        screen.blit(difficult1, (10, 170))
        screen.blit(difficult2, (10, 200))
        screen.blit(difficult3, (10, 230))
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_1]:
            counter_dif = 2
            dif = 0
        if pressed_key[pygame.K_2]:
            counter_dif = 2
            dif = 1
        if pressed_key[pygame.K_3]:
            counter_dif = 2
            dif = 2
    else:

        if counter < 10:

            cha1 = a1 + str(a2)
            cha2 = b1 + str(b2)

            # 写字
            font = pygame.font.SysFont('微软雅黑', 30)
            word1 = font.render(cha1, True, BLACK)
            word2 = font.render(cha2, True, BLACK)
            word3 = font.render(str(player_life), True, BLACK)

            # 填充
            screen.fill(WHITE)
            screen.blit(road_line.image, road_line.rect)
            screen.blit(player.image, player.rect)
            screen.blit(other1.image, other1.rect)
            screen.blit(other2.image, other2.rect)

            other1.move()
            other2.move()
            player.move()
            road_line.move()
            screen.blit(word1, (other1.rect.x + 30, other1.rect.y - 30))
            screen.blit(word2, (other2.rect.x + 30, other2.rect.y - 30))
            screen.blit(word3, (170, 30))

            # 碰撞检测
            t1 = pygame.sprite.collide_rect(player, other1)
            t2 = pygame.sprite.collide_rect(player, other2)

            if t1 and player.rect.x <= 50:
                player_life = a3
            if t2 and player.rect.x > 50:
                player_life = b3
            if t1 or t2:
                ans1 = comp(ans, a1, a2)
                ans2 = comp(ans, b1, b2)

                # 下一次重置
                a1, a2, a3 = makeup(player_life)
                b1, b2, b3 = makeup(player_life)
                other1.up()
                other2.up()
                counter += 1

                # 最优解
                if ans1 > ans2:
                    ans = ans1
                else:
                    ans = ans2
        # boss关卡
        else:
            if counter2 == 0:
                # 生成boss数字

                if ans <= 100:
                    upper = ans
                else:
                    upper = 100
                low = math.ceil(upper * (0.6 + (0.15 * dif)))
                ans = random.randint(low, upper)
                counter2 = 1

            # 打印字
            font = pygame.font.SysFont('微软雅黑', 30)
            font1 = pygame.font.SysFont('微软雅黑', 25)
            word3 = font.render(str(player_life), True, BLACK)
            boss_life = font.render(str(ans), True, BLACK)
            game_win = font.render('you win', True, RED)
            game_lose = font.render('you lose', True, RED)
            game_over1 = font1.render('please touch nothing!!', True, RED)
            game_over2 = font1.render('data is being stored!!', True, RED)

            screen.fill(WHITE)
            screen.blit(player.image, player.rect)
            player.move()
            screen.blit(word3, (player.rect.x + 30, player.rect.y - 30))
            screen.blit(boss.image, boss.rect)
            if counter1 == 0:
                boss.move()
            screen.blit(boss_life, (boss.rect.x + 30, boss.rect.y - 30))

            # 碰撞检测
            t3 = pygame.sprite.collide_rect(player, boss)
            player_life = int(player_life)

            if t3:
                time_now = time.strftime('%Y-%m-%d %H:%M:%S')

                file = open('rank.txt', 'r+')
                lines = file.readlines()
                file.close()
                lines_new = []
                counter3 = 0

                # 排序
                if lines == []:
                    lines_new.append(f'{player_life}     {time_now}   level{dif + 1} {user_name}')
                else:
                    for i in range(len(lines)):
                        lines_new.append(lines[i])
                        take = int(lines[i][0:2])
                        if player_life >= take and counter3 == 0:
                            lines_new.insert(i, f'{player_life}     {time_now}  level{dif + 1} {user_name}')
                            counter3 += 1

                file = open('rank.txt', 'w+')

                for i in range(len(lines_new)):
                    file.write(f'{lines_new[i]}')
                file.close()
            if t3 and player_life >= ans:
                screen.blit(game_win, (70, 100))
                screen.blit(game_over1, (10, 200))
                screen.blit(game_over2, (10, 250))
                counter1 = 1

            if t3 and player_life < ans:
                screen.blit(game_lose, (70, 100))
                screen.blit(game_over1, (10, 200))
                screen.blit(game_over2, (10, 250))
                counter1 = 1

            # rank

            if t3:
                pygame.display.update()
                # 屏幕暂停
                time.sleep(3)
                running=False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    pygame.display.update()
    clock.tick(FPS + 30 * dif)



    #hall of fame
screen=pygame.display.set_mode((500,500))
screen.fill((225,225,225))
font = pygame.font.SysFont('微软雅黑', 25)
running=True
while running:
    for i in range(len(lines_new)):
        title=font.render('Hall of Fame',True,(255,0,0))
        rank = font.render(str(lines_new[i]), True, (255,0,0))
        screen.blit(rank, (30, 20+30*i))
        screen.blit(title,(40,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False