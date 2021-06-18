# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:46:25 2019

@author: ClaudiaLSS
"""

from core import User, np
User_list = []

#User classes definition

LLI = User("Lowlands low income household",1)
User_list.append(LLI)


#Appliances definition

LLI_indoor_bulb = LLI.Appliance(LLI,3,7,2,120,0.2,10)
LLI_indoor_bulb.windows([1082,1440],[0,30],0.35)

LLI_outdoor_bulb = LLI.Appliance(LLI,1,13,2,600,0.2,10)
LLI_outdoor_bulb.windows([0,330],[1082,1440],0.35)

LLI_TV = LLI.Appliance(LLI,1,60,3,90,0.1,5)
LLI_TV.windows([750,840],[1082,1440],0.35,[0,30])

LLI_Antenna = LLI.Appliance(LLI,1,8,3,60,0.1,5)
LLI_Antenna.windows([750,840],[1082,1440],0.35,[0,30])

LLI_Phone_charger = LLI.Appliance(LLI,2,2,1,300,0.2,5)
LLI_Phone_charger.windows([1080,1440],[0,0],0.35)

