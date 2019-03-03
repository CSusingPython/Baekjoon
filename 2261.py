import sys
import itertools
#set functions
r = sys.stdin.readline
def naive_dist_between_sets(set1, set2):
    res = []
    for x1, y1 in set1:
        for x2, y2 in set2:
            res.append( (x1-x2)**2 + (y1-y2)**2  )
    return min(res)

def naive_dist(pts):
    n = len(pts)
    dist = []
    for i in range(n):
        for j in (range(i+1, n)):
            dist.append(((pts[i][0]-pts[j][0])**2 + (pts[i][1]-pts[j][1])**2))
    return min(dist)




#the number of points
m = int(r().strip())

#initialize
part_size = 100
dist = []
#dic = {(i,j):set() for i in range(-10000//part_size, 10000//part_size+1) for j in range(-10000//part_size, 10000//part_size+1)}
dic = {(i,j):set() for i in range(20000//part_size+1) for j in range(20000//part_size+1)}


#get points
for _ in range(m):
    x, y = map(int, r().strip().split())
    x += 10000
    y += 10000
    dic[(x//part_size, y//part_size)].add((x, y))

#organize
dic = {k:v for k, v in dic.items() if len(v)>0}



#if the number of points is less than 1000, do not divide them
if m>1000: 
    for _, value in dic.items():
        target=list(value)
        n = len(target)
        if n == 1 : continue
        temp_dist = []
        for i in range(n):
            for j in range(i+1, n):
                temp_dist.append(((target[i][0]-target[j][0])**2 + (target[i][1]-target[j][1])**2))
        dist.append(min(temp_dist))

    #inter-distance
    if len(dist)>0: #if not, min_dist can not be defined
        min_dist = min(dist)
        min_dist_square = min_dist**0.5
            
        if min_dist ==1: pass #if so, no more search is needed

        else:
            #initialize
            n_keys = len(dic)
            key_list = list(dic.keys())
            key_list.sort()
            new_min = []
            
            for key in key_list:
                partition = dic[key]
                k1, k2 = key
                
                #check the lower partition
                key_abv = (k1, k2-1)
                if key_abv in key_list: 
                    upper_bottom = [(x, y) for x, y in partition if y-(100*k2) < min_dist_square+1]
                    lower_top = [(x, y) for x, y in dic[key_abv] if y-(100*(k2-1)) > 100-min_dist_square-1]
                    #if there are points to check
                    if len(upper_bottom)==0 or len(lower_top)==0: continue
                    else:
                        temp_min = naive_dist_between_sets(upper_bottom, lower_top)
                        if temp_min < min_dist: 
                            new_min.append(temp_min)
                            
                #check the right partition
                key_right = (k1+1, k2)
                if key_right in key_list: 
                    left_rightmost = [(x, y) for x, y in partition if x-(100*k1) > 100-min_dist_square-1]
                    right_leftmost = [(x, y) for x, y in dic[key_right] if x-(100*(k1+1)) < min_dist_square+1]
                    #if there are points to check
                    if len(left_rightmost)==0 or len(right_leftmost)==0: continue
                    else:
                        temp_min = naive_dist_between_sets(left_rightmost, right_leftmost)
                        if temp_min < min_dist: 
                            new_min.append(temp_min)
            dist = [min_dist] + new_min




new_min = []
if len(dist) < 1:
    pts = list(itertools.chain(*map(list, dic.values())))
    #single point duplicates case
    if len(pts)!=m:
        dist.append(0)
    else: 
        dist.append(naive_dist(pts))


print(min(dist))


