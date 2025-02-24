import pygame as pg
from constants import *
from player import *

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clok =  pg.time.Clock()
    dt=0

    playe=player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)



    while True:
        screen.fill(("black"))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        
        playe.update(dt)

        playe.draw(screen)
        pg.display.flip()
        dt = (clok.tick(60))/1000


if __name__ =="__main__":
    main()