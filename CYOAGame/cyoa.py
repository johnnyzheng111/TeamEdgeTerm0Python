# ************************************************************
# CHOOSE YOUR OWN ADVENTURE GAME - YOUR NEW DESTINY
# 
# The main character (you) will control will start in the middle of the forest. 
# They will need to progress through an apocalyptic world and find survival. 
# 
# GAME FEATURES: 
# 1. USER INPUT
# 2. A PLAYER CAN TYPE "GO TO" AND HEAD TO A LOCATION FROM THEIR CURRENT LOCATION
# 3. A PLAYER CAN TYPE "OBSERVE"
# 4. SOME LOCATIONS HAVE NPCs AND YOU CAN INTERACT WITH THEM TO LEARN MORE ABOUT YOUR SURROUNDINGS
# 5. BASED ON YOUR ACTIONS, YOU WILL UNLOCK DIFFERENT TYPES OF ENDINGS. 
# 6. IF A PLAYER ENTERS A LOCATION WITH A MONSTER, THEY WILL LOSE HEALTH
# 7. IF THEY REACH THE CITY, MEET LOVE INTEREST, OR DIE, THE GAME WILL END 
#
# ************************************************************

import random

input_message = "Welcome to ..."
game_running = True # 
input_message = ""
name = ""





#************** DEFINE CLASSES *******************
# Johnny's tasks: clearing, town, and city
# Alex's Tasks: camps/tents, find love interest, meet love interest, cave
# Joel's tasks: variables?
# Allison's tasks: middle of forest, stream (water collection), and wise man
# experience, each new location entered will give experience (ex. 8 points of exp)
# items will also give a bit of experience (ex. 1-2 points of exp)
# 
class Location: 
  def __init__(self, name=None, description=None, items=None, paths=None, visited=None, npcs=None, subLocations=None):
    self.name = name
    self.description = description
    self.items = items
    self.paths = paths # where you can go from this current location (a list [])
    self.npcs = npcs
    self.visited= visited
    self.subLocations = subLocations
        # self.key = key
class subLocation: 
  def __init__(self, name=None, description=None, items=None, npcs=None, belongingTo=None):
    self.name = name  
    self.description = description
    self.items = items
    self.npcs = npcs 
    self.belongingTo = belongingTo 
    # must return back to the location it belongs to
  # hide the love interest here!
  
# class MainCharacter: 
class MainCharacter: 
  def __init__(self, name=None, items=[], type=None, description=None, location=None, health=None, hydration=None, nutrition=None, attackValue=None, experienceValue=none):
    self.name = name
    self.items = items 
    self.description = description 
    self.location = location
    self.health = health
    self.hydration = hydration 
    self.nutrition = nutrition
    self.attackValue = attackValue
    self.experienceValue = experienceValue
# class SideCharacter: 
class NPCs: 
  # specifications for the two types of NPCS:
  # Side Characters (non-harmful):
  #  will have advice
  # Enemies - Monsters (harmful): 
  def __init__(self, name=None, description=None, location=None, subLocation=None, advice=None, attackValue=None, type=None)
    self.name = name
    self.description = description
    self.location = location
    self.subLocation = subLocation
    self.advice = advice
    self.attackValue = attackValue
    self.type = type # specify whether a side character or an enemy

    
# class SideCharacter: 
#   def __init__(self, name=None, description=None, advice=None, location=None, subLocation=None, type=None): 
#     self.name = name
#     self.description = description
#     self.advice = advice
#     self.location = location
#     self.subLocation = subLocation
#     self.type = type 
# # class Enemy: 
# class Enemy: 
#   def __init__(self, name=None, description=None, location=None, subLocation=None, attackValue=None):
#   self.name = name
#   self.description = description
#   self.location = location
#   self.subLocation = subLocation
#   self.attackValue = attackValue
# class Item:  
    # food can increase your health and nutrition, 
    # water purifier at the water stream once to survive at least once

