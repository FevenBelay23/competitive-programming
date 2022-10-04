class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket= {}
        Fruits = 0 
        Start = 0
        for i in range(len(fruits)):
            current = fruits[i]
            if current not in basket:
                basket[current] = 0
            basket[current] += 1 
            while len(basket) > 2:
                remove = fruits[Start] 
                basket[remove] -= 1 
                if basket[remove] == 0:
                    del basket[remove]
                Start += 1 
            Fruits = max(Fruits,i-Start + 1)
        return Fruits