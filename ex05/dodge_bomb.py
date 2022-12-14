from asyncio.windows_events import selector_events
import pygame as pg
import random
import sys
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

class Screen:
    def __init__(self,title,wh,img_path):
        # 練習１
        pg.display.set_caption(title) # 
        self.sfc = pg.display.set_mode(wh) 
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path) 
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,img_path,ratio,xy):
        self.sfc = pg.image.load(img_path) #"fig/6.png"
        self.sfc = pg.transform.rotozoom(self.sfc,0,ratio) #tori_sfc, 0, 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy  #900, 400

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)



class Bomb:
    def __init__(self, color,rad,vxy,scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc,color ,(rad,rad),rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


        self.sfc.blit(self.sfc, self.rct) 
        #scrn_sfc.blit(bomb_sfc, bomb_rct) 
        #vx, vy = +1, +1


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():

    def main(winstyle=0):
    # Initialize pygame
        if pg.get_sdl_version()[0] == 2:
            pg.mixer.pre_init(44100, 32, 2, 1024)
    pg.init()
    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None

        ##boom_sound = load_sound("boom.wav")
        #oot_sound = load_sound("car_door.wav")

    #if pg.mixer:
     #   music = os.path.join(main_dir, "data", "house_lo.wav")
      #  pg.mixer.music.load(music)
       # pg.mixer.music.play(-1)


    clock =pg.time.Clock()

    #1
    scr = Screen("逃げろ!こうかとん",(1600, 900),"fig/pg_bg.jpg")

    # 練習３
    kkt = Bird("fig/6.png",2.0,(900,400))
    kkt.update(scr)

    # 練習５
    bkb_lst=[]
    color_lst = ["rad","green","yellow"]
    for _ in range(5):
        bkb = Bomb((255,0,0),10, (+1, +1),scr)
        bkb_lst.append(bkb)
    #bkb.update(scr)
    

    # 練習２
    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        for i in range(5):
            bkb_lst[i].update(scr)
            if kkt.rct.colliderect(bkb_lst[i].rct):
                return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

            #if pg.mixer:
            #pg.mixer.music.fadeout(1000)
            #pg.time.wait(1000)