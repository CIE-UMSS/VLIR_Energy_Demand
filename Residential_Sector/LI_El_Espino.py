# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:46:25 2019

@author: Lombardi
"""

'''
APRIL
'''
from core import User, np
User_list = []

#User classes definition

LI = User("low income",1)
User_list.append(LI)


#Appliances definition


#Low Income
LI_indoor_bulb = LI.Appliance(LI,3,7,2,120,0.2,10)
LI_indoor_bulb.windows([1082,1440],[0,30],0.35)

LI_outdoor_bulb = LI.Appliance(LI,1,13,2,600,0.2,10)
LI_outdoor_bulb.windows([0,330],[1082,1440],0.35)

LI_TV = LI.Appliance(LI,1,60,3,90,0.1,5)
LI_TV.windows([750,840],[1082,1440],0.35,[0,30])

LI_DVD = LI.Appliance(LI,1,8,3,30,0.1,5)
LI_DVD.windows([750,840],[1082,1440],0.35,[0,30])

LI_Antenna = LI.Appliance(LI,1,8,3,60,0.1,5)
LI_Antenna.windows([750,840],[1082,1440],0.35,[0,30])

LI_Phone_charger = LI.Appliance(LI,3,2,1,300,0.2,5)
LI_Phone_charger.windows([1080,1440],[0,0],0.35)

