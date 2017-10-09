#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__data__ = '2017/9/11'


import os
import sys


PATH = sys.path[0] + '/ALDEn-Ch'


def find_all_txts(dir):
    """
    Get all the paths of .txt documents under specific dir
    """
    everything = [dir + '/' + each for each in os.listdir(dir)]
    # Get all files and dirs
    dirs = [each for each in everything if os.path.isdir(each)]
    # Get all sub_paths for recursion
    result = [each for each in everything if
              os.path.isfile(each) and
              os.path.splitext(each)[1].lower() == '.txt']
    # Filter all .txt documents
    for each in dirs:
        result += find_all_txts(each)
    # Recursion
    return result


# ---[test zone]---
print(PATH)
print(find_all_txts(PATH))

