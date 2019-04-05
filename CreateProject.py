#Devan Scotto-Goon
#3B

# Imports
import random
import time

# Names as global constants 
PLAYER_NAME = "Jotaro"
WOLF_NAME = "Good Boy" # Wolfs Name 
MINATAUR_NAME = "Minataur Peggy" #Minataur's name
GUARDIAN_NAME = "Guardian Vanilla Ice" #Guardians name
DIO_NAME = "Master of all DIO" #Dio's name 

INSTRUCTIONS_MESSAGE = """Hello and welcome to this adventure game.
This game is played by battling monsters in a linear preordered fashion. Before fighting the boss of the game.
Too play the game you will have to choose on of 4 options when a battle starts,
Those 4 options are:
Attack - Dealing damage to the enemy
Defend - raises your defense by 3
Focus - raises your attack by 7
Heal - Heals yourself for 18 damage(Can go over the intial health value)
Stat changes do no persist into the next battle as the stats are reset.
After a battle you gain stats by "Absorbing the soul of the monster"
This stat change does persist.
Both you and the monster have 3 main base stats
Health Points(hp) - How much damage you can take
Defense(def) - subtracts from the intitial damage one recieves from the enemy 
Attack(atk) - how much damage one does to an enemy is decreased by armor of the opponent
You always go first and the enemy attacks second
There is a chance the enemy's attack will miss in which that turn is wasted by the enemy
That is the basics of this game so now your ready to go!
Goodluck
"""

# This is how our story will sequentially unfold 
def main():
    print(INSTRUCTIONS_MESSAGE)
    Start = input("Do you wish to play the game (Y/N)").lower()
    if Start == "y":
        intro()
        playerWon = Wolf_Battle()
        while playerWon == True:
          story1()
          story2()
          story3()
          ending()
          
        
    #else:
        #print("Thats too bad. Have a nice day.")
        

#The player turn for the wolf battle and it checks for win conditions     
def Wolf_Battle():
    print("A Large Wolf attacks you!")
    print("_____________________________________________________________________________________________________________________________________________________________________________\n")
    print("Player Hp: 100\n")
    print("Player Atk: 17\n")
    print("Player Def: 3\n")
    print("Wolf Hp: 80\n")
    print("Wolf Atk: 11\n")
    print("Wolf Def: 0\n")
    print("_____________________________________________________________________________________________________________________________________________________________________________\n")

    
    # Set the hp, attack, and defense for the player and wolf
    playerName = PLAYER_NAME
    playerHp = 100
    playerAtk = 17
    playerDef = 3
    
    wolfName = WOLF_NAME 
    wolfHp = 80
    wolfAtk = 11
    wolfDef = 0
    
    # loop until we explictly reach a conclusion from within the loop
    while (True):
        # Get the player's action choice. This function should always give us a valid value
        player_choice = Get_Player_Choice()        
        
        if player_choice == "attack":
            wolfHp = attackObject(wolfHp, playerAtk, wolfDef, wolfName)
            
        elif player_choice == "defend":
            playerDefIncrease = 3
            playerDef = playerDef + playerDefIncrease
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your defense has increased by " + str(playerDefIncrease) + ".\n")
            
        elif player_choice == "focus":
            playerAtkIncrease = 7
            playerAtk = playerAtk + playerAtkIncrease
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your attack has increased by " + str(playerAtkIncrease) + ".\n")
            
        elif player_choice == "heal":
            playerHealAmount = 18
            playerHp = playerHp + playerHealAmount
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your health points have been raised by " + str(playerHealAmount) + ".\n")
            print("Your new HP is " + str(playerHp) + ".\n")
            
        else:
            # This is an error handling case; we should never execute this block of code
            print("How did we get here?")
            assert(False)
            
        # If the wolf is dead, we win! and we move on
        if (wolfHp <= 0):
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("The soul of the wolf is absorbed into you\n")
            print("Atk increased by 3\n")
            print("Def increased by 1\n")
            print("Hp increased by 25\n")
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            time.sleep(2.5)
            
            # Break out of the loop and function
            return True
        
        # Now the wolf gets to try and kill us
        playerHp = Wolf_Turn(playerHp, wolfAtk, playerDef)
        
        # If we are dead, then we don't win :'( ad the game stops
        if (playerHp <= 0):
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("You die, the wolf feeds on your corpse")
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            return False

