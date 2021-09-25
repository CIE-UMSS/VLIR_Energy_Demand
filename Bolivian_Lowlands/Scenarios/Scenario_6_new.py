# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:25:06 2021

@author: Clau
"""

'''
Paper: Energy sufficiency, lowlands.
SCENARIO 2
'''

from core import User, np
User_list = []

#Defining users
H1 = User("low income", 120) 
User_list.append(H1)

H2 = User("high income", 6)
User_list.append(H2)

Public_lighting = User("Public lighting ", 2)
User_list.append(Public_lighting)

HP = User("Health post", 1)
User_list.append(HP)

SA = User("School type A", 1)
User_list.append(SA)

Church = User("Church", 1)
User_list.append(Church)

WSS = User("water supply system", 1)
User_list.append(WSS)

Coliseum = User("Coliseum", 1)
User_list.append(Coliseum)

R = User("Restaurant", 1)
User_list.append(R)

GS = User("Grocery Store 1", 2)
User_list.append(GS)

EB = User("Entertainment Business", 3)
User_list.append(EB)

WS = User("Workshop", 2)
User_list.append(WS)

LAU = User("Lowlands agro-productive unit", 1)
User_list.append(LAU)

IW = User("Irrigation Water", 7)
User_list.append(IW)


#Appliances

#Low Income Households
H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H1_TV = H1.Appliance(H1,1,60,3,90,0.1,5)
H1_TV.windows([750,840],[1082,1440],0.35,[0,30])

H1_Antenna = H1.Appliance(H1,1,8,3,90,0.1,5)
H1_Antenna.windows([750,840],[1082,1440],0.35,[0,30])

H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
H1_Phone_charger.windows([1080,1440],[0,0],0.35)

#High income households
H2_indoor_bulb = H2.Appliance(H2,4,7,2,120,0.2,10)
H2_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
H2_outdoor_bulb = H2.Appliance(H2,2,13,2,600,0.2,10)
H2_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H2_TV = H2.Appliance(H2,2,60,2,120,0.1,5)
H2_TV.windows([1082,1440],[0,60],0.35)

H2_DVD = H2.Appliance(H2,1,8,2,40,0.1,5)
H2_DVD.windows([1082,1440],[0,60],0.35)

H2_Antenna = H2.Appliance(H2,1,8,2,80,0.1,5)
H2_Antenna.windows([1082,1440],[0,60],0.35)

H2_Radio = H2.Appliance(H2,1,36,2,60,0.1,5)
H2_Radio.windows([390,450],[1082,1260],0.35)

H2_Phone_charger = H2.Appliance(H2,4,2,2,300,0.2,5)
H2_Phone_charger.windows([1110,1440],[0,30],0.35)

H2_Freezer = H2.Appliance(H2,1,200,1,1440,0,30, 'yes',2)
H2_Freezer.windows([0,1440],[0,0])
H2_Freezer.specific_cycle_1(5,15,200,15)
H2_Freezer.specific_cycle_2(200,10,5,20)
H2_Freezer.cycle_behaviour([480,1200],[0,0],[0,479],[1201,1440])

H2_Mixer = H2.Appliance(H2,1,50,3,30,0.1,1, occasional_use = 0.33)
H2_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

H2_Fan = H2.Appliance(H2,1,171,1,220,0.27,60)
H2_Fan.windows([720,1080],[0,0])

H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
H2_Laptop.windows([960,1200],[0,0])

#Health post
HP_indoor_bulb = HP.Appliance(HP,12,7,2,690,0.2,10)
HP_indoor_bulb.windows([480,720],[870,1440],0.35)

HP_outdoor_bulb = HP.Appliance(HP,1,13,2,690,0.2,10)
HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HP_Phone_charger = HP.Appliance(HP,5,2,2,300,0.2,5)
HP_Phone_charger.windows([480,720],[900,1440],0.35)

HP_TV = HP.Appliance(HP,1,150,2,360,0.1,60)
HP_TV.windows([480,720],[780,1020],0.2)

HP_radio = HP.Appliance(HP,1,40,2,360,0.3,60)
HP_radio.windows([480,720],[780,1020],0.35)

HP_PC = HP.Appliance(HP,1,200,2,300,0.1,10)
HP_PC.windows([480,720],[1050,1440],0.35)

HP_printer = HP.Appliance(HP,1,100,1,60,0.3,10)
HP_printer.windows([540,1020],[0,0],0.35)

HP_fan = HP.Appliance(HP,2,60,1,240,0.2,60)
HP_fan.windows([660,960],[0,0],0.35)

HP_sterilizer_stove = HP.Appliance(HP,1,600,2,120,0.3,30)
HP_sterilizer_stove.windows([540,600],[900,960],0.35)

HP_needle_destroyer = HP.Appliance(HP,1,70,1,60,0.2,10)
HP_needle_destroyer.windows([540,600],[0,0],0.35)

HP_water_pump = HP.Appliance(HP,1,400,1,30,0.2,10)
HP_water_pump.windows([480,510],[0,0],0.35)

HP_Fridge = HP.Appliance(HP,3,150,1,1440,0,30, 'yes',3)
HP_Fridge.windows([0,1440],[0,0])
HP_Fridge.specific_cycle_1(150,20,5,10)
HP_Fridge.specific_cycle_2(150,15,5,15)
HP_Fridge.specific_cycle_3(150,10,5,20)
HP_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

#School A
SA_indoor_bulb = SA.Appliance(SA,6,7,2,120,0.25,30)
SA_indoor_bulb.windows([480,780],[840,1140],0.2)

SA_outdoor_bulb = SA.Appliance(SA,1,13,1,60,0.2,10)
SA_outdoor_bulb.windows([1007,1080],[0,0],0.35)

SA_TV = SA.Appliance(SA,1,60,2,120,0.1,5, occasional_use = 0.5)
SA_TV.windows([480,780],[840,1140],0.2)

SA_radio = SA.Appliance(SA,3,4,2,120,0.1,5, occasional_use = 0.5)
SA_radio.windows([480,780],[840,1140],0.2)

SA_DVD = SA.Appliance(SA,1,8,2,120,0.1,5, occasional_use = 0.5)
SA_DVD.windows([480,780],[840,1140],0.2)

#Public lighting
Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,12,40,2,310,0,300, 'yes', flat = 'yes')
Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)

#Church
Ch_indoor_bulb = Church.Appliance(Church,10,26,1,210,0.2,60,'yes', flat = 'yes')
Ch_indoor_bulb.windows([1200,1440],[0,0],0.1)

Ch_outdoor_bulb = Church.Appliance(Church,7,26,1,240,0.2,60, 'yes', flat = 'yes')
Ch_outdoor_bulb.windows([1200,1440],[0,0],0.1)

Ch_speaker = Church.Appliance(Church,1,100,1,240,0.2,60)
Ch_speaker.windows([1200,1350],[0,0],0.1)

#Water supply system
WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)

#Coliseum
Lights = Coliseum.Appliance(Coliseum,25,150,2,310,0.1,300, 'yes', flat = 'yes')
Lights.windows([0,336],[1110,1440],0.2)

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
R_indoor_bulb = R.Appliance(R,2,7,2,120,0.2,10)
R_indoor_bulb.windows([1107,1440],[0,30],0.35)

R_Blender = R.Appliance(R,1,350,2,20,0.375,5)
R_Blender.windows([420,480],[720,780],0.5)

R_freezer = R.Appliance(R,1,200,1,1440,0,30,'yes',3)
R_freezer.windows([0,1440],[0,0])
R_freezer.specific_cycle_1(200,20,5,10)
R_freezer.specific_cycle_2(200,15,5,15)
R_freezer.specific_cycle_3(200,10,5,20)
R_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#Entertainment Business
EB_indoor_bulb = EB.Appliance(EB,2,7,2,120,0.2,10)
EB_indoor_bulb.windows([1107,1440],[0,30],0.35)

EB_outdoor_bulb = EB.Appliance(EB,1,13,2,600,0.2,10)
EB_outdoor_bulb.windows([0,330],[1107,1440],0.35)

EB_Stereo = EB.Appliance(EB,1,150,2,90,0.1,5, occasional_use = 0.33)
EB_Stereo.windows([480,780],[0,0],0.35)

EB_TV = EB.Appliance(EB,1,60,2,120,0.1,5, occasional_use = 0.5)
EB_TV.windows([480,780],[840,1140],0.2)
    
EB_PC = EB.Appliance(EB,1,50,2,210,0.1,10)
EB_PC.windows([480,780],[840,1140],0.35)

EB_freezer = EB.Appliance(EB,1,200,1,1440,0,30,'yes',3)
EB_freezer.windows([0,1440],[0,0])
EB_freezer.specific_cycle_1(200,20,5,10)
EB_freezer.specific_cycle_2(200,15,5,15)
EB_freezer.specific_cycle_3(200,10,5,20)
EB_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#Workshop
WS_indoor_bulb = WS.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30,occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.125,60,occasional_use = 0.3)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([390,450],[1140,1260],0.35)

#trans
LAU_GD = LAU.Appliance(LAU,1,9360,1,180,0.2,30,occasional_use = 0.33)
LAU_GD.windows([420,1080],[0,0],0.35)

LAU_VW = LAU.Appliance(LAU,1,1170,1,480,0.2,15,occasional_use = 0.82)
LAU_VW.windows([420,1140],[0,0],0.35)

LAU_BT = LAU.Appliance(LAU,1,370,2,900,0.2,180)
LAU_BT.windows([360,930],[1080,1440],0.35)

#Irrigation
IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)