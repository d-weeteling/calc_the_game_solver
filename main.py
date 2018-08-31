#!/usr/bin/python3

from game_configs import configs
from game import Game, Solver

if __name__ == '__main__':
    my_game = Game(**configs[2])
    my_solver = Solver(my_game)
    my_solver.solve()
