#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ClaudiaLSS

"""

from core import User, np
User_list = []

"""
Residential sector
"""

#User classes definition

HHI = User("Highlands high income household",1)
User_list.append(HHI)


#High Income
#indoor bulb
HHI_indoor_bulb = HHI.Appliance(HHI,4,7,2,287,0.4,124)
HHI_indoor_bulb.windows([1153,1440],[0,300],0.5)

#outdoor bulb
HHI_outdoor_bulb = HHI.Appliance(HHI,2,13,1,243,0.3,71)
HHI_outdoor_bulb.windows([1197,1440],[0,0])

#radio
HHI_Radio = HHI.Appliance(HHI,1,7,2,160,0.3,49)
HHI_Radio.windows([480,840],[841,1200],0.5)

#TV
HHI_TV = HHI.Appliance(HHI,1,100,3,250,0.3,74)
HHI_TV.windows([1170,1420],[551,1169],0.3,[300,550])

#phone charger
HHI_Phone_charger = HHI.Appliance(HHI,4,5,3,200,0.4,82)
HHI_Phone_charger.windows([1020,1440],[0,420],0.3,[720,1019])

#freezer
HHI_Freezer = HHI.Appliance(HHI,2,200,1,1440,0,30,'yes',3)
HHI_Freezer.windows([0,1440],[0,0])
HHI_Freezer.specific_cycle_1(200,20,5,10)
HHI_Freezer.specific_cycle_2(200,15,5,15)
HHI_Freezer.specific_cycle_3(200,10,5,20)
HHI_Freezer.cycle_behaviour([0,0],[0,0],[480,1200],[0,0],[0,299],[1201,1440])

#blender
HHI_Blender = HHI.Appliance(HHI,1,350,2,20,0.375,7.5)
HHI_Blender.windows([900,1020],[420,600],0.5)

#iron
HHI_Iron = HHI.Appliance(HHI,1,1000,2,22.5,0.5,10,occasional_use =0.03)
HHI_Iron.windows([420,480],[720,780],0.5)

#water_pump
HHI_Water_pump = HHI.Appliance(HHI,1,250,2,37.5,0.47,17.5)
HHI_Water_pump.windows([420,450],[960,1020],0.5)



