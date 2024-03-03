from tkinter import *
from pygame import mixer
import time, random
from tkinter import messagebox
from random import choice as ch
from random import randint as rd
from time import sleep, time

mixer.init()

sound_fon = mixer.Sound("sounds/fon.mp3")
click_sound = mixer.Sound("sounds/click.mp3")
click_sound.set_volume(0.2)

window = Tk()
window.geometry('1300x800')
window.resizable(False, False)
window.title("MazePD")
window.iconbitmap('image/icon.ico')
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Глобальные переменные
playing = True
clisk = 0

# Изображения Меню
for i in range(1):
    image_player = PhotoImage(file = 'image/player.png')
    image_bg_menu = PhotoImage(file = 'image/bg.png')
    play_img1 = PhotoImage(file='image/play1.png')
    play_img2 = PhotoImage(file='image/play2.png')
    exit_img1 = PhotoImage(file='image/exit1.png')
    exit_img2 = PhotoImage(file='image/exit2.png')
    home_img1 = PhotoImage(file='image/home1.png')
    home_img2 = PhotoImage(file='image/home2.png')
    back_img1 = PhotoImage(file='image/back1.png')
    back_img2 = PhotoImage(file='image/back2.png')
    info_img1 = PhotoImage(file='image/info1.png')
    info_img2 = PhotoImage(file='image/info2.png')
    sound_on_img1 = PhotoImage(file='image/sound_on1.png')
    sound_on_img2 = PhotoImage(file='image/sound_on2.png')
    sound_off_img1 = PhotoImage(file='image/sound_off1.png')
    sound_off_img2 = PhotoImage(file='image/sound_off2.png')
    text_img = PhotoImage(file='image/main_text.png')
    Itgenik_img = PhotoImage(file='image/Itgenik.png')

    INFO_img = PhotoImage(file='image/info.png')

    home1_img1 =PhotoImage(file='image/home11.png')
    home2_img1 = PhotoImage(file='image/home22.png')

    level1_img = PhotoImage(file='image/levels/lev1.png')
    level2_img = PhotoImage(file='image/levels/lev2.png')
    level3_img = PhotoImage(file='image/levels/lev3.png')
    level4_img = PhotoImage(file='image/levels/lev4.png')
    level5_img = PhotoImage(file='image/levels/lev5.png')
    level6_img = PhotoImage(file='image/levels/lev6.png')
    level7_img = PhotoImage(file='image/levels/lev7.png')

    list_of_level_image = [level1_img, level2_img, level3_img, level4_img, level5_img, level6_img, level7_img]

    level1_img_Blur = PhotoImage(file='image/levels/lev1_blur.png')
    level2_img_Blur = PhotoImage(file='image/levels/lev2_blur.png')
    level3_img_Blur = PhotoImage(file='image/levels/lev3_blur.png')
    level4_img_Blur = PhotoImage(file='image/levels/lev4_blur.png')
    level5_img_Blur = PhotoImage(file='image/levels/lev5_blur.png')
    level6_img_Blur = PhotoImage(file='image/levels/lev6_blur.png')
    level7_img_Blur = PhotoImage(file='image/levels/lev7_blur.png')

    list_of_level_image_blur = [level1_img_Blur, level2_img_Blur, level3_img_Blur, level4_img_Blur, level5_img_Blur,
                                level6_img_Blur, level7_img_Blur]

    text_levels_img = PhotoImage(file='image/text_levels.png')

# Изображения Уровень 1
for i in range(1):
    wall_texture = PhotoImage(file='image/LevelRon/walltexture.png')
    portal_texture = PhotoImage(file='image/LevelRon/ronportal.png')
    ronlavaframes = [PhotoImage(file='image/LevelRon/ronlava.gif', format='gif -index %i' % (i)) for i in range(32)]
    wall_texture = PhotoImage(file='image/LevelRon/walltexture.png')
    portal_texture = PhotoImage(file='image/LevelRon/ronportal.png')
    ronlavaframes = [PhotoImage(file='image/LevelRon/ronlava.gif', format='gif -index %i' % (i)) for i in range(32)]
    lava_texture = PhotoImage(file='image/LevelRon/ronlava.png')
    old_coin_texture = PhotoImage(file='image/LevelRon/ronoldcoin.png')
    door_texture = PhotoImage(file='image/LevelRon/rondoor.png')
    coin_texture = PhotoImage(file='image/LevelRon/roncoin.png')
    game_texture = PhotoImage(file='image/LevelRon/controller.png')
    gate_texture = PhotoImage(file='image/LevelRon/rongate.png')

# Изображения Уровень 2
for i in range(1):
    image_wallAL = PhotoImage(file='image/LevelAlina/wall.png')
    image_coinAL = PhotoImage(file='image/LevelAlina/coin.png')
    image_florAL = PhotoImage(file='image/LevelAlina/flor.png')
    image_spikeAL = PhotoImage(file='image/LevelAlina/spike.png')
    image_monsterAL = PhotoImage(file='image/LevelAlina/monster.png')
    image_exitAL = PhotoImage(file="image/LevelAlina/door.png")
# Изображения Уровень 3
for i in range(1):
    image_wallMAX = PhotoImage(file="image/LevelMaxim/wall.png")
    image_keyMAX = PhotoImage(file="image/LevelMaxim/key.png")
    image_enemyMAX = PhotoImage(file="image/LevelMaxim/enemy.png")
    image_blockMAX = PhotoImage(file="image/LevelMaxim/block.png")
    image_grassMAX = PhotoImage(file="image/LevelMaxim/grass.png")

# Изображения Уровень 4
for i in range(1):
    image_wallVADIM = PhotoImage(file='image/LevelVadim/wall.png')
    image_key = PhotoImage(file='image/LevelVadim/key.png')
    image_teleport = PhotoImage(file='image/LevelVadim/teleport.png')
    image_door = PhotoImage(file='image/LevelVadim/door.png')
    image_finish = PhotoImage(file='image/LevelVadim/finish.png')
    image_fonVADIM = PhotoImage(file='image/LevelVadim/fon.png')
    frames = [PhotoImage(file='image/LevelVadim/lava.gif', format='gif -index %i' % (i)) for i in range(38)]

# Изображения Уровень 5
for i in range(1):
    image_coinSA = PhotoImage(file = 'image/LevelSasha/coin.png')
    image_wallSA = PhotoImage(file = 'image/LevelSasha/wall.png')
    image_teleportSA = PhotoImage(file = 'image/LevelSasha/teleport.png')
    image_monstrSA = PhotoImage(file = 'image/LevelSasha/monstr.png')
    image_buttonSA = PhotoImage(file = 'image/LevelSasha/open_button.png')
    image_lockSA = PhotoImage(file = 'image/LevelSasha/lock.png')
    image_finishSA = PhotoImage(file = 'image/LevelSasha/finish.png')

# Изображения Уровень 6
for i in range(1):
    image_wall = PhotoImage(file = 'image/LevelValera/wall.png')
    image_coin = PhotoImage(file = 'image/LevelValera/coin.png')
    image_fon = PhotoImage(file = 'image/LevelValera/floor.png')
    image_monster= PhotoImage(file = 'image/LevelValera/monster.png')
    image_spike = PhotoImage(file = 'image/LevelValera/spike.png')

# Изображения Уровень 7
for i in range(1):
    image_wallVE = PhotoImage(file = 'image/LevelVenya/wall.png')
    image_lavaVE = PhotoImage(file = 'image/LevelVenya/lava.png')
    image_fonVE = PhotoImage(file = 'image/LevelVenya/fon.png')
    framesVE = [PhotoImage(file='image/LevelVenya/coin.gif',format = 'gif -index %i' %(i)) for i in range(6)]
    frames_2VE = [PhotoImage(file='image/LevelVenya/monster.gif',format = 'gif -index %i' %(i)) for i in range(5)]

