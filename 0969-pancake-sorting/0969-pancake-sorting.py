class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        def pancakeFlip(last):
            first = 0
            while first < last:
                arr[first] , arr[last] = arr[last] , arr[first]
                first +=1
                last -=1
        for i in range(n-1,-1,-1):
            largest=i
            for j in range(i,-1,-1):
                if arr[j] > arr[largest]:
                    largest = j
            if largest != i:
                pancakeFlip(largest)
                pancakeFlip(i)
                result.append(largest+1)
                result.append(i+1)
        return result
        
        