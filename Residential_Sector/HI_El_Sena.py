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
HI = User("high income",1)
User_list.append(HI)


#Appliances definition
#High-Income
#indoor bulb
HI_indoor_bulb = HI.Appliance(HI,3,7,2,360,0.3,108)
HI_indoor_bulb.windows([1170,1440],[0,30],0.5)

#outdoor bulb
HI_outdoor_bulb = HI.Appliance(HI,2,13,3,324,0.3,96)
HI_outdoor_bulb.windows([1170,1440],[0,30],0.5)

#tv
HI_TV = HI.Appliance(HI,1,60,2,469.8,0.18,84)
HI_TV.windows([870,1020],[1200,1380],0.5)

#phone charger
HI_Phone_charger = HI.Appliance(HI,2,5,1,240,0.25,1)
HI_Phone_charger.windows([1200,1440],[0,0])

#freezer
HI_Freezer = HI.Appliance(HI,2,200,1,746,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,20,5,10)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#mixer
HI_Mixer = HI.Appliance(HI,1,50,1,45,1,45,occasional_use = 0.33)
HI_Mixer.windows([420,660],[0,0])

#fan
HI_Fan = HI.Appliance(HI,1,17.5,1,220,0.27,60)
HI_Fan.windows([720,1080],[0,0])


