from collections import Counter, defaultdict

with open('input.txt') as f:
    content = f.readlines()

# Part 1
def parse(content):
    # format = year-month-day hour:minute
    # only the minute is relevant
    # kvp, key = guard_id, value is list of minutes (0-60)
    guards = defaultdict(lambda: [0 for x in range(60)])
    
    sortedContent = sorted(content)
    for line in sortedContent:
        splitLine = line.split(" ")

        if splitLine[3][0] == '#':            # find guard_id
            g_id = splitLine[3]
        elif splitLine[3][0] == 'a':          # find asleep
            sleep = int(splitLine[1][3:5])
        else:                                 # wake up
            awake = int(splitLine[1][3:5])
            for i in range(sleep,awake):      # for a given guard, increment the minutes that he was asleep in that range
                guards[g_id][i] += 1
    return guards

guards = parse(content)

# Sort the dictionary based on the guards with the most sleep (sum value), get the key of the first one
g1 = sorted(guards.keys(), key=lambda g: sum(guards[g]), reverse=True)[0]

print("Guard", g1, "with the most sleep on minute ", guards[g1].index(max(guards[g1])), "with ", max(guards[g1]), "minutes") 
print("Answer:", int(g1[1:]) * guards[g1].index(max(guards[g1])))

# Part 2 
# Sort the dictionary based on the guards with the longest sleep (max value), get the key of first the first one
g2 = sorted(guards.keys(), key=lambda g: max(guards[g]), reverse=True)[0]
print("Guard", g2, "with the most sleep on minute ", guards[g2].index(max(guards[g2])), "with ", max(guards[g2]), "minutes") 
print("Answer:", int(g2[1:]) * guards[g2].index(max(guards[g2])))