def level_1(e):
    global inportal, xP, yP, HP, mini
    global in_level, arrow
    in_level = True
    if playing:
        click_sound.play()
    def change1(event):
        c.itemconfig(exita, image=home2_img1)
    def change2(event):
        c.itemconfig(exita, image=home1_img1)
    def exitb(event):
        global upd, af, in_level
        in_level = False
        window.after_cancel(upd)
        window.after_cancel(af)
        main_label.destroy()
        to_list_of_levels(1)
    c.delete('all')
    HP = 6
    inportal = False
    xP = yP = 0
    mini = False
    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)
    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)
    def update(ind, obj):
        global af
        frame = ronlavaframes[ind]
        ind += 1
        for i in obj:
            c.itemconfig(i, image=frame)
        af = window.after(100, update, ind, obj)
        if ind >= 31:
            ind = 0
            window.after_cancel(af)
            update(0, image_lavas)
    def level_R():
        global player, walls, coins, portals, lavas, exits, mini_games, gates, coins_count, main_label, antifire, side, image_coins, image_lavas, image_mini_game, p
        level = [
            "WWPWLWWWWWWWWWWWWE WWWWWWW", #Row № 1
            "WI            PW WG   P   ", #Row № 2
            "WW WP WWWWWW C   PWLLLLLL ", #Row № 3
            "LC WW LLWCWWLCLW WWLLLCWWC", #Row № 4
            "LL MW WW  MWLLLW W WWW WWW", #Row № 5
            "LL WW WW       WW    P  CW",#Row № 6
            "LP W  LL  CWWW WWWWWWWWWWW", #Row № 7
            "W     PL   PWW WWCCCWPWMWE", #Row № 8
            "WWWWWWWWWWWWPLLLWW WW   WG", #Row № 9
            "PCLWWWWWW  M WWWWLPWWWWWW ", #Row № 10
            "ECCCWWWWLLL LWLWLWLWLWLWLP", #Row № 11
            "LLLLLLLLLLLLLLLLLLLLLLLLLL", #Row № 12
            "CWCWCWCWCWCWCWCWCWCWCWCWCW", #Row № 13
            " C C C C C C C C C C C C C", #Row № 14
            "WWWWWWWWWWWWPPWWWWWWWWWWWW", #Row № 15
            "E        G      G        E" #Row № 16
        ]
        coins_count = 0
        antifire = False
        main_label = Label(bg="#808080", text=f'Coins: {coins_count}\nAntiFire: {antifire}\n HP: {HP}', fg="blue", font="Arial 12 bold")
        main_label.place(relx=0.9, relwidth=0.1, relheight=0.08)

        x = 0
        y = 0
        side = 50
        walls = []
        portals = []
        lavas = []
        exits = []
        coins = []
        mini_games = []
        gates = []
        image_coins = []
        image_lavas = []
        image_mini_game = []


        for row in level:
            for i in row:
                if i == 'W':
                    c.create_image(x+side/2, y+side/2, image = wall_texture)
                    walls.append((x, y, x + 50, y + 50))
                if i == 'P':
                    c.create_image(x + side / 2, y + side / 2, image=portal_texture)
                    portals.append((x, y, x + 50, y + 50))
                if i == "L":
                    obj = c.create_image(x+side/2, y+side/2, image=lava_texture)
                    lavas.append((x, y, x + 50, y + 50))
                    image_lavas.append(obj)
                if i == "E":
                    c.create_image(x+side/2, y+side/2, image=door_texture)
                    exits.append((x, y, x + 50, y + 50))
                if i == "C":
                    im = c.create_image(x+side/2, y+side/2, image=coin_texture)
                    coins.append((x, y, x + 50, y + 50))
                    image_coins.append(im)
                if i == "M":
                    mgn = c.create_image(x+side/2, y+side/2, image=game_texture)
                    mini_games.append((x, y, x + 50, y + 50))
                    image_mini_game.append(mgn)
                if i == "G":
                    c.create_image(x+side/2, y+side/2, image=gate_texture)
                    gates.append((x, y, x + 50, y + 50))
                if i == 'I':
                    player = c.create_rectangle(x+1, y+1, x+side-1, y+side-1,width = 0)
                    p = c.create_image(x + side / 2, y + side / 2, image=image_player)

                x += 50
            y += 50
            x = 0
    inportal = False
    def portalout():
        global inportal, id
        inportal = False
        window.after_cancel(id)
    def stop_pad(event):
        global xP, yP
        if event.keysym in ('Up', 'Down', 'Left', 'Right', 'w', 'a', 's', 'd'):
            xP = yP = 0
    def movePlayer(event):
        global xP, yP
        key = event.keysym
        if key == "Up" or key == 'w':
            yP = -5
        if key == "Down" or key == 's':
            yP = 5
        elif key == "Left" or key == 'a':
            xP = -5
        elif key == "Right" or key == 'd':
            xP = 5
    def move():
        global coins_count, HP, inportal, id, back_to_menu_but, yP, xP, mini, upd, arrow
        c.tag_raise(p)
        c.move(player, xP, yP)
        c.move(p,  xP, yP)
        for wall in walls:
            if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
        for portal in portals:
            if not inportal:
                if player in c.find_overlapping(portal[0], portal[1], portal[2], portal[3]):
                    randommedportals = ch(portals)
                    c.coords(player, randommedportals[0]+1, randommedportals[1]+1, randommedportals[2]-1, randommedportals[3]-1)
                    c.coords(p, randommedportals[0] + 25, randommedportals[1] + 25)
                    inportal= True
                    id = window.after(3000, portalout)
        for coin in coins:
            if player in c.find_overlapping(coin[0], coin[1], coin[2], coin[3]):
                coins_count += 1
                main_label['text'] = (f'Coins: {coins_count}\nAntiFire: {antifire}\n HP: {HP}')
                index = coins.index(coin)
                c.delete(image_coins[index])
                c.create_image(coin[0]+side/2, coin[1]+side/2, image=old_coin_texture)
                coins.remove(coin)
                image_coins.pop(index)
        for lava in lavas:
            if player in c.find_overlapping(lava[0], lava[1], lava[2], lava[3]):
                if antifire == False:
                    HP -= 1
                    main_label['text'] = (f'Coins: {coins_count}\nAntiFire: {antifire}\n HP: {HP}')
                    c.coords(player, 51, 51, 99, 99)
                    c.coords(p, 75, 75)
                    if HP == 0:
                        c.delete('all')
                        main_label.destroy()
                        c.create_rectangle(0,0,1300,800, fill="orangered3")
                        c.create_text(650, 340, text="GAME OVER!", font="Montserrat 44 bold", fill="turquoise1")
                        arrow = c.create_image(650, 550, image=home_img1)
                        c.tag_bind(arrow, '<Button-1>', exitb)
                        c.tag_bind(arrow, '<Enter>', change_arr1)
                        c.tag_bind(arrow, '<Leave>', change_arr2)
        for gate in gates:
            if player in c.find_overlapping(gate[0], gate[1], gate[2], gate[3]):
                if antifire == False:


                    messagebox.showerror("You Fool!", "You should've completed the mini-game first!\nIf you just quit it"
                                                      " You Should Restart the game to continue playing!")
                    c.move(player, -xP, -yP)
                    c.move(p, -xP, -yP)
                    xP = yP = 0
        for mini_game in mini_games:
            if player in c.find_overlapping(mini_game[0], mini_game[1], mini_game[2], mini_game[3]):
                mini = True
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
                xP = yP = 0

                #MINI GAME WINDOW START:

                global score, R, R1, startTime, button_word
                score = 0
                R = 0
                R1 = 0
                startTime = 0
                if mini:
                    messagebox.showinfo("Attention!",
                                        "You'll have to get 120 points of score to continue solving that maze!")
                    mini = False



                def new_button():
                    global startTime, antifire, mini
                    endTime = time()
                    scoreTime = round(endTime - startTime, 3)
                    global score
                    global button_word
                    button_word.destroy()
                    startTime = time()
                    display_word_on_button = ch(
                        ["ITGEN.IO", "#HACKATHON \n2020", "Python", "Proggraming", "CLICK ME PLS", "Coding", "Keyboard",
                         "Mouse Game", "Text Game", "Keyboard Game"])
                    button_word = Button(rmg, text=display_word_on_button, width=15, height=5, command=new_button,
                                         activebackground='#46211A', activeforeground="white")
                    button_word["bg"] = "#693D3D"
                    button_word["fg"] = "white"
                    x_word_pos = rd(100, 1000)
                    y_word_pos = rd(100, 600)
                    button_word.place(x=x_word_pos, y=y_word_pos)
                    if scoreTime < 1:
                        score += 3
                    elif scoreTime < 2 and scoreTime > 1:
                        score += 2
                    else:
                        score += 1
                    scoreText["text"] = score


                    if score >= 120:
                        antifire= True
                        rmg.destroy()
                        mini_games.clear()
                        for m in image_mini_game:
                            c.delete(m)
                        main_label['text'] = (f'Coins: {coins_count}\nAntiFire: {antifire}\n HP: {HP}')


                # ==== Function 2 = resetscore() ====
                def resetscore():
                    global score
                    score = 0
                    scoreText["text"] = score

                # ==== Function 3 - showRules() ====
                def showHideRules():
                    global R
                    if R == 0:
                        hideShowRulesButton.config(
                            text="Rules: \n 1. You Need to click the button that spawn in a random \n position on the screen with a random word\n 2. If you want to reset the score, click the Reset Score button.\n 3. As Faster You Click the word, you'll get more score.")
                        R = 1
                    else:
                        hideShowRulesButton.config(text="Show Rules")
                        R = 0

                # ==== Function 4 - showWordsCanSpawn() ====
                def showHideWordsCanSpawn():
                    global R1
                    if R1 == 0:
                        showHideWordsCanSpawnButton.config(
                            text='Words Can Spawn: \n "ITGEN.IO", "#HACKATHON 2020", "Python", "Proggraming"\n "CLICK ME PLS", "Coding", "Keyboard", "Mouse Game",\n "Text Game" And "Keyboard Game"')
                        R1 = 1
                    else:
                        showHideWordsCanSpawnButton.config(text="Show Words Can spawn")
                        R1 = 0

                # ==== Function 5 - closeGame() ====
                def closeGame():
                    global mini
                    mini = False
                    rmg.destroy()

                # ==== Settings Continue ====

                rmg = Toplevel(window)
                rmg.title("WordC | EWord")
                rmg.geometry("1200x800")
                rmg.maxsize(1200, 800)
                rmg.minsize(1200, 800)
                rmg["bg"] = "#46211A"
                # ==== Codes For Buttons and Labels ====
                hideShowRules = IntVar()
                hideShowRules.set(0)
                hideShowRulesButton = Checkbutton(rmg, text="Show Rules",
                                                  font=("Bahnschrift SemiBold SemiConden", "13", "bold"),
                                                  variable=hideShowRules, activeforeground="white",
                                                  activebackground="#46211A",
                                                  onvalue=1, offvalue=0, indicatoron=0, height=5, command=showHideRules)
                hideShowRulesButton["bg"] = "#693D3D"
                hideShowRulesButton["fg"] = "#46211A"
                hideShowRulesButton.place(relx=0.6, y="0", relwidth=0.4)
                scoreLabel = LabelFrame(rmg, text="Score")
                scoreLabel.pack(anchor=N, expand=True)
                scoreText = Label(scoreLabel, text=f"{score}", width=10, height=2)
                home_button = Button(rmg, text="Quit The Game", width=84, height=5, command=closeGame,
                                     activebackground="#46211A", activeforeground="white")
                scoreText.pack()
                home_button["bg"] = "#693D3D"
                home_button.pack(anchor=SE)
                scoreLabel["bg"] = "#46211A"
                scoreText["bg"] = "#46211A"
                scoreText["fg"] = "white"
                scoreLabel["fg"] = "white"
                home_button["fg"] = "white"
                scoreResetButton = Button(rmg, text="Reset Score", width=85, height=5, activebackground="#46211A",
                                          bg="#693D3D",
                                          fg="white", activeforeground="white", command=resetscore)
                scoreResetButton.place(x="0", y="714")
                wordsCanSpawnValue = IntVar()
                wordsCanSpawnValue.set(0)
                showHideWordsCanSpawnButton = Checkbutton(rmg, text="Show Words Can Spawn",
                                                          font=("Bahnschrift SemiBold SemiConden", "13", "bold"),
                                                          variable=wordsCanSpawnValue, height=5, indicatoron=0,
                                                          activeforeground="white", activebackground="#46211A",
                                                          command=showHideWordsCanSpawn)
                showHideWordsCanSpawnButton.place(x="0", y="0", relwidth=0.4)
                showHideWordsCanSpawnButton["bg"] = "#693D3D"
                showHideWordsCanSpawnButton["fg"] = "#46211A"
                # ==== Primary Code ====
                display_word_on_button = ch(
                    ["ITGEN.IO", "#HACKATHON \n2020", "Python", "Proggraming", "CLICK ME PLS", "Coding", "Keyboard",
                     "Mouse Game",
                     "Text Game", "Keyboard Game"])
                startTime = time()
                button_word = Button(rmg, text=display_word_on_button, width=15, height=5, command=new_button,
                                     activebackground='#46211A', activeforeground="white")
                button_word["bg"] = "#693D3D"
                button_word["fg"] = "white"
                x_word_pos = rd(100, 1000)
                y_word_pos = rd(100, 600)
                button_word.place(x=x_word_pos, y=y_word_pos)
        for exit in exits:
            if player in c.find_overlapping(exit[0], exit[1], exit[2], exit[3]):
                c.delete('all')

                c.create_rectangle(0,0,1300,800, fill="palegreen1")
                main_label.destroy()
                c.create_text(650, 340, text="CONGRATULATIONS!", font="Montserrat 44 bold", fill="goldenrod4")
                c.create_text(650, 400, text="You've Found The Way Out!", font="Montserrat 44 bold", fill="goldenrod4")

                arrow = c.create_image(650, 550, image=home_img1)
                c.tag_bind(arrow, '<Button-1>', exitb)
                c.tag_bind(arrow, '<Enter>', change_arr1)
                c.tag_bind(arrow, '<Leave>', change_arr2)
        upd = window.after(30, move)
    if in_level:
        level_R()
        update(0, image_lavas)
        c.bind_all('<Key>', movePlayer)
        move()
        c.bind_all("<KeyRelease>", stop_pad)
        exita = c.create_image(25, 25, image=home1_img1)
        c.tag_bind(exita, "<Button-1>", exitb)
        c.tag_bind(exita, '<Enter>', change1)
        c.tag_bind(exita, '<Leave>', change2)
    else:
        return

