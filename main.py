usern = input("请告诉我你的名字: >>> ")
import pgzrun
from random import randint,choice
"""IMPORTANT: Size of the game"""
WIDTH = 700
HEIGHT = 390
"""Up here"""
"""Under Here we process the scores and top10"""
times = 0
maxscore = 666
# read and show top.10
top10score = open("ts", mode="r", encoding="utf-8")
t1stf = open("tts",mode = 'r',encoding='utf-8')
top10player = open("tp", mode="r", encoding="utf-8")
t1ptf = open("ttp",mode = 'r',encoding='utf-8')
tpp = open("tbp",mode = 'r',encoding='utf-8')
tps = open("tbs",mode='r',encoding="utf-8")
t1s = top10score.readline().split("ɞ")
t1st = t1stf.readline().split('ɞ')
t1p = top10player.readline().split("ɞ")
t1pt = t1ptf.readline().split('ɞ')
tppb = tpp.readline().split('ɞ')
tpsb = tps.readline().split('ɞ')
print("---------------------------------------------------------")
print("榜上前九:(正常模式中) ")
for num in range(0, 9):
    if num + 1 == 1:
        pl = '1st'
    elif num + 1 == 2:
        pl = '2nd'
    elif num + 1 == 3:
         pl = '3rd'
    else:
        pl = '%sth' % (num + 1)
    print("%s. %s  by  %s" % (pl, t1s[num], t1p[num]))
print()
print("榜上前九:(传送模式中)")
for num in range(0, 9):
    if num + 1 == 1:
        pl = '1st'
    elif num + 1 == 2:
        pl = '2nd'
    elif num + 1 == 3:
        pl = '3rd'
    else:
        pl = '%sth' % (num + 1)
    print("%s. %s  by  %s" % (pl, t1st[num], t1pt[num]))
print()
print("榜上前九:(奇怪模式中)")
for num in range(0, 9):
    if num + 1 == 1:
        pl = '1st'
    elif num + 1 == 2:
        pl = '2nd'
    elif num + 1 == 3:
        pl = '3rd'
    else:
        pl = '%sth' % (num + 1)
    print("%s. %s  by  %s" % (pl, tpsb[num], tppb[num]))
print("---------------------------------------------------------")
"""UP HERE"""
naton = 0
ppp = 0
got = 0
state = -1
mine = True
lock = False
lives = 1
gamemode = -1
et = 0
st = 0
gs = 0
gs1 = 0
mapn = -1
score = 0
sp_m = 2.9
sp_c = 1.4
sp_b = 2.1
sp_bat = 1.0
title = Actor("title.png")
title.x,title.y = 350,80
wm = Actor("welcome.png")
wm.x = 350
wm.y = 260
start = Actor("start.png")
start.x = 340
start.y = 190
selectMode = Actor("selectmode")
selectMode.x,selectMode.y = -1000,-2000
normal = Actor("normal")
transit = Actor("transit")
bizarre = Actor("bizarre")
normal.x,normal.y = -1000,-1000
transit.x,transit.y = -1000,-1000
bizarre.x,bizarre.y = -1000,-1000
cheese = Actor("cheese")
cheese.x = -500
cheese.y = -500
ball1 = Actor("ball")
ball1.x,ball1.y = -50,-50
ball2 = Actor("ball")
ball2.x,ball2.y = -50,-50
gameover = Actor("gameover")
gameover.x,gameover.y = -1600,-1600
bat = Actor("bat")
bat.x,bat.y = -100,-100
trap = Actor("trap")
trap.x,trap.y = -123,-213
vac = Actor("vac")
vac.x,vac.y = -233,-322
te = Actor("te")
te.x,te.y = 695,385
home = Actor("home")
home.x,home.y = -350,-260
nat = Actor("nat")
nat.x,nat.y = -333,-333
# under here is initing
playt = 0
stayt = 0
direction = ''
dc = ''
db1 = ''
db2 = ''
dbat = 's'
diss = ['w','a','s','d']
dc = choice(diss)
db1 = choice(diss)
db2 = choice(diss)
m0 = Actor('lr')
m1 = Actor('lr')
m2 = Actor('lr')
m3 = Actor('lr')
m4 = Actor('lr')
m5 = Actor('lr')
m6 = Actor('lr')
m7 = Actor('lr')
m8 = Actor('lr')
m9 = Actor('lr')
l = Actor('lr')
l.x,l.y = -1,195
r = Actor('lr')
r.x,r.y = 699,195
t = Actor('tb')
t.x,t.y = 350,0
b = Actor('tb')
b.x,b.y = 350,389
def thanks():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("致谢人名单：\n"
          "首席工程师：周东宜\n"
          "游戏想法框架：朱航（老鼠吃奶酪）\n"
          "实测人员：周东宜  朱航  杨辰宇\n"
          "评测人员：朱航  熊杨  李杨奥珊  杨辰宇  夏诚博  陆勤睿\n"
          "想法提供（非我原创）：\n"
          "  朱航：正常模式撞墙，奶酪会跑，加入配乐，白色地图，配乐El Dorado\n"
          "  熊杨：传送模式撞墙，捕鼠夹（现防疫卡口）\n"
          "  潘天乐：迷惑外卖\n"
          "  李杨奥珊：（未采纳）猫吃鱼加速\n"
          "  杨辰宇：（未采纳）奖励时间\n"
          "其中，朱航予以部分流程指导和精神支持，熊杨予以极大精神支持，\n"
          "夏诚博对本项目十分关注，提出要测试“特性”，但没有实现。\n"
          "我，朱航，熊杨三人共同提出游戏模式的选择。")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def sMode():
    gameover.x, gameover.y = -1600, -1600
    animate(title,pos=(title.x, -128))
    animate(start,pos=(start.x, -128))
    animate(selectMode,duration=2,pos=(350,90))
    animate(normal,duration=2,pos=(330,190))
    animate(transit,duration=2,pos=(400,300))
    animate(bizarre,duration=2,pos=(280,245))
