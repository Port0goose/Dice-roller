import random

def roll_dice(sides, rolls, advantage=False, disadvantage=False):
    
    
    results = []
    
    for _ in range(rolls):
        roll_info = {}
        
        if advantage:
            roll1 = random.randint(1, sides)
            roll2 = random.randint(1, sides)
            result = max(roll1, roll2)
            roll_info["Roll 1"] = roll1
            roll_info["Roll 2"] = roll2
        elif disadvantage:
            roll1 = random.randint(1, sides)
            roll2 = random.randint(1, sides)
            result = min(roll1, roll2)
            roll_info["Roll 1"] = roll1
            roll_info["Roll 2"] = roll2
        else:
            result = random.randint(1, sides)
        
        roll_info["Result"] = result
        
        results.append(roll_info)
        
    return results
