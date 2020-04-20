### 4-19-20 ###
###Combat Estimator 2nd edition###
###My Dbag###

import random

    
def d4(number = 1, modifier = 0):
    return sum([random.randint(1, 4) + modifier for i in range(number)])

    
def d6(number = 1, modifier = 0):
    return sum([random.randint(1, 6) + modifier for i in range(number)])

    
def d8(number = 1, modifier = 0):
    return sum([random.randint(1, 8) + modifier for i in range(number)])

    
def d10(number = 1, modifier = 0):
    return sum([random.randint(1, 10) + modifier for i in range(number)])

    
def d12(number = 1, modifier = 0):
    return sum([random.randint(1, 12) + modifier for i in range(number)])

    
def d20(number = 1, modifier = 0):
    return sum([random.randint(1, 20) + modifier for i in range(number)])

    

def d100(number = 1, modifier = 0):
    return sum([random.randint(1, 100) + modifier for i in range(number)])


