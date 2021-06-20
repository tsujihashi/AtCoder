import os
import glob
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from  collections import Counter

def count_solved_problems():
    AC = []
    TLE = []
    WA = []
    RE = []
    dirs = glob.glob('*/')
    for d in dirs:
        problems = glob.glob(d + '/*')
        for p in problems:
            lev = p.replace(d, '').split('_')[0]
            if '_AC' in p:
                AC.append(lev)
            if '_TLE' in p:
                TLE.append(lev)
            if '_WA' in p:
                WA.append(lev)
            if '_RE' in p:
                RE.append(lev)
    print('AC:  {0}\n'
          'TLE: {1}\n'
          'WA:  {2}\n'
          'RE:  {3}\n'.format(
        Counter(AC), Counter(TLE), Counter(WA), Counter(RE)
    ))
    # DataFrameを作成
    # Matplotlibで描画


if __name__ == '__main__':
    count_solved_problems()