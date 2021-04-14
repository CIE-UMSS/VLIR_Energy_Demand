
# -*- coding: utf-8 -*-
"""

@author: Alejandro Soto
"""

'''
Toconao:Enero 2020
'''

from core import User, np
User_list = []
#User classes definition

HI = User("high income",1)
User_list.append(HI)

#Appliances definition

#High-Income
#indoor bulb
HI_indoor_bulb = HI.Appliance(HI,6,7,2,120,0.1,10,'yes', flat = 'yes')
HI_indoor_bulb.windows([1170,1440],[0,30],0.5)
#outdoor bulb
HI_outdoor_bulb = HI.Appliance(HI,2,13,2,600,0.02,10,'yes', flat = 'yes')
HI_outdoor_bulb.windows([1170,1440],[0,30],0.5)
#radio
HI_Radio = HI.Appliance(HI,1,7,2,240,0.125,30)
HI_Radio.windows([480,720],[1080,1380],0.5)
#tv
HI_TV = HI.Appliance(HI,2,60,2,180,0.3,5)
HI_TV.windows([540,780],[1080,1440],0.5)
#phone charger
HI_Phone_charger = HI.Appliance(HI,4,5,2,360,0.03,10)
HI_Phone_charger.windows([1200,1440],[0,420],0.5)
#freezer
HI_Freezer = HI.Appliance(HI,1,200,1,1440,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,20,5,10)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])
#iron
HI_Iron = HI.Appliance(HI,1,700,1,30,0.5,1)
HI_Iron.windows([600,1200],[0,0])
#laptop
HI_Laptop = HI.Appliance(HI,1,70,1,90,0.3,30)
HI_Laptop.windows([960,1200],[0,0])

