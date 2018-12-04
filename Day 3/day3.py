with open('input.txt') as f:
    content = f.readlines()

# Part 1 
w, h = 1000, 1000;
matrix = [[0 for x in range(w)] for y in range(h)] 

for line in content:
    splitted = line.split(" ")
    
    # Coordinates
    coordinates = splitted[2].split(",")
    x = int(coordinates[0])
    y = int(coordinates[1][:-1])
    
    # Area
    area = splitted[3].split("x")
    endWidth = int(area[0]) + x
    endHeight = int(area[1]) + y

    print("Width: = ", x,endWidth)
    print("Height: = ", y,endHeight)

    for i in range(x,endWidth):
        for j in range(y,endHeight):
            matrix[i][j] += 1

    