def drawmap():
    global m0, m1, m2, m3, m4, m5, m6, m7, m8,m9,mapn
    b = randint(0,9)
    if 0 <= b and b < 4:
        mapn = 0
    elif 4 <= b and b < 7:
        mapn = 1
    elif 7 <= b and b < 9:
        mapn = 2
    elif b == 9:
        mapn = 3
    m0 = Actor('.\\%s\\m0'%(mapn))
    m1 = Actor('.\\%s\\m1'%(mapn))
    m2 = Actor('.\\%s\\m2'%(mapn))
    m3 = Actor('.\\%s\\m3'%(mapn))
    m4 = Actor('.\\%s\\m4'%(mapn))
    m5 = Actor('.\\%s\\m5'%(mapn))
    m6 = Actor('.\\%s\\m6'%(mapn))
    m7 = Actor('.\\%s\\m7'%(mapn))
    m8 = Actor('.\\%s\\m8'%(mapn))
    m9 = Actor('.\\%s\\m9'%(mapn))
    if mapn == 0:
        m0.x, m0.y = 60, 160
        m1.x, m1.y = 60, 40
        m2.x, m2.y = 50, 300
        m3.x, m3.y = 475, 75
        m4.x, m4.y = 550, 120
        m5.x, m5.y = 380, 150
        m6.x, m6.y = 430, 175
        m7.x, m7.y = 610, 345
        m8.x, m8.y = 670, 80
        m9.x,m9.y = 200,338
    if mapn == 1:
        m0.x, m0.y = 75,90
        m1.x, m1.y = 90,200
        m2.x, m2.y = 180,280
        m3.x, m3.y = 240,90
        m4.x, m4.y = 300,120
        m5.x, m5.y = 520,85
        m6.x, m6.y = 360,340
        m7.x, m7.y = 605,300
        m8.x, m8.y = 461,185
        m9.x, m9.y = 469,367
    if mapn == 2:
        m0.x, m0.y = 95,55
        m1.x, m1.y = 100,200
        m2.x, m2.y = 205,300
        m3.x, m3.y = 295,100
        m4.x, m4.y = 340,200
        m5.x, m5.y = 405,335
        m6.x, m6.y = 455,175
        m7.x, m7.y = 530,63
        m8.x, m8.y = 520,363
        m9.x, m9.y = 617,275
    if mapn == 3:
        m0.x, m0.y =60,140
        m1.x, m1.y =145,80
        m2.x, m2.y =180,240
        m3.x, m3.y = 240,240
        m4.x, m4.y = 330,120
        m5.x, m5.y = 350,350
        m6.x, m6.y = 420,200
        m7.x, m7.y = 580,125
        m8.x, m8.y = 610,80
        m9.x, m9.y = 611,300
        sounds.what.play()
