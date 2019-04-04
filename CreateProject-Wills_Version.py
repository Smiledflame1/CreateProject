#Devan Scotto-Goon
#3B

# Imports
import random
import time

# Don't need any global variables any more. However, global constants are fine! Thus, I'm going to leave
# player and wolf names as globals since they're constant and we're never changing them.
#
# Also, it's typically convention to do globals a full caps just to distinguish them.
PLAYER_NAME = "Jotaro"
WOLF_NAME = "Good Boye" # I gave the wolf a new name too :P

INSTRUCTIONS_MESSAGE = """Hello and welcome to this action adventure game.
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

# It's a good habit to put the lowest level instructions in a function. Typically, that function is 
# called main(). We call main() at the end of this file
def main():
    print(INSTRUCTIONS_MESSAGE)
    Start = input("Do you wish to play the game (Y/N)").lower()
    if Start == "y":
        #intro()
        playerWon = Wolf_Battle()
        while playerWon == True:
          story1()
    else:
        print("Thats too bad. Have a nice day.")
        

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
    
    # Set the hp, attack, and defense for the player and wolf
    playerName = PLAYER_NAME # using our global
    playerHp = 100
    playerAtk = 17
    playerDef = 3
    
    wolfName = WOLF_NAME # using our global
    wolfHp = 80
    wolfAtk = 11
    wolfDef = 0
    
    # We want to loop until we explictly reach a conclusion from within the loop
    while (True):
        # Get the player's action choice. This function should always give us a valid value
        player_choice = Get_Player_Choice()        
        
        if player_choice == "attack":
            wolfHp = attackObject(wolfHp, playerAtk, wolfDef, wolfName)
            
        elif player_choice == "defend":
            # Changed the hardcoded '3' to a variable; better style then putting '3' multiple places
            playerDefIncrease = 3
            playerDef = playerDef + playerDefIncrease
            print("Your defense has increased by " + str(playerDefIncrease) + ".\n")
            
        elif player_choice == "focus":
            # Changed the hardcoded '7' to a variable; better style then putting '7' multiple places
            playerAtkIncrease = 3
            playerAtk = playerAtk + playerAtkIncrease
            print("Your attack has increased by " + str(playerAtkIncrease) + ".\n")
            
        elif player_choice == "heal":
            # Changed the hardcoded '18' to a variable; better style then putting '18' multiple places
            playerHealAmount = 18
            playerHp = playerHp + playerHealAmount
            print("Your health points have been raised by " + str(playerHealAmount) + ".\n")
            print("Your new HP is " + str(playerHp) + ".\n")
            
        else:
            # This is an error handling case; we should never execute this block of code
            print("How did we get here?")
            assert(False)
            
        # If the wolf is dead, we win!
        if (wolfHp <= 0):
            print("You win, dude.")
            
            # Break out of the loop and function
            return True
        
        # Now the wolf gets to try and kill us
        playerHp = Wolf_Turn(playerHp, wolfAtk, playerDef)
        
        # If we are dead, then we don't win :'(
        if (playerHp <= 0):
            print("You ded, son.")
            return False
    
def Get_Player_Choice():
    valid_choices = [
        "attack",
        "defend",
        "focus",
        "heal"
    ]
    
    # Btw, POGGERS choice to call ".lower().strip()" here. Input sanitation like this is key to good
    # programs. Idk if you thought to do this or someone else did, but it's absolutely the right call.
    player_choice = input("What will you do Attack, Defend, Focus, or Heal\n").lower().strip()

    # Make sure the user gave us a valid choice, and berate them until they do
    while (player_choice not in valid_choices):
        print("Please select an either Attack, Defend, Focus, or Heal\n")
        player_choice = input("What will you do Attack, Defend, Focus, or Heal\n").lower().strip()  
    
    return player_choice

def Wolf_Turn(oldPlayerHp, wolfAtk, playerDef):
    # By default, the player's new hp is the same as the player's old hp. This handles the case where
    # the wolf misses.
    newPlayerHp = oldPlayerHp

    misschance = random.randint(1, 11)
    if misschance <= 8:
        # Using max() so that we don't deal negative damage
        damage = max(wolfAtk - playerDef, 0)
        newPlayerHp = oldPlayerHp - damage
    
        print("The wolf slashes and deals " + str(damage) + " damage\n")
        print("The player now has " + str(newPlayerHp) + " HP left\n")
        
    else:
        print("The wolf stumbles and misses its attack")
        
    return newPlayerHp
        
              
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
    
    
def attackObject(oldHp, attackerAtk, defenderDef, defenderName):
    damage = max(attackerAtk - defenderDef, 0)
    newHp = oldHp - damage
    print("You have dealt " + str(damage) + " damage to the " + defenderName + ".\n")
    print("The " + defenderName + " now has " + str(newHp) + " hp left\n")
    return newHp


def story1():
    print("You stand over the corpse of the wolf, your breathing heavy from the first real battle in weeks.\n")
    time.sleep(2)
    print("You notice a door directly in front of you with words carved into it reading,\n")
    time.sleep(2)
    print("COME JOTARO IF YOU DARE\n")
    time.sleep(2)
    
    
# Call main() to start the program!
main()

