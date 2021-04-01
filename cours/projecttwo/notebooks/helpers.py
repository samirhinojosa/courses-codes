# -*- coding: utf-8 -*-
from enum import Enum
import numpy as np


class Strategy(Enum):
    CHANGE = 0
    KEEP = 1
    RANDOM = 2


def play_game(strategy):
    """
    Monty Hall problem function

    To see more in details "The Monty Hall problem"
    https://en.wikipedia.org/wiki/Monty_Hall_problem 

    Args:
        strategy (str): Player strategy based on Class Strategy.

    Returns:
        bool: Result based on player selection.
    """
    doors = np.array([0, 1, 2])
    good_door = np.random.randint(0, 2, size=1)

    # Player choice
    first_choice = np.random.randint(0, 2, size=1)

    # Deleting the door selected by player
    doors = np.delete(doors, np.argwhere(doors == first_choice))

    # The presenter eliminates a door based on player choice
    if first_choice[0] == good_door[0]:
        doors = np.delete(doors, np.random.randint(0, 1, size=1))
    else:
        doors[0] = good_door

    second_choice = 0

    # The second choice is based on strategy
    if strategy == Strategy.CHANGE:
        second_choice = doors[0]
    elif strategy == Strategy.KEEP:
        second_choice == first_choice
    else:
        options_second_choice = np.array([first_choice[0], doors[0]])
        second_choice = np.random.choice(options_second_choice)

    return second_choice == good_door[0]


def play(strategy, tours):
    """
    Call to Monty Hall problem function play_game()

    Args:
        strategy (str): Player strategy based on Class Strategy.
        tours (int): Tours samples.

    Returns:
        bool: Result based on player selection.
    """
    return [ 1 if play_game(strategy) else 0 for i in range(tours)]

def play_with_numpy(tours):
    
    good_doors = np.random.randint(0, 3, size=tours)
    first_choices = np.random.randint(0, 3, size=tours)

    change_player_gains = (good_doors != first_choices).astype(int)
    keep_player_gains = (good_doors == first_choices).astype(int)

    return change_player_gains, keep_player_gains


