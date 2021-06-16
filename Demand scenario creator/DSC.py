# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:16:36 2021

@author: Claudia
"""

#Demand Scenario Creator

import numpy as np
import pandas as pd

Alt = int(input("Altitude:")) #altitudeMasl
P = int(input("Population:")) #Population
PPH = int(input("Population per household:"))  #PeoplePerHousehold
PR = float(input("Poverty rate:")) #PovertyRate
Dist = int(input("Distance from the nearest bigger community:")) #DistanceFromAnotherCommunity(hours)


#Users classes definition
#Residential Demand

LI = (round(P/PPH)*PR) #Low Income Household
HI = round(P/PPH) - LI #High Income Household

if (Alt < 2000): #Lowlands
    print('H1 = User("low income",', LI)
    print('User_list.append(H1)')
    print('H2 = User("low income",', HI)
    
else: #highlands
    print('H3 = User("low income",', LI)
    print('User_list.append(H2)')
    print('H4 = User("low income",', HI)

#Health facilities
if (P < 500):
    if (Dist < 2):
        print()
    else:
        print('HP = User("Health post",',1)
        print('User_list.append(HP)')
        
elif (500 < P <1000):
    print('HP = User("Health post",',1)
    print('User_list.append(HP)')
else:
    print('HC = User("Health center",',1)
    print('User_list.append(HC)')
    
#Schools
if (P < 100):
    if (Dist < 1):
        print()
    else:
        print('SA = User("School type A",',1)
        print('User_list.append(SA)')
elif (100 < P < 500):
    print('SB = User("School type B",',1)
    print('User_list.append(SB)')
else:
    print('SC = User("School type C",',1)
    print('User_list.append(SC)')
    
#Public lighting

PL = P/10
print('PL = User("Public lighting ",',PL)
print('User_list.append(PL)')

#Potable water system

if (P<200):
    print()
else: 
    print('PW = User("Potable water system ",',1)
    print('User_list.append(PW)')

"""
Income Generating Activities
"""
     
#Commerce (Grocery Stores, Restaurants, Entertainmet bussiness, Workshops)

if (Alt > 2000)  :
    R1 = P/7
    print('R1 = User("Restaurant 1",',R1)
    print('User_list.append(R1)')
    GS1 = P/7
    print('GS1 = User("Grocery Store 1 ",',GS1)
    print('User_list.append(GS1)')
    EB1 = P/7
    print('EB1 = User("Entertainment bussiness",',EB1)
    print('User_list.append(EB1)')
    WS1 = P/7
    print('WS1 = User("Workshop 1",',WS1)
    print('User_list.append(WS1)')
else:
    R2 = P/7
    print('R2 = User("Restaurant 2",',R2)
    print('User_list.append(R2)')
    GS2 = P/7
    print('GS2 = User("Grocery Store 2",',GS2)
    print('User_list.append(GS2)')
    EB2 = P/7
    print('EB2 = User("Entertainment bussiness 2",',EB2)
    print('User_list.append(EB2)')
    WS2 = P/7
    print("Workshops:", WS2)
    print('WS2 = User("Workshop 2",',WS2)
    print('User_list.append(WS2)')
    
#Agriculture 

if (Alt < 3000):
    print()
    if (Alt > 2000):
        APU2 = P/10
        print('APU2 = User("Agroproductive Unit 2",',APU2)
        print('User_list.append(APU2)')
    elif(Alt < 800):
        print("Agroproductive zone: Gran Chaco")
    else:
        print("Agroproductive zone: Amazonia")
else:
    print("Agroproductive zone: Highlands")
    APU1 = P/10
    print("Number of APU1:", APU1)

"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
