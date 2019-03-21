#aleks calderon
#3.20.2019
#this is the final game ICEBREAKER

#aleks calderon
#3.20.2019
#this is chapter 1. 

import random
def blacksmith():

    global npcName
    npcName = "Blacksmith"
    print(npcName,": Hello, how are you today? Do you need anything?")
#Asks GP if she knows about the castle    
    print("Press Y to ask the Blacksmith about the castle.")
    if input() == 'Y':
        print(npcName,":] The castle is north of here. You'll know you're going the right way the colder it gets. Cross a bridge and head west from there.")
#Asks user to complete task
        print(npcName,":] I could use some help. Do you have the time?")
        print("Press Y to help the Blacksmith.")
        if input() == 'Y':
            print(npcName,":] Thanks. There's a shovel over there. Start shoveling some coal to keep the fire going")
        #shovel coal for blacksmith
            shovelAction = 0
            shovel = input("The Blacksmith points to a shovel sticking out of a pile of coal. Type SHOVEL to begin. ")
            if shovel == 'SHOVEL':
                while shovelAction != 10:
                        shovelAction = random.randrange(1,11)
                if shovelAction >= 8:
                    print("You were able to shovel the coal into the fire quick and easily! Nice job.")
                    shovelAction +=10

                else:
                    shovelStruggle = input("Rough start. You can do it! Continue to SHOVEL.")
                    #while shovelAction != 10:
                    if shovelStruggle == 'SHOVEL':
                        shovelAttack = random.randrange(1,11)
                        if shovelActioN <= 6:
                            print("You were able to shovel the coal! Nice job.")
                            
            print("The Blacksmith thanks you for your hard work.")
            print(npcName,":] Thanks for your help! Here is something for your troubles.")
            print("The Blacksmith hands you a sword. You thank him and hold onto it.")
            print("You thank him once more before you start to head North as he suggested. Determination courses through you as you say, 'I'm on my way.'")
            #end of chapter 1
#want to loop the shovel module in order to have it add up to 10
        else:
            print(npcName, " Safe travels.")
    else:
        print(npcName,":] Have a good day!")

def grandma():

    global npcName

    npcName = "Grandma Piper"
    print(npcName,": Hi sweetie, how are you today? Do you need anything?")
#Asks GP if she knows about the castle    
    print("Press Y to ask Grandma Piper about the castle.")
    if input() == 'Y' or 'y':
        print(npcName,":] I haven't ever traveled that far, but I know there is a bridge you need to cross before you get there. I hope that helps.")
#Asks user to complete task
        print(npcName,":] Would you help me with something before you go on your adventure?")
        print("Press Y to help Grandma Piper. Press n to decline.")
        if input() == 'Y':
            print(npcName,":] Thank you dear! I need help chopping some wood.")
        #chopping wood for grandma
            chopAction = 0
            chop = input("Grandma Piper motions to the pile of wood waiting with an axe. Type chop to begin choping the wood.")
            if chop == 'CHOP':
                while chopAction != 10:
                        chopAction = random.randrange(1,11)
                if chopAction >= 8:
                    print("You were able to chop through the wood quick and easily! Nice job.")
                    chopAction +=10

                else:
                    chopStruggle = input("Rough start. You can do it! Continue to CHOP.")
                    while chopAction != 10:
                        if chopStruggle == 'CHOP':
                            chopAttack = random.randrange(1,11)
                            if chopActioN <= 6:
                                print("You were able to chop through the wood! Nice job.")
#want to loop the CHOP module in order to have it add up to 10
                                
            print("Grandma thanks you for your hard work.")
            print(npcName,":] Thank you dear! Here is something for your troubles.")
            print("Grandma hands you health potions. You thank her and put them into your bag.")
            print(npcName,":] You should go see the Blacksmith! He may be able to help you more, dear.")
            print("You nod and thank her once more before you head over to see the Blacksmith.")
            blacksmith()
                                
                    
#wild loop. while x is less than 10, continue to ask prompt about chop
#return health potions.
        else:
            print(npcName,":] It's okay, sweetie. You be safe now and good luck!")
    #return healthpotions            
#this is for the interaction between grandma piper and user


#chapter 1
chpt1 = input("Please type START to begin.")

