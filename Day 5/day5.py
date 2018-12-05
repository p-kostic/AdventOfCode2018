with open('input.txt') as f:
    content = f.read()

example = "dabAcCaCBAcCcaDA"

# Part 1
def removeUnits(polymer):
    initLength = len(polymer)

    for unit in polymer:
        polymer = polymer.replace(unit.upper() + unit.lower(), '').replace(unit.lower() + unit.upper(), '')
    return initLength != len(polymer), polymer

# removeUnits until fixed point is reached
changed = False
while not changed: 
    changed, content = removeUnits(content)

print(content)
print(len(content))


# Part 2 
# Reread input data
with open('input.txt') as f:
    content = f.read()

# Current min Length
minLength = len(content)
# Set of input data (presumably) contains alphabet :p
for char in set(content.lower()):

    # remove upper and lowerspace occurences of characters of the data for this char
    temp = content.replace(char.lower(), '').replace(char.upper(), '')

    # Call removeUnits until fixed point is reached
    changed = False
    while not changed:
        changed, temp = removeUnits(temp)
    minLength = min(len(temp), minLength)

print(minLength)