def Minataur_Battle():
    print("You engage in battle with the Minitour")
    print("_____________________________________________________________________________________________________________________________________________________________________________\n")
    print("Player Hp: 125\n")
    print("Player Atk: 20\n")
    print("Player Def: 4\n")
    print("Minataur Hp: 200\n")
    print("Minataur Atk: 18\n")
    print("Minataur Def: 9\n")
    print("_____________________________________________________________________________________________________________________________________________________________________________\n")



    playerName = PLAYER_NAME
    playerHp = 125
    playerAtk = 20
    playerDef = 4

    miniName = MINATAUR_NAME
    miniHp = 200
    miniAtk = 18
    miniDef = 9

      # We want to loop until we explictly reach a conclusion from within the loop
    while (True):
        # Get the player's action choice. This function should always give us a valid value
        player_choice = Get_Player_Choice()        
        
        if player_choice == "attack":
            miniHp = attackObject(miniHp, playerAtk, miniDef, miniName)
            
        elif player_choice == "defend":
            playerDefIncrease = 3
            playerDef = playerDef + playerDefIncrease
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your defense has increased by " + str(playerDefIncrease) + ".\n")
            
        elif player_choice == "focus":
            playerAtkIncrease = 7
            playerAtk = playerAtk + playerAtkIncrease
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your attack has increased by " + str(playerAtkIncrease) + ".\n")
            
        elif player_choice == "heal":
            playerHealAmount = 18
            playerHp = playerHp + playerHealAmount
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your health points have been raised by " + str(playerHealAmount) + ".\n")
            print("Your new HP is " + str(playerHp) + ".\n")
            
        else:
            # This is an error handling case; we should never execute this block of code
            print("How did we get here?")
            assert(False)
            
        # If the Minataur is dead, we win! and move on
        if (miniHp <= 0):
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("The soul of the Minataur is absorbed into you\n")
            print("Atk increased by 4\n")
            print("Def increased by 1\n")
            print("Hp increased by 50\n")
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            time.sleep(2.5)
            
            # Break out of the loop and function
            return True
        
        # Now the Minataur gets to try and kill us
        playerHp = Minataur_Turn(playerHp, miniAtk, playerDef)
        
        # If we are dead, then we don't win :'( and the game ends
        if (playerHp <= 0):
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("You lie on the ground beaten and battered the life fading from your body.\n")
            time.sleep(2)
            print("'You were a tough opponent lord DIO was right to send me against you'\n")
            time.sleep(2)
            print("You dont respond because you cant, you just lay there untill finally your eyes close forever\n")
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            time.sleep(2)
            return False

