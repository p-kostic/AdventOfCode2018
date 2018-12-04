from collections import defaultdict

with open('input.txt') as f:
    content = f.readlines()

def parse(row):
    num, _, xy, offset = row.split()
    num = num[1:]
    x, y = xy[:-1].split(",")
    w, h = offset.split('x')
    return int(num), int(x), int(y), int(w), int(h)

# Part 1 
matrix = defaultdict(int)
for line in content:
    num, x, y, w, h = parse(line)
    for i in range(w):
        for j in range(h):
            matrix[(x+i,y+j)] += 1

# the length of of the values bigger than one in the kvp == area
print(len([v for k,v in matrix.items() if v > 1]))

# Part 2
claims        = set()
overlapClaims = set()
for line in content:
    num, x, y, w, h = parse(line)
    
    claims.add(num)
    for i in range(w):
        for j in range(h):
            offsetTuple = (x+i, y+j)
            if matrix[offsetTuple] > 1:
                overlapClaims.add(num)

# first difference between sets shows one that does not overlap
print(next(f for f in claims - overlapClaims))