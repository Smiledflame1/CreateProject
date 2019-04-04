#Devan Scotto-Goon
#3B
import random
import time
#Base Stats
Name = "Jotaro"
Hp = 100
Atk = 17
Def = 3
#Stat Changes 
atkchange = 0
defchange = 0

#IsThePlayerAlive
life = True

instructions_message = """Hello and welcome to this action adventure game.
This will be your instructions for the game.
This will be your only time to view the instructions so please do pay attention and go slow.
Your stats are made up of three different catagories Health Points(HP), Attack(ATK), and Defense(DEF)
HP is how much damage the character can take, Attack is how much damage the player does to enemies, and Defense is how much damage is mitigated from the enemy attacks
You will randomly encounter an enemy from a set of 3 different monsters which changes depending on the floor your on
Battle takes place 1 v 1 with the player attacking first.
There are 4 options while engaged in battle.
Attack, Defend, Focus and Heal
Attack deals your attack stat in damage to the enemy
Defend increases your defense stat for that battle only
Focus increases your attack stat for that battle only
Heal restores the HP of your character but can only be uesd 3 times each fight
All of your base stats reset to what they were before the battle so focus and defend dont carry over
The way to progress through this game is to defeat a set amount of enemies per floor to fight the floor guardian.
After defeating the floor guardian you move to the next floor to fight a new set of monsters.
After going through all the floors you will face against the boss of the game.
Please have fun and enjoy the game.
To view your stats at any time type stats() and your stats page will apear.
"""

def stats():
    print("STATS:")
    print("")
    print(Name)
    print("")
    print(Hp)
    print("")
    print(Atk)
    print("")
    print(Def)
    print("")

    
def Wolf_Battle():
    print("A Large Wolf attacks you!")
    Player_Turn_Wolf()

def Player_Turn_Wolf():
        global Hp
        global Atk
        global Def
        global life
        wolf_dmg = 14
        wolf_hp = 80
        wolf_def = 0
        player_choice = input("What will you do Attack, Defend, Focus, or Heal\n").lower().strip()
        if player_choice == "attack":
            wolf_hp = wolf_hp - ( Atk - wolf_def)
            print("You have dealt " + str(Atk - wolf_def) + " damage to the wolf.\n")
            print("The wolf now has " + str(wolf_hp) + " hp left\n")
            if wolf_hp <= 0:
                print("You have slain the wolf\n" )
                Hp = 100
                Atk = 17
                Def = 3
            else:
                Wolf_Turn()
        elif player_choice == "defend":
            Def = Def + 3
            print("Your defense has increased by 3\n")
            Wolf_Turn()
        elif player_choice == "focus":
            Atk = Atk + 7
            print("Your attack has increased by 7\n")
            Wolf_Turn()
        elif player_choice == "heal":
            Hp = Hp + 18
            print("Your health points have been raised by 18\n")
            print(Hp)
            Wolf_Turn()
        else:
            print("Please select an either Attack, Defend, Focus, or Heal\n")
            Player_Turn_Wolf()

def Wolf_Turn():
        global Def
        global Hp
        wolf_dmg = 14
        wolf_hp = 80
        wolf_def = 0
        misschance = random.randint(1, 11)
        if misschance <= 8:
            Hp = Hp - (wolf_dmg - Def)
            print("The wolf slashes and deals " + str(wolf_dmg - Def) + " damage\n")
            print("The player now has " + str(Hp) + " Left\n")
            if Hp > 0:
                Player_Turn_Wolf()
            else:
                print("YOU HAVE DIED GAME OVER")
                life = False
        else:
            print("The wolf stumbles and misses its attack")
            Player_Turn_Wolf()
          
def intro():
    print("This is the story of when ,Jotaro a young man destined to battle the dastardly DIO, approaches DIO's castle in order to challenge him\n")
    time.sleep(2)
    print("He emerged from the dark woods wearing his modified black trench coat and gold chain.\n")
    time.sleep(2)
    print("Sporting his iconic black hat with gold trim he stands before the lumbering doors to DIO's magnificent palace")
    time.sleep(2)
    print("Jotaro pushes against the palace doors and they grind open.\n")
    time.sleep(2)
    print("He was now delving into quite the bizzare adventure with his life on the line.\n")
    time.sleep(2)
    print("He enters the dark palace when suddenly the walls burst with light as torches ignite.\n")
    time.sleep(2)
    print("He enters further into the room looking around cautiously wary of any upcoming attacks.\n")
    time.sleep(2)
    print("He hears movement out of the corner of his eye, he jerks around desperatly attempting to catch full sight of this hidden creature\n")
    time.sleep(2)
    print("Then a growl as a shadowy figure leaps at Jotaro\n")
    Wolf_Battle()


def story1():
  print("You stand over the corpse of the wolf, your breathing heavy from the first real battle in weeks.\n")
  time.sleep(2)
  print("You notice a door directly in front of you with words carved into it reading,\n")
  time.sleep(2)
  print("COME JOTARO IF YOU DARE\n")
  time.sleep(2)

print(instructions_message)
Start = input("Do you wish to play the game (Y/N)").lower()
if Start == "y":
    intro()
    while life == True:
      story1()
else:
    print("Thats too bad. Have a nice day.")


