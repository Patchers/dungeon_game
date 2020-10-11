
from random import randint, choice

ENEMIES = [{
  "name" : "drake",
  "hp" : 50,
  "attack" : 50,
  "magic" : 25
},
{
  
}]

def init_player():
  user = {}
  user_name = (input('Greetings. What is your name? > '))
  valid_user = False
  while not valid_user:
    user_class = (input("Warrior or Mage? > "))
    if user_class.lower() == "warrior":
      user["hp"] = randint(50,60)
      user["attack"] = randint(55,65)
      user["magic"] = 0
      valid_user = True
    elif user_class.lower() == "mage":
      user["hp"] = randint(45,55)
      user["attack"] = randint(57,70)
      user["magic"] = randint(20,40)
      valid_user = True
    else:
      print("Please enter a valid choice.")
      
  
  user["name"] = user_name
  user["class"] = user_class
  print("Welcome " + user["name"] + " the " + user["class"] + ".")
  print("Your health is at: " + str(user["hp"]) + "\nYour attack power is: " + str(user["attack"])+ "\nYour magic level is: " + str(user["magic"]))
  return user

#0. Function - init Player
#1. Function - Attack

def attack(player, enemy, strike = 1):
  '''
  {
    "name" : #,
    "hp" : #,
    "attack" : #
  }
  '''

  duel = [player, enemy]

  # random strike selection
  fighter = choice([0,1])
  opponent = abs(fighter - 1)
  print("Strike {} made by {}!".format(strike,duel[fighter]["name"]))
  # random strike power
  strike_power = randint(0,duel[fighter]["attack"]) 
  # reduce opponent hp
  duel[opponent]["hp"] = duel[opponent]["hp"] - strike_power
  # check hp > 0
  
  return 
#2. Function - post_battle (XP)


if __name__ == "__main__":
  test_user = {
    "name" : "danie",
    "attack": 50,
    "hp":50
  }

  test_enemy = {
    "name" : "evil danie",
    "attack": 50,
    "hp":50
  }

  player = init_player()
  attack(test_user, test_enemy)
  
  # call init player Function
  # loop through enemies
  ## call attack function
  ## evaluatue result and update post battle