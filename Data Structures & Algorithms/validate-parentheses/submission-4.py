class Solution:
    def isValid(self, s: str) -> bool:
        # Тип данных - строка, делаем через стек
        stack = []
        dict = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in dict:
                top = stack.pop() if stack else 0
                if top != dict[i]:
                    return False
            else:
                stack.append(i)
                
        return not stack        


        # [{(})]