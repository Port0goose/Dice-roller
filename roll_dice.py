import random

def roll_dice(sides, rolls):
    results = []
    
    for _ in range(rolls):
        
        dice = random.randint(1, sides)
        results.append(dice)
        
    return results