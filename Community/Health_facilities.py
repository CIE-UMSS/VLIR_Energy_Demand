# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:34:34 2021

@author: ClaudiaLSS
"""
"Health post"

from core import User, np
User_list = []

#User classes definition

HP = User("Health post",1)
User_list.append(HP)

HC = User("Health center",1)
User_list.append(HC)

#Appliances definition

#Health post
HP_indoor_bulb = HP.Appliance(HP,12,7,2,690,0.2,10)
HP_indoor_bulb.windows([480,720],[870,1440],0.35)

HP_outdoor_bulb = HP.Appliance(HP,1,13,2,690,0.2,10)
HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HP_Phone_charger = HP.Appliance(HP,8,2,2,300,0.2,5)
HP_Phone_charger.windows([480,720],[900,1440],0.35)

HP_TV = HP.Appliance(HP,1,150,2,360,0.1,60)
HP_TV.windows([480,720],[780,1020],0.2)

HP_radio = HP.Appliance(HP,1,40,2,360,0.3,60)
HP_radio.windows([480,720],[780,1020],0.2)

HP_PC = HP.Appliance(HP,1,200,2,300,0.1,10)
HP_PC.windows([480,720],[1050,1440],0.35)

HP_printer = HP.Appliance(HP,1,100,1,60,0.3,10)
HP_printer.windows([540,1020])

HP_fan = HP.Appliance(HP,2,60,1,240,0.2,60)
HP_fan.windows([660,960])

HP_sterilizer_stove = HP.Appliance(HP,1,600,2,120,0.3,30)
HP_sterilizer_stove.windows([540,600],[900,960],)

HP_needle_destroyer = HP.Appliance(HP,1,70,1,60,0.2,10)
HP_needle_destroyer.windows([540,600])

HP_water_pump = HP.Appliance(HP,1,400,1,30,0.2,10)
HP_water_pump.windows([480,510])

HP_Fridge = HP.Appliance(HP,1,150,1,1440,0,30, 'yes',3)
HP_Fridge.windows([0,1440],[0,0])
HP_Fridge.specific_cycle_1(150,20,5,10)
HP_Fridge.specific_cycle_2(150,15,5,15)
HP_Fridge.specific_cycle_3(150,10,5,20)
HP_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

HP_Fridge2 = HP.Appliance(HP,1,150,1,1440,0,30, 'yes',3)
HP_Fridge2.windows([0,1440],[0,0])
HP_Fridge2.specific_cycle_1(150,20,5,10)
HP_Fridge2.specific_cycle_2(150,15,5,15)
HP_Fridge2.specific_cycle_3(150,10,5,20)
HP_Fridge2.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,299],[1201,1440])

HP_Fridge3 = HP.Appliance(HP,1,150,1,1440,0.1,30, 'yes',3)
HP_Fridge3.windows([0,1440],[0,0])
HP_Fridge3.specific_cycle_1(150,20,5,10)
HP_Fridge3.specific_cycle_2(150,15,5,15)
HP_Fridge3.specific_cycle_3(150,10,5,20)
HP_Fridge3.cycle_behaviour([580,1200],[0,0],[420,479],[0,0],[0,419],[1201,1440])

#Health center

HC_indoor_bulb = HC.Appliance(HC,20,7,2,690,0.2,10)
HC_indoor_bulb.windows([480,720],[870,1440],0.35)

HC_outdoor_bulb = HC.Appliance(HC,5,13,2,690,0.2,10)
HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HC_Phone_charger = HC.Appliance(HC,5,2,2,300,0.2,5)
HC_Phone_charger.windows([480,720],[900,1440],0.35)

HC_TV = HP.Appliance(HC,2,150,2,360,0.1,60)
HC_TV.windows([480,720],[780,1020],0.2)

HC_radio = HC.Appliance(HC,5,40,2,360,0.3,60)
HC_radio.windows([480,720],[780,1020],0.2)

HC_PC = HP.Appliance(HC,2,200,2,300,0.1,10)
HC_PC.windows([480,720],[1050,1440],0.35)

HC_printer = HC.Appliance(HC,2,100,1,60,0.3,10)
HC_printer.windows([540,1020])

HC_fan = HP.Appliance(HC,2,60,1,240,0.2,60)
HC_fan.windows([660,960])

HC_sterilizer_stove = HC.Appliance(HC,3,600,2,120,0.3,30)
HC_sterilizer_stove.windows([540,600],[900,960],)

HC_needle_destroyer = HC.Appliance(HC,1,70,1,60,0.2,10)
HC_needle_destroyer.windows([540,600])

HC_water_pump = HP.Appliance(HC,1,400,1,30,0.2,10)
HC_water_pump.windows([480,510])

HC_Fridge = HC.Appliance(HP,1,150,1,1440,0,30, 'yes',3)
HC_Fridge.windows([0,1440],[0,0])
HC_Fridge.specific_cycle_1(150,20,5,10)
HC_Fridge.specific_cycle_2(150,15,5,15)
HC_Fridge.specific_cycle_3(150,10,5,20)
HC_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

HC_Fridge2 = HP.Appliance(HC,1,150,1,1440,0,30, 'yes',3)
HC_Fridge2.windows([0,1440],[0,0])
HC_Fridge2.specific_cycle_1(150,20,5,10)
HC_Fridge2.specific_cycle_2(150,15,5,15)
HC_Fridge2.specific_cycle_3(150,10,5,20)
HC_Fridge2.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,299],[1201,1440])

HC_Fridge3 = HC.Appliance(HC,1,150,1,1440,0.1,30, 'yes',3)
HC_Fridge3.windows([0,1440],[0,0])
HC_Fridge3.specific_cycle_1(150,20,5,10)
HC_Fridge3.specific_cycle_2(150,15,5,15)
HC_Fridge3.specific_cycle_3(150,10,5,20)
HC_Fridge3.cycle_behaviour([580,1200],[0,0],[420,479],[0,0],[0,419],[1201,1440])

HC_Fridge4 = HC.Appliance(HC,1,150,1,1440,0.1,30, 'yes',3)
HC_Fridge4.windows([0,1440],[0,0])
HC_Fridge4.specific_cycle_1(150,20,5,10)
HC_Fridge4.specific_cycle_2(150,15,5,15)
HC_Fridge4.specific_cycle_3(150,10,5,20)
HC_Fridge4.cycle_behaviour([580,1200],[0,0],[420,479],[0,0],[0,419],[1201,1440])

HC_microscope = HP.Appliance(HC,2,3,2,120,0.2,10)
HC_microscope.windows([480,720],[840,960],0.35)

HC_shower = HP.Appliance(HC,3,3000,2,120,0,1,15)
HC_shower.windows([360,720],[780,2400],0.35)

HC_heater = HP.Appliance(HC,2,1500,2,180,0.25,60)
HC_heater.windows([369,720],[1080,1260],0.35)

HC_dental_compresor = HP.Appliance(HC,2,500,2,60,0.15,10)
HC_dental_compresor.windows([480,720],[840,1260],0.2)

HC_centrifuge = HP.Appliance(HC,2,100,1,60,0.15,10)
HC_centrifuge.windows([480,720],[0,0])

HC_serological_rotator = HP.Appliance(HC,2,10,1,60,0.25,15)
HC_serological_rotator.windows([480,720],[0,0])


