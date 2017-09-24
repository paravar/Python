#! /usr/local/bin/python2

""" This script is to rename the files
"Friends Season ## Episode ## - *.avi"
to
"Friends S##E## - *.avi"
Example:
This:
"Friends Season 09 Episode 01 - The One Where No One Proposes.avi"
will be changed to:
"Friends S09e01 - The One Where No One Proposes.avi"
"""

import os
import shutil
import re

series_pattern = re.compile(r'(.*)(Season )(\d{1,2})( Episode )(\d{2})(.*)')
'''
sample_string = "Friends Season 09 Episode 23 & 24 - The One in Barbados.avi"
result = series_pattern.search(sample_string)

for i in range(1, 7):
    print(str(i) + "is: " + result.group(i))
'''

for long_name in os.listdir('.'):
    matched_pattern = series_pattern.search(long_name)
    if matched_pattern is None:
        continue
    series_name = matched_pattern.group(1)
    season = 'S'
    season_number = matched_pattern.group(3)
    episode = 'E'
    episode_number = matched_pattern.group(5)
    episode_name = matched_pattern.group(6)
    short_name = series_name + season + season_number + episode + \
        episode_number + episode_name
    print('renaming %s to %s' % (long_name, short_name))
    shutil.move(long_name, short_name)
