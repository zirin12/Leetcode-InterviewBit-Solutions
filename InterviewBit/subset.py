'''
  Given a set of distinct integers, S, return all possible subsets.
  Also, the subsets should be sorted in ascending ( lexicographic ) order.
'''
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    
    # First Sort A
    # create an empty subset list
    # start the recursion , last element will be base condition
    # keep track of the newest added elements in susbet list from previous call
    # keep adding the elements , it will already be in lexicographic order as we return from each call
    def get_subsets(self, A, index,L):
        if index == len(A)-1:
            L[-1] = [A[index]]
            return len(L)-1
        else :
            end = self.get_subsets(A, index+1, L)
            n = len(L)
            for i in range(1,n-end + 1):
                L[end - i] = []
                L[end - i].append(A[index]) 
                for ele in L[n-i]:
                    L[end - i].append(ele)
            L[end-i-1] = [A[index]]
            return end - i - 1

    def subsets(self, A):
        if len(A) == 0 :
            return [[]]
        L = [""]*(2**len(A))
        A.sort()
        self.get_subsets(A,0,L)
        return L