def Guardian_Battle():
    #Prints the staring stats for both parties
    print("You face off against the Guardian Vanilla Ice\n")
    print("_____________________________________________________________________________________________________________________________________________________________________________\n")
    print("Player Hp: 175\n")
    print("Player Atk: 24\n")
    print("Player Def: 5\n")
    print("Guardian Hp: 300\n")
    print("Guardian Atk: 27\n")
    print("Guardian Def: 11\n")
    print("_____________________________________________________________________________________________________________________________________________________________________________\n")

    playerName = PLAYER_NAME
    playerHp = 175
    playerAtk = 24
    playerDef = 5

    guardName = GUARDIAN_NAME
    guardHp = 300
    guardAtk = 27
    guardDef = 11

      # We want to loop until we explictly reach a conclusion from within the loop
    while (True):
        # Get the player's action choice. This function should always give us a valid value
        player_choice = Get_Player_Choice()        
        
        if player_choice == "attack":
            guardHp = attackObject(guardHp, playerAtk, guardDef, guardName)
            
        elif player_choice == "defend":
            playerDefIncrease = 3
            playerDef = playerDef + playerDefIncrease
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your defense has increased by " + str(playerDefIncrease) + ".\n")
            
        elif player_choice == "focus":
            playerAtkIncrease = 7
            playerAtk = playerAtk + playerAtkIncrease
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your attack has increased by " + str(playerAtkIncrease) + ".\n")
            
        elif player_choice == "heal":
            playerHealAmount = 18
            playerHp = playerHp + playerHealAmount
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your health points have been raised by " + str(playerHealAmount) + ".\n")
            print("Your new HP is " + str(playerHp) + ".\n")
            
        else:
            # This is an error handling case; we should never execute this block of code
            print("How did we get here?")
            assert(False)
            
        # If the guardian is dead, we win! and move on
        if (guardHp <= 0):
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("The soul of the Guardian is absorbed into you\n")
            print("Atk increased by 6\n")
            print("Def increased by 5\n")
            print("Hp increased by 125\n")
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            time.sleep(2.5)
            
            # Break out of the loop and function
            return True
        
        # Now the guardian gets to try and kill us
        playerHp = Guardian_Turn(playerHp, guardAtk, playerDef)
        
        # If we are dead, then we don't win :'( and the game ends
        if (playerHp <= 0):
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Cream pierces your body causing you to scream in agony.\n")
            time.sleep(2)
            print("'Now you realize it is folly to challenge lord DIO'\n")
            time.sleep(2)
            print("Vanilla Ice removes the sword from your body leaving a large hole in you.\n")
            time.sleep(2)
            print("You failed.\n")
            time.sleep(2)
            print("You weren't even strong enough to defeat Vanilla Ice, why did you beleive you could defeat DIO\n")
            time.sleep(2)
            print("These thoughts linger in your mind as you slowly bleed out on the ground.\n")
            time.sleep(2)
            print("Then in your final moments your thoughts change to your mother and sister.\n")
            time.sleep(2)
            print("You wonder what will happen when you don't return.\n")
            time.sleep(2)
            print("You hope they can move on and that their grief subsides quick enough.\n")
            time.sleep(2)
            print("And with that your last spurts of life give out and it cuts to black.\n")
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            return False

def DIO_Battle():
    #Prints the staring stats for both parties
    print("You clash with DIO the Master of ALL\n")
    print("_____________________________________________________________________________________________________________________________________________________________________________\n")
    print("Player Hp: 300\n")
    print("Player Atk: 30\n")
    print("Player Def: 10\n")
    print("DIO Hp: 500\n")
    print("DIO Atk: 45\n")
    print("DIO Def: 15\n")
    print("_____________________________________________________________________________________________________________________________________________________________________________\n")

    playerName = PLAYER_NAME
    playerHp = 300
    playerAtk = 30
    playerDef = 10

    dioName = DIO_NAME
    dioHp = 500
    dioAtk = 45
    dioDef = 15

      # We want to loop until we explictly reach a conclusion from within the loop
    while (True):
        # Get the player's action choice. This function should always give us a valid value
        player_choice = Get_Player_Choice()        
        
        if player_choice == "attack":
            dioHp = attackObject(dioHp, playerAtk, dioDef, dioName)
            
        elif player_choice == "defend":
            playerDefIncrease = 3
            playerDef = playerDef + playerDefIncrease
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your defense has increased by " + str(playerDefIncrease) + ".\n")
            
        elif player_choice == "focus":
            playerAtkIncrease = 7
            playerAtk = playerAtk + playerAtkIncrease
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your attack has increased by " + str(playerAtkIncrease) + ".\n")
            
        elif player_choice == "heal":
            playerHealAmount = 18
            playerHp = playerHp + playerHealAmount
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("Your health points have been raised by " + str(playerHealAmount) + ".\n")
            print("Your new HP is " + str(playerHp) + ".\n")
            
        else:
            # This is an error handling case; we should never execute this block of code
            print("How did we get here?")
            assert(False)
            
        # If DIO is dead, we win! and instigate the ending
        if (dioHp <= 0):
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("The soul of DIO is absorbed into you\n")
            print("Atk increased by 45\n")
            print("Def increased by 15\n")
            print("Hp increased by 500\n")
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            time.sleep(2.5)
            
            # Break out of the loop and function
            return True
        
        # Now the guardian gets to try and kill us
        playerHp = DIO_Turn(playerHp, dioAtk, playerDef)
        
        # If we are dead, then we don't win :'( and the game ends
        if (playerHp <= 0):
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            print("DIO's power was too much for you after all.\n")
            time.sleep(2)
            print("Even after absorbing Vanilla Ice's power, it still paled in comparison to DIO's.\n")
            time.sleep(2)
            print("As you lay on the ground face up, looking straight at DIO you feel guilt.\n")
            time.sleep(2)
            print("You failed.\n")
            time.sleep(2)
            print("After trying so hard and absorbing so much power you still failed.\n")
            time.sleep(2)
            print("Dio bends down placing his lips next to your ear.\n")
            time.sleep(2)
            print("After that pitiful performence shall I visit your family to tell them the news.\n")
            time.sleep(2)
            print("Your thoughts fill with rage as you attempt to headbutt dio. But to no avail.\n")
            time.sleep(2)
            print("You can't move not even a bit.\n")
            time.sleep(2)
            print("And with those words DIO cackles and raises his boot.\n")
            time.sleep(2)
            print("The last thing you see is DIO slamming his boot into your face.\n")
            print("______________________________________________________________________________________________________________________________________________________________________\n")
            return False


    
