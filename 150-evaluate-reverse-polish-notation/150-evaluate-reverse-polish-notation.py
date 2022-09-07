class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num= []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                num1 = num.pop()
                num2 = num.pop()
                if i == "+":
                    num.append(num2 + num1)
                else:
                    if i == "-":
                        num.append(num2 - num1)
                    else:
                        if i == "*":
                            num.append(num2 * num1)
                        else:
                            if i == "/":
                                if num2 * num1 < 0 and num2 % num1:
                                    num.append(num2/num1 + 1)
                                else:
                                    num.append(num2/num1)
            else:
                num.append(int(i))
        return num.pop()