import heapq

class Solution:
    def _findStartPoint(self, grid):
        n = len(grid)
        v = max(min(grid[0][1], grid[1][0]), min(grid[n-1-1][n-1], grid[n-1][n-1-1]))
        start = None
        ps = [(0,1), (1,0), (n-2,n-1), (n-1,n-2)]
        for p in ps:
            if v == grid[p[0]][p[1]]:
                return p
        
        return None

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = [[0 for j in range(n)] for i in range(n)]
        i,j = 0,0
        m[i][j] = 1
        v = grid[i][j]
        q = [(v,(i,j))]
        mv = v

        while True:
            f = heapq.heappop(q)
            v = f[0]
            i,j = f[1]
            m[i][j] = 3
            if v > mv:
                mv = v

            if i == n-1 and j == n-1:
                break
            
            around = [(i-1, j),(i+1, j), (i, j+1), (i, j-1)]
            for i,j in around:
                if (i>=0 and i < n and j>=0 and j < n) and m[i][j] == 0:
                    m[i][j] = 1
                    heapq.heappush(q, (grid[i][j], (i,j)))

        return mv
        

        
s = Solution()
#result = s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
#result = s.swimInWater([[11,15,3,2],[6,4,0,13],[5,8,9,10],[1,14,12,7]])
#result = s.swimInWater([[0,2],[1,3]])
result = s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
print (result)
