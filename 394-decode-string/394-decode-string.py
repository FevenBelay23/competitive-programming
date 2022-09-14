class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringStack = []
        numberStack = []
        temp = ''
        k = ''
        for i in s:
            if i.isdigit():
                if temp: 
                    stringStack.append(temp)
                    temp = ''
                k += i
            elif i == '[':
                numberStack.append(int(k))
                stringStack.append('[') 
                k = ''
            elif i == ']':
                while True:
                    last = stringStack.pop()
                    if last == '[':
                        break
                    temp = last + temp
                temp *= numberStack.pop()
                stringStack.append(temp)
                temp = ''
            else:
                temp += i
        answer = ''
        while len(stringStack) != 0:
            answer = stringStack.pop() + answer
        return answer + temp