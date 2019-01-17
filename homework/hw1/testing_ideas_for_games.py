T = 1

for i in range(T):
    nums = [6,2,2]
    n = nums[0]
    m = nums[1]
    c = nums[2]
    result = int(n/m) # games started with
    new = int(result / c)
    while (new >= c):
    	result += new
    	new = int(new / c)
    print(result)
    