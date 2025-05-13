class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sa = nums1+nums2
        sa.sort()
        if len(sa)%2==1:
            return float(sa[len(sa)//2])
        else:
            mid1 = sa[len(sa)//2-1]
            mid2 =sa[len(sa)//2]
            return (mid1+mid2)/2.0