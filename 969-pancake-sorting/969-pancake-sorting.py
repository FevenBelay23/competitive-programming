class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        List = []
        length = len(arr)
        while  length > 0 and sorted(arr) != arr:
            i = arr.index( length) + 1
            j = arr[:i]        
            j.reverse()
            List.append(i)
            arr[:i] = j
            if sorted(arr) == arr:
                break
            j = arr[: length]
            j.reverse()
            arr[: length] = j
            List.append( length)
            length -= 1
        return List