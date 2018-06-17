class Solution:
    def _c(self, board): # to hash code
        ret = []
        for row in board:
            for v in row:
                ret.append(str(v))
        return "".join(ret)

    def _copy(self, board):
        return [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]]
        ]
    
    def _createNewItem(self, board, i0, j0, i1, j1):
        item = self._copy(board)
        item[i0][j0], item[i1][j1] = item[i1][j1], item[i0][j0]
        return item

    def _addItem(self, item, i, j, n):
        c = self._c(item)
        if c not in self._h:
            self._h[c] = n
            self._q.append([item, [i, j], n])            
        elif self._h[c] > n:
            self._h[c] = n
            self._q.append([item, [i, j], n])

    def _span(self):
        self._q = [([[1,2,3],[4,5,0]], [1,2], 0)]
        self._h = {'123450': 0}

        while len(self._q) > 0:
            [board, [i,j], n] = self._q.pop()
        
            if i+1 < len(board):
                i1 = i + 1
                j1 = j
                item = self._createNewItem(board, i, j , i1, j1)
                self._addItem(item, i1, j1, n+1)
            
            if i-1 >= 0:
                i1 = i - 1
                j1 = j
                item = self._createNewItem(board, i, j , i1, j1)
                self._addItem(item, i1, j1, n+1)
            
            if j+1 < len(board[0]):
                i1 = i
                j1 = j+1
                item = self._createNewItem(board, i, j , i1, j1)
                self._addItem(item, i1, j1, n+1)

            if j-1 >= 0:
                i1 = i
                j1 = j-1
                item = self._createNewItem(board, i, j , i1, j1)
                self._addItem(item, i1, j1, n+1)             
                    
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self._answer = {'123450': 0, '120453': 1, '123405': 1, '103425': 2, '123045': 2, '023145': 3, '203145': 4, '243105': 5, '230145': 5, '235140': 6, '235104': 7, '205134': 8, '235014': 8, '035214': 9, '305214': 10, '315204': 11, '350214': 11, '354210': 12, '354201': 13, '304251': 14, '354021': 14, '054321': 15, '504321': 14, '524301': 15, '540321': 13, '541320': 12, '541302': 11, '501342': 12, '541032': 10, '041532': 9, '401532': 8, '431502': 9, '410532': 7, '412530': 6, '412503': 5, '402513': 6, '412053': 4, '012453': 3, '102453': 2, '152403': 3, '152430': 4, '152043': 4, '052143': 5, '502143': 6, '542103': 7, '520143': 7, '523140': 8, '523104': 9, '503124': 10, '523014': 10, '023514': 11, '203514': 12, '213504': 13, '230514': 13, '234510': 14, '234501': 15, '204531':14, '234051': 16, '034251': 15, '240531': 13, '024531': 15, '524031': 16, '241530': 12, '241503': 11, '201543': 12, '241053': 10, '041253': 9, '401253': 8, '451203': 9, '410253': 7, '413250': 6, '413205': 5, '403215': 6, '413025': 4, '013425': 3, '430215': 7, '043215': 7, '243015': 6, '435210': 8, '435201': 9, '405231': 10, '435021': 10, '035421': 11, '305421': 12, '325401': 13, '350421': 13, '351420': 14, '351402': 13, '301452': 12, '351042': 14, '051342': 13, '310452': 13, '031452': 11, '431052': 10,'312450': 14, '312405': 15, '302415': 16, '312045': 16, '012345': 15, '102345': 14, '142305': 15, '120345': 13, '125340': 12, '125304': 11, '105324': 12, '125034': 10, '025134': 9, '150324': 13, '015324': 13, '315024': 12, '154320': 14, '154302': 13, '104352': 14, '154032': 12, '054132': 11, '504132': 10, '534102': 11, '540132': 9, '542130': 8, '534120': 12, '534012': 12, '034512': 13, '304512': 14, '314502': 15, '340512': 15, '342510': 16, '342501': 17, '302541': 18, '342051': 16, '042351': 15, '402351': 14, '452301': 13, '420351': 15, '421350': 14, '421305': 13, '401325': 12, '421035': 14, '021435': 15, '201435': 16, '231405': 15, '210435': 17, '215430': 18, '215403': 17, '205413': 16, '215043': 18, '015243': 17, '105243': 16, '145203': 17, '150243': 15, '153240': 14, '153204': 13, '103254': 14, '153024': 12, '053124': 11, '130254': 15, '013254': 15, '213054': 14, '134250':16, '134205': 15, '104235': 16, '134025': 14, '034125': 13, '304125': 12, '324105': 13, '340125': 11, '345120': 10, '345102': 9, '305142': 8, '345012': 10, '045312': 11, '405312': 10, '415302': 9, '450312': 11, '452310': 12, '415320': 10, '415032': 8, '015432': 7, '105432': 6, '135402': 5, '150432': 5, '135420': 4, '135042': 6, '035142': 7, '130425': 3, '410325': 11, '350142': 9, '352140': 10, '352104': 11, '302154': 12, '352014': 12, '052314': 13, '502314': 14, '512304': 15, '520314': 15, '524310': 16, '512340': 14, '512034': 16, '012534': 15, '102534': 14, '132504': 15, '120534': 13, '124530': 12, '124503': 11, '104523': 12,'124053': 10, '024153': 9, '204153': 8, '254103': 9, '240153': 7, '243150': 6, '254130': 10, '254013': 10, '054213': 11, '504213': 12, '514203': 13, '540213': 13, '543210': 14, '543201': 13, '503241': 14, '543021': 12, '043521': 11, '403521': 10, '423501': 9, '430521': 11, '431520': 10, '423510': 8, '423051': 10, '023451': 11, '203451': 12, '253401': 13, '230451': 13, '231450':14, '253410': 14, '253041': 14, '053241': 15, '250413': 15, '420513': 7, '530241': 15, '531240': 16, '531204': 17, '501234': 16, '531024': 18, '031524': 19, '301524': 18, '321504': 19, '310524': 17, '314520': 16, '321540': 20, '321054': 20, '021354': 19, '201354': 18, '251304': 17, '210354': 19, '214350': 18, '214305': 17, '204315': 16, '214035': 18, '014235': 17, '240315': 15,'024315': 15, '324015': 14, '245310': 14, '245301': 13, '205341': 14, '245031': 12, '045231': 11, '250341': 15, '025341': 15, '325041': 14, '251340': 16, '251034': 18, '051234': 17, '320541': 19, '510234': 15, '514230': 14, '514023': 14, '014523': 13, '250134': 9, '140523': 13, '143520': 14, '143502': 15, '103542': 16, '143052': 16, '043152': 17, '403152': 18, '453102': 19, '430152': 19, '432150': 20, '432105': 19, '402135': 18, '432015': 18, '032415': 17, '420135': 19, '042135': 17, '142035': 16, '425130': 20, '425103': 19, '405123': 20, '425013': 18, '025413': 17, '450123': 21, '045123': 19, '145023': 18, '453120': 20, '453012': 18, '053412': 17, '503412': 16, '513402': 15, '530412': 17, '532410': 18, '532401': 17, '502431': 16, '532041': 18, '032541': 19, '520431': 15, '052431': 15, '452031': 14, '521430': 14, '521403': 13, '501423': 12, '521043': 14, '021543': 13, '510423': 13, '051423': 11, '451023': 10, '513420': 14, '513042': 16, '013542': 17, '130542': 17, '132540': 16, '132054': 14, '032154': 13, '510342': 13, '320154': 13, '324150': 14, '140235': 17, '145230': 18, '231045': 16, '031245': 15, '301245': 14, '341205':15, '310245': 13, '315240': 12, '341250': 16, '341025': 14, '041325': 13, '340251': 15, '314052': 16, '014352': 15, '530124': 11, '140352': 15, '142350': 16, '320415': 15, '325410': 14, '450231': 11, '451230': 10, '210543': 13, '213540': 14, '542013': 8, '042513': 7}
        #self._span()
        c = self._c(board)
        #print (self._answer)
        if c not in self._answer:
            return -1
        n = self._answer[c]
        return n
        
s = Solution()
n = s.slidingPuzzle([[0,1,3],[2,4,5]])
print (n)