def level_2(e):
    global xP, yP, hp, upd, coins, coins2, af1, move,move1, move2, move3, move4, move5, move6, step, step2,step3,step4,step5,step6,step7,step8, SIDE, SIDE2,SIDE3,SIDE4,SIDE5,SIDE6,SIDE7,SIDE8, label_game_over, label_game_over2
    global in_level, arrow, label_exit1, label_exit2, af1, af2, af3, af4, af5, af6, af7, af8, af9, af10, af11, af12,af13
    in_level = True
    if playing:
        click_sound.play()
    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)
    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)
    def change1(event):
        c.itemconfig(exita, image=home2_img1)
    def change2(event):
        c.itemconfig(exita, image=home1_img1)
    def exitb(event):
        global upd, in_level
        in_level = False
        label_game_over.destroy()
        label_game_over2.destroy()
        label_coins.destroy()
        label_hp.destroy()
        label_exit1.destroy()
        label_exit2.destroy()
        window.after_cancel(upd)
        window.after_cancel(af1)
        window.after_cancel(af2)
        window.after_cancel(af3)
        window.after_cancel(af4)
        window.after_cancel(af5)
        window.after_cancel(af6)
        window.after_cancel(af7)
        window.after_cancel(af8)
        window.after_cancel(af9)
        window.after_cancel(af10)
        window.after_cancel(af11)
        window.after_cancel(af12)
        window.after_cancel(af13)
        to_list_of_levels(1)

    c.delete('all')
    hp = 3
    xP = yP = 0
    coins2 = 0
    label_coins = Label(text="coins = 0", width=8, height=1, justify=LEFT, font="Arian 20")
    label_hp = Label(text=f"hp = {hp}", width=8, height=1, justify=LEFT, font="Arian 20")
    label_coins.place(x=1120, y=6)
    label_hp.place(x=980, y=6)

    label_game_over = Label()
    label_game_over2 = Label()
    label_exit1 = Label()
    label_exit2 = Label()

    def levelAlina():
        global player, walls, coins, image_coins, monsters, MONSTER, MONSTER2, move, move1, label_coins, coins2, MONSTER3, m3, m4, m5, MONSTER4, MONSTER5, \
            move3, move4, MONSTER6, MONSTER7, move5, MONSTER8, MONSTER9, MONSTER10, move6, MONSTER11, MONSTER12, MONSTER13, MONSTER14, MONSTER15, m6, \
            MONSTER16, m7, MONSTER17, spikes, hp, label_hp, exits, monster_pos, monster_pos2, m8, m9, monster_pos3, monster_pos4, monster_pos5, monster_pos6, \
            monster_pos7, monster_pos8, monster_pos9, monster_pos10, monster_pos11, monster_pos12, monster_pos13, monster_pos14, monster_pos15, monster_pos16, \
            monster_pos17, p

        level = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XP    XR    S            X",
            "XXX XXX  X  SCRU XXQ  F  X",
            "X    HX TXX S     XR    RX",
            "X XXXRX   X  XXXX XXX XXXX",
            "X   X XXX XS   RX   X    X",
            "XXX XXX    XJ   X X XSSS X",
            "XRX XX  XX XXXX XRX X    X",
            "X   XX XX  DR S X  RX    X",
            "X XXX     XXXXX X XXX  VBX",
            "X   XLR XXX     XZ  X XXXX",
            "X XXXX   X  SSSSXXX X  Y X",
            "XA   XXX X      S   X    X",
            "X  S G   X SS R S XXX    X",
            "XSSSR    X RS  O  XR N  EX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXX",
        ]

        x = 0
        y = 0
        side = 50
        for i in range(16):
            for j in range(26):
                c.create_image(x + side / 2, y + side / 2, image=image_florAL)
                x += 50
            y += 50
            x = 0

        x = 0
        y = 0
        side = 50
        hp = 3
        walls = []
        coins = []
        coins2 = 0
        monsters = []
        spikes = []
        exits = []
        m3 = []
        m4 = []
        m5 = []
        m6 = []
        m7 = []
        m8 = []
        m9 = []
        image_coins = []
        monster_pos = []
        monster_pos2 = []
        monster_pos3 = []
        monster_pos4 = []
        monster_pos5 = []
        monster_pos6 = []
        monster_pos7 = []
        monster_pos8 = []
        monster_pos9 = []
        monster_pos10 = []
        monster_pos11 = []
        monster_pos12 = []
        monster_pos13 = []
        monster_pos14 = []
        monster_pos15 = []
        monster_pos16 = []
        monster_pos17 = []


        for row in level:
            for i in row:
                if i == 'X':
                    c.create_image(x + side / 2, y + side / 2, image=image_wallAL)
                    walls.append((x, y, x + 50, y + 50))
                if i == 'H':
                    MONSTER = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos.append([x, y, x + 50, y + 50])
                if i == 'T':
                    MONSTER2 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos2.append([x, y, x + 50, y + 50])
                if i == 'G':
                    MONSTER3 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    m3.append([x + side / 2, y + side / 2])
                    monster_pos4.append([x, y, x + 50, y + 50])
                if i == 'Y':
                    MONSTER4 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    m4.append([x + side / 2, y + side / 2])
                    monster_pos5.append([x, y, x + 50, y + 50])
                if i == 'Q':
                    MONSTER5 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos6.append([x, y, x + 50, y + 50])
                if i == 'F':
                    MONSTER6 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos7.append([x, y, x + 50, y + 50])
                if i == 'D':
                    MONSTER7 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    m5.append([x + side / 2, y + side / 2])
                    monster_pos8.append([x, y, x + 50, y + 50])
                if i == "L":
                    MONSTER8 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos9.append([x, y, x + 50, y + 50])
                if i == "C":
                    MONSTER9 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos10.append([x, y, x + 50, y + 50])
                if i == "U":
                    MONSTER10 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos11.append([x, y, x + 50, y + 50])
                if i == "A":
                    MONSTER11 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    m8.append([x + side / 2, y + side / 2])
                    monster_pos3.append([x, y, x + 50, y + 50])
                if i == "J":
                    MONSTER12 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos12.append([x, y, x + 50, y + 50])
                if i == "B":
                    MONSTER13 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos13.append([x, y, x + 50, y + 50])
                if i == "N":
                    MONSTER14 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    monster_pos14.append([x, y, x + 50, y + 50])
                if i == "V":
                    MONSTER15 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    m6.append([x + side / 2, y + side / 2])
                    monster_pos15.append([x, y, x + 50, y + 50])
                if i == "O":
                    MONSTER16 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    m7.append([x + side / 2, y + side / 2])
                    monster_pos16.append([x, y, x + 50, y + 50])
                if i == "Z":
                    MONSTER17 = c.create_image(x + side / 2, y + side / 2, image=image_monsterAL)
                    m9.append([x + side / 2, y + side / 2])
                    monster_pos17.append([x, y, x + 50, y + 50])
                if i == 'S':
                    c.create_image(x + side / 2, y + side / 2, image=image_spikeAL)
                    spikes.append((x, y, x + 50, y + 50))
                if i == 'R':
                    im = c.create_image(x + side / 2, y + side / 2, image=image_coinAL)
                    coins.append((x, y, x + 50, y + 50))
                    image_coins.append(im)
                if i == 'P':
                    player = c.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, width = 0)
                    p = c.create_image(x + side / 2, y + side / 2, image=image_player)
                if i == 'E':
                    c.create_image(x + side / 2, y + side / 2, image=image_exitAL)
                    exits.append((x, y, x + 50, y + 50))
                x += 50
            y += 50
            x = 0

    def stop_pad(event):
        global xP, yP
        if event.keysym in ('Up', 'Down', 'Left', 'Right', 'w', 'a', 's', 'd'):
            xP = yP = 0

    def movePlayer(event):
        global xP, yP
        key = event.keysym
        if key == "Up" or key == 'w':
            yP = -5
        if key == "Down" or key == 's':
            yP = 5
        elif key == "Left" or key == 'a':
            xP = -5
        elif key == "Right" or key == 'd':
            xP = 5

    def moveALINA():
        global xP, yP, upd, hp, coins2, arrow, label_game_over, label_game_over2, label_exit1, label_exit2
        c.move(player, xP, yP)
        c.move(p, xP, yP)
        for wall in walls:
            if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
        for coin in coins:
            if player in c.find_overlapping(coin[0], coin[1], coin[2], coin[3]):
                index = coins.index(coin)
                c.delete(image_coins[index])
                coins.remove(coin)
                coins2 = coins2 + 1
                label_coins.config(text=f"coins = {coins2}")
                label_coins.place(x=1120, y=6)
                image_coins.pop(index)
        for spike in spikes:
            if player in c.find_overlapping(spike[0], spike[1], spike[2], spike[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for exit in exits:
            if player in c.find_overlapping(exit[0], exit[1], exit[2], exit[3]):
                c.delete("all")
                label_coins.place_forget()
                label_hp.place_forget()
                c.config(bg="#b9faf8")
                label_exit1.config(text="Поздравляю!!!", width=11, height=2, font="Arian 70", fg="#3c34ed",
                                    bg="#b9faf8")
                label_exit2.config(text="Ты прошёл/ла уровень!", width=19, height=2, font="Arian 50", fg="#3c34ed",
                                    bg="#b9faf8")
                window.after_cancel(upd)
                arrow = c.create_image(650, 700, image=home_img1)
                c.tag_bind(arrow, '<Button-1>', exitb)
                c.tag_bind(arrow, '<Enter>', change_arr1)
                c.tag_bind(arrow, '<Leave>', change_arr2)
                label_exit1.place(x=350, y=250)
                label_exit2.place(x=280, y=400)
        for monster in monster_pos:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos2:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos3:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos4:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos5:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos6:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos7:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos8:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos9:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos10:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos11:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos12:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos13:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos14:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos15:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos16:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        for monster in monster_pos17:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp = hp - 1
                label_hp.config(text=f"hp = {hp}")
                label_hp.place(x=980, y=6)
        if hp <= 0:
            c.delete("all")
            label_hp.place_forget()
            label_coins.place_forget()
            c.config(bg="#f76d6d")
            label_game_over.config(text="Game Over!!!", width=11, height=2, font="Arian 70", fg="#ef040c",
                                    bg="#f76d6d")
            label_game_over2.config(text="Ты проиграл/ла!", width=19, height=2, font="Arian 50", fg="#ef040c",
                                     bg="#f76d6d")
            label_game_over.place(x=350, y=250)
            label_game_over2.place(x=280, y=400)
            window.after_cancel(upd)
            arrow = c.create_image(650, 700, image=home_img1)
            c.tag_bind(arrow, '<Button-1>', exitb)
            c.tag_bind(arrow, '<Enter>', change_arr1)
            c.tag_bind(arrow, '<Leave>', change_arr2)
        upd = window.after(30, moveALINA)

    move = True
    move1 = True
    move3 = True
    move4 = True
    move5 = True
    move6 = True

    def monsters_move1():
        global move, monster_pos, af1
        if move == True:
            c.move(MONSTER, -5, 0)
            monster_pos[0][0] = monster_pos[0][0] - 5
            monster_pos[0][2] = monster_pos[0][2] - 5
            for wall in walls:
                if MONSTER in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move = False

        else:
            c.move(MONSTER, 5, 0)
            monster_pos[0][0] = monster_pos[0][0] + 5
            monster_pos[0][2] = monster_pos[0][2] + 5
            for wall in walls:
                if MONSTER in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move = True
        af1 = window.after(100, monsters_move1)

    def monsters_move2():
        global move1, af2
        if move1 == True:
            c.move(MONSTER2, 0, -5)
            monster_pos2[0][1] = monster_pos2[0][1] - 5
            monster_pos2[0][3] = monster_pos2[0][3] - 5
            for wall in walls:
                if MONSTER2 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move1 = False

        else:
            c.move(MONSTER2, 0, 5)
            monster_pos2[0][1] = monster_pos2[0][1] + 5
            monster_pos2[0][3] = monster_pos2[0][3] + 5
            for wall in walls:
                if MONSTER2 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move1 = True
        af2 = window.after(100, monsters_move2)

    SIDE = 'right'
    step = 0
    SIDE2 = 'left'
    step2 = 0
    SIDE3 = 'up'
    step3 = 0
    SIDE4 = 'up'
    step4 = 0
    SIDE5 = 'left'
    step5 = 0
    SIDE7 = 'up'
    step7 = 0
    SIDE8 = 'up'
    step8 = 0

    def monster_move3():
        global step
        global SIDE
        global MONSTER3
        global m3, m4, MONSTER4, af3
        step = step + 0.1
        if step > 1 and step < 1.5:
            SIDE = 'down'
        elif step > 2 and step < 2.5:
            SIDE = 'up'
        elif step > 3 and step < 3.5:
            SIDE = 'left'
        elif step > 4 and step < 4.5:
            SIDE = 'right'
            step = 0
            c.coords(MONSTER3, m3[0][0], m3[0][1])
            c.coords(MONSTER4, m4[0][0], m4[0][1])

        if SIDE == 'right':
            c.move(MONSTER3, 5, 0)
            c.move(MONSTER4, 5, 0)
            monster_pos4[0][0] = monster_pos4[0][0] + 5
            monster_pos4[0][2] = monster_pos4[0][2] + 5
            monster_pos5[0][0] = monster_pos5[0][0] + 5
            monster_pos5[0][2] = monster_pos5[0][2] + 5
        elif SIDE == 'down':
            c.move(MONSTER3, 0, 5)
            c.move(MONSTER4, 0, 5)
            monster_pos4[0][1] = monster_pos4[0][1] + 5
            monster_pos4[0][3] = monster_pos4[0][3] + 5
            monster_pos5[0][1] = monster_pos5[0][1] + 5
            monster_pos5[0][3] = monster_pos5[0][3] + 5
        elif SIDE == 'up':
            c.move(MONSTER3, 0, -5)
            c.move(MONSTER4, 0, -5)
            monster_pos4[0][1] = monster_pos4[0][1] - 5
            monster_pos4[0][3] = monster_pos4[0][3] - 5
            monster_pos5[0][1] = monster_pos5[0][1] - 5
            monster_pos5[0][3] = monster_pos5[0][3] - 5
        elif SIDE == 'left':
            c.move(MONSTER3, -5, 0)
            c.move(MONSTER4, -5, 0)
            monster_pos4[0][0] = monster_pos4[0][0] - 5
            monster_pos4[0][2] = monster_pos4[0][2] - 5
            monster_pos5[0][0] = monster_pos5[0][0] - 5
            monster_pos5[0][2] = monster_pos5[0][2] - 5

        af3 = window.after(100, monster_move3)

    def monster_move5():
        global move3, af4
        if move3 == True:
            c.move(MONSTER5, 5, 0)
            monster_pos6[0][0] = monster_pos6[0][0] + 5
            monster_pos6[0][2] = monster_pos6[0][2] + 5
            for wall in walls:
                if MONSTER5 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move3 = False

        else:
            c.move(MONSTER5, -5, 0)
            monster_pos6[0][0] = monster_pos6[0][0] - 5
            monster_pos6[0][2] = monster_pos6[0][2] - 5
            for wall in walls:
                if MONSTER5 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move3 = True

        af4 = window.after(100, monster_move5)

    def monster_move6():
        global move4, af5
        if move4 == True:
            c.move(MONSTER6, 5, 0)
            monster_pos7[0][0] = monster_pos7[0][0] + 5
            monster_pos7[0][2] = monster_pos7[0][2] + 5
            for wall in walls:
                if MONSTER6 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move4 = False

        else:
            c.move(MONSTER6, -5, 0)
            monster_pos7[0][0] = monster_pos7[0][0] - 5
            monster_pos7[0][2] = monster_pos7[0][2] - 5
            for wall in walls:
                if MONSTER6 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move4 = True

        af5 = window.after(100, monster_move6)

    def monster_move7():
        global SIDE2, MONSTER7, step2, af6
        step2 = step2 + 0.1
        if step2 > 2 and step2 < 2.5:
            SIDE2 = 'down'
        elif step2 > 3 and step2 < 3.5:
            SIDE2 = 'up'
        elif step2 > 4 and step2 < 4.5:
            SIDE2 = 'right'
        elif step2 > 6 and step2 < 6.5:
            SIDE2 = 'left'
            step2 = 0
            c.coords(MONSTER7, m5[0][0], m5[0][1])
        if SIDE2 == 'left':
            c.move(MONSTER7, -5, 0)
            monster_pos8[0][0] = monster_pos8[0][0] - 5
            monster_pos8[0][2] = monster_pos8[0][2] - 5
        elif SIDE2 == 'down':
            c.move(MONSTER7, 0, 5)
            monster_pos8[0][1] = monster_pos8[0][1] + 5
            monster_pos8[0][3] = monster_pos8[0][3] + 5
        elif SIDE2 == 'up':
            c.move(MONSTER7, 0, -5)
            monster_pos8[0][1] = monster_pos8[0][1] - 5
            monster_pos8[0][3] = monster_pos8[0][3] - 5
        elif SIDE2 == 'right':
            c.move(MONSTER7, 5, 0)
            monster_pos8[0][0] = monster_pos8[0][0] + 5
            monster_pos8[0][2] = monster_pos8[0][2] + 5

        af6 = window.after(100, monster_move7)

    def monster_move8():
        global move5, af7
        if move5 == True:
            c.move(MONSTER8, -5, 0)
            monster_pos9[0][0] = monster_pos9[0][0] - 5
            monster_pos9[0][2] = monster_pos9[0][2] - 5
            for wall in walls:
                if MONSTER8 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move5 = False

        else:
            c.move(MONSTER8, 5, 0)
            monster_pos9[0][0] = monster_pos9[0][0] + 5
            monster_pos9[0][2] = monster_pos9[0][2] + 5
            for wall in walls:
                if MONSTER8 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move5 = True
        af7 = window.after(100, monster_move8)

    def monsters_move9_10():
        global move6, af8
        if move6 == True:
            c.move(MONSTER9, 0, -5)
            monster_pos10[0][1] = monster_pos10[0][1] - 5
            monster_pos10[0][3] = monster_pos10[0][3] - 5
            c.move(MONSTER10, 0, 5)
            monster_pos11[0][1] = monster_pos11[0][1] + 5
            monster_pos11[0][3] = monster_pos11[0][3] + 5
            for wall in walls:
                if MONSTER9 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move6 = False

        else:
            c.move(MONSTER9, 0, 5)
            monster_pos10[0][1] = monster_pos10[0][1] + 5
            monster_pos10[0][3] = monster_pos10[0][3] + 5
            c.move(MONSTER10, 0, -5)
            monster_pos11[0][1] = monster_pos11[0][1] - 5
            monster_pos11[0][3] = monster_pos11[0][3] - 5
            for wall in walls:
                if MONSTER9 in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                    move6 = True
        af8 = window.after(100, monsters_move9_10)

    def monster_move11():
        global step3
        global SIDE3
        global MONSTER11, af9
        step3 = step3 + 0.1
        if step3 > 4 and step3 < 4.5:
            SIDE3 = 'down'
        elif step3 > 8 and step3 < 8.5:
            SIDE3 = 'up'
            step3 = 0
            c.coords(MONSTER11, m8[0][0], m8[0][1])

        if SIDE3 == 'up':
            c.move(MONSTER11, 0, -5)
            monster_pos3[0][1] = monster_pos3[0][1] - 5
            monster_pos3[0][3] = monster_pos3[0][3] - 5

        elif SIDE3 == 'down':
            c.move(MONSTER11, 0, 5)
            monster_pos3[0][1] = monster_pos3[0][1] + 5
            monster_pos3[0][3] = monster_pos3[0][3] + 5
        af9 = window.after(100, monster_move11)

    def monsters_move12_13_14():
        global step4
        global SIDE4
        global MONSTER12, MONSTER13, MONSTER14, m9, af10
        step4 = step4 + 0.1
        if step4 > 2 and step4 < 2.5:
            SIDE4 = 'down'
        elif step4 > 4 and step4 < 4.5:
            SIDE4 = 'up'
            step4 = 0

        if SIDE4 == 'up':
            c.move(MONSTER12, 0, -5)
            monster_pos12[0][1] = monster_pos12[0][1] - 5
            monster_pos12[0][3] = monster_pos12[0][3] - 5
            c.move(MONSTER13, 0, -5)
            monster_pos13[0][1] = monster_pos13[0][1] - 5
            monster_pos13[0][3] = monster_pos13[0][3] - 5
            c.move(MONSTER14, 0, -5)
            monster_pos14[0][1] = monster_pos14[0][1] - 5
            monster_pos14[0][3] = monster_pos14[0][3] - 5
        elif SIDE4 == 'down':
            c.move(MONSTER12, 0, 5)
            monster_pos12[0][1] = monster_pos12[0][1] + 5
            monster_pos12[0][3] = monster_pos12[0][3] + 5
            c.move(MONSTER13, 0, 5)
            monster_pos13[0][1] = monster_pos13[0][1] + 5
            monster_pos13[0][3] = monster_pos13[0][3] + 5
            c.move(MONSTER14, 0, 5)
            monster_pos14[0][1] = monster_pos14[0][1] + 5
            monster_pos14[0][3] = monster_pos14[0][3] + 5
        af10 = window.after(100, monsters_move12_13_14)

    def monster_move15():
        global SIDE5, MONSTER15, step5, m6, af11
        step5 = step5 + 0.1
        if step5 > 2 and step5 < 2.5:
            SIDE5 = 'up'
        elif step5 > 3 and step5 < 3.5:
            SIDE5 = 'down'
        elif step5 > 4 and step5 < 4.5:
            SIDE5 = 'right'
        elif step5 > 6 and step5 < 6.5:
            SIDE5 = 'left'
            step5 = 0
            c.coords(MONSTER15, m6[0][0], m6[0][1])

        if SIDE5 == 'left':
            c.move(MONSTER15, -5, 0)
            monster_pos15[0][0] = monster_pos15[0][0] - 5
            monster_pos15[0][2] = monster_pos15[0][2] - 5
        elif SIDE5 == 'up':
            c.move(MONSTER15, 0, -5)
            monster_pos15[0][1] = monster_pos15[0][1] - 5
            monster_pos15[0][3] = monster_pos15[0][3] - 5
        elif SIDE5 == 'down':
            c.move(MONSTER15, 0, 5)
            monster_pos15[0][1] = monster_pos15[0][1] + 5
            monster_pos15[0][3] = monster_pos15[0][3] + 5
        elif SIDE5 == 'right':
            c.move(MONSTER15, 5, 0)
            monster_pos15[0][0] = monster_pos15[0][0] + 5
            monster_pos15[0][2] = monster_pos15[0][2] + 5

        af11 = window.after(100, monster_move15)

    def monster_move16():
        global SIDE7, MONSTER16, step7, m7, af12
        step7 = step7 + 0.1
        if step7 > 2 and step7 < 2.5:
            SIDE7 = 'left'
        elif step7 > 4 and step7 < 4.5:
            SIDE7 = 'right'
        elif step7 > 6 and step7 < 6.5:
            SIDE7 = 'down'
        elif step7 > 8 and step7 < 8.5:
            SIDE7 = 'up'
            step7 = 0
            c.coords(MONSTER16, m7[0][0], m7[0][1])

        if SIDE7 == 'up':
            c.move(MONSTER16, 0, -5)
            monster_pos16[0][1] = monster_pos16[0][1] - 5
            monster_pos16[0][3] = monster_pos16[0][3] - 5
        elif SIDE7 == 'left':
            c.move(MONSTER16, -5, 0)
            monster_pos16[0][0] = monster_pos16[0][0] - 5
            monster_pos16[0][2] = monster_pos16[0][2] - 5
        elif SIDE7 == 'right':
            c.move(MONSTER16, 5, 0)
            monster_pos16[0][0] = monster_pos16[0][0] + 5
            monster_pos16[0][2] = monster_pos16[0][2] + 5
        elif SIDE7 == 'down':
            c.move(MONSTER16, 0, 5)
            monster_pos16[0][1] = monster_pos16[0][1] + 5
            monster_pos16[0][3] = monster_pos16[0][3] + 5

        af12 = window.after(100, monster_move16)

    def monster_move17():
        global step8
        global SIDE8
        global MONSTER17, af13
        step8 = step8 + 0.1
        if step8 > 4 and step8 < 4.5:
            SIDE8 = 'down'
        elif step8 > 8 and step8 < 8.5:
            SIDE8 = 'up'
            step8 = 0
            c.coords(MONSTER17, m9[0][0], m9[0][1])

        if SIDE8 == 'up':
            c.move(MONSTER17, 0, -5)
            monster_pos17[0][1] = monster_pos17[0][1] - 5
            monster_pos17[0][3] = monster_pos17[0][3] - 5
        elif SIDE8 == 'down':
            c.move(MONSTER17, 0, 5)
            monster_pos17[0][1] = monster_pos17[0][1] + 5
            monster_pos17[0][3] = monster_pos17[0][3] + 5
        af13 = window.after(100, monster_move17)
    if in_level:
        levelAlina()
        c.bind_all('<Key>', movePlayer)
        moveALINA()
        c.bind_all("<KeyRelease>", stop_pad)
        monsters_move1()
        monsters_move2()
        monster_move3()
        monster_move5()
        monster_move6()
        monster_move7()
        monster_move8()
        monsters_move9_10()
        monster_move11()
        monsters_move12_13_14()
        monster_move15()
        monster_move16()
        monster_move17()

        exita = c.create_image(25, 25, image=home1_img1)
        c.tag_bind(exita, "<Button-1>", exitb)
        c.tag_bind(exita, '<Enter>', change1)
        c.tag_bind(exita, '<Leave>', change2)
    else:
        return

def level_3(e):
    global xP, yP, hp, upd, coins, score, af1
    global in_level, arrow
    in_level = True
    if playing:
        click_sound.play()
    def change1(event):
        c.itemconfig(exita, image=home2_img1)
    def change2(event):
        c.itemconfig(exita, image=home1_img1)
    def exitb(event):
        global upd, in_level
        in_level = False
        window.after_cancel(upd)
        finish_label.destroy()
        score_label.destroy()
        to_list_of_levels(1)

    c.delete('all')
    hp = 3
    xP = yP = 0
    score = 0
    finish_label = Label(text="Игра окончена!", fg="grey", height=2, font='Arial, 50')
    score_label = Label(text=f'Score: {score} HP: {hp}', fg='blue', font='Arial, 20')
    score_label.place(x=555, y=5)
    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)
    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)
    def levelMaxim():
        global player, walls, keys, image_keys, p, monsters, monsters_img, finishes
        global hp
        level = ["WWWWWWWWWWWWWWWWWWWWWWWWWW",
                 'WP         BWOOOOOO O    W',
                 'WWWW  WWWW  WWWWWWWWWWWW W',
                 "W OW    BWB    W   W   W W",
                 "W BW  W BWWWWB   W   W   W",
                 "W WW  WOBWBBWWWWWWWWWWWWWW",
                 "W OW  WWWWBOW      E W   W",
                 "W BW     WB WE BBW  BWOB W",
                 "W WW  WB WB WO   W  BWOB W",
                 "W OW  WW WB WWWWWW E WOB W",
                 "W BW  WO WB        BWWOB W",
                 "W WW  WWWWWWWWWW B WBWWB W",
                 "W  W       WBO   W WWBWW W",
                 "W BW WWWWW WWWWWWW W   B W",
                 "W    WV              E   W",
                 "WWWWWWWWWWWWWWWWWWWWWWWWWW"]
        x = 0
        y = 0
        side = 50
        for i in range(16):
            for j in range(26):
                c.create_image(x + side / 2, y + side / 2, image=image_grassMAX)
                x += 50
            y += 50
            x = 0
        x = 0
        y = 0
        side = 50
        walls = []
        keys = []
        image_keys = []
        monsters = []
        monsters_img = []
        finishes = []


        for row in level:
            for i in row:
                if i == "W":
                    wall = c.create_image(x + side / 2, y + side / 2, image=image_wallMAX)
                    walls.append((x, y, x+side, y+side))
                if i == "O":
                    key = c.create_image(x + side / 2, y + side / 2, image=image_keyMAX)
                    keys.append((x, y, x+side, y+side))
                    image_keys.append(key)
                if i == "P":
                    player = c.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, width=0)
                    p = c.create_image(x + side / 2, y + side / 2, image=image_player)
                if i == "B":
                    block = c.create_image(x + side / 2, y + side / 2, image=image_blockMAX)
                    monsters.append((x, y, x + side, y + side))
                    monsters_img.append(block)
                if i == "E":
                    enemy = c.create_image(x + side / 2, y + side / 2, image=image_enemyMAX)
                    monsters.append((x, y, x + side, y + side))
                    monsters_img.append(enemy)
                if i == "V":
                    ex = c.create_rectangle(x, y, x + side, y + side, fill = 'red', outline = 'red')
                    finishes.append((x, y, x + side, y + side))
                    finish = c.create_image(x + side / 2, y + side / 2, image=image_finish)

                x += 50
            y += 50
            x = 0

    def stop_pad(event):
        global xP, yP
        if event.keysym in ('Up', 'Down', 'Left', 'Right', 'w', 'a', 's', 'd'):
            xP = yP = 0

    def movePlayer(event):
        global xP, yP
        key = event.keysym
        if key == "Up" or key == 'w':
            yP = -5
        if key == "Down" or key == 's':
            yP = 5
        elif key == "Left" or key == 'a':
            xP = -5
        elif key == "Right" or key == 'd':
            xP = 5

    def move():
        global xP, yP, upd, hp, score, arrow
        c.move(player, xP, yP)
        c.move(p, xP, yP)
        for wall in walls:
            if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
        for coin in keys:
            if player in c.find_overlapping(coin[0], coin[1], coin[2], coin[3]):
                score += 1
                index = keys.index(coin)
                c.delete(image_keys[index])
                keys.remove(coin)
                image_keys.pop(index)
                score_label.config(text=f'Score: {score} HP: {hp}')
        for monster in monsters:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp -= 1
                score_label.config(text=f'Score: {score} HP: {hp}')
                if hp <= 0:
                    score_label.destroy()
                    c.delete("all")
                    finish_label.place(x=420, y=320)
                    window.after_cancel(upd)
                    arrow = c.create_image(650, 600, image=home_img1)
                    c.tag_bind(arrow, '<Button-1>', exitb)
                    c.tag_bind(arrow, '<Enter>', change_arr1)
                    c.tag_bind(arrow, '<Leave>', change_arr2)
        for finish in finishes:
            if player in c.find_overlapping(finish[0], finish[1], finish[2], finish[3]):
                score_label.destroy()
                c.delete("all")
                window.after_cancel(upd)
                arrow = c.create_image(650, 550, image=home_img1)
                c.tag_bind(arrow, '<Button-1>', exitb)
                c.tag_bind(arrow, '<Enter>', change_arr1)
                c.tag_bind(arrow, '<Leave>', change_arr2)
                finish_label.config(text="Поздравляем! Вы прошли уровень!", fg="grey",
                                    font='Arial, 50')
                finish_label.place(x=100, y=300)
        upd = window.after(30, move)


    if in_level:
        levelMaxim()
        c.bind_all('<Key>', movePlayer)
        move()
        c.bind_all("<KeyRelease>", stop_pad)
        exita = c.create_image(25, 25, image=home1_img1)

        c.tag_bind(exita, "<Button-1>", exitb)

        c.tag_bind(exita, '<Enter>', change1)
        c.tag_bind(exita, '<Leave>', change2)
    else:
        return

