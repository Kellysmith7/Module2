"""
Program: average_score_2.py
Author: Kelly Smith
Last date updated: 09/17/2019

Program to find the average of three numbers
"""


def average():
    score_1 = input("enter first score ")
    score_2 = input("enter second score ")
    score_3 = input("enter third score ")
    x = int(score_1)
    y = int(score_2)
    z = int(score_3)
    scores = [x, y, z]
    return sum(scores) / len(scores)


if __name__ == '__main__':
    first_name = input("Please enter first name ")
    last_name = input("Please enter last name ")
    age = input("Please enter age ")
    print(last_name + ", " + first_name + " " + "Age: " + age + " " + "Average Score: % 5.2f" % average())
