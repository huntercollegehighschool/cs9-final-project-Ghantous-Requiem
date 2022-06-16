"""
Name(s): Sophia Miriam Ghantous
Name of Project: The Most Boring RPG You Will Ever Play
"""

name = str(input("What is your name, young hero? \n"))
playername = name.upper()


playerhealth = 350
playerstrength = 100
dragonhealth = 500
round = 0


##############################################################################
import random
import time
def counter():
  global playerhealth
  threat = ("Yikes!", "Zoinks!", "Goodness gracious!")
  counterattack = random.choice(threat)
  print(counterattack)
  time.sleep(1)
  if counterattack == "Yikes!":
    print("> THE DRAGON's terrible roar reverberates throughout the room, shaking you to your core! You were dealt 90 damage!")
    playerhealth = playerhealth - 90
  elif counterattack == "Zoinks!":
    print("> THE DRAGON swung its tail around the room too quickly for you to react! You got hit and suffered 90 damage.\n")
    time.sleep(1)
    print("... But the damages done to your lovely furniture result in another 30 HP worth of mental anguish!")
    playerhealth = playerhealth - 120
  else:
    print("> THE DRAGON opened its mouth and blew scorching flames all over the place! If your house wasn't ruined already, it certainly is now! You also lost 200 HP in the process!")
    playerhealth = playerhealth - 200

##############################################################################                  
def move1():
  if playerclass == "knight":
    print("> You brandished your sword!\n... The gleam of the steel blade blinds the dragon! It did 90 damage!")
  elif playerclass == "mage":
    print("> You strode forward and hit the dragon with your staff!\n ... That seemed kind of like a stupid idea! But it did 90 damage anyway, somehow!")
  else:
    print("> You turned around, grabbed the door handle, and attempted to escape!\n ... Why on earth would you do that, young hero? The dragon was so offended by your idiocy that it suffered 90 damage! Spectacular!")   

def move2():
  if playerclass == "knight":
    print("> You slashed at the dragon!\n... It did 120 damage!")
  elif playerclass == "mage":
    print("> You picked a random potion out of your satchel and threw it at the dragon! The bottle breaks, and thick fumes fill the air!\n ... You have no idea what kind of potion it was, but it seems to have done 120 damage!")
  else:
    print("> Feeling frightened and powerless, you burst into tears!\n ... The salt from your tears burns the dragon somehow and deals 120 damage! Wow!")

def move3():
  if playerclass == "knight":
    print("> You grabbed your blade by its hilt and plunged it into the dragon's scaly flesh!\n... Now there's blood all over your beautiful sword! But at least you did 200 damage!")
  elif playerclass == "mage":
    print("> You released a blazing fireball from your staff!\n ... The dragon is scorched and suffers 200 damage!")
  else:
    print("> Desperate, you rummaged through the pocket of your jeans and pulled out ... a quarter?!\n \n ")
    print(playername, ": L-Look! It's shiny! Dragons like shiny things, don't they? ... R-Right?\n \n > ... The dragon is in awe, not of the shininess, but of your crippling poverty!\n ... While it's distracted, you lunge forward and punch the dragon in the face! It does 200 damage!\n ... Could this be character development?!")
    
##############################################################################
def introduction():
  if playerclass == "knight":
    print(playername, ":  Hark! It is I,", name+"ius of the Crimson Tower! The noblest night in all the land!\n \n> Very impressive, young hero. But who are you talking to? The dragon doesn't understand English ...")
  elif playerclass == "mage":
    print(playername, ":  Hark! It is I,", name+"etheron of the Prethavernian Court! The most accomplished mage in all the land!\n \n> Very impressive, young hero. But who are you talking to? The dragon doesn't understand English ...")
  else:
    print(playername, ":  P-Please ... Please just go away ... I'm just a regular person. Why is this happening to me?\n \n> Very unimpressive, young hero. But the dragon won't show you any mercy. Steel yourself and fight like you mean it ... !")

##############################################################################
def start():
  print("-------------\n> You're walking home after a long day at work. It's already nighttime, and you haven't eaten in hours. \nExhausted, you unlock your door and step inside. \n")
  time.sleep(2)
  print("But as you take a few cautious steps into your living room and switch on the light, you realize something ... \n")
  time.sleep(3)
  print("THIS ISN'T YOUR LIVING ROOM! \n \n")
  time.sleep(2)
  print("> As you glance around the blank room, you realize ... \n")
  time.sleep(3)
  print("THERE'S A DRAGON IN YOUR HOUSE! \n \n")
  time.sleep(2)
  print("... Get rid of that pesky vermin,", playername, "!\n-------------\n ")
  time.sleep(4)
  print(introduction())
  time.sleep(4)
  print(battle())
