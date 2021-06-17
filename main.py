# I have to confess that the first approach to solve the problem, was doing it with Javascript. 
# After that, I did it with python.
# Remarkable observation: Based on the fact that by default Python language is Synchronous (in contrast with Javascript), I didn't have to explicity make async/await procedures.

import datetime 
import math
def timeMeter (functionToRun):
    initTime = datetime.datetime.now().timestamp() #Starting to record when the function started

    functionToRun() #This is the function I am measuring, how much time it takes to run.

    finishTime = datetime.datetime.now().timestamp() #Finish time
    timeDiff = ((finishTime - initTime)) #This is the original time elapsed, in milliseconds...

    # In this next section I make some math operations in order to separate minutes, hours, days, etc.
    milliseconds = timeDiff
    seconds = math.floor(timeDiff)
    timeDiff = math.floor(timeDiff / 60)
    minutes = round(timeDiff % 60)
    timeDiff = math.floor(timeDiff / 60)
    hours = round(timeDiff % 24)
    timeDiff = math.floor(timeDiff / 24)
    days = math.floor(timeDiff % 365)
    timeDiff = math.floor(timeDiff / 365)

    # This function shows the output data in a more readable format
    def betterFormat ():
        print (str(days)+"d:"+str(hours)+"h:"+str(minutes)+"m:"+str(seconds)+"."+str(math.floor(((milliseconds - math.floor(milliseconds))*1000)))+"s")

    # This was my first approach of giving outputs to the user, then I refactored my code, to use also the betterFormat function.
    if (days > 0 ):
        print ("Time elapsed: " + str(days) + " days, " + str(hours) + " hours and " + (minutes - hours*60) + " minutes")
        betterFormat()
    elif (hours > 0): 
        print ("Time elapsed: " + str(hours) + " hours and " + str(minutes - hours*60) + " minutes")
        betterFormat()
    elif (minutes > 0): 
        print ("Time elapsed: " + str(minutes) + " minutes and " + str(seconds - minutes*60) + " seconds with " + str((milliseconds - math.floor(milliseconds))*1000) + " milliseconds")
        betterFormat()
    elif (seconds > 0): 
        print (("Time elapsed: " + str(seconds) + " seconds and " + str((milliseconds - math.floor(milliseconds))*1000) + " milliseconds"))
        betterFormat()
    elif (milliseconds > 0):
        print ("Time elapsed: " + str(milliseconds) + " milliseconds")
        betterFormat()
    else:
        print ("That was blazzing fast! It took 0 seconds")
        
# Inside this goes the function that is going to be measured.
# Observation: Just change the value of n. n = 18000 in my laptop runs in less than a minute, but a value of n > 28000 can take up to 2 minutes.
def functionToMeasure (): 
    n = 18000
    for numero in range(1, n):
        for num in range(1, n):
            a = math.sqrt(num) - 2
            
# This is the function that runs all the procedure.
timeMeter(functionToMeasure)