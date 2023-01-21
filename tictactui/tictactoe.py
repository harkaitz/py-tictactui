"""
Usage: tictactoe ARGS...

The classic TicTacToe game that follows the UNIX philosophy.

    -h      : Print this help.
    -v      : Show version.
    -m MOVE : Specify a move, ie 'a1'.
    -M      : Specify all posible moves.
    -i      : Select a move using the Minimax algorithm.
    -a      : Apply specified moves.
"""

from .ttt     import Ttt
from .minimax import minimax
import os
import io
import sys
import getopt
VERSION = "0.1"
COPYRIGHT_LINE = """
Bug reports, feature requests to gemini|https://harkadev.com/oss
Copyright (c) 2023 Harkaitz Agirre, harkaitz.aguirre@gmail.com
"""
START = """
turn: x
%
  1 2 3
a| | | |
b| | | |
c| | | |
.
"""


def tictactoe_main():
    ttt         = Ttt()
    moves       = []
    moves_apply = False
    moves_print = False
    stream      = sys.stdin
    opts, args  = getopt.getopt(sys.argv[1:], "hvgm:aMi")
    for optopt, optarg in opts:
        if optopt == "-h":
            sys.stdout.write(__doc__.strip()+"\n"+COPYRIGHT_LINE)
            sys.exit(0)
        elif optopt == "-v":
            sys.stdout.write(VERSION+"\n")
            sys.exit(0)
        elif optopt == "-g":
            stream = io.StringIO(START)
        elif optopt == "-m":
            moves.append(optarg)
        elif optopt == "-i":
            moves.append("minimax")
        elif optopt == "-a":
            moves_apply = True
        elif optopt == "-M":
            moves_print = True
    ttt.read(stream)
    if moves_apply: 
        for move in moves:
            if move == 'minimax':
                move, value, count = minimax(ttt, ttt.getTurn(), MAX=1, MIN=-1)
                if move is None:
                    break
                sys.stdout.write("minimax: "+move+
                                 " "+str(value)+
                                 " "+str(count)+
                                 "\n")
            ttt.applyMove(move)
        moves = []
    if moves_print:
        for move in ttt.getMoves():
            sys.stdout.write("move: "+move+"\n")
    
    ttt.write(sys.stdout)
