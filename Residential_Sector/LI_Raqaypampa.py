#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ClaudiaLSS
Raqaypampa.
"""

from core import User, np
User_list = []
#User classes definition

LI = User("low income",1)
User_list.append(LI)


#Lower Income
#indoor bulb
LI_indoor_bulb = LI.Appliance(LI,3,7,2,287,0.4,124)
LI_indoor_bulb.windows([1153,1440],[0,300],0.5)

#outdoor bulb
LI_outdoor_bulb = LI.Appliance(LI,1,13,1,243,0.3,71)
LI_outdoor_bulb.windows([1197,1440],[0,0])

#radio
LI_Radio = LI.Appliance(LI,1,7,2,160,0.3,49)
LI_Radio.windows([480,840],[841,1200],0.5)

#TV
LI_TV = LI.Appliance(LI,1,100,3,250,0.3,74)
LI_TV.windows([1170,1420],[551,1169],0.3,[300,550])

#phone charger
LI_Phone_charger = LI.Appliance(LI,2,5,3,200,0.4,82)
LI_Phone_charger.windows([1020,1440],[0,420],0.3,[720,1019])

#Washing machine
LI_Whasing_machine = LI.Appliance(LI,1,500,1,10,0.1,5, occasional_use = 0.03)
LI_Whasing_machine.windows([600,780],[0,0])

#freezer
LI_Freezer = LI.Appliance(LI,2,200,1,1440,0,30,'yes',3)
LI_Freezer.windows([0,1440],[0,0])
LI_Freezer.specific_cycle_1(200,20,5,10)
LI_Freezer.specific_cycle_2(200,15,5,15)
LI_Freezer.specific_cycle_3(200,10,5,20)
LI_Freezer.cycle_behaviour([0,0],[0,0],[480,1200],[0,0],[0,299],[1201,1440])

#DVD
LI_DVD = LI.Appliance(LI,1,8,3,220,0.2,37)                                                                  
LI_DVD.windows([1200,1440],[840,1080],0.3,[720,940])

#water_pump
LI_Water_pump = LI.Appliance(LI,1,250,2,37.5,0.47,17.5)
LI_Water_pump.windows([420,450],[960,1020],0.5)

#blender
LI_Blender = LI.Appliance(LI,1,350,2,20,0.375,7.5)
LI_Blender.windows([900,1020],[420,600],0.5)

#iron
LI_Iron = LI.Appliance(LI,1,1000,2,22.5,0.5,10,occasional_use =0.03)
LI_Iron.windows([420,480],[720,780],0.5)

#mill
LI_Mill = LI.Appliance(LI,1,745,2,90,0.48,43, occasional_use = 0.08)
LI_Mill.windows([600,690],[960,1020],0.5)

#Blender
LI_Blender = LI.Appliance(LI,1,350,2,20,0.375,7.5)
LI_Blender.windows([420,480],[720,780],0.5)



