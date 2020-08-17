#Exercise 6
    #Plot days since last fill up and observed MPG
    #Make scatter points and draw regression line

import datetime
import turtle


def scatnreg(filesname):
    filesList = []

    for line in filesname:
        file_item = line.split(',')
        
        filesList.append(file_item)

    mpgList = []
    daysb4fill = []
    time_periods = []

    idx = len(filesList)-2

    while idx > 0:
        data_withq = filesList[idx]

        #remove quotes
        data_noq = []
        for i in data_withq:
            z = i.strip('\"')
            data_noq.append(z)

        if (data_noq[6]) == "Full":
            #fetch mpg data
            mpg = float(data_noq[1])   
            mpgList.append(mpg)

            #fetch date
            dateStr = data_noq[2]
            
            year = dateStr[:4]
            month = dateStr[5:7]
            day = dateStr[8:10]

            timeStr = data_noq[3]
            if len(timeStr) ==8:
                hour = timeStr[:2]
                minute = timeStr[3:5]

            else:
                hour = '0'+timeStr[0]
                minute = timeStr[2:5]
                
            curr_time = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute))
            
            #get days before fill up
            if len(time_periods) == 0:
                time_diff = 0
                daysb4fill.append(time_diff)
            else:
                time_diff = curr_time -time_periods[-1]
                if time_diff.days < 0:
                    daysb4fill.append(0)
                #print(time_diff)
                else:
                    daysb4fill.append(time_diff.days)

            time_periods.append(curr_time)
        idx -= 1 
    
    #highest mpg
    highest_mpg = 0
    for i in mpgList:
        if i > highest_mpg:
            highest_mpg = i

    highest_dayb4refill = 0
    for i in daysb4fill:
        if i > highest_dayb4refill:
            highest_dayb4refill = i

    #regression line
        #sum of all x values
        #sum of all y values
        #sum of x**2 values
        #sum of x*y values
        #formula --> y = avg(y) +m(x-avg(x))
                # m = sigma(x*y)-n(avg(x)*avg(y))
                #     divide by sigma(x**2)-n*avg(x)**2
    sigmaX = 0
    sigmaY = 0
    sigmaXY = 0
    sigmaXq= 0
    xList = daysb4fill
    yList = mpgList
    n = len(xList)
    for i in range(0,n):
        sigmaX += xList[i]
        sigmaY += yList[i]
        sigmaXq += xList[i]**2
        sigmaXY +=  xList[i] * yList[i]

    avgX = sigmaX / n
    avgY = sigmaY / n
    
    m = ((sigmaXY)- (n * avgX * avgY))/(sigmaXq-n*(avgX**2))

    #get 2 points
    #y = avg(y) + m(x-avg(x))
    x1 = xList[1]
    x2 = highest_dayb4refill
    y1 = avgY + m *(x1-avgX)
    y2 = avgY + m *(x2-avgX)

    

    


    #Implement the graph
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.tracer(100)

    screen.setworldcoordinates(0,0,20,highest_mpg)
    #plot x and y axis
    #x axis
    t.forward(20)
    t.write("Days before refill",align="right")

    #y axis
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(90)
    t.forward(highest_mpg)
    t.write("Observed MPG",align="left")

    #plot the points
    for i in range(0,len(mpgList)):
        
        t.penup()
        t.goto(xList[i],yList[i])
        t.pendown()
        t.dot(3)

    t.penup()
    t.goto(x1,y1)
    t.pendown()
    
    t.goto(x2,y2)
    screen.update()
    turtle.exitonclick()




nissan_file = open("Toyota4Runner.csv",'r')
scatnreg(nissan_file)
