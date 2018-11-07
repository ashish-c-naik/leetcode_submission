class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        comb = list()
        head1 = head2 = 0
        nums1.append(sys.maxint)
        nums2.append(sys.maxint)
        while head1 != len(nums1) - 1 or head2 != len(nums2) - 1:
            if nums1[head1] < nums2[head2]:
                comb.append(nums1[head1])
                head1+=1
            else:
                comb.append(nums2[head2])
                head2+=1
        index = (len(comb) - 1) // 2
        if (len(comb) % 2):
            return comb[index]
        else:
            return (comb[index] + comb[index + 1])/2.0