def gamo1():
    global gamemode
    gamemode = 1
    animate(normal, pos=(-1000, -1000))
    animate(transit, pos=(-1000, -1000))
    animate(bizarre, pos=(-1000, -1000))
    animate(selectMode, pos=(-1000, -2000))
    stArt()
def gamo2():
    global gamemode
    gamemode = 2
    animate(transit, pos=(-1000, -1000))
    animate(normal, pos=(-1000, -1000))
    animate(bizarre, pos=(-1000, -1000))
    animate(selectMode, pos=(-1000, -2000))
    stArt()
def gamo3():
    global gamemode
    gamemode = 3
    animate(transit, pos=(-1000, -1000))
    animate(normal, pos=(-1000, -1000))
    animate(bizarre, pos=(-1000, -1000))
    animate(selectMode, pos=(-1000, -2000))
    stArt()
def on_mouse_down(pos):
    if start.collidepoint(pos):
        sMode()
    if transit.collidepoint(pos):
        gamo2()
    if normal.collidepoint(pos):
        gamo1()
    if bizarre.collidepoint(pos):
        gamo3()
    if te.collidepoint(pos):
        thanks()
def on_key_down(key):
    global direction,state
    if key == keys.RETURN and state == 1:
        sMode()
    if key == keys.W or key == keys.UP:
        direction = 'w'
    if key == keys.A or key == keys.LEFT:
        direction = 'a'
    if key == keys.D or key == keys.RIGHT:
        direction = 'd'
    if key == keys.S or key == keys.DOWN:
        direction = 's'
    if key == keys.E or key == keys.Q:
        if wm.colliderect(home):
            direction = ''
def stArt():
    global dc,db1,db2,dbat,direction,state,trap,sp_c,sp_b,sp_m,sp_bat,score,maxscore,times,mapn,playt,st,gs,mine,\
        gamemode,lives,gs1,et,vt,got,naton,stayt,ppp
    drawmap()
    sounds.start.play()
    if mapn == 3:
        music.play("m")
    else:
        music.play('m0')
    sounds.dead.stop()
    sounds.cough.stop()
    lives = 1
    cheese.image = 'cheese'
    mine = True
    ppp = 0
    naton = 0
    stayt = 0
    got = 0
    et = 0
    vt = 0
    st = 0
    gs = 0
    gs1 = 0

    score = 0
    sp_m = 3
    sp_c = 2
    sp_b = 2.1
    sp_bat = 1.0
    playt = 0
    # gameover.x,gameover.y = -1600,-1600
    nx, ny = randint(50, 650), randint(50, 350)
    while nx in range(int(wm.x) - 16, int(wm.x) + 16) and ny in range(int(wm.y) - 16, int(wm.y) + 16):
        print(nx,ny)
        nx, ny = randint(50, 650), randint(50, 350)
        print(nx,ny)
    trap.x, trap.y = nx, ny
    while trap.colliderect(m0) or trap.colliderect(m1) or trap.colliderect(m2) or trap.colliderect(
            m3) or trap.colliderect(m4) \
            or trap.colliderect(m5) or trap.colliderect(m6) or trap.colliderect(m7) or trap.colliderect(m8) \
            or trap.colliderect(m9):
        print(nx,ny)
        nx, ny = randint(50, 650), randint(50, 350)
        trap.x, trap.y = nx, ny
    state = 0
    animate(bat,pos = (51,15))
    dbat = 's'
    direction = ''
    # Here we check if balls colliderected wall if so,then it changes another place
    cheese.x, cheese.y = randint(50, 650), randint(50, 340)
    ball1.x, ball1.y = randint(50, 650), randint(50, 340)
    ball2.x, ball2.y = randint(50, 650), randint(50, 340)
    while ball1.colliderect(m0) or ball1.colliderect(m1) or ball1.colliderect(m2) or ball1.colliderect(m3) or ball1.colliderect(m4) \
            or ball1.colliderect(m5) or ball1.colliderect(m6) or ball1.colliderect(m7) or ball1.colliderect(m8)\
            or ball1.colliderect(m9) \
        or ball2.colliderect(m0) or ball2.colliderect(m1) or ball2.colliderect(m2) or ball2.colliderect(m3) or ball2.colliderect(m4) \
        or ball2.colliderect(m5) or ball2.colliderect(m6) or ball2.colliderect(m7) or ball2.colliderect(m8) \
        or ball2.colliderect(m9):
        ball1.x, ball1.y = randint(50, 650), randint(50, 340)
        ball2.x, ball2.y = randint(50, 650), randint(50, 340)
    dc,db1,db2 = choice(diss),choice(diss),choice(diss)
    wm.image = "mou1"
    while wm.colliderect(m0) or wm.colliderect(m1) or wm.colliderect(m2) or wm.colliderect(m3) or wm.colliderect(m4) \
            or wm.colliderect(m5) or wm.colliderect(m6) or wm.colliderect(m7) or wm.colliderect(m8) or wm.colliderect(m9):
        wm.x,wm.y = randint(50,650),randint(50,340)
    top10score = open("ts", mode="r", encoding="utf-8")
    t1stf = open("tts",mode = 'r',encoding='utf-8')
    top10player = open("tp", mode="r", encoding="utf-8")
    t1ptf = open("ttp",mode = 'r',encoding='utf-8')
    tpp = open("tbp",mode = 'r',encoding='utf-8')
    tps = open("tbs",mode='r',encoding="utf-8")
    t1s = top10score.readline().split("ɞ")
    t1st = t1stf.readline().split('ɞ')
    t1p = top10player.readline().split("ɞ")
    t1pt = t1ptf.readline().split('ɞ')
    tppb = tpp.readline().split('ɞ')
    tpsb = tps.readline().split('ɞ')
    if gamemode == 1:
        maxscore = t1s[0]
    elif gamemode == 2:
        maxscore = t1st[0]
    elif gamemode == 3:
        maxscore = tpsb[0]
    top10score.close()
    top10player.close()
    t1stf.close()
    t1ptf.close()
    tpp.close()
    tps.close()
    home.x, home.y = wm.x,wm.y