def level_4(e):
    global xP, yP, HP, upd, coins
    global in_level, arrow
    in_level = True
    if playing:
        click_sound.play()
    def change1(event):
        c.itemconfig(exita, image=home2_img1)
    def change2(event):
        c.itemconfig(exita, image=home1_img1)
    def exitb(event):
        global upd, af, in_level
        in_level = False
        window.after_cancel(upd)
        window.after_cancel(af)
        label2.destroy()
        label.destroy()
        to_list_of_levels(1)
    c.delete('all')
    HP = 6
    xP = yP = 0
    coins = 0
    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)
    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)
    def levelVadim():
        global player, walls, keys, portals, doors, image_keys
        global image_doors, teleports, obj, gif_list, lava_coords
        global hp, finish, finish_list, p
        level = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWW",
            "WP LL    WKW LLW   WL   LW",
            "W     LW W W   W L W  W LW",
            "WWWWWWWW W   WWW W WL WKLW",
            "W        W L     W W  WWWW",
            "WWLWWWWW WWWWW WWW     LLW",
            "WK W KW  W LL   KWWWWW   W",
            "W LWL WL      LL WWWWDDL W",
            "W  WL W  WWWWWWW WT   DL W",
            "WL W  W LWLLWKWW WWW  DLKW",
            "WL    W   WLW     LWWWWWWW",
            "WL  W WWW WLW LLL  LWTLLLW",
            "WWW W    KWLWWWWWW  W LLLW",
            "WKL WWWWWWWLWK LWW LWD   W",
            "W       K WLWL      WLLLFW",
            "WWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]

        x = 0
        y = 0
        side = 50
        for i in range(16):
            for j in range(26):
                c.create_image(x + side / 2, y + side / 2, image=image_fonVADIM)
                x += 50
            y += 50
            x = 0

        x = 0
        y = 0
        side = 50
        hp = 5
        walls = []
        keys = []
        teleports = []
        doors = []
        image_keys = []
        image_doors = []
        gif_list = []
        lava_coords = []
        finish_list = []

        # Делаем лабиринт
        for row in level:
            for i in row:
                if i == 'W':
                    c.create_image(x + side / 2, y + side / 2, image=image_wallVADIM)
                    walls.append((x, y, x + 50, y + 50))
                if i == 'K':
                    k = c.create_image(x + side / 2, y + side / 2, image=image_key)
                    image_keys.append(k)
                    keys.append((x, y, x + 50, y + 50))
                if i == 'D':
                    d = c.create_image(x + side / 2, y + side / 2, image=image_door)
                    image_doors.append(d)
                    doors.append((x, y, x + 50, y + 50))
                if i == 'T':
                    c.create_image(x + side / 2, y + side / 2, image=image_teleport)
                    teleports.append((x, y, x + 50, y + 50))
                if i == 'F':
                    finish = c.create_image(x + side / 2, y + side / 2, image=image_finish)
                    finish_list = [x, y, x + 50, y + 50]
                if i == 'P':
                    player = c.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, width=0)
                    p = c.create_image(x + side / 2, y + side / 2, image=image_player)
                if i == 'L':
                    obj = c.create_image(x + side / 2, y + side / 2, image=image_fon)
                    gif_list.append(obj)
                    lava_coords.append((x, y, x + 50, y + 50))
                x += 50
            y += 50
            x = 0
    def stop_pad(event):
        global xP, yP
        if event.keysym in ('Up', 'Down', 'Left', 'Right', 'w', 'a', 's', 'd'):
            xP = yP = 0
    def movePlayer(event):
        global xP, yP
        key = event.keysym
        if key == "Up" or key == 'w':
            yP = -5
        if key == "Down" or key == 's':
            yP = 5
        elif key == "Left" or key == 'a':
            xP = -5
        elif key == "Right" or key == 'd':
            xP = 5
    label = Label(text = f'Keys: {coins}. HP: {HP}', fg = 'white', bg = 'blue', font="Montserrat 20 bold")
    label.place(x = 600, y = 5)
    label2 = Label(text = f'CONGRATULATIONS!', fg = 'white', bg = 'blue', font="Montserrat 40 bold")
    def move():
        global xP, yP, coins
        global HP, upd, arrow
        c.move(player, xP, yP)
        c.move(p, xP, yP)
        for wall in walls:
            if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
        for key in keys:
            if player in c.find_overlapping(key[0], key[1], key[2], key[3]):
                coins += 1
                label.config(text=f'Keys: {coins}. HP: {HP}')
                idx = keys.index(key)
                keys.remove(key)
                c.delete(image_keys[idx])
                image_keys.pop(idx)
                if len(keys) == 0:
                    for door in image_doors:
                        c.delete(door)
                    doors.clear()
                    image_doors.clear()

        for door in doors:
            if player in c.find_overlapping(door[0], door[1], door[2], door[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)

        if player in c.find_overlapping(teleports[0][0], teleports[0][1], teleports[0][2], teleports[0][3]):
            c.coords(player, teleports[1][0] + 1, teleports[1][1] + 1, teleports[1][2] - 1, teleports[1][3] - 1)
            c.coords(p,  teleports[1][0] + 25, teleports[1][1] + 25)

        for lava in lava_coords:

            if player in c.find_overlapping(lava[0], lava[1], lava[2], lava[3]):
                HP -= 1
                label.config(text = f'Keys: {coins}. HP: {HP}')
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                if HP <= 0:
                    c.delete('all')
                    label.destroy()
                    c.config(bg = 'red')
                    label2.config(bg = 'red', text = 'GAME OVER!')
                    label2.place(x = 470, y = 300)
                    window.after_cancel(upd)
                    arrow = c.create_image(650, 550, image=home_img1)
                    c.tag_bind(arrow, '<Button-1>', exitb)
                    c.tag_bind(arrow, '<Enter>', change_arr1)
                    c.tag_bind(arrow, '<Leave>', change_arr2)


        if player in c.find_overlapping(finish_list[0], finish_list[1], finish_list[2], finish_list[3]):
            c.delete('all')
            label.destroy()
            c.config(bg='blue')
            label2.config(bg='blue', text='You won,\nand found all keys!!')
            label2.place(x=420, y=250)
            window.after_cancel(upd)
            arrow = c.create_image(650, 550, image=home_img1)
            c.tag_bind(arrow, '<Button-1>', exitb)
            c.tag_bind(arrow, '<Enter>', change_arr1)
            c.tag_bind(arrow, '<Leave>', change_arr2)

        upd = window.after(30, move)
    def update(ind, obj):
        global af
        frame = frames[ind]
        ind += 1
        for i in obj:
            c.itemconfig(i, image=frame)
        af = window.after(100, update, ind, obj)
        if ind >= 37:
            ind = 0
            window.after_cancel(af)
            update(0, gif_list)
    if in_level:
        levelVadim()
        update(0, gif_list)
        c.bind_all('<Key>', movePlayer)
        move()
        c.bind_all("<KeyRelease>", stop_pad)
        exita = c.create_image(25, 25, image=home1_img1)

        c.tag_bind(exita, "<Button-1>", exitb)

        c.tag_bind(exita, '<Enter>', change1)
        c.tag_bind(exita, '<Leave>', change2)
    else:
        return

def level_5(e):
    global xP, yP, hp, upd, coins, score, af1
    global in_level, arrow
    in_level = True
    if playing:
        click_sound.play()
    def change1(event):
        c.itemconfig(exita, image=home2_img1)
    def change2(event):
        c.itemconfig(exita, image=home1_img1)
    def exitb(event):
        global upd, af, in_level
        in_level = False
        window.after_cancel(upd)
        window.after_cancel(af1)
        finish_label.destroy()
        score_label.destroy()
        to_list_of_levels(1)
    c.delete('all')
    hp = 3
    xP = yP = 0
    score = 0
    finish_label = Label(text="Игра окончена!", fg="grey", height=2,font='Arial, 50')
    score_label = Label(text=f'Score: {score}\nHP: {hp}', height=2, width=8, fg='blue', bg='grey', font='Badelfish, 30')
    score_label.place(x=555, y=502)
    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)
    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)
    def levelSasha():
        global player, walls, coins, teleports, monsters, locks, lock, finishes, buttons, image_coins, image_locks, score, hp, teleport1, teleport2, score_label, monsters_pos, monsters_rot, p
        level = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWW",
            "WP    O                  W",
            "WWWWW WWWWWW  WWWWWWWWW  W",
            "WO OW WWBWM     WW       W",
            "WW WW WW W WWWW WW      MW",
            "WW WW WW W   OW WW WWWWWWW",
            "WM  W WW W WWWW WW WWWWWOW",
            "W   W W  W    WOWW       W",
            "WW WW W  WWW  WWWWWWWWWWWW",
            "WW WW W  W     MWWW     SW",
            "W   W WW W WWWW WWWM     W",
            "W  MW WW W WWWW WWW      W",
            "WW WW WW W      FWW     MW",
            "WW WW WW WWWWWWWWWW      W",
            "WW          L    DWO     W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
        x = 0
        y = 0
        side = 50
        walls = []
        coins = []
        teleports = []
        monsters = []
        buttons = []
        locks = []
        finishes = []
        image_coins = []
        image_buttons = []
        image_locks = []
        monsters = []
        monsters_rot = []
        monsters1 = []
        monsters1_rot = []
        score = 0
        hp = 3
        teleport1 = []
        teleport2 = []
        monsters_pos = []
        c.config(bg = 'light blue')
        for row in level:
            for i in row:
                if i == 'W':
                    c.create_image(x + side / 2, y + side / 2, image=image_wallSA)
                    walls.append((x, y, x + 50, y + 50))
                if i == 'D':
                    c.create_image(x + side / 2, y + side / 2, image=image_teleportSA)
                    teleport1.append((x, y, x + 50, y + 50))
                if i == 'S':
                    c.create_image(x + side / 2, y + side / 2, image=image_teleportSA)
                    teleport2.append((x, y, x + 50, y + 50))
                if i == 'O':
                    im = c.create_image(x + side / 2, y + side / 2, image=image_coinSA)
                    coins.append((x, y, x + 50, y + 50))
                    image_coins.append(im)
                if i == 'M':
                    m = c.create_image(x + side / 2, y + side / 2, image=image_monstrSA)
                    monsters.append(m)
                    monsters_pos.append([x, y, x + 50, y + 50])
                    monsters_rot.append(random.choice([True, False]))
                if i == 'B':
                    im_b = c.create_image(x + side / 2, y + side / 2, image=image_buttonSA)
                    buttons.append((x, y, x + 50, y + 50))
                if i == 'L':
                    lock = c.create_image(x + side / 2, y + side / 2, image=image_lockSA)
                    locks.append((x, y, x + 50, y + 50))
                    image_locks.append(lock)
                if i == 'F':
                    c.create_image(x + side / 2, y + side / 2, image=image_finishSA)
                    finishes.append((x, y, x + 50, y + 50))
                if i == 'P':
                    player = c.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, width = 0)
                    p = c.create_image(x + side / 2, y + side / 2, image=image_player)
                x += 50
            y += 50
            x = 0
    def stop_pad(event):
        global xP, yP
        if event.keysym in ('Up', 'Down', 'Left', 'Right', 'w', 'a', 's', 'd'):
            xP = yP = 0
    def movePlayer(event):
        global xP, yP
        key = event.keysym
        if key == "Up" or key == 'w':
            yP = -5
        if key == "Down" or key == 's':
            yP = 5
        elif key == "Left" or key == 'a':
            xP = -5
        elif key == "Right" or key == 'd':
            xP = 5
    def move():
        global xP, yP, upd, hp, score, arrow
        c.move(player, xP, yP)
        c.move(p, xP, yP)
        for wall in walls:
            if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
        for lock in locks:
            if player in c.find_overlapping(lock[0], lock[1], lock[2], lock[3]):
                c.move(player, -x, -y)
                c.move(p, -xP, -yP)
        for button in buttons:
            if player in c.find_overlapping(button[0], button[1], button[2], button[3]):
                index = buttons.index(button)
                c.delete(image_locks[index])
                image_locks.pop(index)
                locks.clear()
                buttons.clear()
        for coin in coins:
            if player in c.find_overlapping(coin[0], coin[1], coin[2], coin[3]):
                score += 1
                index = coins.index(coin)
                c.delete(image_coins[index])
                coins.remove(coin)
                image_coins.pop(index)
                score_label.config(text=f'Score: {score}\nHP: {hp}', height=2, width=8, fg='blue', bg='grey',
                                   font='Badelfish, 30')
        for monster in monsters_pos:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.coords(player, 51, 51, 99, 99)
                c.coords(p, 75, 75)
                hp -= 1
                score_label.config(text=f'Score: {score}\nHP: {hp}', height=2, width=8, fg='blue', bg='grey',
                                   font='Badelfish, 30')
                if hp <= 0:
                    score_label.destroy()
                    c.delete("all")
                    finish_label.place(x=280, y=320)
                    window.after_cancel(upd)
                    arrow = c.create_image(650, 600, image=home_img1)
                    c.tag_bind(arrow, '<Button-1>', exitb)
                    c.tag_bind(arrow, '<Enter>', change_arr1)
                    c.tag_bind(arrow, '<Leave>', change_arr2)
        for finish in finishes:
            if player in c.find_overlapping(finish[0], finish[1], finish[2], finish[3]):
                score_label.destroy()
                c.delete("all")
                window.after_cancel(upd)
                arrow = c.create_image(650, 550, image=home_img1)
                c.tag_bind(arrow, '<Button-1>', exitb)
                c.tag_bind(arrow, '<Enter>', change_arr1)
                c.tag_bind(arrow, '<Leave>', change_arr2)
                finish_label.config(text="Поздравляем! Вы прошли уровень!", fg="grey",
                                     font='Arial, 50')
                finish_label.place(x=100, y=300)
        for teleport in teleport1:
            if player in c.find_overlapping(teleport[0], teleport[1], teleport[2], teleport[3]):
                c.coords(player, teleport2[0][0] + 1, teleport2[0][1] + 1, teleport2[0][2] - 1, teleport2[0][3] - 1)
                c.move(player, 0, 50)
                c.coords(p, teleport2[0][0] + 25, teleport2[0][1] + 25)
                c.move(p, 0, 50)
        for teleport in teleport2:
            if player in c.find_overlapping(teleport[0], teleport[1], teleport[2], teleport[3]):
                c.coords(player, teleport1[0][0] + 1, teleport1[0][1] + 1, teleport1[0][2] - 1, teleport1[0][3] - 1)
                c.move(player, -50, 0)
                c.coords(p, teleport2[0][0] + 25, teleport2[0][1] + 25)
                c.move(p, -50, 0)
        upd = window.after(30, move)
    def monsters_move():
        global monsters_pos, af1
        for i in range(len(monsters)):
            if monsters_rot[i]:
                c.move(monsters[i], -3, 0)
                monsters_pos[i][0] = monsters_pos[i][0] - 3
                monsters_pos[i][2] = monsters_pos[i][2] - 3
                for wall in walls:
                    if monsters[i] in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                        monsters_rot[i] = False
            else:
                c.move(monsters[i], 3, 0)
                monsters_pos[i][0] = monsters_pos[i][0] + 3
                monsters_pos[i][2] = monsters_pos[i][2] + 3
                for wall in walls:
                    if monsters[i] in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                        monsters_rot[i] = True
        af1 = window.after(100, monsters_move)
    if in_level:
        levelSasha()
        c.bind_all('<Key>', movePlayer)
        move()
        monsters_move()
        c.bind_all("<KeyRelease>", stop_pad)
        exita = c.create_image(25, 25, image=home1_img1)

        c.tag_bind(exita, "<Button-1>", exitb)

        c.tag_bind(exita, '<Enter>', change1)
        c.tag_bind(exita, '<Leave>', change2)
    else:
        return

