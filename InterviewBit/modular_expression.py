'''
Implement pow(A, B) % C.

In other words, given A, B and C,
find (AB)%C.

Input : A = 2, B = 3, C = 3
Return : 2 
2^3 % 3 = 8 % 3 = 2
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    
    # O(logn) time complexity as the problem space is halved each time
    # when calculating power the computation can take a lot time in the normal way even for moderately large numbers
    # Sometimes or many a times the result is so large we can't even fit it in 31 bits ( 1 bit for sign )
    # so calculating the power first and then doing the modulo is bad
    # so we try to get the result through associative and commutative property of modulo 
    # we reduce the size of the problem by half using exponent properties by representing a^n as a^(n/2) x a^(n/2) for even n
    # for odd n a^1 x a^(n-1)
    def Mod(self, A, B, C):
        if B == 0 :
            return 1 if A else 0
        elif B%2 == 0:
            return (self.Mod(A,B//2,C)**2) % C
        else:
            return (A%C * self.Mod(A,B-1,C)) % C
