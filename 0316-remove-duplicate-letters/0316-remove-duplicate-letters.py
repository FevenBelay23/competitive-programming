class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        
        for i in s:
            if i in stack:
                count[i] -= 1
                continue
            while len(stack) > 0 and stack[-1] > i and count[stack[-1]] > 0:
                stack.pop()
            count[i] -= 1
            stack.append(i) 
            
        return "".join(stack)
        