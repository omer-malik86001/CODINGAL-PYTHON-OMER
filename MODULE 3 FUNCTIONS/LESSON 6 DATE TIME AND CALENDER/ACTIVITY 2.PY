import random
import time
# write a function to generate a random date from the given start and end date
def getRandomDate(startDate,endDate):
    r=random.random()
    dateFormat="%m/%d/%Y"
    startTime=time.mktime(time.strptime(startDate,dateFormat))
   # print(startTime)
    endTime=time.mktime(time.strptime(endDate,dateFormat))
   # print(endTime)
    randomTime=startTime + r *(endTime-startTime)
   # print(randomTime)

    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate



#______---------------_____________----
startDate="1/1/2026"
endDate="12/31/2026"
print(getRandomDate(startDate,endDate))