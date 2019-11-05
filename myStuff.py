import os
import time

def myRound(x):
  y = x % 1
  x -= y
  return x



'''defines the player'''
class player:
  def __init__(self,mps,mpc,money):
    self.mps = mps
    self.mpc =mpc
    self.money = money

'''THE GAME'''
class Game:
  def __init__(self,costA,costB,player):
    self.player = player
    self.costA = costA
    self.costB = costB
  def moneyPerSecond(self):
      while(True):
          time.sleep(1)
          self.player.money += self.player.mps

  def mainMenu(self):
      print("your money is: $", self.player.money)
      print("Money per click: $",self.player.mpc)
      print("Money per second: $",self.player.mps)
      print("s for shop")
  def clickInput(self):
    click = input()
    if click == "":
      self.player.money += self.player.mpc
    elif click == "s":
      self.shop()
    elif click == "asdfghjkl":
      self.player.money += 100000000000
    else:
      print("that is not a valid input")
      time.sleep(1)


  def shop(self):
    os.system("cls")
    buy = "a"
    while(buy != "e"):
      self.costA = myRound(self.costA)
      self.costB = myRound(self.costB)
      print("your money is: $",self.player.money)
      print("Money per click: $",self.player.mpc)
      print("Money per second: $",self.player.mps)
      print("(e) for exit")
      print("(a) to buy more money per click $",self.costA)
      print("(b) to buy more money per second $",self.costB)
      buy = input()
      if (buy == "a" or buy == "A") and self.player.money >= self.costA:
        self.player.mpc += 1
        self.player.money -= self.costA
        self.costA *= 1.25
        print("succesfully purchased!")
        time.sleep(0.2)
        os.system("cls")
      elif (buy == "b" or buy == "B") and self.player.money >= self.costB:
        self.player.mps += 1
        self.player.money -= self.costB
        self.costB *= 1.25
        print("succesfully purchased!")
        time.sleep(0.2)
        os.system("cls")
      elif ((buy =="a" or buy == "A") and (self.player.money < self.costA)) or ((buy =="b" or buy =="B") and (self.player.money <self.costB)):
        print("you don't have enough money.")
        time.sleep(1)
        os.system("cls")
      elif buy != "e":
        print("that is not a  valid input")
        time.sleep(1)
        os.system("cls")