def Get_Player_Choice():
    #Uses a list to define what the player can pick from
    valid_choices = [
        "attack",
        "defend",
        "focus",
        "heal"
    ]
    

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
        print("______________________________________________________________________________________________________________________________________________________________________\n")
        
    else:
        print("The wolf stumbles and misses its attack")
        print("______________________________________________________________________________________________________________________________________________________________________\n")
        
    return newPlayerHp

def Minataur_Turn(oldPlayerHp, miniAtk, playerDef):
    # By default, the player's new hp is the same as the player's old hp. This handles the case where
    # the wolf misses.
    newPlayerHp = oldPlayerHp

    misschance = random.randint(1, 11)
    if misschance <= 8:
        # Using max() so that we don't deal negative damage
        damage = max(miniAtk - playerDef, 0)
        newPlayerHp = oldPlayerHp - damage
    
        print("The Minitaurs fist strikes you dealing " + str(damage) + " damage\n")
        print("The player now has " + str(newPlayerHp) + " HP left\n")
        print("______________________________________________________________________________________________________________________________________________________________________\n")
        
    else:
        print("In the Minitaurs arrogence he taunts you instead of attacking\n")
        print("______________________________________________________________________________________________________________________________________________________________________\n")

    return newPlayerHp

def Guardian_Turn(oldPlayerHp, guardAtk, playerDef):
    # By default, the player's new hp is the same as the player's old hp. This handles the case where
    # the wolf misses.
    newPlayerHp = oldPlayerHp

    misschance = random.randint(1, 11)
    if misschance <= 8:
        # Using max() so that we don't deal negative damage
        damage = max(guardAtk - playerDef, 0)
        newPlayerHp = oldPlayerHp - damage
    
        print("Vanilla Ice slashes you with Cream dealing " + str(damage) + " damage\n")
        print("The player now has " + str(newPlayerHp) + " HP left\n")
        print("______________________________________________________________________________________________________________________________________________________________________\n")
        
    else:
        print("The guardian stalls to goad you into a rage to make the battle tougher.\n")
        print("______________________________________________________________________________________________________________________________________________________________________\n")

    return newPlayerHp

def DIO_Turn(oldPlayerHp, dioAtk, playerDef):
    # By default, the player's new hp is the same as the player's old hp. This handles the case where
    # the wolf misses.
    newPlayerHp = oldPlayerHp

    misschance = random.randint(1, 11)
    if misschance <= 8:
        # Using max() so that we don't deal negative damage
        damage = max(dioAtk - playerDef, 0)
        newPlayerHp = oldPlayerHp - damage
    
        print("DIO's vast power slams into you dealing " + str(damage) + " damage\n")
        print("The player now has " + str(newPlayerHp) + " HP left\n")
        print("______________________________________________________________________________________________________________________________________________________________________\n")
        
    else:
        print("DIO remained recoiled from your most recent attack.\n")
        print("______________________________________________________________________________________________________________________________________________________________________\n")

    return newPlayerHp