def lunlock():
    global lock
    lock = False
def nomine():
    global mine
    mine = True
def gameOver(why=0):
    global gameover,wm,ball1,ball2,direction,dc,db1,dbat,db2,score,maxscore,stayt,t1s,t1p,t1st,t1pt,tppb,tpsb,usern,mapn,state,gamemode,times,lives
    direction, dc, db1, db2,dbat = '','','','',''
    # animate(cheese,pos = (-160,-160))
    cheese.x,cheese.y = -160,-160
    stayt = 0
    ball1.x,ball1.y,ball2.x,ball2.y = -33,-33,-55,-55
    bat.x,bat.y = -100,-100
    music.stop()
    sounds.dead.stop()
    sounds.cough.stop()
    gameover.x, gameover.y = 350, 195
    nat.x, nat.y = -333, -333
    home.x,home.y = -1233,-3211
    if why == 1:
        wm.image = 'die2'
        gameover.image = 'go2'
        sounds.dead.play()
    elif why == 0:
        wm.image = 'die'
        gameover.image = 'gameover'
        sounds.cough.play()
    elif why == 2:
        wm.image = 'die2'
        gameover.image = 'g3'
        sounds.dead.play()
    elif why == 3:
        wm.image = "die2"
        gameover.image="gm3"
        sounds.dead.play()
    state = 1
    trap.x,trap.y = -33,-33
    bat.x,bat.y = -100,-100
    vac.x,vac.y = -233,-322
    # find if you made a record
    if gamemode == 1:
        for i in range(9):
            if score > int(t1s[i]):
                t1s.insert(i,t1s[i-1])
                t1s[i] = str(score)
                t1s = t1s[0:10]
                t1p.insert(i,t1p[i-1])
                if mapn == 3:
                    t1p[i] = str(usern) + " At StrangeMap3"
                else:
                    t1p[i] = str(usern) + " 在正常模式"
                t1p = t1p[0:10]
                break
        top10playe = open("tp", mode='w', encoding="utf-8")
        top10scor = open("ts", mode="w", encoding="utf-8")
        top10scor.write("ɞ".join(t1s))
        top10playe.write("ɞ".join(t1p))
        top10playe.close()
        top10scor.close()
    if gamemode == 2:
        for i in range(9):
            if score > int(t1st[i]):
                t1st.insert(i,t1st[i-1])
                t1st[i] = str(score)
                t1st = t1st[0:10]
                t1pt.insert(i,t1pt[i-1])
                if mapn == 3:
                    t1pt[i] = str(usern) + " At StrangeMap3" + " 在传送模式"
                else:
                    t1pt[i] = str(usern) + " 在传送模式"
                t1pt = t1pt[0:10]
                break
        top10playe = open("ttp", mode='w', encoding="utf-8")
        top10scor = open("tts", mode="w", encoding="utf-8")
        top10scor.write("ɞ".join(t1st))
        top10playe.write("ɞ".join(t1pt))
        top10playe.close()
        top10scor.close()
    if gamemode == 3:
        for i in range(9):
            if score > int(tpsb[i]):
                tpsb.insert(i,tpsb[i-1])
                tpsb[i] = str(score)
                tpsb = tpsb[0:10]
                tppb.insert(i,tppb[i-1])
                if mapn == 3:
                    tppb[i] = str(usern) + " At StrangeMap3" + " 在奇怪模式"
                else:
                    tppb[i] = str(usern) + " 在奇怪模式"
                tppb = tppb[0:10]
                break
        top10playe = open("tbp", mode='w', encoding="utf-8")
        top10scor = open("tbs", mode="w", encoding="utf-8")
        top10scor.write("ɞ".join(tpsb))
        top10playe.write("ɞ".join(tppb))
        top10playe.close()
        top10scor.close()
    times += 1
    if times != 0:
        """Under Here we process the scores and top9"""
        # read and show top.10
        top10score = open("ts", mode="r", encoding="utf-8")
        t1stf = open("tts", mode='r', encoding='utf-8')
        top10player = open("tp", mode="r", encoding="utf-8")
        t1ptf = open("ttp", mode='r', encoding='utf-8')
        tpp = open("tbp", mode='r', encoding='utf-8')
        tps = open("tbs", mode='r', encoding="utf-8")
        t1s = top10score.readline().split("ɞ")
        t1st = t1stf.readline().split('ɞ')
        t1p = top10player.readline().split("ɞ")
        t1pt = t1ptf.readline().split('ɞ')
        tppb = tpp.readline().split('ɞ')
        tpsb = tps.readline().split('ɞ')
        print("---------------------------------------------------------")
        print("榜上前九:(正常模式中)")
        for num in range(0, 9):
            if num + 1 == 1:
                pl = '1st'
            elif num + 1 == 2:
                pl = '2nd'
            elif num + 1 == 3:
                pl = '3rd'
            else:
                pl = '%sth' % (num + 1)
            print("%s. %s  by  %s" % (pl, t1s[num], t1p[num]))
        print()
        print("榜上前九:(传送模式中)")
        for num in range(0, 9):
            if num + 1 == 1:
                pl = '1st'
            elif num + 1 == 2:
                pl = '2nd'
            elif num + 1 == 3:
                pl = '3rd'
            else:
                pl = '%sth' % (num + 1)
            print("%s. %s  by  %s" % (pl, t1st[num], t1pt[num]))
        print()
        print("榜上前九:(奇怪模式中)")
        for num in range(0, 9):
            if num + 1 == 1:
                pl = '1st'
            elif num + 1 == 2:
                pl = '2nd'
            elif num + 1 == 3:
                pl = '3rd'
            else:
                pl = '%sth' % (num + 1)
            print("%s. %s  by  %s" % (pl, tpsb[num], tppb[num]))
        print("---------------------------------------------------------")
        top10score.close()
        top10player.close()
        t1stf.close()
        t1ptf.close()
        tpp.close()
        tps.close()
        print("")
