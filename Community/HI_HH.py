# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:46:25 2019

@author: Claudia
"""


from core import User, np
User_list = []

#User classes definition


HH = User("household",1)
User_list.append(HH)


#Appliances definition

#Higher-Middle Income
HH_indoor_bulb = HH.Appliance(HH,5,7,2,120,0.2,10)
HH_indoor_bulb.windows([1082,1440],[0,30],0.35)

HH_outdoor_bulb = HH.Appliance(HH,2,13,2,600,0.2,10)
HH_outdoor_bulb.windows([0,330],[1082,1440],0.35)

HH_TV = HH.Appliance(HH,1,60,2,120,0.1,5)
HH_TV.windows([1082,1440],[0,60],0.35)

HH_DVD = HH.Appliance(HH,1,8,2,40,0.1,5)
HH_DVD.windows([1082,1440],[0,60],0.35)

HH_Antenna = HH.Appliance(HH,1,8,2,80,0.1,5)
HH_Antenna.windows([1082,1440],[0,60],0.35)

HH_Radio = HH.Appliance(HH,1,36,2,60,0.1,5)
HH_Radio.windows([390,450],[1082,1260],0.35)

HH_Phone_charger = HH.Appliance(HH,4,2,2,300,0.2,5)
HH_Phone_charger.windows([1110,1440],[0,30],0.35)

HH_Freezer = HH.Appliance(HH,1,200,1,1440,0,30, 'yes',2)
HH_Freezer.windows([0,1440],[0,0])
HH_Freezer.specific_cycle_1(5,15,200,15)
HH_Freezer.specific_cycle_2(200,10,5,20)
HH_Freezer.cycle_behaviour([480,1200],[0,0],[0,479],[1201,1440])

HH_Mixer = HH.Appliance(HH,1,50,3,30,0.1,1, occasional_use = 0.33)
HH_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

