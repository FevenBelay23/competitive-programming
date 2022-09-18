class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        current = chars[0]
        temp = 0
        count = 0
        for i in range(len(chars)):
            if chars[i] != current:  
                chars[temp] = current
                temp += 1
                if count > 1:
                    for j in str(count): 
                        chars[temp] = j
                        temp += 1
                current = chars[i]
                count = 1    
            else:
                count += 1
        if count >= 1:
            chars[temp] = current
            temp += 1
            if count > 1:
                for k in str(count): 
                    chars[temp] = k
                    temp += 1  
        return temp
