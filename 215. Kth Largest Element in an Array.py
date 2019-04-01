class Solution(object):
    def partition(self, arr, low, high):
            mid = (low+high)//2
            arr[mid], arr[high] = arr[high], arr[mid]
            pivot = arr[high]
            i = low-1
            j = low
            while j < high:
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                j+=1
            i+=1
            arr[high], arr[i] = arr[i], arr[high]
            return i
    def findK(self, arr, low, high, K):
        if low <= high:
            index = self.partition(arr, low, high)
            if K == index: return arr[index]
            return (self.findK(arr, low, index-1, K), self.findK(arr, index+1, high, K))[index<K]
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findK(nums, 0 , len(nums)-1, len(nums)-k)
        
            