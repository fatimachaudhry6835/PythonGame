from gamelib import *

game = Game(800, 600, "Senpai ♥")
bk = Image("school.jpg", game)#background image

logo =Image ("logo.png", game)
logo.moveTo(400, 20)
logo2= Image("logo2.png", game)
logo2.moveTo(400, 60)

senpai= Image("garry.png", game)

monster  = Image("monster.png", game)


knife = Image("knife.png", game)

bk.resizeTo(800,600)# set rise to image to specific values
bk.draw()


knife.draw()

monster.setSpeed(4, 60)

senpai.setSpeed(6, 45)
mouse.visible = False

theme= Sound("theme.ogg", 1)

hit= Sound("hit.ogg", 2)

x = randint(senpai.width, game.width-senpai.width)
y = randint(senpai.height, game.height-senpai.height)

while not game.over:
    game.processInput()
    #draw images to screen after resizing
    bk.draw()
    logo.draw()
    logo2.draw()
   
    monster.move(True)
    senpai.move(True)
    theme.play()

    knife.moveTo(mouse.x, mouse.y)
    
    if monster.collidedWith(knife) and mouse.LeftButton:
        x = randint(senpai.width, game.width-senpai.width)
        y = randint(senpai.height, game.height-senpai.height)
        senpai.moveTo(x,y)
        monster.moveTo(x,y)
        game.score += 10
        monster.speed +=2

    if monster.collidedWith(senpai):
        game.score -=5
        x = randint(senpai.width, game.width-senpai.width)
        y = randint(senpai.height, game.height-senpai.height)
        senpai.moveTo(x,y)
        monster.moveTo(x,y)
        hit.play()

    if senpai.collidedWith(mouse) and mouse.LeftButton:
        game.time -=10
        x = randint(senpai.width, game.width-senpai.width)
        y = randint(senpai.height, game.height-senpai.height)
        senpai.moveTo(x,y)
        monster.moveTo(x,y)
        hit.play()
    if game.time <= 0:
       game.over = True


    game.displayScore(400,50)#displays score at (x,y) location
    game.displayTime(50,20)#displays game time
    game.update(30)#displays game(refresh game)
game.quit()#ends game