#The begining of the story first thing that plays when you start the game            
def intro():
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    print("This is the story of when ,Jotaro a young man destined to battle the dastardly DIO, approaches DIO's castle in order to challenge him\n")
    time.sleep(2)
    print("You emerge from the dark woods wearing your modified black trench coat and gold chain.\n")
    time.sleep(2)
    print("Sporting your iconic black hat with gold trim you stands before the lumbering doors to DIO's magnificent palace\n")
    time.sleep(2)
    print("You push against the palace doors and they grind open.\n")
    time.sleep(2)
    print("You were now delving into quite the bizzare adventure with your life on the line.\n")
    time.sleep(2)
    print("You enter the dark palace when suddenly the walls burst with light as torches ignite.\n")
    time.sleep(2)
    print("You enter further into the room looking around cautiously wary of any upcoming attacks.\n")
    time.sleep(2)
    print("You see movement out of the corner of his eye, you jerk around desperatly attempting to catch full sight of this hidden creature\n")
    time.sleep(2)
    print("Then a growl as a shadowy figure leaps at You\n")
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    
    
#This is our function for when we attack because its more complicated than the other options I made it a function     
def attackObject(oldHp, attackerAtk, defenderDef, defenderName):
    damage = max(attackerAtk - defenderDef, 0)
    newHp = oldHp - damage
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    print("You have dealt " + str(damage) + " damage to the " + defenderName + ".\n")
    print("The " + defenderName + " now has " + str(newHp) + " hp left\n")
    return newHp

#The story after you slay the wolf instigates the fight against the Minotaur 
def story1():
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    print("You stand over the corpse of the wolf, your breathing heavy from the first real battle in weeks.\n")
    time.sleep(2)
    print("You notice a door directly in front of you with words carved into it reading,\n")
    time.sleep(2)
    print("COME JOTARO IF YOU DARE\n")
    time.sleep(2)
    print("You gladly welcome the challenge.\n")
    time.sleep(2)
    print("You have been studying Dio's palace for months.\n")
    time.sleep(2)
    print("You know that this was the first test and that there are still two more tests before you can face DIO\n")
    time.sleep(2)
    print("You smile at the thought of two more fights then you force open the door\n")
    time.sleep(2)
    print("You stand at the door way to a stadium like room.\n")
    time.sleep(2)
    print("In the center of this stadium is a large minataur.\n")
    time.sleep(2)
    print("'Hah so this is the human lord DIO told me about'\n")
    time.sleep(2)
    print("He looks strong with his ripped physique and menacing presence\n")
    time.sleep(2)
    print("You approach him and prepare to battle\n")
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    Minataur_Battle()
#THe story after the Minotaur instigates the fight with the Guardian     
def story2():
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    print("The monstrous Minataur lays motionless on the ground its corpse still demanding great attention\n")
    time.sleep(2)
    print("You just stand there for a moment absolutley stunned.\n")
    time.sleep(2)
    print("Sweat pours profusley from your brow, your muscles stiff from the battle.\n")
    time.sleep(2)
    print("You drop to one knee to regain your breath, this battle was tough as the Minataurs flesh was hard to pierce for your enhanced hands.\n")
    time.sleep(2)
    print("You camp for 15 minutes than move past the corpse to exit the stadium.\n")
    time.sleep(2)
    print("You exit the stadium and find yourself in a hall with statues acting as pillar along the sides of the hall\n")
    time.sleep(2)
    print("A large metalic figure stands before you, cloaked in shadow\n")
    time.sleep(2)
    print("Then a red light awakens from the eyes of this figure.\n")
    time.sleep(2)
    print("'Have you come to slay my master little Jotaro'\n")
    time.sleep(2)
    print("You recognize that voice, devoid of feelings or compassion\n")
    time.sleep(2)
    print("Its the voice of DIO's most loyal minion and the strongest\n")
    time.sleep(2)
    print("He has slautered entire villages at DIO's command.\n")
    time.sleep(2)
    print("Nicknamed as DIO's guardian, just mentioning his name strikes fear in the hearts of man.\n")
    time.sleep(2)
    print("VANNILA ICE\n")
    time.sleep(2)
    print("The torches along the wall ignite and reveal Vanilla Ice's form.\n")
    time.sleep(2)
    print("A enchanted suit of obsidian armor towering above you.\n")
    time.sleep(2)
    print("He wields the demon blade CREAM, a blade which has conquered countless battlefields.\n")
    time.sleep(2)
    print("'Now come little Jotaro show me how much you have grown since our last battle'\n")
    time.sleep(2)
    print("Not one to keep people waiting you let out a battlecry and charge the guardian\n")
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    Guardian_Battle()

