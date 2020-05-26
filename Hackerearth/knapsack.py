'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
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
