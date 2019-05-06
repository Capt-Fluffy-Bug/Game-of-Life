grid = []
res = 5
row = 0
col = 0
def setup():
    global res, row, col, grid
    size(600,400)
    col = width/res
    row = height/res
    grid = initGrid(col, row)

    
    
def draw():
    global res, row, col, grid
    background(255)


    next = initNext(col, row)
    
    for i in range(0, col):
        for j in range(0, row):
            state = grid[i][j]
                
            neighbour = computeNeighbour(grid, i, j)
                  
            
            if state == 0 and neighbour == 3:
                next[i][j] = 1
            elif state == 1 and (neighbour < 2 or neighbour > 3):
                next[i][j] = 0
            else:
                next[i][j] = state
    grid = next;
    
    for i in range(0, col):
        for j in range(0, row):
            x = i * res
            y = j * res
            if grid[i][j] == 1:
                fill(0)
                rect(x, y, res, res)
            else:
                fill(255)
                rect(x, y, res, res)
                
                

                
    
def initGrid(rows, columns):
    a = [[floor(random(2)) for x in range(columns)] for y in range(rows)]
    return a

def initNext(rows, columns):
    a = [[None for x in range(columns)] for y in range(rows)]
    return a

def computeNeighbour(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            c = (x + i + col) % col
            r = (y + j + row) % row
            sum += grid[c][r] 
            
    sum -= grid[x][y]
    return sum
