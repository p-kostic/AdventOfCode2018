with open('input.txt') as f:
    content = f.readlines()

# Part 1
freq = 0
for line in content:
    freq += int(line)
print(freq)

# Part 2
freq = 0
seen = set()
found = False

while found is False:
    for line in content:
        freq += int(line)
        if freq in seen and found is False:
            print(freq)
            found = True
        seen.add(freq)

print(freq)