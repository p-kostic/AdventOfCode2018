
with open('input.txt') as f:
    content = f.readlines()

# Part 2 
doubles = 0
triples = 0

for line in content:
    occurences = {};
    for c in line:
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1
    if [key for (key, val) in occurences.items() if val == 3]:
        triples += 1
    if [key for (key, val) in occurences.items() if val == 2]:
        doubles += 1

print(triples * doubles)

# Part 2
commonLetters = []

for lineX in content:
    for lineY in content:
        if lineX == lineY:
            continue
        similarities = []
        for i in range(len(lineY)):
            if (lineX[i] == lineY[i]):
                similarities.append(lineY[i])
        if len(similarities) > len(commonLetters):
            commonLetters = similarities
print(''.join(commonLetters))

