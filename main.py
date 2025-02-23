import pygame as pg
from constants import *
def main():
    pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.display.flip()


if __name__ =="__main__":
    main()