class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 1. Devide the list into halves
        def mergeSort(arr, l , r):
            if l == r:
                return arr

            # 2. Recursively sort left and right halves
            m = (l+r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            
            merge(arr, l, m, r)
            return arr
        
        # 3. Merge sorted halves
        def merge(arr, l, m, r):
            leftArr = arr[l:m+1]
            rightArr = arr[m+1:r+1]
            ptr, leftPtr, rightPtr = l, 0, 0

            while leftPtr < len(leftArr) and rightPtr < len(rightArr):
                if leftArr[leftPtr] < rightArr[rightPtr]:
                    arr[ptr] = leftArr[leftPtr]
                    leftPtr += 1
                else: 
                    arr[ptr] = rightArr[rightPtr]
                    rightPtr += 1
                ptr += 1

            #While either half still has leftover 
            while leftPtr < len(leftArr):
                arr[ptr] = leftArr[leftPtr]
                leftPtr += 1
                ptr += 1

            while rightPtr > len(rightArr):
                arr[ptr] = rightArr[rightPtr]
                rightPtr += 1
                ptr += 1 

        return mergeSort(nums, 0, len(nums) - 1)
