"""
Program: average_score_2.py
Author: Kelly Smith
Last date updated: 09/09/2019

Program to find the average of three numbers
"""


def average(scores):
    score_1 = input("enter first score")
    score_2 = input("enter second score")
    score_3 = input("enter third score")
    x = int(score_1)
    y = int(score_2)
    z = int(score_3)
    scores = [x, y, z]
    return sum(scores) / len(scores)


def scores(args):
    pass


print(average(scores))
