with open('input.txt') as f:
    content = f.readlines()

example = "dabAcCaCBAcCcaDA"

# Find matching pairs

# Remove recursively 

# after each recursive call, check if length still matches

def funcname(polymer):
    for (unit in polymer):
        if(unit == polymer[unit+1].upper()):
            polymer = polymer.replace(unit)