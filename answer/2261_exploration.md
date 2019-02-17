
### 새로 알게 된 사항들
- list of tuple을 sort하면 알아서 '잘' 해준다 (list of list도 가능)  
- set of tuple도 가능하다!  
- pairwise로 점들의 거리를 구할 때, 이중 for문이 permutation-lambda보다 빠르다 ㅜㅜ
- set을 매번 새로 assign 하는 건 개느리다. append는 역시 엄청나다
- append는 대단하지만, 10만번 append보다는 한 번 flattening이 쪼오끔 싸다!

### Speed comparison between nested for loop and permutation-map


```python
import random
import itertools
m = 1000
pts = []
for _ in range(m):
    x, y = random.randint(-10000,10000)+10000, random.randint(-10000,10000)+10000
    pts.append((x, y))
```


```python
get_dist = lambda pt_pair: (pt_pair[0][0] - pt_pair[1][0])**2 + (pt_pair[0][1] - pt_pair[1][1])**2
```


```python
%%time
dists = (map(get_dist, itertools.permutations(pts, 2)))
print(min(dists))
```

    290
    Wall time: 1.19 s
    


```python
def naive_dist(pts):
    n = len(pts)
    dist = []
    for i in range(n):
        temp = pts[i]
        for j in (range(i+1, n)):
            dist.append(((temp[0]-pts[j][0])**2 + (temp[1]-pts[j][1])**2))
    return min(dist)
```


```python
%%time
print(naive_dist(pts))
```

    290
    Wall time: 593 ms
    

### speed comparison between set and list


```python
%%time
import sys

m = 150000
pts = []

dist = []
dic = dict()

#read data
for _ in range(m):
    x, y = random.randint(-10000,10000)+10000, random.randint(-10000,10000)+10000
    pts.append(tuple([x, y]))
    dic[(x//200, y//200)] = dic.get((x//200, y//200), set()) | set([(x%200, y%200)])

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
    if len(dist)>=1: print(min(dist))
```

    1
    Wall time: 2.74 s
    


```python
%%time
import sys

m = 150000
pts = []

dist = []
dic = dict()

#read data
for _ in range(m):
    x, y = random.randint(-10000,10000)+10000, random.randint(-10000,10000)+10000
    pts.append(tuple([x, y]))
    dic[(x//200, y//200)] = dic.get((x//200, y//200), []) + [(x%200, y%200)]

if m>1000: 
    for _, value in dic.items():
        target=list(set(value))
        n = len(target)
        if n == 1 : continue
        temp_dist = []
        for i in range(n):
            for j in range(i+1, n):
                temp_dist.append(((target[i][0]-target[j][0])**2 + (target[i][1]-target[j][1])**2))
        dist.append(min(temp_dist))
    if len(dist)>=1: print(min(dist))
```

    1
    Wall time: 2.52 s
    


```python
%%time
test_set = set([])
for i in range(50000):
    test_set = test_set|set([i])
```

    Wall time: 29.9 s
    


```python
%%time
test_set = set([])
for i in range(50000):
    test_set.add(i)
```

    Wall time: 8.02 ms
    


```python
%%time
test_list = []
for i in range(50000):
    test_list = test_list + [i]
```

    Wall time: 4.23 s
    


```python
%%time
m = 10000
dic = dict()
for _ in range(m):
    x, y = random.randint(-100,100)+100, random.randint(-100,100)+100
    dic[(x//10, y//10)] = dic.get((x//10, y//10), []) + [(x%10, y%10)]
for key in dic.keys():
    dic[key] = set(dic[key])
```

    Wall time: 70.2 ms
    


```python
%%time
m = 10000
dic = dict()
for _ in range(m):
    x, y = random.randint(-100,100)+100, random.randint(-100,100)+100
    if (x//10, y//10) in dic.keys():
        dic[(x//10, y//10)].add((x%10, y%10))
    else: dic[(x//10, y//10)] = set([(x%10, y%10)])
```

    Wall time: 40.2 ms
    


