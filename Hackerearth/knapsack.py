'''

'''

# Write your code here

N,W = list(map(int,input().split()))
v = list(map(int,input().split()))
w = list(map(int,input().split()))

memo = [[-1 for i in range(N)] for j in range(W)]

# Solving 0/1 knapsack using recursion with memoization , Takes a lot of time for big Ns and Ws
def max_knapsack(max_weight,index):
    if index == N or max_weight == 0:
        return 0

    if memo[max_weight-1][index] != -1 :
        return memo[max_weight-1][index]

    if max_weight - w[index] < 0 :
        included = 0
    else : 
        included = v[index] + max_knapsack(max_weight - w[index],index+1)
    
    not_included = max_knapsack(max_weight,index+1)    
    memo[max_weight-1][index] = max(included,not_included)
    return memo[max_weight-1][index]
'''
def max_knapsack(curr_W,index):
    if index == N or curr_W == W:
        return 0
    if w[index] + curr_W > W :
        included = 0
    else :
        included = v[index] + max_knapsack(curr_W + w[index],index+1)
    not_included = max_knapsack(curr_W,index+1)
    return max(included,not_included)
'''
print(max_knapsack(W,0))

#Another Solution 
#***********************************************************************************************************
N,W = list(map(int,input().split()))
v = list(map(int,input().split()))
w = list(map(int,input().split()))

# Dp solution using weights and indexes as states , simplified from 2d matrix to 1d array
memo = [0 for i in range(W+1)]
for j in range(W+1):
    memo[j] = 0 if j < w[0] else v[0]

for i in range(1,N):
    for j in range(W,0,-1):
        if j >= w[i] :
            memo[j] = max(v[i] + memo[j-w[i]],memo[j])

print(memo[W])

#Another Solution
***************************************************************************************************************
N,W = list(map(int,input().split()))
v = list(map(int,input().split()))
w = list(map(int,input().split()))

memo = [[0 for i in range(50000+1)] for j in range(N)]

# Dp solution using values and indexes as states , in this case take minimum weight of item included and item not included
memo[0][v[0]] = w[0]
for i in range(1,N):
    for j in range(50000+1):
        if j == v[i] :
            memo[i][j] = w[i]
        if memo[i-1][j]:
            memo[i][j] = memo[i-1][j]
        if j > v[i] and memo[i-1][j-v[i]] :
            if memo[i-1][j] :
                memo[i][j] = min(w[i] + memo[i-1][j-v[i]],memo[i-1][j])
            else :
                memo[i][j] = w[i] + memo[i-1][j-v[i]]
        
for j in range(50000,0,-1):
    if memo[N-1][j] != 0 and memo[N-1][j] <= W:
        print(j)
        break


# Another Solution
******************************************************************************************************
N,W = list(map(int,input().split()))
v = list(map(int,input().split()))
w = list(map(int,input().split()))

memo = [0 for i in range(50000+1)]

# Simplification of the above solution to 1d array and starting the inner loop backwards 
# Still doesn't pass all test cases , some of them time out
# Have to choose which state to choose , weight or value against index 
# This choice should be done to see if W > 50000
memo[v[0]] = w[0]
for i in range(1,N):
    for j in range(50000,0,-1):
        if j < v[i]:
            break
        if j == v[i] :
            if memo[j]:
                memo[j] = min(w[i],memo[j])
            else :
                memo[j] = w[i]
        if j > v[i] and memo[j-v[i]] :
            if memo[j] :
                memo[j] = min(w[i] + memo[j-v[i]],memo[j])
            else :
                memo[j] = w[i] + memo[j-v[i]]
        
for j in range(50000,0,-1):
    if memo[j] != 0 and memo[j] <= W:
        print(j)
        break
