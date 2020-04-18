import pygame as pg
def start():
    pg.font.init()
    font = pg.font.SysFont(None, 50)
    screen = pg.display.set_mode((1280,720))
    pg.display.set_caption("Choose a Difficulty")
    pg.mouse.set_visible(True)
    while True:
        mysz = pg.mouse.get_pos()
        pg.draw.rect(screen, (100, 100, 200), pg.Rect(0, 0, 1280, 720))
        pg.draw.rect(screen, (50, 50, 50), pg.Rect(490, 50, 300, 100))
        text = font.render("Easy", True, (0, 255, 0))
        screen.blit(text, [590,75])
        pg.draw.rect(screen, (50, 50, 50), pg.Rect(490, 200, 300, 100))
        text = font.render("Medium", True, (255, 255, 0))
        screen.blit(text, [570, 225])
        pg.draw.rect(screen, (50, 50, 50), pg.Rect(490, 350, 300, 100))
        text = font.render("Hard", True, (255, 0, 0))
        screen.blit(text, [590, 375])
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                 sys.exit(0)
            if mysz[0] < 790 and mysz[0] > 490 and mysz[1] < 150 and mysz[1] > 50:
                pg.draw.rect(screen, (0, 0, 50), pg.Rect(490, 50, 300, 100))
                text = font.render("Easy", True, (0, 255, 0))
                screen.blit(text, [590, 75])
                pg.display.update()
                if pg.mouse.get_pressed()[0]:
                    return 1000
            if mysz[0] > 490 and mysz[0] < 790 and mysz[1] > 200 and mysz[1] < 300:
                pg.draw.rect(screen, (0, 0, 50), pg.Rect(490, 200, 300, 100))
                text = font.render("Medium", True, (255, 255, 0))
                screen.blit(text, [570, 225])
                pg.display.update()
                if pg.mouse.get_pressed()[0]:
                    return 500
            if mysz[0] > 490 and mysz[0] < 790 and mysz[1] > 350 and mysz[1] < 450:
                pg.draw.rect(screen, (0, 0, 50), pg.Rect(490, 350, 300, 100))
                text = font.render("Hard", True, (255, 0, 0))
                screen.blit(text, [590, 375])
                pg.display.update()
                if pg.mouse.get_pressed()[0]:
                    return 300
