class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        c=0
        m=0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[c])
                c=c+1
            a.add(s[i])
            m=max(m,i-c+1)
        return m