def donat():
    global naton
    if naton >= 15:
        naton = 0
        sounds.enhen.play()
        cheese.x, cheese.y = randint(50, 650), randint(50, 340)
        nat.x,nat.y = -100,-100
    else:
        pass
def update():
    global direction,dc,diss,db1,db2,wm,top,left,right,bot,m0, m1, m2, m3, m4, m5,\
        m6, m7, m8,m9,score,sp_m,sp_c,sp_b,sp_bat,ball2,ball1,trap,dbat,playt,et,mapn,\
        st,gs,gamemode,et,lives,gs1,lock,vt,mine,mines,got,naton,stayt,ppp
    if stayt >= 600:
        gameOver(why=3)
    # Do nat
    if nat.colliderect(wm):
        donat()
    # When Touched cheese
    if wm.colliderect(cheese):
        if not wm.colliderect(home):
            stayt = 0
        if mine:
            if sp_c < 34:
                sp_c += 0.051
                sp_b += 0.031
                sp_m += 0.011
                sp_bat += 0.008
            got += 2
            gs += 2
            gs1 += 2
            naton += 2
            if naton <= 15:
                cheese.x, cheese.y = randint(50, 650), randint(50, 340)
            else:
                sounds.nope.play()
                nat.x, nat.y = randint(55, 645), randint(55, 335)
                cheese.x, cheese.y = -100,-100
            et = 1
            sounds.pick.play()
            dc = choice(diss)
            mines = randint(0, 5)
        elif not mine:
            gameOver(why=2)
        if naton <= 15:
            if mines < 2:
                mine = False
            else:
                mine = True
    # Bring them back home
    if wm.colliderect(home):
        score += got
        stayt += 1
        if got != 0:
            sounds.bb.play()
        got = 0
    # When touched wm
    if ball1.colliderect(wm) or ball2.colliderect(wm):
        if not wm.colliderect(home):
            if direction == 's':
                direction = 'w'
                wm.y -= sp_b * 1.4
            elif direction == 'd':
                direction = 'a'
                wm.x -= sp_b * 1.4
            elif direction == 'w':
                direction = 's'
                wm.y += sp_b * 1.4
            elif direction == 'a':
                direction = 'd'
                wm.x += sp_b * 1.4
            if not lock:
                lives -= 1
                db1,db2 = choice(diss),choice(diss)
                vt -= 1
                sounds.min.play()
                clock.schedule(lunlock,1.5)
        else:
            sounds.stop.stop()
            sounds.stop.play()
            db1,db2 = choice(diss),choice(diss)
    if trap.colliderect(wm) or wm.colliderect(bat):
        if state == 0:
            gameOver(why = 1)
    if lives <= 0 and state != 1:
        gameOver()
    if wm.colliderect(vac) and lives <= 3:
        lives += 1
        sounds.get.play()
        vac.x,vac.y = -222,-222
        vt += 1
    # cat who likes to eat cheese
    if ball2.colliderect(cheese) or ball1.colliderect(cheese):
        if et == 1 and (score - 2) > 0:
            yn = randint(0,7)
            if yn == 1 or yn == 2 or yn == 3 or yn == 6:
                cheese.x, cheese.y = randint(50, 650), randint(50, 340)
                score -= 1
                sounds.yummy.play()
                et = 0
            et = 0
        else:
            pass
    # Just get some vaccines!
    if gs1 == 12:
        if vt < 3:
            vac.x,vac.y = randint(50,650),randint(50,340)
        gs1 = 0
    # Go somewhere
    if direction == 'w' and wm.top > 0 and state != 1 and state != -1:
        wm.y -= sp_m
    if direction == 'a' and wm.left >0 and state != 1 and state != -1:
        wm.x -= sp_m
    if direction == 'd' and wm.right < WIDTH and state != 1 and state != -1:
        wm.x += sp_m
    if direction == 's' and wm.bottom < HEIGHT and state != 1 and state != -1:
        wm.y += sp_m
    #bat moving
    if dbat == 's':
        if bat.colliderect(b):
            dbat = 'd'
        bat.y += sp_bat
    elif dbat == 'w':
        if bat.colliderect(t):
            dbat = 'a'
        bat.y -= sp_bat
    elif dbat == 'a':
        if bat.colliderect(l):
            dbat = 's'
        bat.x -= sp_bat
    elif dbat == 'd':
        if bat.colliderect(r):
            dbat = 'w'
        bat.x += sp_bat
    #cheese moving
    if mine:
        cheese.image = 'cheese'
        if dc == 'w' and cheese.top > 0:
            cheese.y -= sp_c
        if dc == 'a' and cheese.left >0:
            cheese.x -= sp_c
        if dc == 'd' and cheese.right < WIDTH:
            cheese.x += sp_c
        if dc == 's' and cheese.bottom < HEIGHT:
            cheese.y += sp_c
    else:
        cheese.image = 'cheese2'
        animate(cheese,tween='linear',duration=1.4,pos=(int(trap.x),int(trap.y)))
        # What's this?
        if int(cheese.x) in list(range(int(trap.x) - 20, int(trap.x) + 20)) and int(cheese.y) in list(
                range(int(trap.y) - 15, int(trap.y) + 15)) and not mine:
            mine = True
            sounds.en.play()
    #ball moving
    if db1 == 'w' and ball1.top > 0:
        ball1.y -= sp_c
    if db1 == 'a' and ball1.left >0:
        ball1.x -= sp_c
    if db1 == 'd' and ball1.right < WIDTH:
        ball1.x += sp_c
    if db1 == 's' and ball1.bottom < HEIGHT:
        ball1.y += sp_c
    if db2 == 'w' and ball2.top > 0:
        ball2.y -= sp_c
    if db2 == 'a' and ball2.left >0:
        ball2.x -= sp_c
    if db2 == 'd' and ball2.right < WIDTH:
        ball2.x += sp_c
    if db2 == 's' and ball2.bottom < HEIGHT:
        ball2.y += sp_c
    # When Meet Walls
    if wm.colliderect(m0) or wm.colliderect(m1) or wm.colliderect(m2) or wm.colliderect(m3) or wm.colliderect(m4) \
            or wm.colliderect(m5) or wm.colliderect(m6) or wm.colliderect(m7) or wm.colliderect(m8) or wm.colliderect(m9):
        if gamemode == 1:
            if direction == 's':
                direction = 'w'
                wm.y -= sp_m * 1.25
            elif direction == 'd':
                direction = 'a'
                wm.x -= sp_m * 1.25
            elif direction == 'w':
                direction = 's'
                wm.y += sp_m * 1.25
            elif direction == 'a':
                direction = 'd'
                wm.x += sp_m * 1.25
        if gamemode == 2:
            wm.x,wm.y = randint(40,660),randint(40,350)
        if gamemode == 3:
            if direction == 's':
                direction = choice(diss)
                wm.y -= sp_m * 1.25
            elif direction == 'd':
                direction = choice(diss)
                wm.x -= sp_m * 1.25
            elif direction == 'w':
                direction = choice(diss)
                wm.y += sp_m * 1.25
            elif direction == 'a':
                direction = choice(diss)
                wm.x += sp_m * 1.25
    # When cheese meets walls
    if cheese.colliderect(m0) or cheese.colliderect(m1) or cheese.colliderect(m2) or cheese.colliderect(m3) or cheese.colliderect(m4) \
            or cheese.colliderect(m5) or cheese.colliderect(m6) or cheese.colliderect(m7) or cheese.colliderect(m8)\
            or cheese.colliderect(m9) or cheese.colliderect(l) or cheese.colliderect(r) or cheese.colliderect(b) or cheese.colliderect(t):
         if mine:
            if dc == 's':
                cheese.y -= sp_c * 1.25
                dc = choice(diss)
            elif dc == 'd':
                cheese.x -= sp_c * 1.25
                dc = choice(diss)
            elif dc == 'w':
                cheese.y += sp_c * 1.25
                dc = choice(diss)
            elif dc == 'a':
                cheese.x += sp_c * 1.25
                dc = choice(diss)
    # When Ball met walls
    if ball1.colliderect(m0) or ball1.colliderect(m1) or ball1.colliderect(m2) or ball1.colliderect(m3) or ball1.colliderect(m4) \
            or ball1.colliderect(m5) or ball1.colliderect(m6) or ball1.colliderect(m7) or ball1.colliderect(m8)\
            or ball1.colliderect(m9) or ball1.colliderect(l) or ball1.colliderect(r) or ball1.colliderect(b) or ball1.colliderect(t) \
        or ball2.colliderect(m0) or ball2.colliderect(m1) or ball2.colliderect(m2) or ball2.colliderect(
            m3) or ball2.colliderect(m4) \
        or ball2.colliderect(m5) or ball2.colliderect(m6) or ball2.colliderect(m7) or ball2.colliderect(m8) \
        or ball2.colliderect(m9) or ball2.colliderect(l) or ball2.colliderect(r) or ball2.colliderect(
            b) or ball2.colliderect(t):
        if db1 == 's':
            db1 = choice(diss)
            ball1.y -= sp_b * 1.25
        elif db1 == 'd':
            db1 = choice(diss)
            ball1.x -= sp_b * 1.25
        elif db1 == 'w':
            db1 = choice(diss)
            ball1.y += sp_b * 1.25
        elif db1 == 'a':
            db1 = choice(diss)
            ball1.x += sp_b * 1.25
        if db2 == 's':
            db2 = choice(diss)
            ball2.y -= sp_b * 1.25
        elif db2 == 'd':
            db2 = choice(diss)
            ball2.x -= sp_b * 1.25
        elif db2 == 'w':
            db2 = choice(diss)
            ball2.y += sp_b * 1.25
        elif db2 == 'a':
            db2 = choice(diss)
            ball2.x += sp_b * 1.25
    # Trap
    if gs == 10:
        nx,ny = randint(50,650),randint(50,350)
        while nx in range(int(wm.x)-16,int(wm.x)+16) and ny in range(int(wm.y)-16,int(wm.y)+16):
            nx, ny = randint(50, 650), randint(50, 350)
        trap.x, trap.y = nx, ny
        while trap.colliderect(m0) or trap.colliderect(m1) or trap.colliderect(m2) or trap.colliderect(
                m3) or trap.colliderect(m4) \
                or trap.colliderect(m5) or trap.colliderect(m6) or trap.colliderect(m7) or trap.colliderect(m8) \
                or trap.colliderect(m9):
            nx, ny = randint(50, 650), randint(50, 350)
            trap.x, trap.y = nx, ny
        gs = 0
    # Prize
    if score >= 46:
        ppp += 1
    elif score >= 31:
        ppp += 1
    elif score >= 16:
        ppp += 1
    if ppp == 1:
        playt = 1
    elif ppp == 2:
        playt = 2
    elif ppp == 3:
        playt = 3
    if score >= 16 and playt == 1:
        wm.image = 'mous'
        if mapn != 3:
            music.stop()
            music.play('m4')
        sounds.nb.play()
        playt += 1
    elif score >= 31 and playt == 2:
        wm.image = 'mou2'
        if mapn != 3:
            music.stop()
            music.play("m1")
        sounds.nb.play()
        playt += 1
    elif score >= 46 and playt == 3:
        wm.image = 'mou3'
        if mapn != 3:
            music.stop()
            music.play("m2")
        sounds.nb.play()
        playt += 1
