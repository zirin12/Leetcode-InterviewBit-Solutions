class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    
    # min distance  = distance to diagonal element + distance to target from diagonal element
    # boils down to the maximum of the difference between the 2 given points.
    def minSteps(self,p1, p2):
        diff = (abs(p2[0]-p1[0]),abs(p2[1]-p1[1]))
        return max(diff)
  
    def coverPoints(self, A, B):
        points = list(zip(A,B))
        length = len(points)
        steps = 0
        if len==1:
            return 0
        for i in range(0,length-1):
            steps += self.minSteps(points[i],points[i+1])
        return steps