print("FLASHBACK")
print("Eerie silence fills the thick air of your town area. Everyone’s eyes cascade down to the pebbles on the ground as King Iceberg emerges from his carriage. The ground beneath his feet freeze with each smooth glide. ")
print("The crunch rings loud in your ears as they inch closer and closer, your heart stopping as they come to a halt.")
print("A frosty mist hovers around you as you cling to your sister tightly, shaking in fear as his eyes scan the both of you. “This one,” he says, your heart dropping as you believe you are the one he chooses.")
print("Suddenly, your sister is ripped from your grasp. You look up in shock as she struggles against the frozen guards.")
choice1 = input("What do you do? Type save or freeze.")
#player gets slightly different outcome but ultimate same result
if choice1 == 'SAVE':
        print("Your fists ball up as you glare deeply towards the King. Before you can take a step, your father puts his hand on your shoulder. “Let me handle this.” He says to you; you obey your father’s wishes but your glare still remains.")
        print("'You let her go!' he demands, the King turning his head towards your father.")
        print("And who do you think you’re talking to?” he says, squinting as your father balls up his fists.")
        print("“Give me back my daughter!” your father hollers. The final straw for him is when King Iceberg laughs in his face. Your father cocks his arm back, but King Iceberg is faster. With a touch of his fingertip to your father’s forehead, he freezes into a block of ice.")
        print("“Is there anyone else who wishes to defy me?” He announces, the silence ensues briefly once more. With a content nod, King Iceberg climbs into his carriage and disappears from sight.")
else:
        print("Your body hits you with shock as you stare, vision blurred by the tears in your eyes. Your father steps up to King Iceberg, beginning to yell for (sisters name). “You let her go!” he demands, the King turning his head towards your father.")
        print("'You let her go!' he demands, the King turning his head towards your father.")
        print("And who do you think you’re talking to?” he says, squinting as your father balls up his fists.")
        print("“Give me back my daughter!” your father hollers. The final straw for him is when King Iceberg laughs in his face. Your father cocks his arm back, but King Iceberg is faster. With a touch of his fingertip to your father’s forehead, he freezes into a block of ice.")
        print("“Is there anyone else who wishes to defy me?” He announces, the silence ensues briefly once more. With a content nod, King Iceberg climbs into his carriage and disappears from sight.")
print("PRESENT DAY")
print("Today marks one year since your sister was taken from your arms, and that your father was frozen into ice. You’ve been dreading this day for months, and it makes you sick to think that you couldn’t do anything about it.")
print("Your mother insists on keeping yourself busy, giving you a few chores to do instead of sitting in your own self-pity.")
print("“Sweep the floors for me, sweetheart. It’ll get your mind off of things.” She says as she motions to the broom. “I’m going to the market and will be back later on.")
print("You grab the old broom and begin to sweep up the dirt from days before. No matter much you try to focus on what you are doing, the memory keeps replaying in your head.")
#SWEEPING TRANSITION. Player finds out about their powers
choice2 = input("Type SWEEP to begin.")
if choice2 == 'SWEEP':
    print("You could’ve jumped in to help your father.")
else:
    print("Type SWEEP.")
choice3 = input("Continue.")
if choice3 == 'SWEEP':
    print("You could've gotten other townspeople to help support him.")
else:
    print("Type SWEEP.")
choice4 = input("Continue.")
if choice4 == 'SWEEP':
    print("You could’ve tried to save her.")
else:
    print("Type SWEEP .")
choice5 = input("Last time.")
if choice5 == 'SWEEP':
    print("But you didn't.")
else:
    print("Type SWEEP.")
      
print("The thought strikes you in your core, a scowl on your face as you grip the broom tighter. Your anger bubbles in your mind, every sweep against the old wood getting louder and louder in your mind. King Iceberg’s condescending laugh echoes, and all you want to do is burn his whole kingdom down.")
print("Until suddenly the bristles on your broom burst into flames!")
choice6 = input("Put out the fire! Type extinguish to put out.")
while choice6 != "EXTINGUISH":
    if choice6 == "EXTINGUISH":
         print("You quickly extinguish the fire by stomping it out. The blackened bristles fill the air with a pungent odor.")
    else:
        print("Put out the fire!")
        choice6 = input("Put out the fire! Type extinguish to put out.")
print("You come to the realization, you’ve produced fire with your mind! You are suddenly filled with determination, knowing that if you could use this new found power that your sister can come home!")
print("You write your mother a quick note, saying that you are going to go save your sister and avenge your father. You love her and will return home soon. You rush to grab your cloak and rush out the door. You come to the realization that you have no idea how to get to the castle. Maybe you should ask a local.")
print("You think for a moment as you walk outside. You decide to go see Grandma Piper first.")
grandma()

