#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ClaudiaLSS

"""

from core import User, np
User_list = []
#User classes definition

HLI = User("Highlands low income household",1)
User_list.append(HLI)


#Lower Income
#indoor bulb
HLI_indoor_bulb = HLI.Appliance(HLI,3,7,2,287,0.4,124)
HLI_indoor_bulb.windows([1153,1440],[0,300],0.5)

#outdoor bulb
HLI_outdoor_bulb = HLI.Appliance(HLI,1,13,1,243,0.3,71)
HLI_outdoor_bulb.windows([1197,1440],[0,0])

#radio
HLI_Radio = HLI.Appliance(HLI,1,7,2,160,0.3,49)
HLI_Radio.windows([480,840],[841,1200],0.5)

#TV
HLI_TV = HLI.Appliance(HLI,1,100,3,250,0.3,74)
HLI_TV.windows([1170,1420],[551,1169],0.3,[300,550])

#phone charger
HLI_Phone_charger = HLI.Appliance(HLI,2,5,3,200,0.4,82)
HLI_Phone_charger.windows([1020,1440],[0,420],0.3,[720,1019])

#freezer
HLI_Freezer = HLI.Appliance(HLI,2,200,1,1440,0,30,'yes',3)
HLI_Freezer.windows([0,1440],[0,0])
HLI_Freezer.specific_cycle_1(200,20,5,10)
HLI_Freezer.specific_cycle_2(200,15,5,15)
HLI_Freezer.specific_cycle_3(200,10,5,20)
HLI_Freezer.cycle_behaviour([0,0],[0,0],[480,1200],[0,0],[0,299],[1201,1440])

#iron
HLI_Iron = HLI.Appliance(HLI,1,1000,2,22.5,0.5,10,occasional_use =0.03)
HLI_Iron.windows([420,480],[720,780],0.5)

#water_pump
HLI_Water_pump = HLI.Appliance(HLI,1,250,2,37.5,0.47,17.5)
HLI_Water_pump.windows([420,450],[960,1020],0.5)





