#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ClaudiaLSS
Raqaypampa.
"""

from core import User, np
User_list = []
#User classes definition

HI = User("high income",1)
User_list.append(HI)


#High-Income

#indoor bulb
HI_indoor_bulb = HI.Appliance(HI,3,7,1,320,0.6,190)
HI_indoor_bulb.windows([1080,1440],[0,0])

#outdoor bulb
HI_outdoor_bulb = HI.Appliance(HI,1,13,1,340,0.1,300)
HI_outdoor_bulb.windows([1100,1440],[0,0])

#Radio
HI_Radio = HI.Appliance(HI,1,7,1,280,0.3,110)
HI_Radio.windows([420,708],[0,0])

#tv
HI_TV = HI.Appliance(HI,1,60,3,300,0.38,114)
HI_TV.windows([1140,1440],[651,1139],0.35,[300,650])

#phone charger
HI_Phone_charger = HI.Appliance(HI,2,5,3,250,0.4,95)
HI_Phone_charger.windows([1190,1440],[0,420],0.35,[421,1189])

#freezer
HI_Freezer = HI.Appliance(HI,2,200,1,1440,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,20,5,10)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([0,0],[0,0],[480,1200],[0,0],[0,299],[1201,1440])

#water_heater
HI_Water_heater = HI.Appliance(HI,1,150,1,60,0.05,30)
HI_Water_heater.windows([0,1440],[0,0])
'''
Appliances of services in  HI household
'''

HI_Welder = HI.Appliance(HI,1,5500,1,60,0.5,30,occasional_use = 0.3)
HI_Welder.windows([0,1440],[0,0])

#grinder***
HI_Grinder = HI.Appliance(HI,1,750,1,480,0.125,60)
HI_Grinder.windows([0,1440],[0,0])

#dryer
HI_Dryer = HI.Appliance(HI,1,750,1,60,0.5,30)
HI_Dryer.windows([0,1440],[0,0])


