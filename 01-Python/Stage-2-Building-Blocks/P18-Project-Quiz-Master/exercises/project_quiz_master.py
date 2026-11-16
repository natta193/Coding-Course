import csv
import os
import random
import time

SAMPLE = """category,question,a,b,c,d,answer
Science,What is H2O?,Salt,Water,Gold,Air,b
Science,What planet is closest to the Sun?,Venus,Earth,Mercury,Mars,c
Computing,What does CPU stand for?,Central Processing Unit,Computer Power Unit,Core Program Utility,Central Program Unit,a
Computing,How many bits in a byte?,4,8,16,32,b
Geography,Capital of Australia?,Sydney,Melbourne,Canberra,Perth,c
Geography,Longest river in the world?,Amazon,Thames,Nile,Yangtze,c
"""

if not os.path.exists("questions.csv"):
    with open("questions.csv", "w") as f:
        f.write(SAMPLE)


def load_questions(filename):
    """Return a list of question dictionaries."""
    pass
