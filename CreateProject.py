#Devan Scotto-Goon
#3B
import random
import time
#Base Stats
Name = "Jotaro"
Hp = 100
Atk = 8
Def = 10
exp = 0
#Stat Changes 
atkchange = 0
defchange = 0
#Temperary Stats for while in battle
TempAtk = Atk
TempDef = Def
TempHP = Hp 


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
The amount you heal, how much your Atk is raised, and how much your Def is raised is determined by your level
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



          
def intro():
    print("")
    print("This is the story of when Jotoro a young man destined to battle the dastardly DIO approached DIO's castle in order to challenge him")
    print("")
    time.sleep(2)
    print("He emerged from the dark woods wearing his modified black trench coat and gold chain.")
    print("")
    time.sleep(2)
    print("Sporting his iconic black hat with gold trim he stands before the lumbering doors to DIO's magnificent palace")
    print("")
    time.sleep(2)
    print("Jotoro pushes against the palace doors and they grind open.")
    print("")
    time.sleep(2)
    print
    
    
    
    
print(instructions_message)

