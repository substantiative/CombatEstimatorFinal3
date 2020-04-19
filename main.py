### 4-19-20 ###
###Combat Estimator 2nd edition###
###Made By Substantiative###

# this is going to be the main program. its first order of business is to
# take json files as inputs, parse them, and then create actors using the
# Actor class. second order of business is simulating rounds, calling methods
# from the Actor class, and recording information from simulations.

#import json
import actorClass
import random
import dbag

### TODO NEXT: HAVE ACTORS BE READ FROM A JSON TO BE LOADED ###
### THE ACTORS WILL BE HARDCODED FIRST TO TEST ACTOR CLASS FUNCTIONALITY ###
### AND ROUND IMPLEMENTATION ###
#actor1 = str
#actor2 = str
#userInput1 = input('type the exact file name of the already created PC json: ')
#userInput2 = input('type the exact file name of the already created NPC json: ')
###


def rollInit(pc, npc):
    #this rolls initiative and determines who goes first for combat
    #pc and npc are actor objects
    #returns str pc if pc goes first, string npc if npc goes first
    #todo later: handle equal rolls better, right now a tie goes in favor
    #of the pc
    rollPc = random.randrange(1,10)
    rollNpc = random.randrange(1,10)
    ### VVVVVVVV IS IT pc.initMod OR pc.initmod() ###
    # VVVV if NPC wins initaitve roll
    if ((rollPc + pc.initMod) > (rollNpc + npc.initMod)): 
        result = 'npc'
        return result
    #VVVV if PC wins initiarive roll
    if ((rollPc + pc.initMod) <= (rollNpc + npc.initMod)):
        result = 'pc'
        return result
    

def combatRound(pc, npc, initWin):
    #this defines what happens in a round
    #pc, npc are actor object, initWin is str == 'pc' or 'npc')    
    if (initWin =='pc'):
        pcHitRoll = pc.attack(npc)
        if (pcHitRoll == 0): #normal miss
            npc.changeHp(0)
        if (pcHitRoll == 1): #normal hit
            dmg = pc.dmgCalc()
            npc.changeHp(dmg)
        if (pcHitRoll == 2): #critical hit
            dmg = (2 * pc.dmgCalc())
            npc.changeHp(dmg)
        if (pcHitRoll == -1): #critical miss
            #ToDo: figure out how to account for losing an attack in a round
            dmg = 0
            pc.changeHp(dmg)
        npcHitRoll = npc.attack(pc)
        if (npcHitRoll == 0): #normal miss
            return 0
        if (npcHitRoll == 1): #normal hit
            dmg = npc.dmgCalc()
            pc.changeHp(dmg)
        if (npcHitRoll == 2): #critical hit
            dmg = (2 * pc.dmgCalc())
            pc.changeHp(dmg)
        if (npcHitRoll == -1): #critical miss
            #ToDo: figure out how to account for losing an attack in a round
            dmg = 0
            pc.changeHp(dmg)
       
        
    if (initWin == 'npc'):
        npcHitRoll = npc.attack(pc)
        if (npcHitRoll == 0): #normal miss
            pc.changeHp(0)
        if (npcHitRoll == 1): #normal hit
            dmg = pc.dmgCalc()
            pc.changeHp(dmg)
        if (npcHitRoll == 2): #critical hit
            dmg = (2 * pc.dmgCalc())
            npc.changeHp(dmg)
        if (npcHitRoll == -1): #critical miss
            #ToDo: figure out how to account for losing an attack in a round
            dmg = 0
            pc.changeHp(dmg)
        pcHitRoll = npc.attack(pc)
        if (npcHitRoll == 0): #normal miss
            npc.changHp(0)
        if (npcHitRoll == 1): #normal hit
            dmg = npc.dmgCalc()
            pc.changeHp(dmg)
        if (npcHitRoll == 2): #critical hit
            dmg = (2 * pc.dmgCalc())
            pc.changeHp(dmg)
        if (npcHitRoll == -1): #critical miss
            #ToDo: figure out how to account for losing an attack in a round
            dmg = 0
            pc.changeHp(dmg)
       
            
def statusUpdate(pc, npc):
    #pc and npc are actor objects
    pcHp = pc.currentHp
    npcHp = npc.currentHp
    print('Player Character HP: ', pcHp)
    print('NPC HP: ',  npcHp)
    
gobbo = actorClass.Actor('gobbo', 'npc', (2, 4), 1, 19, 8, 0, 0, 1, 3, (1,6), (1,1))
# ^^^ goblin, 2d4 hitpoints, 19 thaco, 8 AC, +0 to hp rolls +0 to attack rolls
# +1 to damage rolls, +3 to initiative roll, 1d6 damage roll, 1 atk per round 
player = actorClass.Actor('drizzit', 'pc', (6, 8), 1, 17, 3, 3, 3, 3, 0, (1, 8), (2,1))
#^^^ our hero, 6d8 hit dice, 17 thaco, 3 ac, +3 to hp roll, +3 to attack,
# +3 to damage, +0 to initiative, 1d8 damage (sweet scimitars), 2 atk per rnd

gobbo.setHp()
player.setHp()
initWin = rollInit(player, gobbo)

while (player.currentHp > 0 and gobbo.currentHp >0):
    #while no one is dead
    combatRound(player, gobbo, initWin)
    x = statusUpdate(player, gobbo)
    print(statusUpdate)
if (player.currentHp <= 0):
    print('Drizzit Loses!')
if (gobbo.currentHp <= 0):
    print('gobbo Loses!')
    
    
            
            


    