#Story after beating the guardian and instigates the final battle
def story3():
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    print("Vanilla Ice, the fearsome and legendary guardian of DIO, has been slain.\n")
    time.sleep(2)
    print("The once enchanted armor that was his vessle lays beneath your feet cold and powerless.\n")
    time.sleep(2)
    print("His soul swirls around you as if resisting you.\n")
    time.sleep(2)
    print("Even in death he remains extremley loyal to DIO.\n")
    time.sleep(2)
    print("But even his loyalty can not prevent his soul from being absorbed.\n")
    time.sleep(2)
    print("You feel his power surge within you and your wounds start to fade.\n")
    time.sleep(2)
    print("After the power surge subsists you feel oddly refreshed.\n")
    time.sleep(2)
    print("This must be a special attribute of his soul.\n")
    time.sleep(2)
    print("Now that your healed theres no need to wait to fight DIO\n")
    time.sleep(2)
    print("You push into the throne room to find DIO sitting on the throne.\n")
    time.sleep(2)
    print("'Oh if it isn't little Jotaro, Im quite surprised you managed to defeat Vanilla Ice but that just means you have grown.\n")
    time.sleep(2)
    print("'Ive come for you DIO.' you move towards him\n")
    time.sleep(2)
    print("'Oh? Your approaching me.'\n")
    time.sleep(2)
    print("'I can't beat the crap out of you without coming closer.'\n")
    time.sleep(2)
    print("'Oh really? Now I am quite intriqued.'\n")
    time.sleep(2)
    print("He leaves the throne and walks down to meet you.")
    time.sleep(2)
    print("Then you start sprinting towards each other at top speed.\n")
    time.sleep(2)
    print("You clash in the middle and a legendary battle begins\n")
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    DIO_Battle()
    
#Is the ending of the game and ends the game
def ending():
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    print("Finally after all this time you have finally beat him.\n")
    time.sleep(2)
    print("You spent all those years training and slaying monsters for this moment.\n")
    time.sleep(2)
    print("As his shadow enters your body you feel fulfilled.\n")
    time.sleep(2)
    print("Now the world can rest easy knowing that DIO shall no longer threaten mankind.\n")
    time.sleep(2)
    print("DIO's soul seems to have the same properties as Vanilla Ice's because after absorbing it you feel refreshed.\n")
    time.sleep(2)
    print("You exit the throne backtracking to the entrance of the palace.\n")
    time.sleep(2)
    print("As you walk back seeing all of the previous battles, it all feels worth it.\n")
    time.sleep(2)
    print("The blood, sweat, and pain all feels like nothing in comparison to this feeling of accomplishment.\n")
    time.sleep(2)
    print("Now you can return to the village and relax with your mother and sister.\n")
    time.sleep(2)
    print("So our hero returns to his village, and relaxs never again having to worry about DIO.\n")
    time.sleep(3)
    print("Or so he thought.")
    print("______________________________________________________________________________________________________________________________________________________________________\n")
    return False
# Call main() to start the program!
main()