def draw():
    global m0, m1, m2, m3, m4, m5, m6, m7, m8,score,ball1,ball2,gameover,maxscore,lives,got,stayt
    screen.fill((0,0,129))
    screen.draw.text('得分: '+str(score),(605,5),fontname='msyh.ttc',fontsize=16)
    screen.draw.text("榜上第一: "+str(maxscore),(595,25),fontname='msyh.ttc',fontsize=16)
    screen.draw.text("命数:"+str(lives),(608,45),fontname='msyh.ttc',fontsize=16)
    screen.draw.text("负载："+str(got),(605,65),fontname='msyh.ttc',fontsize=16)
    screen.draw.text("宅家时间：" + str(stayt//60)+"s", (587, 85), fontname='msyh.ttc', fontsize=16)
    title.draw()
    nat.draw()
    home.draw()
    te.draw()
    selectMode.draw()
    transit.draw()
    normal.draw()
    bizarre.draw()
    wm.draw()
    start.draw()
    cheese.draw()
    ball1.draw()
    ball2.draw()
    gameover.draw()
    bat.draw()
    vac.draw()
    trap.draw()
    l.draw()
    r.draw()
    t.draw()
    b.draw()
    m0.draw()
    m1.draw()
    m2.draw()
    m3.draw()
    m4.draw()
    m5.draw()
    m6.draw()
    m7.draw()
    m8.draw()
    m9.draw()
pgzrun.go()
