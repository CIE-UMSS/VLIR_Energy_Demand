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

if (Alt < 2000): 
    print('H1 = User("low income",LI)'
    print("H1:" , LI)
    print("H2:" , HI)
    
else:
    print("Highlands")
    print("H3:" , LI)
    print("H4:" , HI)

HI = User("high income",11)
User_list.append(HI)



#Altitude

    
    
"""
Social Services Facilities
"""
#Health facilities
if (P < 500):
    print("Inssuficient population. Asses the distance from other community")
    if (Dist < 2):
        print("No health facility")
    else:
        print("1 health post")
elif (500 < P <1000):
    print("1 health post")
else:
    print("1 health center")
    
#Schools
if (P < 100):
    print("Inssuficient population. Asses the distance from other community")
    if (Dist < 1):
        print("No school")
    else:
        print("1 School type A")
elif (100 < P < 500):
    print("1 School type B")
else:
    print("1 school type C") 
    
#Public lighting
PL = P/10
print(" Public lamp posts:", PL)

#Potable water system
PW = 
print("Water pumps:", PW)


"""
Income Generating Activities
"""
#Agriculture 
"""
if (Alt < 3000):
    print(" ")
    if (Alt > 2000):
        print("Agroproductive zone: Valleys")
        APU2 = P/10
        print("Number of APU2:", APU2)
    elif(Alt > 1000):
        print("Agroproductive zone: Gran Chaco")
    else:
        print("Agroproductive zone: Amazonia")
else:
    print("Agroproductive zone: Highlands")
    APU1 = P/10
    print("Number of APU1:", APU1)
"""
if (Alt > 3000):
    print("Agroproductive zone: Highlands")
elif (1500 < Alt < 3000):
    print("Agroproductive zone: Valleys")
else:
    print("Three posibilities: Gran Chaco, Tropical lowlands and Amazonia")    
    
#Commerce (Grocery Stores, Restaurants, Entertainmet bussiness, Workshops)
if (Alt > 2000)  :
    R1 = P/7
    print("Restaurants:", R1)
    GS1 = P/7
    print("Grocery Stores:", GS1)
    EB1 = P/7
    print("Entertainment bussiness:", EB1)
    WS1 = P/7
    print("Workshops:", WS1)
else:
    R2 = P/7
    print("Restaurants:", R1)
    GS2 = P/7
    print("Grocery Stores:", GS1)
    EB2 = P/7
    print("Entertainment bussiness:", EB1)
    WS2 = P/7
    print("Workshops:", WS1)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
