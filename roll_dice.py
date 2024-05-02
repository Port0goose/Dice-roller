import random

def roll_dice(sides, rolls, advantage=False, disadvantage=False):
    results = []

    for _ in range(rolls):
        if advantage:
            roll1 = random.randint(1, sides)
            roll2 = random.randint(1, sides)
            result = max(roll1, roll2)
            results.append(result)
        elif disadvantage:
            roll1 = random.randint(1, sides)
            roll2 = random.randint(1, sides)
            result = min(roll1, roll2)
            results.append(result)
        else:
            result = random.randint(1, sides)
            results.append(result)

    return results
    
