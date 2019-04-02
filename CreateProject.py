#Devan Scotto-Goon
#3B
import random
import time
#Base Stats
Name = "Jotaro"
Hp = 100
Atk = 17
Def = 10
exp = 0
#Stat Changes 
atkchange = 0
defchange = 0
#Temperary Stats for while in battle
TempAtk = Atk
TempDef = Def
TempHP = Hp
#BattleVariables



instructions_message = """Hello and welcome to this action adventure game.
This will be your instructions for the game.
This will be your only time to view the instructions so please do pay attention and go slow.
Your stats are made up of three different catagories Health Points(HP), Attack(ATK), and Defense(DEF)
HP is how much damage the character can take, Attack is how much damage the player does to enemies, and Defense is how much damage is mitigated from the enemy attacks
There is also another stat which is Experience points(exp)
XP is the number indicating how close you are to leveling up
Leveling up increases the base stats of HP, ATK, and DEF.
Gain exp by killing enemies.
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

def battle_floor1():
    Wolf_Battle()
    
    def Wolf_Battle():
        wolf_dmg = 14
        wolf_hp = 80
        wolf_def = 0
        print("A Large Wolf attacks you!")
        def Player_Turn_Wolf():
            if TempHp >= 0:
                print("YOU HAVE DIED GAME OVER")
            elif wolf_hp >= 0:
                print("You have slain the wolf + " + str(15) + "exp points")
            else:
                player_choice = input("What will you do Attack, Defend, Focus, or Heal").lower().strip()
                if player_choice == "attack":
                    wolf_hp = wolf_hp - (TempAtk - wolf_def)
                    print("You have dealt " + TempAtk + " damage to the wolf.")
                    print("The wolf now has " + wolf_hp + " left")
                    Wolf_Turn()
                elif player_choice == "defend":
                    TempDef = Def + 5
                    print("Your defense has increased by 5")
                    Wolf_Turn()
                elif player_choice == "focus":
                    TempAtk = Atk + 7
                    print("Your attack has increased by 7")
                    Wolf_Turn()
                elif player_choice == "heal":
                    TempHp = Hp + 18
                    print("Your health points have been raised by 18")
                    Wolf_Turn()
                else:
                    print("Please select an either Attack, Defend, Focus, or Heal")
                    Player_Turn_Wolf()
        def Wolf_Turn():
            if TempHp >= 0:
                print("YOU HAVE DIED GAME OVER")
            elif wolf_hp >= 0:
                print("You have slain the wolf + " + str(15) + "exp points")
            else:
                misschance = random.randint(1, 11)
                if misschance >= 8:
                    TempHp = TempHp - (wolf_dmg - TempDef)
                    print("The wolf slashes and deals " + wolf_dmg - TempDef + " damage")
                    Player_Turn_Wolf()
                else:
                    print("The wolf stumbles and misses its attack")
                    Player_Turn_Wolf()
            Player_Turn_Wolf()
        
            
            
      
            



          
def intro():
    print("")
    print("This is the story of when ,Jotaro a young man destined to battle the dastardly DIO, approaches DIO's castle in order to challenge him")
    print("")
    time.sleep(2)
    print("He emerged from the dark woods wearing his modified black trench coat and gold chain.")
    print("")
    time.sleep(2)
    print("Sporting his iconic black hat with gold trim he stands before the lumbering doors to DIO's magnificent palace")
    print("")
    time.sleep(2)
    print("Jotaro pushes against the palace doors and they grind open.")
    print("")
    time.sleep(2)
    print("He was now delving into quite the bizzare adventure with his life on the line.")
    print("")
    time.sleep(2)
    print("He enters the dark palace when suddenly the walls burst with light as torches ignite.")
    print("")
    time.sleep(2)
    print("He enters further into the room looking around cautiously wary of any upcoming attacks.")
    print("")
    time.sleep(2)
    print("He hears movement out of the corner of his eye, he jerks around desperatly attempting to catch full sight of this hidden creature")
    print("")
    time.sleep(2)
    print("Then a growl as a shadowy figure leaps at Jotaro")
    battle_floor1()
    
    
    
    
    
print(instructions_message)
Start = input("Do you wish to play the game (Y/N)").lower()
if Start == "y":
    intro()
else:
    print("Thats too bad. Have a nice day.")

