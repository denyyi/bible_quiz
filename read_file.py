#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:57:48 2020

@author: aaderinto
"""

#%%
import csv, sys

filename = sys.argv[1]
"""Reads a CSV file and prints each row, which is a list. """
f = open(filename)
for row in csv.reader(f):
    print(row)
f.close()
