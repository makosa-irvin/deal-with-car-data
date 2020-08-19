#Plot a graph of mpg/time 
import datetime
import turtle
import math


def readnplot(filesname):

    filesList = []
    for line in filesname:
        file_list = line.split(",")
        filesList.append(file_list)

    datanoQList = []
    mpgList = []
    time_periods = []
    idx = len(filesList)-2
    #noQ_datas = []
    #Iterate over the list but leave the first line out
    while idx > 0:
        
        data_withq = filesList[idx]

        #remove quotes
        data_noq = []
        for i in data_withq:
            z = i.strip('\"')
            data_noq.append(z)
        datanoQList.append(data_noq)
        #fetch mpg data
        if float(data_noq[1]) > 0 and data_noq[0] == 'Gas' :
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
            time_periods.append(curr_time)

        idx -= 1
    
    #time difference
    try:
        startTime = time_periods[0]
        
        stopTime = time_periods[-1]
        time_diff = stopTime - startTime
        total_time = time_diff.days
        #print(total_time)
        time_periods = time_periods[::-1]
        #highest mpg
        highest_mpg = 0
        for i in mpgList:
            if i > highest_mpg:
                highest_mpg = i
        
        return  total_time,highest_mpg, mpgList,stopTime, time_periods

    except IndexError:
        return mpgList,time_periods

def main():
    #for nissan
    nissan_file = open("NissanVersa.csv","r")   
    nissan_totalTime,nissan_highestMPG, nissan_mpgList, nissan_stopTime,nissan_timePeriods = readnplot(nissan_file) 
    #toyota_file.close()

    #for toyota
    toyota_file = open("Toyota4Runner.csv","r")   
    toyota_totalTime,toyota_highestMPG, toyota_mpgList, toyota_stopTime,toyota_timePeriods = readnplot(toyota_file) 
    #toyota_file.close()

    #for suzuki
    suzuki_file = open("SuzukiS40.csv","r")   
    suzuki_totalTime,suzuki_highestMPG, suzuki_mpgList, suzuki_stopTime,suzuki_timePeriods = readnplot(suzuki_file) 
    #suzuki_file.close()


    #draw turtle
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.tracer(100)

    #write text
    # t.penup()
    # t.setpos(0,0)
    # t.pendown()

    #mark the points
    #for nissan
    screen.setworldcoordinates(-10,-5,toyota_totalTime,nissan_highestMPG)
    t.penup()
    t.goto(0,nissan_mpgList[0])
    t.pendown()

    t.pencolor('green')

    for j in range(len(nissan_mpgList)-1):
        time_diffx = nissan_stopTime - nissan_timePeriods[j]
        
        x = time_diffx.days
        y = nissan_mpgList[j]/2
        

        #t.penup()
        t.goto(x,y)
        #t.pendown
        t.dot(4)

    t.write("Nissan", font=(50), align = "right")
    #for toyota
    #screen.setworldcoordinates(0,0,toyota_totalTime,toyota_highestMPG)
    t.penup()
    t.goto(0,toyota_mpgList[0])
    t.pendown()
    t.pencolor('blue')
    for j in range(len(toyota_mpgList)-1):
        time_diffx = toyota_stopTime - toyota_timePeriods[j]
        
        x = time_diffx.days
        y = toyota_mpgList[j]/2
        

        #t.penup()
        t.goto(x,y)
        #t.pendown
        t.dot(4)
    t.write("Toyota", font=(50))
    #for suzuki
    #screen.setworldcoordinates(0,0,suzuki_totalTime,suzuki_highestMPG)
    t.penup()
    t.goto(0,suzuki_mpgList[0])
    t.pendown()

    t.pencolor('red')
    for j in range(len(suzuki_mpgList)-1):
        time_diffx = suzuki_stopTime - suzuki_timePeriods[j]
        
        x = time_diffx.days
        y = suzuki_mpgList[j]/2
        

        #t.penup()
        t.goto(x,y)
        #t.pendown
        t.dot(4)
    t.write("Suzuki", font=(50))
    #the x and y axis
    t.pencolor('black')

    t.pensize(3)
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.left(270)
    t.forward(300)
    t.left(90)
    t.forward(300) 

    #to put the measurement points


    t.penup()
    t.goto(10,-1.2)
    t.pendown()
    t.write("Time",font=(10))

    t.penup()
    t.goto(-13,20)
    t.pendown()
    t.write("MPG",font=(10))


    screen.update()
    turtle.exitonclick()

if __name__ == "__main__":
    main()