def level_6(e):
    global xP, yP, hp, upd, score_coin, label2
    global in_level, arrow
    in_level = True
    if playing:
        click_sound.play()
    def change1(event):
        c.itemconfig(exita, image=home2_img1)
    def change2(event):
        c.itemconfig(exita, image=home1_img1)
    def exitb(event):
        global upd, af, in_level, label2
        in_level = False
        window.after_cancel(upd)
        window.after_cancel(af)
        window.after_cancel(af1)
        label_score.destroy()
        label2.destroy()
        to_list_of_levels(1)

    c.delete('all')
    xP = yP = 0
    score_coin = 0
    hp = 3
    label_score = Label(text='score: ' + str(score_coin) + '\nhp:' + str(hp), bg='orange', fg='white',
                        font=('Arial', 13))
    label_score.place(x=1015, y=90)
    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)
    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)
    def levelValera():
        global player, p, walls, coins, monsters, spikes, monsters_rot, monster_pos, monster_pos1, monsters1, finsih1, monsters1_rot, monsters_gif_rot, MONSTER, image_coins, finish, coina, finishs, spike
        level = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWW",
            "WP                 WWWW OW",
            "WWWWWWWWWWWKWW    MWWWW  W",
            "W            WWS WWWWWW WW",
            "WOKSWW   WS WWWW     OW  W",
            "WW WWO S WW W     WWWWWW W",
            "WOWWWWWW WWWW WWWWWWWW   W",
            "W   WWW  WWW       WWW SOW",
            "W S   W    W WWSW  WW  WWW",
            "WWWW WWWWW  SO WWK W M  WW",
            "W    W     WWW       W   W",
            "WWOW WWW WWW WWWWWWWWWWWWW",
            "W  M   W    M  WWWWWO    W",
            "WWWWW WW WOWWW WWWWWW WW W",
            "W         S            WEW",
            "WWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
        x = 0
        y = 0
        side = 50
        for i in range(16):
            for j in range(26):
                c.create_image(x + side / 2, y + side / 2, image=image_fon)
                x += 50
            y += 50
            x = 0
        x = 0
        y = 0
        side = 50
        walls = []
        coins = []
        gif_list = []
        monsters = []
        monsters_rot = []
        monsters1 = []
        monsters1_rot = []
        MONSTER = []
        image_coins = []
        finishs = []
        hps = []
        spikes = []
        monster_pos = []
        monster_pos1 = []
        for row in level:
            for i in row:
                if i == 'W':
                    c.create_image(x + side / 2, y + side / 2, image=image_wall)
                    walls.append((x, y, x + 50, y + 50))
                if i == 'O':
                    coins.append((x, y, x + 50, y + 50))
                    im = c.create_image(x + side / 2, y + side / 2, image=image_coin)
                    image_coins.append(im)
                if i == 'S':
                    c.create_image(x + side / 2, y + side / 2, image=image_spike)
                    spikes.append((x, y, x + 50, y + 50))
                if i == 'M':
                    m = c.create_image(x + side / 2, y + side / 2, image=image_monster)
                    monsters.append(m)
                    monsters_rot.append(False)
                    monster_pos.append([x, y, x + 50, y + 50])
                if i == 'K':
                    m = c.create_image(x + side / 2, y + side / 2, image=image_monster)
                    monsters1.append(m)
                    monsters1_rot.append(False)
                    monster_pos1.append([x, y, x + 50, y + 50])
                if i == 'P':
                    player = c.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, outline='white', width = 0)
                    p = c.create_image(x + side / 2, y + side / 2, image=image_player)
                if i == 'E':
                    finish = c.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, fill='red', outline='white')
                    finishs.append((x, y, x + 50, y + 50))
                    finish = c.create_image(x + side / 2, y + side / 2, image=image_finish)
                x += 50
            y += 50
            x = 0
    label2 = Label(text='You completed the level. Good luck on the next level!', bg='white',
                                     font=('Arial', 20))
    def move():
        global score_coin, hp, xP, yP, upd, arrow, label2
        c.move(player, xP, yP)
        c.move(p, xP, yP)
        for wall in walls:
            if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
        for coin in coins:
            if player in c.find_overlapping(coin[0], coin[1], coin[2], coin[3]):
                index = coins.index(coin)
                c.delete(image_coins[index])
                coins.remove(coin)
                image_coins.pop(index)
                score_coin += 1
                label_score.config(text='score:' + str(score_coin) + '\nhp:' + str(hp))
        for finish in finishs:
            if player in c.find_overlapping(finish[0], finish[1], finish[2], finish[3]):
                c.delete('all')
                label_score.place_forget()
                label2.place(x=380, y=350)
                window.after_cancel(upd)
                arrow = c.create_image(650, 550, image=home_img1)
                c.tag_bind(arrow, '<Button-1>', exitb)
                c.tag_bind(arrow, '<Enter>', change_arr1)
                c.tag_bind(arrow, '<Leave>', change_arr2)
        for spike in spikes:
            if player in c.find_overlapping(spike[0], spike[1], spike[2], spike[3]):
                hp -= 1
                label_score.config(text='score:' + str(score_coin) + '\nhp:' + str(hp))
                if hp <= 0:
                    c.delete('all')
                    label_score.place_forget()
                    label2.config(text='You lost, repeat again :(', bg='white')
                    label2.place(x=510, y=350)
                    window.after_cancel(upd)
                    arrow = c.create_image(650, 550, image=home_img1)
                    c.tag_bind(arrow, '<Button-1>', exitb)
                    c.tag_bind(arrow, '<Enter>', change_arr1)
                    c.tag_bind(arrow, '<Leave>', change_arr2)
                else:
                    c.coords(player, 51, 51, 99, 99)
                    c.coords(p, 75,75)
        for monster in monster_pos:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                hp -= 1
                label_score.config(text='score:' + str(score_coin) + '\nhp:' + str(hp))
                if hp <= 0:
                    c.delete('all')
                    label_score.place_forget()
                    label2.config(text='You lost, repeat again :(', bg='white')
                    label2.place(x=510, y=350)
                    window.after_cancel(upd)
                    arrow = c.create_image(650, 550, image=home_img1)
                    c.tag_bind(arrow, '<Button-1>', exitb)
                    c.tag_bind(arrow, '<Enter>', change_arr1)
                    c.tag_bind(arrow, '<Leave>', change_arr2)
                else:
                    c.coords(player, 51, 51, 99, 99)
                    c.coords(p, 75, 75)
        for monster1 in monster_pos1:
            if player in c.find_overlapping(monster1[0], monster1[1], monster1[2], monster1[3]):
                hp -= 1
                label_score.config(text='score:' + str(score_coin) + '\nhp:' + str(hp))
                if hp <= 0:
                    c.delete('all')
                    label_score.place_forget()
                    label2.config(text='You lost, repeat again :(', bg='white')
                    label2.place(x=510, y=350)
                    window.after_cancel(upd)
                    arrow = c.create_image(650, 550, image=home_img1)
                    c.tag_bind(arrow, '<Button-1>', exitb)
                    c.tag_bind(arrow, '<Enter>', change_arr1)
                    c.tag_bind(arrow, '<Leave>', change_arr2)
                else:
                    c.coords(player, 51, 51, 99, 99)
                    c.coords(p, 75, 75)
        upd = window.after(30, move)
    def monsters_move():
        global monster_pos, monster_pos1, af
        for i in range(len(monsters)):
            if monsters_rot[i]:
                c.move(monsters[i], -5, 0)
                monster_pos[i][0] = monster_pos[i][0] - 5
                monster_pos[i][2] = monster_pos[i][2] - 5
                for wall in walls:
                    if monsters[i] in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                        monsters_rot[i] = False
            else:
                c.move(monsters[i], 5, 0)
                monster_pos[i][0] = monster_pos[i][0] + 5
                monster_pos[i][2] = monster_pos[i][2] + 5
                for wall in walls:
                    if monsters[i] in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                        monsters_rot[i] = True
        af = window.after(100, monsters_move)
    def monsters1_move():
        global monster_pos1, af1
        for i in range(len(monsters1)):
            if monsters1_rot[i]:
                c.move(monsters1[i], 0, 5)
                monster_pos1[i][1] = monster_pos1[i][1] + 5
                monster_pos1[i][3] = monster_pos1[i][3] + 5
                for wall in walls:
                    if monsters1[i] in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                        monsters1_rot[i] = False
            else:
                c.move(monsters1[i], 0, -5)
                monster_pos1[i][1] = monster_pos1[i][1] - 5
                monster_pos1[i][3] = monster_pos1[i][3] - 5
                for wall in walls:
                    if monsters1[i] in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                        monsters1_rot[i] = True
        af1 = window.after(100, monsters1_move)
    def stop_pad(event):
        global xP, yP
        if event.keysym in ('Up', 'Down', 'Left', 'Right', 'w', 'a', 's', 'd'):
            xP = yP = 0
    def movePlayer(event):
        global xP, yP
        key = event.keysym
        if key == "Up" or key == 'w':
            yP = -5
        if key == "Down" or key == 's':
            yP = 5
        elif key == "Left" or key == 'a':
            xP = -5
        elif key == "Right" or key == 'd':
            xP = 5
    if in_level:
        levelValera()
        monsters_move()
        monsters1_move()
        c.bind_all('<Key>', movePlayer)
        move()
        c.bind_all("<KeyRelease>", stop_pad)
        exita = c.create_image(25, 25, image=home1_img1)

        c.tag_bind(exita, "<Button-1>", exitb)

        c.tag_bind(exita, '<Enter>', change1)
        c.tag_bind(exita, '<Leave>', change2)
    else:
        return