class Item: 
  def __init__(self, name=None, type=None, location=None, subLocation=None, healthValue=None, hydrationValue=None, nutritionValue=None, experienceValue=None, attackValue=None): 
    self.name = name
    self.type = type 
    # weapons - increases attackValue of character
    # consumables - increases healthValue, hydrationValue, nutritionalValue, etc
    self.location = location
    self.subLocation = subLocation
    # for consumables only
    self.healthValue = healthValue
    self.hydrationValue = hydrationValue
    self.nutritionValue = nutritionValue
    self.experienceValue = experienceValue
    self.attackValue = attackValue
#************** CREATION OF VARIABLES *********************

# starting values 

### MAIN CHARACTER ### 
    
player = MainCharacter()
player.items = []
player.health = 100
player.hydration = 78
player.nutrition = 85

### SIDE CHARACTERS ### 3

loveInterest = NPCs()
loveInterest.name = "Your Love Interest"
loveInterest.type = "Side Character" ;
loveInterest.location = "field with flowers"
loveInterest.advice = "'Hey...I'm Olive. Nice to meet you.' Warm eyes stare into yours and a smile graces your face. You finally feel at peace."

wiseMan = NPCs() 
wiseMan.name = "Wise Man"
wiseMan.type = "Side Character"
wiseMan.location = "hollow tree stump"
wiseMan.advice = "'I've been asleep for a while haven't I?' he pauses. 'I came from just around the riverbend a couple of years ago' he looks around at the large tree behind him. 'This is my tree hollow. You're welcome to stay, but I don't have any food to share. It's hard enough to come by now that I'm getting older and my traps are becoming less effective.' A small looking raccoon-dog scampers to his side. 'This is Jengo!' He smiles. 'Jengo has stuck by me for the last couple of months after I found him as a runt.' He mumbles something that you can't quite make out, and guffaws wholehartedly then promptly starts hacking and coughing. You smile and laugh along awkwardly. 'You need advice, soldier?' he states, boring into your eyes with his electric blue ones. You're suprised he can still make out your army uniform with all the dirt caked on. 'Be careful, and watch out for the monsters. Oh, and remember to hydrate' This makes you uneasy. You know riverwater can be deadly and you have the only water purifier for miles. You smile, and say 'Ok'. You turn to leave, and he says an old AKSA saying you distinctly remember hushed whispers about from your childhood:'May your prayers be heard by your people and may you forever feel at peace.' He salutes you the traditional AKSA way, and makes his way back into the hollow before you can reply with the expected response, 'And you, much fortune'."

### ENEMIES ###

enemy1 = NPCs()
enemy1.name = "GENDOM wolf"
enemy1.description = "An abnoramlly large deadly mammal"
enemy1.type = "Enemy"
enemy1.location = "forest near the camp"
enemy1.attackValue = 5.0

enemy2 = NPCs()
enemy2.name = ""
enemy2.description = ""
enemy2.type = "Enemy"
enemy2.location = ""
enemy2.attackValue = 0.0

enemy3 = NPCs()
enemy3.name = ""
enemy3.description = ""
enemy3.type = "Enemy"
enemy3.location = ""
enemy3.attackValue = 0.0

enemy4 = NPCs()
enemy4.name = ""
enemy4.description = ""
enemy4.type = "Enemy"
enemy4.location = ""
enemy4.attackValue = 0.0

enemy5 = NPCs()
enemy5.name = ""
enemy5.description = ""
enemy5.type = "Enemy"
enemy5.location = ""
enemy5.attackValue = 0.0

enemy6 = NPCs()
enemy6.name = ""
enemy6.description = ""
enemy6.type = "Enemy"
enemy6.location = ""
enemy6.attackValue = 0.0

enemy7 = NPCs()
enemy7.name = ""
enemy7.description = ""
enemy7.type = "Enemy"
enemy7.location = ""
enemy7.attackValue = 0.0

enemy8 = NPCs()
enemy8.name = ""
enemy8.description = ""
enemy8.type = "Enemy"
enemy8.location = ""
enemy8.attackValue = 0.0

enemy9 = NPCs()
enemy9.name = ""
enemy9.description = ""
enemy9.type = "Enemy"
enemy9.location = ""
enemy9.attackValue = 0.0


stream = Location()
stream.name = "Stream"
stream.description ="You come across a stream."
stream.items = ["raw water"]
stream.paths = ["Middle Of Forest"]

