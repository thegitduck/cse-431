# take a branch and recursively check how many G's in that direction
# checks next point from point given
# return length in that direction
def test_branch(arr, i, d, v):
    if not (i[0] + d[0], i[1] + d[1]) in arr:
        return v
    else:
        return test_branch(arr, (i[0] + d[0], i[1] + d[1]), d, v + 1)

# takes a location direction and length and returns true if branch is valid 
def valid_branch(arr, i, d, l):
    if not (i[0] + (d[0] * l), i[1] + (d[1] * l)) in arr:
        return False
    return True
        
# gets an array of points in the plus symbol
def get_plus(arr, C, L):
    new = [C]
    for i in range(1,L+1):
        new.append((C[0] + i, C[1])) # right
        new.append((C[0] - i, C[1])) # left
        new.append((C[0], C[1] - i)) # up
        new.append((C[0], C[1] + i)) # down
    return new
        
# take point and array
# must calc points to remove
# returns None if the given values did not produce a valid plus
# return array with used points
def test_center(arr, C, l):
    save = arr # original array
    used = [] # the ones to remove from arr
    right = valid_branch(arr, C, (1,0), l)
    left = valid_branch(arr, C, (-1,0), l)
    up = valid_branch(arr, C, (0,-1), l)
    down = valid_branch(arr, C, (0,1), l)
    if right and left and up and down:
        used = get_plus(arr, C, l)
    return used

############################################### Driver Code

nums = [int(x) for x in raw_input().split()]

N = nums[0]
M = nums[1]
arr = []
good = []

for i in range(N): # make "matrix"
    arr.append(raw_input())
    
for i in range(len(arr)): # each row as a string
    for j in range(len(arr[i])):
        if arr[i][j] == "G":
            good.append((j, i))
good = list(set(good))

# get all posible plus orientations
sizes = []
for i in range(len(good)):
    for j in range(1,len(good)):
        i_count = 0
        j_count = 0
        if i != j:
            A = good[i]
            B = good[j]
            sizes.append((1, 1, A, B))
            while A:
                i_count += 1
                j_count = 0
                A = test_center(good, good[i], i_count)
                B = test_center(list(set(good)^set(A)), good[j], j_count)
                while B:
                    if A and B:
                        sizes.append((len(A), len(B), A, B))
                    j_count += 1
                    A = test_center(good, good[i], i_count)
                    B = test_center(list(set(good)^set(A)), good[j], j_count)
                    
print(sizes)

result = 0
used_pair = None
for pair in sizes:
    if (pair[0] * pair[1]) > result:
        result = (pair[0] * pair[1])
        used_pair = pair

print(result)

# for debugging
"""
print(used_pair[0])
print(used_pair[1])

for i in range(len(arr)): # each row as a string
    s = ""
    for j in range(len(arr[i])):
        if (j,i) in used_pair[2]:
            s += "*"
        elif (j,i) in used_pair[3]:
            s += "+"
        else:
            s+= arr[i][j]
    print(s)

print(sizes)
"""