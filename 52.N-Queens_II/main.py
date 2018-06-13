class Solution:
    def _toS(self, i, j): # /
        return i+j

    def _toBS(self, i, j): # \
        return j - i + len(self.m)

    def _canSelect(self, i, j):
        t1 = self.s[self._toS(i,j)]
        t2 = self.bs[self._toBS(i,j)]
        t3 = self.v[j]
        if t1 + t2  + t3 == 0:
            return True
        return False

    def _select(self, i, j):
        self.m[i][j] = 1
        self.s[self._toS(i,j)] = 1
        self.bs[self._toBS(i,j)] = 1
        self.v[j] = 1
    
    def _deSelect(self, i, j):
        self.m[i][j] = 0
        self.s[self._toS(i,j)] = 0
        self.bs[self._toBS(i,j)] = 0
        self.v[j] = 0

    def _findJ(self, i, j):
        n = len(self.m)
        if j >= n:
            return -1
        for c in range(j, n):
            if self._canSelect(i, c):
                return c
        return -1

    def _genThisRowItem(self, item):
        i = item[0]
        j = self._findJ(i, item[1] + 1)
        if j < 0:
            return None
        
        return [i, j]

    def _genNextRowItem(self, row, col):
        i = row+1
        if i >= len(self.m):
            return None
        
        j = self._findJ(i, col)
        if j < 0:
            return None
        
        return [i, j]
    
    def _convertM(self):
        m = self.m
        
        tmp = [ ["." if m[i][j] == 0 else "Q" for i in range(len(m))] for j in range(len(m)) ]
        ret = []
        for row in tmp:
            s = "".join(row)
            ret.append(s)

        return ret
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.m = [ [0 for i in range(n)] for j in range(n) ]
        self.s = [ 0 for i in range(2*n) ]
        self.bs = [ 0 for i in range(2*n) ]
        self.v = [ 0 for i in range(n) ]

        output = []
        Q = []

        i = 0
        j = 0
        Q.append([i, j])
        self._select(i, j)
        nJ = 0

        while len(Q) > 0:
            last = Q[-1]
            nextItem = self._genNextRowItem(last[0], nJ)

            if not nextItem or (len(Q) == n): # can not gen next row Item
                if len(Q) == n:
                    output.append(self._convertM())
                    #print ("find a sol:", Q)

                last = Q.pop()
                self._deSelect(last[0], last[1])
                nextItem = self._genThisRowItem(last)
                if not nextItem: #gen fail
                    nJ = last[1] + 1
                    continue                    

            self._select(nextItem[0], nextItem[1])
            Q.append(nextItem)
            nJ = 0
        return output

s = Solution()
out = s.solveNQueens(8)
for sol in out:
    print (sol)

print (len(out))