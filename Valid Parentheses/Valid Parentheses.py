class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        bracket = {')': '(', '}': '{', ']': '['}
        for i in s :
            if i in bracket :
                b= a.pop() if a else None 
                if b != bracket[i]:
                    return False
            else:
                a.append(i)

        return not a 