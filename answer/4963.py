import sys
r = sys.stdin.readline
toprint = []

def search_close(i, j):
    ones = []
    for x in range(max(0,i-1), min(i+1, n_row-1)+1):
        for y in range(max(0,j-1), min(j+1, n_col-1)+1):
            if x==i and y==j: continue
            if isl_visit[x][y]==False:
                isl_visit[x][y] = True
                if isl_map[x][y]==1: ones.append([x,y])
    return ones

def get_target(isl_count):
    
    for i in range(n_row):
        for j in range(n_col):
            if isl_visit[i][j]==False:
                isl_visit[i][j]=True
                if isl_map[i][j] == 1: 
                    isl_count += 1
                    return isl_count, [[i, j]]
    return isl_count, []

def marking_island(target_container):
    while target_container:
        current_container = []
        for target in target_container:
            found_ones = search_close(*target)
            [current_container.append(one) for one in found_ones]
        target_container = current_container
    

def cal_isl(isl_map, n_row, n_col):
    isl_count = 0
    while sum(sum(i) for i in isl_visit) < n_row*n_col:
        isl_count, target_container = get_target(isl_count)
        marking_island(target_container)
    toprint.append(isl_count)


while True:
    #get inputs
    n_col, n_row = list(map(int, r().split()))

    #end signal
    if n_col==n_row==0: break
    
    #get input
    isl_map = []
    for row in range(n_row):
        isl_map.append(list(map(int, r().split())))
    
    #dummy variable
    isl_visit = [[False]*n_col for _ in range(n_row)]
    
    #calculate the number of island
    isl_count = 0
    cal_isl(isl_map, n_row, n_col)

for i in toprint:
    print(i)