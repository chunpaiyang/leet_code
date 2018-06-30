class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        vs = [0 for i in s]
        for i in range(len(s)):
            if s[i] == '(':
                if i - 1 >=0 and s[i-1]==')':
                    vs[i]=vs[i-1]
                continue
            
            if s[i] == ')':
                if i - 1 < 0:
                    continue
                # pre is '('
                if s[i-1] == '(':
                    vs[i] = 2
                    if i-2 >= 0 and s[i-2] == ')':
                        vs[i]+=vs[i-2]
                    continue
                # pre is ')'
                if s[i-1] == ')':
                    if vs[i-1]==0: # pre is redundant ')'
                        continue
                    elif vs[i-1]>0:
                        if 0 > (i - vs[i-1] - 1):
                            continue
                        if s[i - vs[i-1] - 1] == '(':
                            vs[i] = vs[i-1] + vs[i - vs[i-1] - 1]  + 2

        max = 0
        for v in vs:
            if v > max:
                max = v
        
        return max




s = Solution()
#n = s.longestValidParentheses(")()())")
#n = s.longestValidParentheses("())")
#n = s.longestValidParentheses("()()")
#n = s.longestValidParentheses("()(())")
#n = s.longestValidParentheses("()(()")
n =n = s.longestValidParentheses("()(())")
print (n)