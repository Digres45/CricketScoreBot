from CricketScore import CricketScore
from time import sleep

your_team = input("Enter You Team:\t")

while True:
    CricketScore().getScore(your_team)
    sleep(600)