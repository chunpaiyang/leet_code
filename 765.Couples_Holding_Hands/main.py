class Solution:
    def _isCouple(self, i, j):
        m = i+1 if i%2 == 0 else i-1
        return True if (m==j) else False

    def _c(self, value): # couple value
        return value+1 if value%2 == 0 else value-1

    def _n(self, index): # neighbor index
        return self._c(index)
    
    def _g(self, arr, firstIndex): # chain values to a group
        c = 0
        p = firstIndex
        i = firstIndex
        while (not self._isCouple(i,p)):
            couple_index = arr.index(self._c(arr[i]))
            neighbor_index = self._n(i)

            # swap
            tmp = arr[neighbor_index]
            arr[neighbor_index] = arr[couple_index]
            arr[couple_index] = tmp

            self._done[i] = True
            self._done[neighbor_index] = True

            p = i
            i = couple_index
            c = c +1
        return c-1 if c > 0 else 0
            
    def minSwapsCouples(self, arr):
        """
        :type row: List[int]
        :rtype: int
        """
        total = 0
        self._done = {}
        for i,v in enumerate(arr):
            if i not in self._done:
                total += self._g(arr, i)
        
        return total
        



        

s = Solution()
print (s.minSwapsCouples([10,7,4,2,3,0,9,11,1,5,6,8]))