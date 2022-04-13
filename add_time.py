def add_time(start, duration, dayWeek=False):

    dayChange = 0
    
    startTime = start.split()
    
    startHour = int(startTime[0].split(":")[0])
    startMin = int(startTime[0].split(":")[1])
    dayPeriod = startTime[1]
    
    durationHour = int(duration.split(":")[0])
    durationMin = int(duration.split(":")[1])
    
    timeMinSum = startMin + durationMin
    timeHourSum = startHour + durationHour
    
    while timeMinSum >= 60:
        timeHourSum += 1
        timeMinSum -= 60
    
    while timeHourSum > 12:
        if dayPeriod == "PM":
            timeHourSum -= 12
            dayChange += 1
            dayPeriod = "AM"
        elif dayPeriod == "AM":
            timeHourSum -= 12
            dayPeriod = "PM"
            
    if timeHourSum == 12:
        if dayPeriod == "PM":
            dayChange += 1
            dayPeriod = "AM"
        elif dayPeriod == "AM":
            dayPeriod = "PM"        
            
    
    if dayChange == 0:
        changeStr = ""
    elif dayChange == 1:
        changeStr = "(next day)"
    else:
        changeStr = "(%s days later)" %(dayChange)
        
    
    if dayWeek != False:
        weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        indexWeek = weekDays.index(dayWeek.lower().capitalize())
        numberIndex = indexWeek + dayChange
        
        while numberIndex >= len(weekDays):
            numberIndex -=7
            
        timeSum_str = "%d:%02d %s, %s %s" %(timeHourSum, timeMinSum, dayPeriod, weekDays[numberIndex], changeStr)
    else:
        timeSum_str = "%d:%02d %s %s" %(timeHourSum, timeMinSum, dayPeriod, changeStr)
    
    dayWeek = False
    
    print(timeSum_str)