#END OF CHAPTER 1

#aleks calderon
#3.13.2019
#this is chapter 2. user will fight two ice wolves using fire magic

import random

print("CHAPTER 2")
print("A few hours into your hike up the north hillside, you start to realize that you do not have much of a plan. You know that your end goal is to save your sister, but because you were so excited about your newfound powers, that you forgot to figure out how you planned to defeat King Iceberg.")
print("You get lost in your thoughts. So much so, that you failed to notice that the bright summer leaves are fading into a mixture of deep reds and oranges as you march forward.")
print("Soon, the leaves start to fall to the floor and a cool breeze slaps you in the face. As you look around to take in your surroundings, you can see that snow is starting to fall from the sky. You must be going the right way.")
print("You search through your bag, finding a thick cloak you packed up before you left and pull it over your shoulders. You hold each side together as you continue up the hill.")
print("The comfortable silence disappears after your next few steps, the crunch of snow beneath your feet isn’t the only thing you hear anymore.")
print("A deep growl comes from either side of you, two wolves walk out from behind the shadows of the trees. Their teeth are made of sharp icicles, their fur replaced with pure white ice as they begin to circle you.")
#fight sequence
action = input("Do you want ATTACK or FLEE?")
#actionChoice = ["Hit", "Miss"]
#actionChoice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def fightWolves():
    
    global fireCounter
    fireballCounter = 0
    global weaponCounter
    weaponCounter = 0
    global hitCounter
    hitCounter = 0

    if action == "ATTACK":
        #COUNTERS keep track of hit points. which ever counter reaches first determines outcome.
        while fireballCounter != 3 and weaponCounter != 5 and hitCounter != 10:
            attackChoice = input("What do you want to hit them with? (WEAPON or FIRE).")
#fire attack
            if attackChoice == 'FIRE':
#                for fireballAttack in range(10):
                fireballAttack = random.randrange(1, 10)
                if fireballAttack < 6:
                    print("Fireballs fly from your palms and you hit the wolf for 4 damage!")
                    fireballCounter += 1
                else:
                    print("You missed! The wolf jumps forward and bites you. You take 3 damage.")
                    hitCounter += 1
                if fireballCounter == 3:
                    print("The wolves are dead! You discover new power of FIREBALL.")
                    break    
            else:
#                while fireballCounter != 3 and weaponCounter != 5 and hitCounter != 10:
#do not need second while statement
#weapon attack
                if attackChoice == 'WEAPON':
#                        for weaponAttack in range(10):
                    weaponAttack = random.randrange(1, 10)
                    #   has program pick out a random number. if the number is less than 5 then the user hits
                if weaponAttack < 5:
                    print("You swing your sword and you hit the wolf for 4 damage!")
                    #
                    weaponCounter += 1
                else:
                    print("You missed! The wolf jumps forward and bites you. You take 3 damage.")
                    hitCounter += 1
                if weaponCounter == 5:
                    print("The wolves are dead! You discover new power of FIREBALL.")
                    break
                    
        if hitCounter == 10:
            perish = input("You perished. Would you like to try again? Yes or No.")
            if perish == 'YES':
                fightWolves()
            else:
                raise SystemExit
        if hitCounter >= 8: 
            print("Your HP is currently ",hitCounter," . Would you like to use one of your health potions? YES or NO.")
            if input() == 'YES':
                hitCounter = 0
                print("You are now full HP.")
            else:
                print("You did not use your health potions.")
    else:
        raise SystemExit

fightWolves()

print("You look at your hands in awe. You begin to wonder what else you could do. You create one small fire ball to keep you warm as you move forward to continue on your quest to save your sister.")

#GO INTO CHAPTER 3
##print("Your HP is currently ",hitCounter," . Would you like to use one of your health potions? Yes or No.")
##if input() == 'use':
##    print("You are now full HP.")
##else:
##    print("You did not use your health potions.")

#END OF CHAPTER 2

#aleks calderon
#3.13.2019
#this is chapter 3. user will fight an ice monster under the bridge they stand on
#IF MODULE DOESN'T SHOW UP YOU ARE NOT CALLING IT I.E. def bridgeMonster needs to be called like this --> bridgeMonster()
import random

print("You continue our your way, your plan slowly beginning to come together. The fireballs you produced from your hands could be useful when you ambush the castle. You create one small flame in the palm of your hand to keep yourself warm as you continue forward.")
print("You arrive to an old rickety bridge that’s held together with old planks of wood and some rope. A deep sigh escapes your lips as you approach. Peering over the edge, you see nothing but fog that hides what ever has fallen down there before.")
cross = input("Do you want to cross? YES or NO.")

