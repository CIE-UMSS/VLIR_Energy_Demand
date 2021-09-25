# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:50:31 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
Paper: Energy sufficiency, lowlands.
User: Coliseum
'''

#Definig users

Coliseum = User("Coliseum", 1)
User_list.append(Coliseum)

#Appliances

Lights = Coliseum.Appliance(Coliseum,25,150,2,310,0.1,300, 'yes', flat = 'yes')
Lights.windows([0,336],[1110,1440],0.2)