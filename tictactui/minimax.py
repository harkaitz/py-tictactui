from .game import Game
from copy  import deepcopy
import sys


def minimax(game: Game,
            player: str,
            max_depth: int = 9,
            MAX: int =  1000,
            MIN: int = -1000) -> (str, int, int):
    turn       = game.getTurn()
    maximizer  = (player == turn)
    ret_move   = None
    ret_value  = MIN if maximizer else MAX
    ret_count  = 0
    if max_depth > 0:
        for move in game.getMoves():
            new_game = deepcopy(game)
            new_game.applyMove(move)
            ___, new_value, count = minimax(new_game, player, max_depth - 1, MAX, MIN)
            ret_count = ret_count + count
            if maximizer == True and new_value >= ret_value:
                ret_move  = move
                ret_value = new_value
                if ret_value == MAX: break
            elif maximizer == False and new_value <= ret_value:
                ret_move  = move
                ret_value = new_value
                if ret_value == MIN: break
    if ret_move is None:
        return None, game.getValue(player), 1
    else:
        return ret_move, ret_value, ret_count

