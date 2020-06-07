#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:26:12 2020

@author: aaderinto
"""
no_of_tries = 3
attempts = 0
score = 1
import csv, sys


infile = sys.argv[1]
data = open(infile)
question_prompts = csv.reader(data)
for questions in question_prompts:
    if attempts < no_of_tries:
        print(questions[0])
        print("a",questions[1])
        print("b",questions[2])
        print("c",questions[3])  
        print("")
        answer = input("Please enter your answer here: ").upper()
        print("")
        attempts = attempts + 1
        if answer == " ":
            break
        elif answer == questions[4]:
            score = score + 1
print("Your score is",score)
data.close()
