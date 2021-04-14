#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:08:23 2020

@author: alejandrosoto
"""

"""
Created on Fri Feb  8 10:46:25 2019

@author: Alejandro Soto
"""

'''
October_El  SEna Modificado
'''

from core import User, np
User_list = []

#User classes definition
LI = User("low income",1)
User_list.append(LI)


#Appliances definition

#Lower Income
#indoor bulb
LI_indoor_bulb = LI.Appliance(LI,3,7,3,370,0.24,90)
LI_indoor_bulb.windows([1200,1440],[0,30],0.13)

#outdoor bulb
LI_outdoor_bulb = LI.Appliance(LI,2,13,2,284,0.24,70)
LI_outdoor_bulb.windows([1200,1440],[0,30],0.2)

#TV
LI_TV = LI.Appliance(LI,1,60,3,480,0.16,77)
LI_TV.windows([0,1440],[660,1170],0.2,[720,840])

#phone chargeri
LI_Phone_charger = LI.Appliance(LI,2,5,3,230,0.26,60)
LI_Phone_charger.windows([0,1440],[720,1320],0.35,[660,930])

#freezer
LI_Freezer = LI.Appliance(LI,1,200,1,1160,0,30,'yes',3)
LI_Freezer.windows([0,1440],[0,0])
LI_Freezer.specific_cycle_1(200,20,5,10)
LI_Freezer.specific_cycle_2(200,15,5,15)
LI_Freezer.specific_cycle_3(200,10,5,20)
LI_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])
