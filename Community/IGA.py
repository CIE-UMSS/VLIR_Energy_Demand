# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:31:57 2021

@author: Clau
"""

#Income Generating Activities

#User class definition
from core import User, np
User_list = []

GS = User("Grocery Store",1)
User_list.append(GS)

Rest= User("restaurant", 1)
User_list.append(Rest)

EB = User("Entertainment bussiness", 1)
User_list.append(EB)

WS = User("workshop", 1)
User_list.append(WS)

APU1 = User("Agroproductive Unit 1")
User_list.append(APU1)

APU2 = User("Agroproductive Unit 2")
User_list.append(APU2)

APU3 = User("Agroproductive Unit 3")
User_list.append(APU3)

#Appliances definition
#Grocery Store

GS_indoor_bulb = GS.Appliance(GS,2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(GS,1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)
    
GS_freezer = GS.Appliance(GS,1,200,1,1440,0,30,'yes',3)
GS_freezer.windows([0,1440],[0,0])
GS_freezer.specific_cycle_1(200,20,5,10)
GS_freezer.specific_cycle_2(200,15,5,15)
GS_freezer.specific_cycle_3(200,10,5,20)
GS_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

GS_Radio = GS.Appliance(GS,1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

#Restaurant

Rest_indoor_bulb = Rest.Appliance(Rest,2,7,2,120,0.2,10)
Rest_indoor_bulb.windows([1107,1440],[0,30],0.35)

Rest_Blender = Rest.Appliance(Rest,1,350,2,20,0.375,7.5)
Rest_Blender.windows([420,480],[720,780],0.5)

Rest_freezer = Rest.Appliance(Rest,1,200,1,1440,0,30,'yes',3)
Rest_freezer.windows([0,1440],[0,0])
Rest_freezer.specific_cycle_1(200,20,5,10)
Rest_freezer.specific_cycle_2(200,15,5,15)
Rest_freezer.specific_cycle_3(200,10,5,20)
Rest_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#Workshop

WS_indoor_bulb = Rest.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30,occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0])

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.125,60)
WS_grinding_machine.windows([0,1440],[0,0])

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([390,450],[1140,1260],0.35)




