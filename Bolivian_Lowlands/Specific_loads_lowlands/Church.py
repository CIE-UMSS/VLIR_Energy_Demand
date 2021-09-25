# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:41:40 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
Paper: Energy sufficiency, lowlands.
User: Church
'''

#Definig users

Church = User("Church", 1)
User_list.append(Church)

#Church

Ch_indoor_bulb = Church.Appliance(Church,10,26,1,210,0.2,60,'yes', flat = 'yes')
Ch_indoor_bulb.windows([1200,1440],[0,0],0.1)

Ch_outdoor_bulb = Church.Appliance(Church,7,26,1,240,0.2,60, 'yes', flat = 'yes')
Ch_outdoor_bulb.windows([1200,1440],[0,0],0.1)

Ch_speaker = Church.Appliance(Church,1,100,1,240,0.2,60)
Ch_speaker.windows([1200,1350],[0,0],0.1)