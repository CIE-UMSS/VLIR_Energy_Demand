
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


LI = User("low income",1)
User_list.append(LI)

#Appliances definition

#Lower Income
#indoor bulb
LI_indoor_bulb = LI.Appliance(LI,2,7,2,120,0.1,10,'yes', flat = 'yes')
LI_indoor_bulb.windows([1170,1440],[0,30],0.5)
#outdoor bulb
LI_outdoor_bulb = LI.Appliance(LI,1,13,2,600,0.02,10,'yes', flat = 'yes')
LI_outdoor_bulb.windows([1170,1440],[0,30],0.5)
#radio
LI_Radio = LI.Appliance(LI,1,7,2,240,0.125,30)
LI_Radio.windows([480,720],[1080,1380],0.5)
#TV
LI_TV = LI.Appliance(LI,1,60,2,240,0.125,30)
LI_TV.windows([540,780],[1080,1440],0.5)
#phone charger
LI_Phone_charger = LI.Appliance(LI,8,5,2,60,0.08,5)
LI_Phone_charger.windows([1200,1440],[0,420],0.5)
#Iron
LI_Iron = LI.Appliance(LI,2,2,1,300,0.02,5)
LI_Iron.windows([600,1200],[0,0])
