import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kouka_img = pg.image.load("fig/3.png")
    kouka_img = pg.transform.flip(kouka_img, True, False)
    kouka_rct = kouka_img.get_rect()
    kouka_rct.center = 300, 200
    tmr = 0
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        bg_x = bg_x % 3200

        screen.blit(bg_img, [-bg_x, 0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600-bg_x, 0])
        screen.blit(bg_img, [3200-bg_x, 0])
        key_lst = pg.key.get_pressed()
    
        kouka_rct.move_ip(2 * key_lst[pg.K_RIGHT]-key_lst[pg.K_LEFT], key_lst[pg.K_DOWN]-key_lst[pg.K_UP])
        kouka_rct.x = max(0, kouka_rct.x-1)
        screen.blit(kouka_img, kouka_rct)
        pg.display.update()
        tmr += 1
        bg_x += 1      
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()