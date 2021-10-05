# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:01:53 2021

@author: dhruv
"""

import matplotlib.pyplot as plt
import pandas as pd

#from matplotlib.gridspec import GridSpec


plot=pd.read_excel('D:\Downloads\matches.xlsx')
df=pd.DataFrame(plot)

group= df.groupby('winner').agg('count')
#df.info()


print(group)

plt.bar(df['win_by_runs'], df['team1'])
plt.title("Win by runs")
plt.xlabel("Runs")
plt.ylabel("Teams")

