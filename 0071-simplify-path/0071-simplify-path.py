class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split('/')
        stack = []

        for i in directory:
            if i and i != '.':
                if i == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)

        simplified_canonical_path = '/' + '/'.join(stack)
        return simplified_canonical_path
        