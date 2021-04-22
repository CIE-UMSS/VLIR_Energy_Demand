# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:34:34 2021

@author: Clau
"""
"Health post"

from core import User, np
User_list = []

#User classes definition

Hospital = User("Hospital",1)
User_list.append(Hospital)

#Appliances definition

Ho_indoor_bulb = Hospital.Appliance(Hospital,12,7,2,690,0.2,10)
Ho_indoor_bulb.windows([480,720],[870,1440],0.35)

Ho_outdoor_bulb = Hospital.Appliance(Hospital,1,13,2,690,0.2,10)
Ho_outdoor_bulb.windows([0,342],[1037,1440],0.35)

Ho_Phone_charger = Hospital.Appliance(Hospital,8,2,2,300,0.2,5)
Ho_Phone_charger.windows([480,720],[900,1440],0.35)

Ho_TV = Hospital.Appliance(Hospital,1,150,2,360,0.1,60)
Ho_TV.windows([480,720],[780,1020],0.2)

Ho_radio = Hospital.Appliance(Hospital,1,40,2,360,0.3,60)
Ho_radio.windows([480,720],[780,1020],0.2)

Ho_PC = Hospital.Appliance(Hospital,1,200,2,300,0.1,10)
Ho_PC.windows([480,720],[1050,1440],0.35)

Ho_printer = Hospital.Appliance(Hospital,1,100,2,60,0.3,10)
Ho_printer.windows([540,1020])

Ho_fan = Hospital.Appliance(Hospital,2,60,1,240,0.2,60)
Ho_fan.windows([660,960])

Ho_sterilizer_stove = Hospital.Appliance(Hospital,1,600,2,120,0.3,30)
Ho_sterilizer_stove.windows([540,600],[900,960],)

Ho_needle_destroyer = Hospital.Appliance(Hospital,1,70,1,60,0.2,10)
Ho_needle_destroyer.windows([540,600])

Ho_water_pump = Hospital.Appliance(Hospital,1,400,1,30,0.2,10)
Ho_water_pump.windows([480,510])

Ho_Fridge = Hospital.Appliance(Hospital,1,150,1,1440,0,30, 'yes',3)
Ho_Fridge.windows([0,1440],[0,0])
Ho_Fridge.specific_cycle_1(150,20,5,10)
Ho_Fridge.specific_cycle_2(150,15,5,15)
Ho_Fridge.specific_cycle_3(150,10,5,20)
Ho_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

Ho_Fridge2 = Hospital.Appliance(Hospital,1,150,1,1440,0,30, 'yes',3)
Ho_Fridge2.windows([0,1440],[0,0])
Ho_Fridge2.specific_cycle_1(150,20,5,10)
Ho_Fridge2.specific_cycle_2(150,15,5,15)
Ho_Fridge2.specific_cycle_3(150,10,5,20)
Ho_Fridge2.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,299],[1201,1440])

Ho_Fridge3 = Hospital.Appliance(Hospital,1,150,1,1440,0.1,30, 'yes',3)
Ho_Fridge3.windows([0,1440],[0,0])
Ho_Fridge3.specific_cycle_1(150,20,5,10)
Ho_Fridge3.specific_cycle_2(150,15,5,15)
Ho_Fridge3.specific_cycle_3(150,10,5,20)
Ho_Fridge3.cycle_behaviour([580,1200],[0,0],[420,479],[0,0],[0,419],[1201,1440])

