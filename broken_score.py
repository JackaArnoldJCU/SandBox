"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
score = float(input("Enter score: "))


def main(score):

    if score > 100:
        print("Invalid score")
    elif score > 50:
        print("Passable")
    elif score > 90:
        print("Excellent")
    elif score < 50:
        print("Bad")
    else:
        print("Invalid score")


main(score)


def random_number():

    random_score = random.randint(0,100)
    main(random_score)


random_number()