def level_7(e):
    global xP, yP, HP, upd, score_coin, l_end, COINS, af, af1, af2, Frame
    global in_level, arrow
    in_level = True
    if playing:
        click_sound.play()
    def change1(event):
        c.itemconfig(exita, image=home2_img1)
    def change2(event):
        c.itemconfig(exita, image=home1_img1)
    def exitb(event):
        global upd, af, in_level, l_end, af2, Frame
        Frame.destroy()
        in_level = False
        window.after_cancel(upd)
        window.after_cancel(af)
        window.after_cancel(af1)
        window.after_cancel(af2)
        l_end.destroy()
        to_list_of_levels(1)
    c.delete('all')
    xP = yP = 0
    COINS = 0
    HP = 5
    Frame = LabelFrame(text='статистика', width=175, height=90)
    Frame.place(x=50, y=480)
    l = Label(Frame, text='HP: ', justify=LEFT)
    l.pack(padx=10, pady=10)
    l_2 = Label(Frame, text='Собрано монеток: ', justify=LEFT)
    l_2.pack(padx=10, pady=10)
    l_end = Label(font='Arial 20 bold', text='UNFORTUNATELY\nYou missed your chance')
    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)
    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)
    def levelVenya():
        global player, walls, obj, gif_list, keys, monsters, lavas, finishes, monsters_gif, monsters_gif_rot, coins, monster_pos, p
        level = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWW",
            "WO      M     W L  OL  OLW",
            "WWW  WWWWW   OWL  L   L KW",
            "W    WWWWWL  LW  WWWWWWWWW",
            "WWWL    WW  L W LWL      W",
            "E  L WWWWWL   W  W   LW  W",
            "WW W WWWW   LLWL WLL LW  W",
            "WO    WWWL            W  W",
            "W M      WWWWWWWWWWWWWW LW",
            "WWWWWL  LW   M           W",
            "WWWWWWW  WWW   LWWWWWW   W",
            "WWWWW    LWWL      WWWW LW",
            "W  W  WW  W     WWWWWW   W",
            "W W  LWL W     WLL   L  WW",
            "WO   L W OW M   W   LO  PW",
            "WWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]

        x = 0
        y = 0
        side = 50
        for i in range(16):
            for j in range(26):
                c.create_image(x + side / 2, y + side / 2, image=image_fonVE)
                x += 50
            y += 50
            x = 0
        walls = []

        gif_list = []
        monsters_gif = []
        monsters_gif_rot = []
        monster_coords = []
        coins = []

        monster_pos = []
        lavas = []
        finishes = []

        x = 0
        y = 0
        for row in level:
            for i in row:
                if i == 'W':
                    c.create_image(x + side / 2, y + side / 2, image=image_wallVE)
                    walls.append((x, y, x + 50, y + 50))
                if i == 'O':
                    obj = c.create_image(x + side / 2, y + side / 2, image=image_wallVE)
                    gif_list.append(obj)
                    coins.append((x, y, x + 50, y + 50))
                if i == 'L':
                    c.create_image(x + side / 2, y + side / 2, image=image_lavaVE)
                    lavas.append((x, y, x + 50, y + 50))
                if i == 'M':
                    m = c.create_image(x + side / 2, y + side / 2, image=image_wallVE)
                    monsters_gif.append(m)
                    monster_coords.append((x, y, x + 50, y + 50))
                    monsters_gif_rot.append(False)
                    monster_pos.append([x, y, x + 50, y + 50])
                if i == 'P':
                    player = c.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, width = 0)
                    p = c.create_image(x + side / 2, y + side / 2, image=image_player)
                if i == 'E':
                    finish = c.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1, fill='red', outline='white')
                    finishes.append((x, y, x + 50, y + 50))
                    finish = c.create_image(x + side / 2, y + side / 2, image=image_finish)
                x += 50
            y += 50
            x = 0
    def move():
        global HP, COINS, arrow, xP, xP, upd, l_end
        c.move(player, xP, yP)
        c.move(p, xP, yP)
        for wall in walls:
            if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
        for finish in finishes:
            if player in c.find_overlapping(finish[0], finish[1], finish[2], finish[3]):
                c.move(player, -xP, -yP)
                c.move(p, -xP, -yP)
                c.delete('all')
                Frame.destroy()
                c.config(bg='SpringGreen2')
                l_end.config(font='Arial 20 bold', text='CONGRATULATIONS!\nYou have found a way out!')
                l_end.place(x=500, y=300)
                arrow = c.create_image(650, 550, image=home_img1)
                c.tag_bind(arrow, '<Button-1>', exitb)
                c.tag_bind(arrow, '<Enter>', change_arr1)
                c.tag_bind(arrow, '<Leave>', change_arr2)
        for coin in coins:
            if player in c.find_overlapping(coin[0], coin[1], coin[2], coin[3]):
                index = coins.index(coin)
                c.delete(gif_list[index])
                coins.remove(coin)
                gif_list.pop(index)
                COINS += 1
                l_2.config(text='Собрано монеток: ' + str(COINS))
        for lava in lavas:
            if player in c.find_overlapping(lava[0], lava[1], lava[2], lava[3]):
                c.coords(player, 1201, 701, 1249, 749)
                c.coords(p, 1225, 725)
                HP -= 1
                l.config(text='HP: ' + str(HP))
                if HP == 0:
                    c.delete('all')
                    Frame.destroy()
                    c.config(bg='SpringGreen2')
                    l_end.place(x = 500, y = 300)
                    window.after_cancel(upd)
                    arrow = c.create_image(650, 550, image=home_img1)
                    c.tag_bind(arrow, '<Button-1>', exitb)
                    c.tag_bind(arrow, '<Enter>', change_arr1)
                    c.tag_bind(arrow, '<Leave>', change_arr2)
        for monster in monster_pos:
            if player in c.find_overlapping(monster[0], monster[1], monster[2], monster[3]):
                c.move(player, -x, -y)
                c.coords(player, 1201, 701, 1249, 749)
                c.coords(p, 1225, 725)
                HP -= 1
                l.config(text='HP: ' + str(HP))
                if HP == 0:
                    c.delete('all')
                    Frame.destroy()
                    l_end.config(font='Arial 20 bold', text='UNFORTUNATELY\nYou missed your chance')
                    l_end.place(x = 500, y = 300)
                    window.after_cancel(upd)
                    arrow = c.create_image(650, 550, image=home_img1)
                    c.tag_bind(arrow, '<Button-1>', exitb)
                    c.tag_bind(arrow, '<Enter>', change_arr1)
                    c.tag_bind(arrow, '<Leave>', change_arr2)
        upd = window.after(30, move)
    def stop_pad(event):
        global xP, yP
        if event.keysym in ('Up', 'Down', 'Left', 'Right', 'w', 'a', 's', 'd'):
            xP = yP = 0
    def movePlayer(event):
        global xP, yP
        key = event.keysym
        if key == "Up" or key == 'w':
            yP = -5
        if key == "Down" or key == 's':
            yP = 5
        elif key == "Left" or key == 'a':
            xP = -5
        elif key == "Right" or key == 'd':
            xP = 5
    def update(ind, obj):
        global af
        frame = framesVE[ind]
        ind += 1
        for i in obj:
            c.itemconfig(i, image=frame)
        af = window.after(100, update, ind, obj)
        if ind >= 6:
            ind = 0
            window.after_cancel(af)
            update(0, gif_list)
    def monsters_gif_move():
        global monster_pos, af2
        for i in range(len(monsters_gif)):
            if monsters_gif_rot[i]:
                c.move(monsters_gif[i], -5, 0)
                monster_pos[i][0] = monster_pos[i][0] - 5
                monster_pos[i][2] = monster_pos[i][2] - 5
                for wall in walls:
                    if monsters_gif[i] in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                        monsters_gif_rot[i] = False
            else:
                c.move(monsters_gif[i], 5, 0)
                monster_pos[i][0] = monster_pos[i][0] + 5
                monster_pos[i][2] = monster_pos[i][2] + 5
                for wall in walls:
                    if monsters_gif[i] in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
                        monsters_gif_rot[i] = True
        af2 = window.after(100, monsters_gif_move)
    def update_2(ind, obj):
        global af1
        frame = frames_2VE[ind]
        ind += 1
        for i in obj:
            c.itemconfig(i, image=frame)
        af1 = window.after(100, update_2, ind, obj)
        if ind >= 5:
            ind = 0
            window.after_cancel(af1)
    if in_level:
        levelVenya()
        update(0, gif_list)
        update_2(0, monsters_gif)
        monsters_gif_move()
        c.bind_all('<Key>', movePlayer)
        move()
        c.bind_all("<KeyRelease>", stop_pad)
        exita = c.create_image(25, 25, image=home1_img1)
        c.tag_bind(exita, "<Button-1>", exitb)
        c.tag_bind(exita, '<Enter>', change1)
        c.tag_bind(exita, '<Leave>', change2)
    else:
        return

