class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        
        if (len(a)>len(b)):
            a, b = b, a
        
        total = len(a)+len(b)
        half = total//2

        l = 0
        r = len(a)-1

        while (True):
            mid_a = (l+r)//2
            mid_b = half-mid_a-2

            a_1 = a[mid_a] if mid_a>=0 else float('-inf')
            a_2 = a[mid_a+1] if mid_a<len(a)-1 else float('inf')
            
            b_1 = b[mid_b] if mid_b>=0 else float('-inf')
            b_2 = b[mid_b+1] if mid_b<len(b)-1 else float('inf')

            if (a_1<=b_2 and b_1<=a_2):
                if (total%2):
                    return min(a_2, b_2)
                else:
                    return (max(a_1, b_1)+min(a_2, b_2))/2
            elif (a_1>b_2):
                r = mid_a-1
            else:
                l = mid_a+1



