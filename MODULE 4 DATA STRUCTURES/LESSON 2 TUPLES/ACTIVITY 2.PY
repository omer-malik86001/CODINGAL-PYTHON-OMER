#0=SUNNY
#1=RAINY
weather=(1,0,1,0,1,0,1,1,1,)        

#PREDICT THE NEXT DAY WEATHER
#PREDICT WHICH WIND WAS MORE:0 OR 1

weather.count(0)

if weather.count(0)>weather.count(1):
    print("prediction is sunny")
else:
    print("prediction is rainy")
