import pygame, sys, random, math
from pygame.color import THECOLORS


def drawrect(screen):
    for i in range(150):
        left = random.randint(0, 1024)
        top = random.randint(0, 800)
        width = random.randint(0, 1024)
        height = random.randint(0, 800)
        line = random.randint(0, 2)
        color_name = random.choice(
            ['gray17', 'gold', 'gray10', 'yellow', 'gray11', 'grey61', 'grey60', 'darkseagreen', 'grey62', 'grey65',
             'gray12', 'grey67', 'grey66', 'grey69', 'gray21', 'lightsalmon4', 'lightsalmon2', 'lightsalmon3',
             'lightsalmon1', 'gray32', 'green4', 'gray30', 'gray31', 'green1', 'gray37', 'green3', 'green2',
             'darkslategray1', 'darkslategray2', 'darkslategray3', 'aquamarine1', 'aquamarine3', 'aquamarine2',
             'papayawhip', 'black', 'darkorange3', 'oldlace', 'lightgoldenrod4', 'gray90', 'orchid1', 'orchid2',
             'orchid3',
             'grey68', 'brown', 'purple2', 'gray80', 'antiquewhite3', 'antiquewhite2', 'antiquewhite1',
             'palevioletred3',
             'hotpink', 'lightcyan', 'coral3', 'gray8', 'gray9', 'grey32', 'bisque4', 'cyan', 'gray0', 'gray1', 'gray6',
             'bisque1', 'bisque2', 'bisque3', 'skyblue', 'gray', 'darkturquoise', 'rosybrown4', 'deepskyblue3',
             'grey63',
             'indianred1', 'grey78', 'lightpink', 'gray88', 'gray22', 'red', 'grey11', 'lemonchiffon3', 'lemonchiffon2',
             'lemonchiffon1', 'indianred3', 'violetred1', 'plum2', 'plum1', 'lemonchiffon4', 'gray99', 'grey13',
             'grey55',
             'darkcyan', 'chocolate4', 'lightgoldenrodyellow', 'gray54', 'lavender', 'chartreuse3', 'chartreuse2',
             'chartreuse1', 'grey48', 'grey16', 'thistle', 'chartreuse4', 'darkorchid4', 'grey42', 'grey41', 'grey17',
             'dimgrey', 'dodgerblue4', 'darkorchid2', 'darkorchid3', 'blue', 'rosybrown2', 'honeydew', 'gray18',
             'cornflowerblue', 'grey91', 'gray14', 'gray15', 'gray16', 'maroon4', 'maroon3', 'maroon2', 'maroon1',
             'gray13',
             'gold3', 'gold2', 'gold1', 'grey79'])
        color = THECOLORS[color_name]
    pygame.draw.rect(screen, color, [left, top, width, height], line)


def drawcircle(screen):
    pygame.draw.circle(screen, [255, 0, 0], [100, 100], 10, 0)


def drawrect1(screen):
    pygame.draw.rect(screen, [0, 0, 255], [200, 200, 400, 400], 2)


def drawpoint(screen):
    pointArr = []
    for x in range(0, 600):
        y = int(math.sin(x / 1024.0 * 8 * math.pi) * 200 + 260)
        # small rects make up sin shape
        # pygame.draw.rect(screen, [0, 0, 0], [x, y, 1, 1], 1)
        pointArr.append([x, y])
    pygame.draw.lines(screen, [0, 0, 0], False, pointArr, 2)


def animation(screen):
    boll = pygame.image.load("footboll.png")
    x = 50
    y = 50
    screen.blit(boll, [x, y])
    pygame.display.flip()
    for looper in range(1, 100):
        pygame.time.delay(20)
        pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
        x += 5
        screen.blit(boll, [x, y])
        pygame.display.flip()


def music(screen):
    """add music"""
    pygame.mixer.init()
    # splat = pygame.mixer.Sound("yuanzou.wav")
    # splat.play()
    pygame.mixer.music.load("yuanzou.mp3")
    pygame.mixer.music.set_volum(0.3)
    # 3 repeat three times
    # -1 repeat for ever
    pygame.mixer.music.play(3)


pygame.init()
screen = pygame.display.set_mode([1024, 600])
screen.fill([255, 255, 255])
music(screen)
animation(screen)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # if music is end ,then exit program
    if not pygame.mixer.music.get_busy():
        sys.exit()
