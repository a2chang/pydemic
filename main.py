from sys import path as syspath
from os import path as ospath
import os
path = ospath.join(os.getcwd(), '../networkx/')
syspath.append(path)

import pydemic


def main():
    game = pydemic.Game(num_players=4, num_epidemic_cards=5)
    game.game_setup()


if __name__ == '__main__':
    main()
