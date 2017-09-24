#! /usr/local/bin/python3
# import os
# import shutil

for i in range(1, 10):
    sample = open(
     'Friends Season 9 Episode 0' + str(i) + ' - string' + str(i) + '.avi', 'w'
     )
    sample.close()

for i in range(10, 23):
    sample = open(
     'Friends Season 9 Episode ' + str(i) + ' - string' + str(i) + '.avi', 'w')
    sample.close()

sample = open(
 'Friends Season 09 Episode 23 & 24 - The One in Barbados.avi', 'w')
sample.close()
