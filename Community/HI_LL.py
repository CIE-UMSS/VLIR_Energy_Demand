# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:46:25 2019

@author: ClaudiaLSS
"""


from core import User, np
User_list = []

#User classes definition


LHI = User("lowlands high income household",1)
User_list.append(LHI)


#Appliances definition

LHI_indoor_bulb = LHI.Appliance(LHI,4,7,2,120,0.2,10)
LHI_indoor_bulb.windows([1082,1440],[0,30],0.35)

LHI_outdoor_bulb = LHI.Appliance(LHI,2,13,2,600,0.2,10)
LHI_outdoor_bulb.windows([0,330],[1082,1440],0.35)

LHI_TV = LHI.Appliance(LHI,2,60,2,120,0.1,5)
LHI_TV.windows([1082,1440],[0,60],0.35)

LHI_DVD = LHI.Appliance(LHI,1,8,2,40,0.1,5)
LHI_DVD.windows([1082,1440],[0,60],0.35)

LHI_Antenna = LHI.Appliance(LHI,1,8,2,80,0.1,5)
LHI_Antenna.windows([1082,1440],[0,60],0.35)

LHI_Radio = LHI.Appliance(LHI,1,36,2,60,0.1,5)
LHI_Radio.windows([390,450],[1082,1260],0.35)

LHI_Phone_charger = LHI.Appliance(LHI,4,2,2,300,0.2,5)
LHI_Phone_charger.windows([1110,1440],[0,30],0.35)

LHI_Freezer = LHI.Appliance(LHI,1,200,1,1440,0,30, 'yes',2)
LHI_Freezer.windows([0,1440],[0,0])
LHI_Freezer.specific_cycle_1(5,15,200,15)
LHI_Freezer.specific_cycle_2(200,10,5,20)
LHI_Freezer.cycle_behaviour([480,1200],[0,0],[0,479],[1201,1440])

LHI_Mixer = LHI.Appliance(LHI,1,50,3,30,0.1,1, occasional_use = 0.33)
LHI_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

LHI_Fan = LHI.Appliance(LHI,1,17.5,1,220,0.27,60)
LHI_Fan.windows([720,1080],[0,0])

LHI_Laptop = LHI.Appliance(LHI,1,70,1,90,0.3,30)
LHI_Laptop.windows([960,1200],[0,0])
