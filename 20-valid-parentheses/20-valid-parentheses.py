class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in s:
            if i in "{[(":
                stack.append(i)
            elif i in "}])":
                if not stack:
                    return False
                open_brack = stack.pop()
                if open_brack == "(" and  i == ")":
                    continue
                elif open_brack == "[" and i == "]":
                    continue
                elif open_brack == "{" and i == "}":
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        