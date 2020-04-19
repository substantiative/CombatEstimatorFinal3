### 4-19-20 ###
###Combat Estimator 2nd edition###
### Currently Very Depreciated Json Creator###
###Made By Substantiative###

import json

def solicitInput():
# This solicits the user for information to define an actor. actors are things that have a name, can attack, have relevant statistics for combat calculations,
#  and has hit points.
# returns a list of the format [actorName, HP, AC, Thac0, atkMod,(x,y),dmgMod]
# actorName is a string, HP, AC, Thac0, atkMod, and dmgMod are integers
#(x,y) is dice roll for damage, xDy
### note: the modifiers here are the inherent ones. there can be other mods
### added later in different program parts

    actorName = str 
    Thac0 = int  #To Hit Armor Class Zero - integer from 0 to 20
    AC = int # Armor Class - integer from -10 to 10
    dmgRng = [] #this stores the number of dice and number of sides
    hdMod = int # modifiers to hit dice for hp calculation
    dmgMod = int # misc modifiers to weapon damage roll valid for all integers
    atkMod = int # misc modifiers to hit roll
    initMod = int #modifier to initiative
    ###TODO: make HP hit dice instead
    hd = [] # Hit Dice = (p, q) such that pDq determines hp
    atkPerRnd = [] #this ends up a tuple of (attacks, round) 
    team = {'npc', 'pc'}
    
    actorName = input("Please Enter actor ID. string: ")
    whoseSide = input("enter either npc or pc: ")
    Thac0 = int(input("Please Enter Thac0, 0<=Thac0<=20: "))
    AC = int(input("Please enter actors AC: -10<=AC<=10: "))
    atkMod = int(input("Please enter the total bonus modifier to attack: "))
    dmgMod = int(input("please enter the modifier to damage rolls: "))
    initMod = int(input("Please enter actors initative modifier: "))

    print("Please enter the base dice damage the actor does \
            in the format XdY where X is the number of Y sided dice")
    x = int(input("X: ")) #number of dice: integer, positive
    y = int(input("Y: ")) #number of sides of dice: integer, positive
    dmgRng.append(x)
    dmgRng.append(y)

    print("Please enter the number of attacks per round u attacks per v rounds:")
    u = int(input("u (attacks): "))
    v = int(input("per v (rounds): "))
    atkPerRnd.append(u)
    atkPerRnd.append(v)

    print("please enter the number, p, of q sided dice for hit dice: ")
    p = int(input("p: "))
    q = int(input("q: "))
    hd.append(p)
    hd.append(q)
    
    actorDeets = dict([('actorName', actorName), ('whichTeam', whoseSide),
                       ('hd' , hd), ('maxHp', maxHp), ('thac0', Thac0), \
                       ('ac', AC), ('hdMod', hdMod), ('atkMod',atkMod), \
                       ('dmgMod', dmgMod), ('initMod', initMod), \
                       ('dmgRng',dmgRng), ('atkPerRnd', atkPerRnd)])
    return actorDeets
#doneCheck = 0
#while (doneCheck == 0):
#    x = solicitInput()
#    fileName = x['actorName']
#    with open((fileName + '.json'), 'w') as json_file:
#        json.dump(x, json_file)
#    doneCheck = int(input("enter 0 to define more actors, 0 to exit: ")


x = solicitInput()
fileName = x['actorName']
with open((fileName + '.json'), 'w') as json_file:
    json.dump(x, json_file)
   
                    
                    

                       
                       
    
    