##############################################################################
def battle():
  global playerhealth
  global playerstrength
  global dragonhealth
  global round
  round = round + 1

  if round >= 5 and playerhealth >=0 and dragonhealth >=0:
    print("\033c", end='')
    print("What a loser! You couldn't even finish the job. Might as well go and buy a collar for your new pet dragon.")
  elif playerhealth <= 0:
    print("\033c", end='')
    print ("Oh dear,", playername+"! You've been bested by the dragon!")
    time.sleep(2)
    print("... Wait, who am I talking to, anyway, now that", playername, "is gone?\n \nOh no, I ... I think I'm having a ... a ... \n")
    time.sleep(3)
    print("... an EXISTENTIAL CRISIS!!!")
  elif dragonhealth <= 0:
    print("\033c", end='')
    print ("Congratulations,", playername+"! You've defeated the dragon! But now you have to figure out what to do with this huge dragon corpse in your house ... and the dragon wasn't guarding any gold. So you're still poor! What a joke!")
  else:
    attack = str(input("> Whatever shall you do, "+playername+"? You have "+str(playerhealth)+" HP and "+str(playerstrength)+" stamina remaining.\n \n               "+str(moveset)+"\n \n "))
    if playerclass == "knight":
      if attack == "brandish sword":
        attack = move1()
        print(attack)
        dragonhealth = dragonhealth - 90
        playerstrength = playerstrength + 10
        print(counter())
        print(battle())
      elif attack == "slash" and playerstrength >= 15:
        attack = move2()
        print(attack)
        playerstrength = playerstrength - 15
        dragonhealth = dragonhealth - 120
        playerstrength = playerstrength + 10
        print(counter())
        print(battle())
      elif attack == "stab" and playerstrength >= 30:
        attack = move3()
        print(attack)
        playerstrength = playerstrength - 30
        dragonhealth = dragonhealth - 200
        playerstrength = playerstrength + 10
        print(counter())
        print(battle())
      else:
        print("Slow down,", playername+"! You only have", int(playerstrength), "stamina left!")
        print(battle())
    if playerclass == "mage":
      if attack == "swing staff":
        attack = move1()
        print(attack)
        dragonhealth = dragonhealth - 90
        playerstrength = playerstrength + 10
        print(counter())
        print(battle())
      elif attack == "throw potion" and playerstrength >= 15:
        attack = move2()
        print(attack)
        playerstrength = playerstrength - 15
        dragonhealth = dragonhealth - 120
        playerstrength = playerstrength + 10
        print(counter())
        print(battle())
      elif attack == "shoot fireball" and playerstrength >= 30:
        attack = move3()
        print(attack)
        playerstrength = playerstrength - 30
        dragonhealth = dragonhealth - 200
        playerstrength = playerstrength + 10
        print(counter())
        print(battle())
      else:
        print("Slow down,", playername+"! You only have", int(playerstrength), "stamina left!")
        print(battle())
    if playerclass == "coward":
      if attack == "run":
        attack = move1()
        print(attack)
        dragonhealth = dragonhealth - 90
        playerstrength = playerstrength + 8
        print(counter())
        print(battle())
      elif attack == "cry" and playerstrength >= 15:
        attack = move2()
        print(attack)
        playerstrength = playerstrength - 15
        dragonhealth = dragonhealth - 120
        playerstrength = playerstrength + 8
        print(counter())
        print(battle())
      elif attack == "negotiate" and playerstrength >= 30:
        attack = move3()
        print(attack)
        playerstrength = playerstrength - 30
        dragonhealth = dragonhealth - 200
        playerstrength = playerstrength + 8
        print(counter())
        print(battle())
      else:
        print("Slow down,", playername+"! You only have", int(playerstrength), "stamina left!")
        print(battle())
         
       
  
##############################################################################

playerclass = str(input(" \nSelect your class: \n \n               KNIGHT  |  MAGE  |  COWARD \n \n"))


if playerclass == "knight":
  s1 = "BRANDISH SWORD"
  s2 = "SLASH"
  s3 = "STAB"
  moveset = [s1, s2, s3]
  print(start())
elif playerclass == "mage":
  s1 = "SWING STAFF"
  s2 = "THROW POTION"
  s3 = "SHOOT FIREBALL"
  moveset = [s1, s2, s3]
  print(start())
else:
  s1 = "RUN"
  s2 = "CRY"
  s3 = "NEGOTIATE"
  moveset = [s1, s2, s3]
  print(start())

##############################################################################