def to_list_of_levels(e):
    global playing
    c.delete('all')
    if playing:
        click_sound.play()
    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)

    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)

    def change_blur1(nd, event, i):
        c.itemconfig(list_of_levels[i], image=list_of_level_image_blur[i])

    def change_blur2(nd, event, i):
        c.itemconfig(list_of_levels[i], image=list_of_level_image[i])

    c.create_image(650, 400, image=image_bg_menu)
    c.create_image(650, 150, image=text_levels_img)
    arrow = c.create_image(130, 150, image=home_img1)


    level1 = c.create_image(200, 400, image=level1_img)
    level2 = c.create_image(350, 640, image=level2_img)
    level3 = c.create_image(500, 400, image=level3_img)
    level4 = c.create_image(650, 640, image=level4_img)
    level5 = c.create_image(800, 400, image=level5_img)
    level6 = c.create_image(950, 640, image=level6_img)
    level7 = c.create_image(1100, 400, image=level7_img)

    list_of_levels = [level1, level2, level3, level4, level5, level6, level7]

    c.tag_bind(arrow, '<Enter>', change_arr1)
    c.tag_bind(arrow, '<Leave>', change_arr2)

    c.tag_bind(level1, '<Enter>', lambda index=0, i=0: change_blur1(index, '<Enter>', i))
    c.tag_bind(level1, '<Leave>', lambda index=0, i=0: change_blur2(index, '<Leave>', i))

    c.tag_bind(level2, '<Enter>', lambda index=0, i=1: change_blur1(index, '<Enter>', i))
    c.tag_bind(level2, '<Leave>', lambda index=0, i=1: change_blur2(index, '<Leave>', i))

    c.tag_bind(level3, '<Enter>', lambda index=0, i=2: change_blur1(index, '<Enter>', i))
    c.tag_bind(level3, '<Leave>', lambda index=0, i=2: change_blur2(index, '<Leave>', i))

    c.tag_bind(level4, '<Enter>', lambda index=0, i=3: change_blur1(index, '<Enter>', i))
    c.tag_bind(level4, '<Leave>', lambda index=0, i=3: change_blur2(index, '<Leave>', i))

    c.tag_bind(level5, '<Enter>', lambda index=0, i=4: change_blur1(index, '<Enter>', i))
    c.tag_bind(level5, '<Leave>', lambda index=0, i=4: change_blur2(index, '<Leave>', i))

    c.tag_bind(level6, '<Enter>', lambda index=0, i=5: change_blur1(index, '<Enter>', i))
    c.tag_bind(level6, '<Leave>', lambda index=0, i=5: change_blur2(index, '<Leave>', i))

    c.tag_bind(level7, '<Enter>', lambda index=0, i=6: change_blur1(index, '<Enter>', i))
    c.tag_bind(level7, '<Leave>', lambda index=0, i=6: change_blur2(index, '<Leave>', i))

    c.tag_bind(arrow, '<Button-1>', menu)

    c.tag_bind(level1, '<Button-1>', level_1)
    c.tag_bind(level2, '<Button-1>', level_2)
    c.tag_bind(level3, '<Button-1>', level_3)
    c.tag_bind(level4, '<Button-1>', level_4)
    c.tag_bind(level5, '<Button-1>', level_5)
    c.tag_bind(level6, '<Button-1>', level_6)
    c.tag_bind(level7, '<Button-1>', level_7)

