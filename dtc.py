'''from datetime import date,time,datetime
# calling the today
# function of date class
today=date.today()
now=datetime.now()
print("today's date is", today)
print("\nCurrent date and time is", now)
print("\nDate components", today.year, today.month,today.day)'''

import random
import time

def getRandomDate(startDate, endDate ): 
    print("printing random date between", startDate,"and",endDate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%Y'
    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime=time.mktime(time.strptime(endDate, dateFormat))
    randomTime=startTime+randomGenerator* (endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate

print("Random Date=",getRandomDate("1/1/2016","12/12/2018"))
