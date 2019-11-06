import myStuff
import os
import time
from threading import Thread
mps = 1
mpc = 1
money = 0
cost1 = 300
cost2 = 1000
click = 0


player = myStuff.player(mps,mpc,money)
game = myStuff.Game(cost1,cost2,player,click)
def myRound(x):
   y = x % 1
   x -= y
   return x
def display():
    while(True):
    game.clickInput()
def otherDisplay():
    while(True):
        game.mainMenu()
        time.sleep(.25)
def play():

  Thread(target = game.moneyPerSecond).start()
  Thread(target = display).start()
  Thread(target = otherDisplay).start()

play()
