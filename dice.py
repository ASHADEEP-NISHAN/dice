import random as r

def biased_dice():
    a= [1, 2, 3, 4, 5, 6]
    p = [0.1, 0.1, 0.1, 0.1, 0.1, 0.4]

    result = r.choices(a, p)[0]
    return result
y=biased_dice()
print(y)