def bridgeMonster():
    
    global fireballCounter
    fireballCounter = 0
    global firebreathCounter
    firebreathCounter = 0
    global weaponCounter
    weaponCounter = 0
    global hitCounter
    hitCounter = 0
    if monsterAttack == "ATTACK":
        while firebreathCounter != 2 and fireballCounter != 4 and weaponCounter != 8 and hitCounter != 11:
            attackChoice = input("What do you want to hit them with? Choose: FIREBALL, FIREBREATH, or WEAPON.")
            if attackChoice == 'FIREBALL':
        #        for fireballAttack in range(10):
                fireballAttack = random.randrange(1,10)
                if fireballAttack >= 4:
                    print("A fireball flies from your palms and you hit the monster's tentacles for 4 damage!")
                    fireballCounter += 1
                else:
                    print("You missed! The monster's tentacle hits hard on your left side. You take 5 damage.")
                    hitCounter += 2
      #              break
          #new ability FIREBREATH          
            elif attackChoice == 'FIREBREATH':
     #           for firebreathAttack in range(10):
                firebreathAttack = random.randrange(1,10)
                if firebreathAttack >= 8:
                    print("You feel a deep rumble in your throat and open your mouth as a stream of fire rushes out and spreads across the tentacles of the monster! You hit for 10 damage!")
                    firebreathCounter += 1
                else:
                    bridgeFall = int(input("You missed! The monster hits you from behind and grabs your leg. It tugs you towards the edge of the rope. Save yourself! Pick a number 1 to 6."))
      #              for bridgeFall in range(10):
      #                  bridgeFall = random.randrange(1,10)
      #if you do not hit FIREBREATH, you run the risk of being thrown off the bridge. Player has to guess the number 3 or higher.
                    if bridgeFall >= 3:
                        print("You kick the monster's tentacle as hard as you can and it lets go. You rush to get back up.")
                    else:
                        print("The monster gives one pull and throws you off the bridge!")
                        hitCounter += 11
           #             break
            else:
         #       while fireballCounter != 3 or weaponCounter != 5 or hitCounter != 11:
                if attackChoice == 'WEAPON':
         #           for weaponAttack in range(10):
                    weaponAttack = random.randrange(1,10)
                    if weaponAttack >= 3:
                        print("You slash your sword downwards onto the monster's tentacle. You hit for 3 damage!")
                        weaponCounter += 1
                    else:
                        print("You missed! The tentacle strikes and hits you for 5 damage!")
                        hitCounter += 2
          #              break
                                    
            if hitCounter == 11:
                perish = input("You perished. Would you like to try again? Yes or No.")
                if perish == 'YES':
                    bridgeMonster()
                else:
                    raise SystemExit
            if hitCounter >= 8: 
                print("Your HP is currently ",hitCounter," . Would you like to use one of your health potions? Yes or No.")
                if input() == 'YES':
                    hitCounter = 0
                    print("You are now full HP.")
                else:
                    print("You did not use your health potions.")                      
#fight sequence     
    else:
        print("There’s no where but to go but back home. You don’t want to do that.")
        cross = input("Do you want to cross? Yes or No.") 
#fight sequence
      #user discovers they can create flame bursts around them


if cross == 'YES':
    print("Your heaving breath suddenly comes to a halt as you see what looks like a tentacle slither it’s way onto the rope of the bridge in front of you. “Oh no..” you mutter.")
    monsterAttack =input("A loud roar erupts from beneath you, eight other tentacles grab onto the bridge and begin to come towards you. What do you do? ATTACK or RUN.")
    bridgeMonster()
else:
    raise SystemExit




#ask same prompt about health potions
print("You rush off the bridge, the monster screeching as it falls back into the fog and silence washes over the air once more. You pant heavily, your heart racing fast as you begin to realize what you just accomplished. You look at your hands, wondering what else you are capable of.")
print("Once you gather your barings, you stand up and continue towards the castle.")

#END OF CHAPTER 3

#aleks calderon
#3.17.2019
#this is chapter 4

import random

def knightFight():
    global fireballCounter
    fireballCounter = 0
    global firebreathCounter
    firebreathCounter = 0
    global weaponCounter
    weaponCounter = 0
    global hitCounter
    hitCounter = 0