```python
%%time
m = 10000
dic = {(i, j):set() for i in range(21) for j in range(21)}
for _ in range(m):
    x, y = random.randint(-100,100)+100, random.randint(-100,100)+100
    dic[(x//10, y//10)].add((x%10, y%10))
```

    Wall time: 43.1 ms
    

### comparison between append and flattening nested list


```python
%%time
dist = []
dic = dict()

#read data
m = 1000000
for _ in range(m):
    x, y = random.randint(-10000,10000)+10000, random.randint(-10000,10000)+10000
    dic[(x//200, y//200)] = dic.get((x//200, y//200), set()) | set([(x, y)])
pts = list(itertools.chain(*map(list, dic.values())))
```

    Wall time: 11.9 s
    


```python
%%time
pts = []
dic = dict()
for _ in range(m):
    x, y = random.randint(-10000,10000)+10000, random.randint(-10000,10000)+10000
    pts.append((x, y))
    dic[(x//200, y//200)] = dic.get((x//200, y//200), set()) | set([(x%200, y%200)])
```

    Wall time: 15.3 s
    

### partition size


```python
import itertools
import random
import time
part_sizes = [50, 100, 150, 200, 300, 500, 1000]
prc_time = []

dist = []
dic = dict()

m = 100000
for part_size in part_sizes:
    start = time.time()
    for _ in range(m):
        x, y = random.randint(-10000,10000)+10000, random.randint(-10000,10000)+10000
        dic[(x//part_size, y//part_size)] = dic.get((x//part_size, y//part_size), set()) | set([(x, y)])
    pts = list(itertools.chain(*map(list, dic.values())))

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
        if len(dist)>=1: print(min(dist))

    if len(dist) < 1:
        pts2 = list(set(pts))
        #single point case
        if len(pts)!=len(pts2):
            print(0)
        else: 
            dist = []
            for i in range(len(pts2)):
                temp = pts2[i]
                for j in (range(i+1, len(pts2))):
                    dist.append(((temp[0]-pts2[j][0])**2 + (temp[1]-pts2[j][1])**2))
            print(min(dist))
    end = time.time()
    prc_time.append(round(end-start,2))
prc_time
```

    1
    1
    1
    1
    1
    1
    1
    




    [0.94, 1.23, 2.1, 3.89, 7.8, 16.44, 48.94]




```python
for i in range(len(prc_time)):
    print(part_sizes[i], ":", prc_time[i])
```

    50 : 0.94
    100 : 1.23
    150 : 2.1
    200 : 3.89
    300 : 7.8
    500 : 16.44
    1000 : 48.94
    


```python
import itertools
import random
import time
part_sizes = [5, 10, 20, 30, 50]
prc_time = []

dist = []
dic = dict()

m = 100000
for part_size in part_sizes:
    start = time.time()
    for _ in range(m):
        x, y = random.randint(-10000,10000)+10000, random.randint(-10000,10000)+10000
        dic[(x//part_size, y//part_size)] = dic.get((x//part_size, y//part_size), set()) | set([(x, y)])
    pts = list(itertools.chain(*map(list, dic.values())))

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
        if len(dist)>=1: print(min(dist))

    if len(dist) < 1:
        pts2 = list(set(pts))
        #single point case
        if len(pts)!=len(pts2):
            print(0)
        else: 
            dist = []
            for i in range(len(pts2)):
                temp = pts2[i]
                for j in (range(i+1, len(pts2))):
                    dist.append(((temp[0]-pts2[j][0])**2 + (temp[1]-pts2[j][1])**2))
            print(min(dist))
    end = time.time()
    prc_time.append(round(end-start,2))
for i in range(len(prc_time)):
    print(part_sizes[i], ":", prc_time[i])
```

    1
    1
    1
    1
    1
    5 : 1.01
    10 : 1.09
    20 : 1.18
    30 : 1.5
    50 : 1.85
    
