# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:54:49 2021

@author: Clau
"""

import numpy as np
import pandas as pd

#El Espino
#HI
HI_ES = pd.read_csv('HI_El_Espino.csv') 
HI_ES.columns = ['T' , 'W'] 
HI_ES_Kwh = (((HI_ES['W'].sum())/60)/1000)
print(HI_ES_Kwh)

#HMI
df2 = pd.read_csv('HMI_El_Espino.csv') 
df2.columns = ['T' , 'W'] 
HMI_Kwh = (((df2['W'].sum())/60)/1000)
print(HMI_Kwh)

#LMI
df3 = pd.read_csv('LMI_El_Espino.csv') 
df3.columns = ['T' , 'W'] 
LMI_Kwh = (((df3['W'].sum())/60)/1000)
print(LMI_Kwh)

#LI
df4 = pd.read_csv('LI_El_Espino.csv') 
df4.columns = ['T' , 'W'] 
LI_Kwh = (((df4['W'].sum())/60)/1000)
print(LI_Kwh)

df = pd.DataFrame()
df['Income category'] = ['HI' , 'HMI' , 'LMI' , 'LI']
df['Kwh/month'] = [HI_Kwh , HMI_Kwh , LMI_Kwh , LI_Kwh]
print(df)

import matplotlib.pyplot as plt
df = pd.DataFrame({'Income category':['HI' , 'HMI' , 'LMI' , 'LI'], 'Kwh/month': [154, 75, 8, 7]})
ax = df.plot.bar(x='Income category', y='Kwh/month', rot=0)
plt.axhline(y=70, xmin=0, xmax=1, color='r')

#El Sena
#HI
