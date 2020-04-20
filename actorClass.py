### 4-19-20 ###
###Combat Estimator 2nd edition###
###Actor Class###
###Made By Substantiative###

# this class defines an actor object (pc or npc) with certain attributes and
# and actions that they can take.
###
### 4/14/20 VERSION GOALS ###
# make an actor object that can roll to hit, determine damage dealt, and
# change its own hp
# TODO later:
#   incorporate different attacks (e.x. 2x 1d4 claw, 1x1d12 bite)
#   incorporate status effects (stunned, slowed, etc)           
import random
import dBag

class Actor:
    ###AVAILABLE METHODS###
    # changeHp(x) x = int, changes hp of actor
    # attack(target) target= another actor: returns an int indicating type of hit
    def __init__(self, ident,side, hd, maxHp, thac0, ac, hdMod, atkMod, dmgMod, initMod, \
                 dmgRng, atkPerRnd):
    # ident: name <str>
    # side: pc or npc <str? or 1/0 int?>
    # hd: Hit Dice- tuple of ints, (p,q) pDq
    # currentHp: int
    # thac0: chance To Hit Armor Class 0 (I know I know) <int, 0<=thac0<=20>
    # ac: Armor Class <int, -10<=ac<=10>
    # hdMod: modifier to hit dice rolls <int, -k<=atkMod<= 
    # atkMod: modifiers to attack rolls <int, -k<=atkMod<=k>
    # dmgMod: modifiers to damage rolls <int, -k<=dmgMod<=k>
    # initMod: modifier to initiatve roll <int, -k<=dmgMod<=k>
    # dmgRange: the attacks damage range, expressed as xDy (dice) <tuple (x, y)>
    # atkPerRound: expressed as a tuple (u,v) u attacks every v rounds
        self.ident = ident
        self.side = side
        self.hd = hd
        self.thac0 = thac0
        self.ac = ac
        self.hdMod = hdMod
        self.atkMod = atkMod
        self.dmgMod = dmgMod
        self.initMod = initMod
        self.dmgRng = dmgRng
        self.atkPerRnd = atkPerRnd
        self.maxHp = 69
        self.currentHp = self.maxHp
        
    def changeHp(self, incoming):
        #this alters the hp of the actor
        self.currentHp = self.currentHp - incoming
        
    def setHp(self):
        #todo later: reroll 1's
        baseHp = 0
        for x in range(0, self.hd[0]):
            baseHp += random.randint(1, self.hd[1]) + self.hdMod
        self.maxHp = baseHp

    def attack(self, target):
        #Checks to see if the actor hits a target
        #legit targets are other actor objects.
        #returns -1 if critical miss
        #         0 if miss
        #         1 if hit
        #         2 if critical hit
        atkRoll = dBag.d20(1,0)#rolls a 1d20
        ac = target.ac
        thac0 = self.thac0
        if (atkRoll == 1): #if critical miss, return -1
            return -1
        if (atkRoll == 20): #if critical hit, return 2
            return 2
        if ((atkRoll + self.atkMod) < (thac0 - ac)): #if miss, return 0
            return 0
        if ((atkRoll + self.atkMod) > (thac0 - ac)): #if hit, return 1
            return 1
        else: #I fucked up my code
            return 69

    def dmgCalc(self):
        #rolls for damage, adds modifiers
        #returns an int representing damage dealt by the actor
        numberRolled = self.dmgRng[0] #number of dice rolled
        diceSides = self.dmgRng[1] #number of sides of the damage dice
        modifier = self.dmgMod
        baseDmg = 0
        for i in range(0, numberRolled):
            baseDmg += (random.randint(1, diceSides) + modifier)
        return baseDmg
    
        
        


        