#if user failed twice, then they get thrown into a fight with the guards
    #if meltFail == 2:
    attackKnight = input("The lock shatters in your hands, the chains clank as they fall and the castle doors swing open. Three ice guards tower over you and draw their swords. What do you do? ATTACK or FLEE.")
    if attackKnight == 'ATTACK':
        #attackChoice = input("What do you want to hit them with? Choose: FIREBALL, FIREBREATH, WEAPON.")
#while loop keeps track of the counters. each counter takes whichever number hits the goal first.
        while firebreathCounter != 3 and fireballCounter != 6 and weaponCounter != 10 and hitCounter != 14:
            attackChoice = input("What do you want to hit them with? Choose: FIREBALL, FIREBREATH, WEAPON.")   
#fireball attack
            if attackChoice == 'FIREBALL':
                fireballAttack = random.randrange(1,10)
                if fireballAttack >= 4:
                    print("A fireball flies from your palms and you hit the guards for 4 damage!")
                    fireballCounter += 1
                else:
                    print("You missed! An ice guard slashes their sword at you and hits you for 3 damage.")
                    hitCounter += 2
                if fireballCounter == 6:
                    print("The guards all melt instantly! You continue into the castle.")
                    
#firebreath attack. hits really hard, but is really hard to hit.
            elif attackChoice == 'FIREBREATH':
                firebreathAttack = random.randrange(1,10)
                if firebreathAttack >= 6:
                    print("You feel a deep rumble in your throat and open your mouth as a stream of fire rushes out and hits all the ice guards! You hit them for 10 damage.")
                    firebreathCounter += 1

#if you fail, you get hit for half your hitCounter points
                else:
                    print("One guard rushes towards you and slashes their sword, leaving a big gash in your arm! You take 9 damage.")
                    hitCounter += 7
                if firebreathCounter == 3:
                    print("The guards all melt instantly! You continue into the castle.")
            else:

#weapon attack
                if attackChoice == 'WEAPON':
                    weaponAttack = random.randrange(1,10)
                    if weaponAttack >= 3:
                        print("You slash your sword towards the guards. You hit them for 2 damage!")
                        weaponCounter += 1
                    else:
                        print("You missed! The guards swing their swords at you and hit you for 5 damage.")
                        hitCounter += 3
                if weaponAttack == 10:
                    print("The guards shatter before your eyes! You continue into the castle.")

#user dies
            if hitCounter == 14:
                perish = input("You perished. Would you like to try again? YES or NO.")
                if perish == 'YES':
                    knightFight()
                else:
                    raise SystemExit

#if user's hitcounter is 10 or higher they ask if they want to heal.
            if hitCounter >= 7:
                print("You have been hit",hitCounter,". Would you like to use one of your health potions? YES or NO.")
                if input() == 'YES':
                    hitCounter = 0
                    print("You are now full HP.")
                else:
                    print("You did not use your health potions.") 

def meltLOCK():
    global meltLock
    meltLock = 0
    global meltFail
    meltFail = 0
    if lock == 'MELT':
        while meltLock != 2 or meltFail !=2:
            #program asks for number. if number is 3 then they melt it. if the number is different thenthey don't melt it
            meltingLock = int(input("Pick a number 1 to 5."))
            if meltingLock == 3:
                print("You notice that the first layer of frost disappears. A clear glossy ice remains on the lock. Keep going.")
                meltLock += 1
                meltingLock = int(input("Pick a number 1 to 5."))
#if user wins two times then they can pass through without guard fight
                if meltLock == 2:
                    print("You melted the lock and it clicks open. You tug it out of the chains and they fall to the cold floor. The door creaks open and you head inside.")
                    break
            else:
                print("The lock does not change. Try again!")
                meltFail += 1
                meltingLock = int(input("Pick a number 1 to 5."))
#if user fails 2 times then they get into a fight with three ice guards.
                if meltFail == 2:
                    knightFight()
    
        
print("Your heart pounds hard in your chest as you finally see the ice castle. Your chance is right in front of you and now is the time to bring your sister back home.")
print("The ice bridge is a long and silent walk. Your hands heat up as you think about his laugh, picturing your sister calling out for help. “I’m on my way,” you say quietly as you finally approach the entrance to the castle.")
print("Oddly, there are no guards in front of the castle. It must be time for the shift change. You have fifteen minutes to find a way inside.")
lock = input("You rush to the front, which is chained with a large, frozen padlock. You raise your hand to inspect the lock which has a thick frost. What do you want to do? MELT or FIND ANOTHER WAY.")
if lock == 'MELT':
    meltLOCK()
