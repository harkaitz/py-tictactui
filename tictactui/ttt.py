from .board import Board
import re
import copy

wins = [
    [ (0,0), (0,1), (0,2) ],
    [ (1,0), (1,1), (1,2) ],
    [ (2,0), (2,1), (2,2) ],

    [ (0,0), (1,0), (2,0) ],
    [ (0,1), (1,1), (2,1) ],
    [ (0,2), (1,2), (2,2) ],

    [ (0,0), (1,1), (2,2) ],
    [ (2,0), (1,1), (0,2) ],
]

class Ttt (Board):
    def getWinner(self) -> str:
        for l in wins:
            p1 = self.pieces.get(l[0])
            p2 = self.pieces.get(l[1])
            p3 = self.pieces.get(l[2])
            if p1 is None or p2 is None or p3 is None:
                continue
            if p1 == p2 and p2 == p3:
                return p1
        return None
    def getValue(self,player: str) -> int:
        w = self.getWinner()
        if w is None:
            return 0
        elif w == player:
            return 1
        else:
            return -1
    def getMoves(self):
        if self.getWinner() is None:
            for x in range(0, self.X):
                for y in range(0, self.Y):
                    if not (x, y) in self.pieces:
                        yield chr(ord('a')+y)+chr(ord('1')+x)
    def applyMove(self, move: str):
        if not self.getWinner() is None:
            raise Exception("Game over")
        try:
            x = ord(re.search('[1-9]', move).group())-ord('1')
            y = ord(re.search('[a-z]', move).group())-ord('a')
        except:
            raise Exception("Invalid move: " + move)
        p = self.getTurn()
        if (x, y) in self.pieces:
            raise Exception("Invalid move: " + move)
        else:
            self.pieces[x,y] = p
        if p == 'o':
            self.turn = 'x'
        else:
            self.turn = 'o'

