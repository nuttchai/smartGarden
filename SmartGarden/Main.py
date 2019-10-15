from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump
from SetEquipment.Sunlight import GrowLight, LightBulb
from editfiles import writeFile 
import sched
import time

s = sched.scheduler(time.time, time.sleep)

while True:
    
    s.enter(2, 1, checkHumidity); s.enter(2, 1, checkTemperature)#every xSeconds run checkHumidity & checkTemperature
    
    humVal = checkHumidity()
    if humVal < 40: #below 40 is stress level
        pass
#        WaterPump(10) #10 (Dummy Variable) Second to open Valve

    tempVal = checkTemperature()
    if tempVal > 80: #Dummy Value 80
        LightBulb(False)  #Turn off Grow Light
        GrowLight(False) 
    elif tempVal < 10:
        LightBulb(True) #Turn on Light Bulb & Grow Light
        GrowLight(True)
    else:
        LightBulb(False) #Trun on only Grow Light; Turn off Light Bulb
        GrowLight(True)
    
    print("hum",humVal)
    print("tem",tempVal)
    writeFile(humVal, tempVal)
    
    s.run()