middleofForest = Location()
middleofForest.name = "middle of forest"
middleofForest.description = "You look around at your surroundings. There's trees on every side of you. You can go in all 4 directions."
middleofForest.items = ["mushrooms" , "wild okra" , "katniss" , "wild onions", "potatoes"]
middleofForest.paths = ["stream" , "hollow tree stump" , "camp" , "clearing"]
middleofForest.npcs = []


city = Location()
city.name = ""
city.description = ""
city.items = [""]
city.paths = ["town"]
city.npcs = [""]


town = Location()
town.name = ""
town.description = ""
town.items = [""]
town.paths = ["city" , "clearing"]
town.npcs = [""]




## Location CAMP ##
camp = Location()
camp.name= "camp"
camp.description ="As you walk further through the forest, you stumble upon a deserted camp. You are too weakened to be concerned by the potential of danger to ponder why it might be there. What do you choose to explore in the camp area?"
camp.items = ["Tent","Axe"]
camp.paths =["tent", "camp area", "forest near camp", "cave", "middle forest", "hollow tree stump"]
camp.npcs = []
camp.visited = False

# subLocation for CAMP(tent)
tent = subLocation()
tent.name= "tent"
tent.description ="You hesitantly step into the abandoned tent. A dusty musk tickles your nostrils--it smells faintly of dried blood. The air is thick with your uncertainty and you strive to avoid the humidity by covering your mouth and nose with your shirt. You look to see what might be useful to you."
tent.items = ["Knife","Lighter","Bandaid"]
tent.npcs = []
tent.belongingTo = ["camp"]

# subLocation for CAMP(camp area)
camp_area = subLocation()
camp_area.name= "camp area"
camp_area.description ="You see a thin trail of smoke floating up from a recently put-out fire. You feel a bit of apprehension. It hasn't been long since the camp's inhabitants were here..."
camp_area.items = ["Wood"]
camp_area.npcs = []
camp_area.belongingTo = ["camp"]

# subLocation for CAMP(forest near the camp) with enemy
forest_near_camp = subLocation()
forest_near_camp.name= "forest near the camp"
forest_near_camp.description ="You exit the camp and walk towards the forest on the other side where you see a GENDOM, or genetically modified, wolf among the trees just 10 feet from the site. It's foaming at the mouth, and you assess that it has probably contracted some uncurable sickness. It snarls at you, it's teeth are stained red and yellow and bits of flesh escape with drool. It looks like it's coming straight for you."
forest_near_camp.items = []
forest_near_camp.npcs = []
forest_near_camp.belongingTo = ["camp"]

## location CAVE(cave) ##
cave = Location()
cave.name= "cave"
cave.description ="You come across a cave opening under a couple of logs in the forest. Sounds of running water can be heard."
cave.items = ["Fish"]
cave.paths =["camp", "field with flowers", "small lake", "stalactites"]
cave.npcs = []
cave.visited = False

# subLocation for CAVE(small lake) with enemy
small_lake = subLocation()
small_lake.name= "small lake"
small_lake.description = ""
small_lake.items = []
small_lake.npcs = []
small_lake.belongingTo = ["cave"]

# subLocation for CAVE(stalactites)
stalactites = subLocation()
stalactites.name= "stalactites"
stalactites.description = ""
stalactites.items = ["Stalactites","Bones"]
stalactites.npcs = []
stalactites.belongingTo = ["cave"]

## location FIELD with flowers(location(FIND love interest)) ##
field = Location()
field.name= "Field with flowers"
field.description =""
field.items = ["Water"]
field.paths =["camp", "field with flowers", "small lake", "stalactites"]
field.npcs = []
field.visited = False

# subLocation for FIELD(river)
river = subLocation()
river.name= "river"
river.description = ""
river.items = [""]
river.npcs = []
river.belongingTo = ["field"]

# subLocation for FIELD(cottage in the meadow)
cottage = subLocation()
cottage.name= "Cottage in the meadow"
cottage.description = ""
cottage.items = [""]
cottage.npcs = []
cottage.belongingTo = ["field"]

# subLocation for FIELD(edge of a wood)
edge = subLocation()
edge.name= ""
edge.description = ""
edge.items = [""]
edge.npcs = []
edge.belongingTo = ["field"]

