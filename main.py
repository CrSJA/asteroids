import pygame as pg
from constants import *
def main():

    pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clok = pg.time.Clock()
    dt=0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        



        pg.display.flip()
        dt = (clok.tick(60))/1000


if __name__ =="__main__":
    main()