def info_func(e):
    if playing:
        click_sound.play()
    c.delete('all')

    def change_arr1(e):
        c.itemconfig(arrow, image=home_img2)

    def change_arr2(e):
        c.itemconfig(arrow, image=home_img1)

    c.create_image(650, 400, image=image_bg_menu)
    c.create_image(650, 400, image=INFO_img)


    arrow = c.create_image(220, 700, image=home_img1)


    c.tag_bind(arrow, '<Button-1>', menu)
    c.tag_bind(arrow, '<Enter>', change_arr1)
    c.tag_bind(arrow, '<Leave>', change_arr2)

def menu(e):
    global playing, clisk
    def exit_func(e):
        window.destroy()
        exit()

    def change_play1(e):
        c.itemconfig(play_btn, image=play_img2)
    def change_play2(e):
        c.itemconfig(play_btn, image=play_img1)
    def change_exit1(e):
        c.itemconfig(exit_btn, image=exit_img2)
    def change_exit2(e):
        c.itemconfig(exit_btn, image=exit_img1)
    def change_info1(e):
        c.itemconfig(info_btn, image=info_img2)
    def change_info2(e):
        c.itemconfig(info_btn, image=info_img1)
    def change_s1(e):
        if playing:
            c.itemconfig(sound_btn, image=sound_on_img2)
        else:
            c.itemconfig(sound_btn, image=sound_off_img2)
    def change_s2(e):
        if playing:
            c.itemconfig(sound_btn, image=sound_on_img1)
        else:
            c.itemconfig(sound_btn, image=sound_off_img1)

    def sound_what(e):
        global playing
        if playing:
            sound_fon.stop()
            playing = False
            c.itemconfig(sound_btn, image=sound_off_img1)
        else:
            sound_fon.play()
            playing = True
            c.itemconfig(sound_btn, image=sound_on_img1)


    if clisk == 0:
        if playing:
            sound_fon.stop()
            sound_fon.play()
    if clisk != 0:
        if playing:
            click_sound.play()

    c.delete('all')
    clisk = 1
    c.create_image(650, 400, image = image_bg_menu)
    c.create_image(650, 130, image=text_img)
    c.create_image(1150, 400, image=Itgenik_img)

    play_btn = c.create_image(650, 500, image=play_img1)
    exit_btn = c.create_image(130, 310, image=exit_img1)
    info_btn = c.create_image(130, 690, image=info_img1)


    if playing:
        sound_btn = c.create_image(130, 500, image=sound_on_img1)
    else:
        sound_btn = c.create_image(130, 500, image=sound_off_img1)

    c.tag_bind(play_btn, '<Enter>', change_play1)
    c.tag_bind(play_btn, '<Leave>', change_play2)

    c.tag_bind(exit_btn, '<Enter>', change_exit1)
    c.tag_bind(exit_btn, '<Leave>', change_exit2)

    c.tag_bind(info_btn, '<Enter>', change_info1)
    c.tag_bind(info_btn, '<Leave>', change_info2)

    c.tag_bind(sound_btn, '<Enter>', change_s1)
    c.tag_bind(sound_btn, '<Leave>', change_s2)

    c.tag_bind(play_btn, '<Button-1>', to_list_of_levels)
    c.tag_bind(exit_btn, '<Button-1>', exit_func)
    c.tag_bind(info_btn, '<Button-1>', info_func)

    c.tag_bind(sound_btn, '<Button-1>', sound_what)

c = Canvas(window, width = 1300, height = 1300, bg = 'white')
c.pack()
menu(0)
window.mainloop()
