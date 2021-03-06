# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 08:12:16 2021

@author: Claudia
"""
#User class definition
from core import User, np
User_list = []

S1 = User("school type 1",1)
User_list.append(S1)

S2 = User("school type 2",1)
User_list.append(S2)

S3 = User("school type 3",1)
User_list.append(S3)



#Appliances definition

#School type 1
S1_indoor_bulb = S1.Appliance(S1,6,7,2,120,0.25,30)
S1_indoor_bulb.windows([480,780],[840,1140],0.2)

S1_outdoor_bulb = S1.Appliance(S1,1,13,1,60,0.2,10)
S1_outdoor_bulb.windows([1007,1080],[0,0],0.35)

S1_TV = S1.Appliance(S1,1,60,2,120,0.1,5, occasional_use = 0.5)
S1_TV.windows([480,780],[840,1140],0.2)

S1_radio = S1.Appliance(S1,3,4,2,120,0.1,5, occasional_use = 0.5)
S1_radio.windows([480,780],[840,1140],0,2)

S1_DVD = S1.Appliance(S1,1,8,2,120,0.1,5, occasional_use = 0.5)
S1_DVD.windows([480,780],[840,1140],0,2)


#School type 2

S2_indoor_bulb = S2.Appliance(S2,12,7,2,120,0.25,30)
S2_indoor_bulb.windows([480,780],[840,1140],0.2)

S2_outdoor_bulb = S2.Appliance(S2,1,13,1,60,0.2,10)
S2_outdoor_bulb.windows([1007,1080],[0,0],0.35)

S2_Phone_charger = S2.Appliance(S2,1,2,2,180,0.2,5)
S2_Phone_charger.windows([480,780],[840,1140],0.35)

S2_TV = S2.Appliance(S2,1,60,2,120,0.1,5, occasional_use = 0.5)
S2_TV.windows([480,780],[840,1140],0.2)

S2_radio = S2.Appliance(S2,3,4,2,120,0.1,5, occasional_use = 0.5)
S2_radio.windows([480,780],[840,1140],0,2)

S2_DVD = S2.Appliance(S2,2,8,2,120,0.1,5, occasional_use = 0.5)
S2_DVD.windows([480,780],[840,1140],0,2)

S2_Freezer = S2.Appliance(S2,1,200,1,1440,0,30, 'yes',3)
S2_Freezer.windows([0,1440])
S2_Freezer.specific_cycle_1(200,20,5,10)
S2_Freezer.specific_cycle_2(200,15,5,15)
S2_Freezer.specific_cycle_3(200,10,5,20)
S2_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

S2_PC = S2.Appliance(S3,1,50,2,210,0.1,10)
S2_PC.windows([480,780],[840,1140],0.35)

#School type 3

S3_indoor_bulb = S3.Appliance(S3,27,7,1,60,0.2,10)
S3_indoor_bulb.windows([480,780],[0,0])

S3_outdoor_bulb = S3.Appliance(S3,7,13,1,60,0.2,10)
S3_outdoor_bulb.windows([480,780],[0,0])

S3_Phone_charger = S3.Appliance(S2,5,2,2,180,0.2,5)
S3_Phone_charger.windows([480,780],[0,0])

S3_PC = S1.Appliance(S3,25,50,2,210,0.1,10)
S3_PC.windows([480,780],[0,0])

S3_Printer = S3.Appliance(S3,1,20,2,30,0.1,5)
S3_Printer.windows([480,780],[0,0])

S3_Freezer = S3.Appliance(S3,1,200,1,1440,0,30, 'yes',3)
S3_Freezer.windows([0,1440])
S3_Freezer.specific_cycle_1(200,20,5,10)
S3_Freezer.specific_cycle_2(200,15,5,15)
S3_Freezer.specific_cycle_3(200,10,5,20)
S3_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

S3_TV = S3.Appliance(S3,5,60,2,120,0.1,5, occasional_use = 0.5)
S3_TV.windows([480,780],[0,0])

S3_DVD = S3.Appliance(S3,2,8,2,120,0.1,5, occasional_use = 0.5)
S3_DVD.windows([480,780],[0,0])

S3_Stereo = S3.Appliance(S3,1,150,2,90,0.1,5, occasional_use = 0.33)
S3_Stereo.windows([480,780],[0,0])

S3_radio = S3.Appliance(S3,24,4,2,120,0.1,5, occasional_use = 0.5)
S3_radio.windows([480,780],[0,0])

S3_data = S3.Appliance(S3,1,420,2,60,0.1,5, occasional_use = 0.5)
S3_data.windows([480,780],[0,0])
