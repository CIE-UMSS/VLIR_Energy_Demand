# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:12:42 2021

@author: Clau
"""

from core import User, np
User_list = []

#Defining users

H2 = User("high income", 252)
User_list.append(H2)

HC = User("Health center", 1)
User_list.append(HC)

SC = User("School type C", 1)
User_list.append(SC)

Church = User("Church", 1)
User_list.append(Church)

Public_lighting = User("Public lighting ", 12)
User_list.append(Public_lighting)

WSS = User("water supply system", 2)
User_list.append(WSS)

Coliseum = User("Coliseum", 1)
User_list.append(Coliseum)

R = User("Restaurant", 2)
User_list.append(R)

GS = User("Grocery Store 1", 4)
User_list.append(GS)

EB = User("Entertainment Business", 5)
User_list.append(EB)

WS = User("Workshop", 5)
User_list.append(WS)

LAU = User("Lowlands agro-productive unit", 3)
User_list.append(LAU)

IW = User("Irrigation Water", 15)
User_list.append(IW)

#Appliances

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
H2_Fan.windows([720,1080],[0,0],0.35)

H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
H2_Laptop.windows([960,1200],[0,0],0.35)

#Health Center
HC_indoor_bulb = HC.Appliance(HC,20,7,2,690,0.2,10)
HC_indoor_bulb.windows([480,720],[870,1440],0.35)

HC_outdoor_bulb = HC.Appliance(HC,5,13,2,690,0.2,10)
HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HC_Phone_charger = HC.Appliance(HC,5,2,2,300,0.2,5)
HC_Phone_charger.windows([480,720],[900,1440],0.35)

HC_TV = HC.Appliance(HC,2,150,2,360,0.1,60)
HC_TV.windows([480,720],[780,1020],0.2)

HC_radio = HC.Appliance(HC,5,40,2,360,0.3,60)
HC_radio.windows([480,720],[780,1020],0.35)

HC_PC = HC.Appliance(HC,2,200,2,300,0.1,10)
HC_PC.windows([480,720],[1050,1440],0.35)

HC_printer = HC.Appliance(HC,2,100,1,60,0.3,10)
HC_printer.windows([540,1020],[0,0],0.35)

HC_fan = HC.Appliance(HC,2,60,1,240,0.2,60)
HC_fan.windows([660,960],[0,0],0.35)

HC_sterilizer_stove = HC.Appliance(HC,3,600,2,120,0.3,30)
HC_sterilizer_stove.windows([540,600],[900,960],0.35)

HC_needle_destroyer = HC.Appliance(HC,1,70,1,60,0.2,10)
HC_needle_destroyer.windows([540,600],[0,0],0.35)

HC_water_pump = HC.Appliance(HC,1,400,1,30,0.2,10)
HC_water_pump.windows([480,510],[0,0],0.35)

HC_Fridge = HC.Appliance(HC,4,150,1,1440,0,30, 'yes',3)
HC_Fridge.windows([0,1440],[0,0])
HC_Fridge.specific_cycle_1(150,20,5,10)
HC_Fridge.specific_cycle_2(150,15,5,15)
HC_Fridge.specific_cycle_3(150,10,5,20)
HC_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

HC_microscope = HC.Appliance(HC,2,3,2,120,0.2,10)
HC_microscope.windows([480,720],[840,960],0.35)

HC_shower = HC.Appliance(HC,3,3000,2,120,0.1,15)
HC_shower.windows([360,720],[780,1400],0.35)

HC_heater = HC.Appliance(HC,2,1500,2,180,0.25,60)
HC_heater.windows([369,720],[1080,1260],0.35)

HC_dental_compresor = HC.Appliance(HC,2,500,2,60,0.15,10)
HC_dental_compresor.windows([480,720],[840,1260],0.2)

HC_centrifuge = HC.Appliance(HC,2,100,1,60,0.15,10)
HC_centrifuge.windows([480,720],[0,0],0.35)

HC_serological_rotator = HC.Appliance(HC,2,10,1,60,0.25,15)
HC_serological_rotator.windows([480,720],[0,0],0.35)

#School C
SC_indoor_bulb = SC.Appliance(SC,27,7,1,60,0.2,10)
SC_indoor_bulb.windows([480,780],[0,0],0.35)

SC_outdoor_bulb = SC.Appliance(SC,7,13,1,60,0.2,10)
SC_outdoor_bulb.windows([480,780],[0,0],0.35)

SC_TV = SC.Appliance(SC,5,60,1,120,0.1,5, occasional_use = 0.5)
SC_TV.windows([480,780],[0,0],0.35)

SC_radio = SC.Appliance(SC,24,4,1,120,0.1,5, occasional_use = 0.5)
SC_radio.windows([480,780],[0,0],0.35)

SC_DVD = SC.Appliance(SC,2,8,1,120,0.1,5, occasional_use = 0.5)
SC_DVD.windows([480,780],[0,0],0.35)

SC_Freezer = SC.Appliance(SC,1,200,1,1440,0,30, 'yes',3)
SC_Freezer.windows([0,1440])
SC_Freezer.specific_cycle_1(200,20,5,10)
SC_Freezer.specific_cycle_2(200,15,5,15)
SC_Freezer.specific_cycle_3(200,10,5,20)
SC_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

SC_PC = SC.Appliance(SC,25,50,1,210,0.1,10)
SC_PC.windows([480,780],[0,0],0.35)

SC_Phone_charger = SC.Appliance(SC,5,2,1,180,0.2,5)
SC_Phone_charger.windows([480,780],[0,0],0.35)

SC_Printer = SC.Appliance(SC,1,20,1,30,0.1,5)
SC_Printer.windows([480,780],[0,0],0.35)

SC_Stereo = SC.Appliance(SC,1,150,1,90,0.1,5, occasional_use = 0.33)
SC_Stereo.windows([480,780],[0,0],0.35)

SC_data = SC.Appliance(SC,1,420,1,60,0.1,5, occasional_use = 0.5)
SC_data.windows([480,780],[0,0],0.35)

#Church
Ch_indoor_bulb = Church.Appliance(Church,10,26,1,210,0.2,60,'yes', flat = 'yes')
Ch_indoor_bulb.windows([1200,1440],[0,0],0.1)

Ch_outdoor_bulb = Church.Appliance(Church,7,26,1,240,0.2,60, 'yes', flat = 'yes')
Ch_outdoor_bulb.windows([1200,1440],[0,0],0.1)

Ch_speaker = Church.Appliance(Church,1,100,1,240,0.2,60)
Ch_speaker.windows([1200,1350],[0,0],0.1)

#Public lighting
Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,12,40,2,310,0,300, 'yes', flat = 'yes')
Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)

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

EB_Stereo = EB.Appliance(EB,1,150,1,90,0.1,5, occasional_use = 0.33)
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

WS_indoor_bulb = WS.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30,occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.125,60)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([390,450],[1140,1260],0.35)

#Transformation
LAU_GD = LAU.Appliance(LAU,1,9360,1,180,0.2,30,occasional_use = 0.33)
LAU_GD.windows([420,1080],[0,0],0.35)

LAU_VW = LAU.Appliance(LAU,1,1170,1,480,0.2,15,occasional_use = 0.82)
LAU_VW.windows([420,1140],[0,0],0.35)

LAU_BT = LAU.Appliance(LAU,1,370,2,900,0.2,180)
LAU_BT.windows([360,930],[1080,1440],0.35)

#Irrigation
IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)