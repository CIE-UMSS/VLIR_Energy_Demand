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

#Entertanment bussiness

EB_Stereo = EB.Appliance(EB,1,150,2,90,0.1,5, occasional_use = 0.33)
EB_Stereo.windows([480,780],[0,0])
    
EB_TV = EB.Appliance(EB,1,60,2,120,0.1,5, occasional_use = 0.5)
EB_TV.windows([480,780],[840,1140],0.2)
        
EB_PC = EB.Appliance(EB,1,50,2,210,0.1,10)
EB_PC.windows([480,780],[840,1140],0.35)

#Workshop

WS_indoor_bulb = Rest.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30,occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0])

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.125,60)
WS_grinding_machine.windows([0,1440],[0,0])

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([390,450],[1140,1260],0.35)

#Agroproductive unit 1

APU1_WP = APU1.Appliance(APU1,1,1700,3,60,0.2,10, occasional_use = 0.33)
APU1_WP.windows([1107,1440],[0,30],0.35)

APU1_GM = APU1.Appliance(APU1,2,7,2,120,0.2,10)
APU1_GM.windows([1107,1440],[0,30],0.35)

APU1_GD = APU1.Appliance(APU1,2,7,2,120,0.2,10)
APU1_GD.windows([1107,1440],[0,30],0.35)

APU1_SM = APU1.Appliance(APU1,2,7,2,120,0.2,10)
APU1_SM.windows([1107,1440],[0,30],0.35)

#Agroproductive unit 2

APU2_WP = APU2.Appliance(APU2,2,7,2,120,0.2,10)
APU2_WP.windows([1107,1440],[0,30],0.35)

APU2_GM = APU2.Appliance(APU2,2,7,2,120,0.2,10)
APU2_GM.windows([1107,1440],[0,30],0.35)

APU2_GD = APU2.Appliance(APU2,2,7,2,120,0.2,10)
APU2_GD.windows([1107,1440],[0,30],0.35)

APU2_VW = APU2.Appliance(APU2,2,7,2,120,0.2,10)
APU2_VW.windows([1107,1440],[0,30],0.35)

APU2_SM = APU2.Appliance(APU2,2,7,2,120,0.2,10)
APU2_SM.windows([1107,1440],[0,30],0.35)

APU2_refrigerator = APU2.Appliance(APU2,2,7,2,120,0.2,10)
APU2_refrigerator.windows([1107,1440],[0,30],0.35)

APU2_CT = APU2.Appliance(APU2,2,7,2,120,0.2,10)
APU2_CT.windows([1107,1440],[0,30],0.35)
#Agroproductive unit 3

APU3_WP = APU3.Appliance(APU3,2,7,2,120,0.2,10)
APU3_WP.windows([1107,1440],[0,30],0.35)


APU3_GD = APU3.Appliance(APU3,2,7,2,120,0.2,10)
APU3_GD.windows([1107,1440],[0,30],0.35)

APU3_VW = APU3.Appliance(APU2,2,7,2,120,0.2,10)
APU3_VW.windows([1107,1440],[0,30],0.35)


APU3_refrigerator = APU3.Appliance(APU3,2,7,2,120,0.2,10)
APU3_refrigerator.windows([1107,1440],[0,30],0.35)

APU3_BT = APU3.Appliance(APU3,2,7,2,120,0.2,10)
APU3_BT.windows([1107,1440],[0,30],0.35)

