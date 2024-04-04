from .game import Game
import io
import re

class Board (Game):
    def __init__(self):
        self.turn   = ''
        self.X      = 0
        self.Y      = 0
        self.pieces = dict()
    def getTurn(self) -> str:
        if self.turn != '':
            return self.turn
        else:
            raise Exception("No turn")
    def read(self, fp: io.TextIOWrapper):
        section = 0
        for line in fp:
            line = line.strip()
            if line == '.':
                break
            elif line == '%':
                section = section + 1
            elif section == 0:
                l = re.split(": *", line)
                if len(l) != 2:
                    pass
                elif l[0] == "turn":
                    self.turn = l[1]
                elif l[0] == "move":
                    self.moves.append(l[1])
                else:
                    pass
            elif section == 1:
                l = re.findall("\|[a-zA-Z ]", line)
                if len(l) > 0:
                    x = 0
                    for c in l:
                        if c[1] != ' ':
                            self.pieces[x,self.Y] = c[1]
                        x = x + 1
                    if self.X < x:
                        self.X = x
                    self.Y = self.Y + 1
    def write(self, fp: io.TextIOWrapper):
        if len(self.turn):
            fp.write("turn: " + self.turn + "\n")
        w = self.getWinner()
        if not w is None:
            fp.write("winner: " + w + "\n")
        elif len(list(self.getMoves())) == 0:
            fp.write("winner: n\n")
        fp.write("%\n ")
        for x in range(0, self.X):
            fp.write(" "+chr(ord('1')+x))
        fp.write("\n")
        for y in range(0, self.Y):
            fp.write(chr(ord('a')+y))
            for x in range(0, self.X):
                if (x,y) in self.pieces:
                    p = self.pieces[x,y]
                else:
                    p = ' '
                fp.write("|"+p)
            fp.write("|\n")
        fp.write(".\n")

