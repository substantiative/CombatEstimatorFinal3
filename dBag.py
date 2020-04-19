### 4-19-20 ###
###Combat Estimator 2nd edition###
### Dice Bag Helper Class Code Name Dbag ###
###Made By Substantiative###


import random

class dbag:
    
    def d4(number, modifier):
        rollResult = 0
        for i in range(1, number):
            rollResult += (random.randint(1, 4) + modifier)
        return rollResult

    
    def d6(number, modifier):
        rollResult = 0
        for i in range(1, number):
            rollResult += (random.randint(1, 6) + modifier)
        return rollResult

    
    def d8(number, modifier):
        rollResult = 0
        for i in range(1, number):
            rollResult += (random.randint(1, 8) + modifier)
        return rollResult

    
    def d10(number, modifier):
        rollResult = 0
        for i in range(1, number):
            rollResult += (random.randint(1, 10) + modifier)
        return rollResult

    
    def d12(number, modifier):
        rollResult = 0
        for i in range(1, number):
            rollResult += (random.randint(1, 12) + modifier)
        return rollResult

    
    def d20(number, modifier):
        rollResult = 0
        for i in range(1, number):
            rollResult += (random.randint(1, 20) + modifier)
        return rollResult

    
    def d100(number, modifier):
        rollResult = 0
        for i in range(1, number):
            rollResult += (random.randint(1, 100) + modifier)
        return rollResult
