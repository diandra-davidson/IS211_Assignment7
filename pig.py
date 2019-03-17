#!/usr/bin/env
# -*- coding: utf-8 -*-
"""IS211 Assignment 7 by Diandra Vega"""


import sys


class Player(object):
    """Players in game of Pig"""
    def __init__(self, score=0):
        """Constructor"""
        self.score = score

    def score(self, points=0):
        """Tally player score"""
        self.score += points
        result = self.score
        return result


class playPig(object):
    """Play a game of Pig"""

    def status(self, firstscore, secondscore):
        """Check if any player hit a score of 100"""
        if firstscore >= 100:
            print "Player one wins!"
            sys.exit(1)
        elif secondscore >= 100:
            print "Player two wins!"
            sys.exit(1)
        else:
            return False


    def playGame(self, playerone, playertwo):
        """Roll dice"""
        if self.status(playerone, playertwo) == False:#
            roll = "roll the dice!"
            return roll
        else:
            return "game over!"


#playerone = Player()
#playertwo = Player()
#playgame = playPig()
#
#
#print playgame.status((playerone.score + 100), playertwo.score)


