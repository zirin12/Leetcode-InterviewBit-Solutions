'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''

class Solution:
    
    # Read the Leetcode solution editorial based of a mathematical solution where the basic notion of a median is used
    # Implement that later
    
    # Have two pointers to the two lists beginning , compare both of them and add min element to new list
    # At the same time checking for the median element since we know it's position already in (m+n) final array
    # complexity : worse case is O(m+n) , space = O(m+n)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first = 0
        second = 0
        m = len(nums1)
        n = len(nums2)
        tlen = m+n
        mid = tlen//2
        res = []
        count = 0
        while first<m and second<n :
            if nums1[first] < nums2[second]:
                res.append(nums1[first])
                first += 1
                count += 1
            else :
                res.append(nums2[second])
                second += 1
                count += 1
        
            if tlen%2:
                if count-1 == mid:
                    return res[count-1]
            else :
                if count-1 == mid:
                    return (res[count-2] + res[count-1])/2
        
        if first==m:
            while second < n :
                res.append(nums2[second])
                second += 1
        if second==n:
            while first < m:
                res.append(nums1[first])
                first += 1
        
        if tlen%2:
            return res[mid]
        else:
            return (res[mid-1] + res[mid])/2
      
        