### ITEMS ### 

    ## WEAPONS ##
    # Guns: Glock, AK-47, AR-15, Minigun, etc
    # Melee Weapons: Baseball Bat, Knife, Katana, Brass Knuckles, Axe
item1 = Item()
item1.name = "Glock-19"
item1.type = "weapon"
item1.location = ""
item1.subLocation = ""
item1.healthValue = None
item1.hydrationValue = None
item1.nutritionValue = None
item1.experienceValue = None
item1.attackValue = 15.0

item1 = Item()
item1.name = "AK-47"
item1.type = "weapon"
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 35.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0
item1 = Item()

item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0

item1 = Item()
item1.name = ""
item1.type = ""
item1.location = ""
item1.subLocation = ""
item1.healthValue = 0.0
item1.hydrationValue = 0.0
item1.nutritionValue = 0.0
item1.experienceValue = 0.0
item1.attackValue = 0.0


# self.healthValue = healthValue
#     self.hydrationValue = hydrationValue
#     self.nutritionValue = nutritionValue
#     self.experienceValue = experienceValue
#     self.attackValue = attackValue
    ## CONSUMABLES ## 
    # Food: Burrito, Sandwich,fish, etc
    # Drinks: Water, Mountain Dew, Beer, Lemonade, etc
    # Medical items: Bandaid, First-Aid Kit, etc

    ## Experience ##
    # Stalactites, Bones, Wood, Tent, Lighter


def check_answer(input): 
  global name
  input_message = input

  if input_message == "help": 
    print("Here are some commands you can run...")
    # commands: 
    # go -> head to a location next to this one
    # help -> lists the possible commands a player can do
    # location -> show what place the player is currently in
    # grab -> take an object
    # consume -> drink/eat a food/drink item for consumption
    # look -> show what the surroundings ar
    # inventory -> shows what items the character currently has 
  elif input_message == "go": 
    message_list = input_message.split(" ")
    message = message_list[1:]
    new_room = " ".join(message)
    # help page *to be filled out*
  elif input_message == "location": 
    # print the current location that the main character is in
  elif input_message == "grab": 
    # grab "" should give the character the item that they chose to grab
  elif input_message == "consume":
    # consume "" should "use up" the item, meaning the item should disappear from their inventory, restoring the corresponding values
  elif input_message == "look":

  elif input_message = "inventory":

  elif input_message = "end": 
    # end the game here
  else:   
    print("Please enter in a valid command!")
  
def prompt_user(): 
  reply = input("What action do you want to perform? >> ")
  return reply
#****************** START THE GAME ******************
def Start(): 
  global name
  print("Welcome to 'Your New Destiny', Krawfen soldier. You have just betrayed secrets to the AKSA organization, the Krawfen empire's sworn enemy, and they pursue you while you run blindly into the woods located in the outskirts of your town. As you sprint through the vegetation, you look over your shoulder and see that the AKSA's army is falling behind and their shouts start to get quieter and quieter. You hide among the shrubs and bushes on the dirt floor, realizing your pursuers have lost you. A fleeting spark of hope feels like a lit fire in the pit of your stomach. Despite this, you find yourself alone in an expansive forest with nothing but a small pack containing crackers and a water purfier. You don't know what kinds of people and animals you will find in these woods. This used to be a testing site for freak animal combinations. As you peer through the genetically modified pines of 2084, you start to realize the implications of your situation. You are determined to survive.")
  name = input("What is your name, soldier?")
  
  print("Welcome, " + name)
  
  print("You can type 'help' to learn how to play")
  while game_running: 
    check_answer(prompt_user())
    # write a function to check the answesr from the user
    
Start()


###
# def return_element(list):
#     ret_string = ""
#     for l in list: 
#         ret_string += str(l) + ", "
#         if l == list[len(list)-1]: 
#             ret_string += str(l) + ""
#     return ret_string

# print("My name is " + str(new_dict["name"]) + ".\n" 
# + "Am I an adult? " + str(new_dict["adult"]) + ".\n" 
# + "My age is " + str(new_dict["age"]) + ".\n"
# + "My hobbies are " + return_element(new_dict["hobbies"]) + ".\n" 
# + "Has this dictionary been modified? Yes!" + new_dict["modification"] + "."
# )
###