else:
    knightFight()
#here the user would have to pick random numbers. these would determine if they melt the padlock
  #if they don't, then they fight three ice guards.
  #if they do, they can go straight to the castle.
#END OF CHAPTER 4

#aleks calderon
#3.17.2019
#this is chapter 5

import random

def kingFight():
    
    global fireballCounter
    fireballCounter = 0
    global firebreathCounter
    firebreathCounter = 0
    global weaponCounter
    weaponCounter = 0
    global hitCounter
    hitCounter = 0
    if kingAttack == "FIGHT":
        while firebreathCounter != 4 and fireballCounter != 6 and weaponCounter != 10 and hitCounter != 16:
            attackChoice = input("What do you want to hit them with? Choose: FIREBALL, FIREBREATH, or WEAPON.")
            if attackChoice == 'FIREBALL':
                fireballAttack = random.randrange(1,10)
                if fireballAttack >= 4:
                    print("A fireball flies from your palms and you hit the King for 4 damage!")
                    fireballCounter += 1
                else:
                    print("You missed! The king sends an beam of ice from his hands. You take 5 damage.")
                    hitCounter += 2
                    
            elif attackChoice == 'FIREBREATH':
                firebreathAttack = random.randrange(1,10)
                if firebreathAttack >= 7:
                    print("You feel a deep rumble in your throat and open your mouth as a stream of fire rushes out and spreads across throne room! You hit the King for 10 damage!")
                    firebreathCounter += 1
                else:
                    freezeYou = int(input("You missed! The king tries to freeze you into a block of ice! Save yourself! Pick a number 1 to 6."))
                    if freezeYou >= 3:
                        print("You let out a burst of fire around you and melt the ice!")
                    else:
                        print("King Iceberg freezes you into a block of ice and paralyzes you. He breaks the ice and it shatters into your skin. You take 10 damage.")
                        hitCounter += 8
            else:
                if attackChoice == 'WEAPON':
 
                    weaponAttack = random.randrange(1,10)
                    if weaponAttack >= 3:
                        print("You slash your sword towards King Iceberg and slice his arm. You hit for 3 damage!")
                        weaponCounter += 1
                    else:
                        print("You missed! The king throws an icicile and it catches you in the arm. You take 5 damage.")
                        hitCounter += 2
                                    
            if hitCounter == 11:
                perish = input("You perished. Would you like to try again? Yes or No.")
                if perish == 'YES':
                    kingFight()
                else:
                    raise SystemExit
            if hitCounter >= 8: 
                print("You where hit ",hitCounter," times. Would you like to use one of your health potions? Yes or No.")
                if input() == 'YES':
                    hitCounter = 0
                    print("You are now full HP.")
                else:
                    print("You did not use your health potions.")                           


print("Once you get inside, the cold air seems even more intense. Your anger rises as you get closer and closer to the throne room. You get up to the double doors and push them with all your might.")
print("Your dramatic entrance catches the king’s attention immediately. He doesn’t seem to recognize you. “What’s your business here?” he demands as he matches your glare as you approach.")
asknicely = input("What do you do? Type ask or demand.")
#if user types as
if asknicely == 'ASK' or 'DEMAND':
    print("The king signature laugh echos throughout the thrown room. He looks over to  your terrified sister who is physically trembling out of fear. He wraps his arm around her shoulders and smirks knowingly.'She's mine now. Now get out of my sight.' he snaps at you.")
    kingAttack = input("What do you do? FIGHT or LEAVE.")
    if kingAttack == 'FIGHT':
        print("“I’m getting you out of here!” you say to your sister and a fireball flies out of your hands.")
        kingFight()
    else:
        freeze = input("He gets furious and stands. “I warned you,” he says dangerously and steps down from his throne.")
        kingFight()

print("King Iceberg's cries rumble the entire room as he begins to melt. He scrambles to try and save himself, but he turns into a puddle at your feet.")
print("Your sister rushes down the steps from the throne and hugs you tightly. 'I've missed you so mmuch! Thank you, I love you so much.' she cries as you squeezes tightly and hold her close.")
print("'I love you too,' you smile and look towards her. You wipe her tears. 'Let's head home,' you say as you take her hand and head out of the castle.")
print("You arrive back home and the townspeople cheer for you! They thank you over and over for your hard work to end King Iceberg's tyranny on the town.")
print("CONGRADULATIONS! YOU WIN!")
        
#END GAME

