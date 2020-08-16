#Plot a graph of mpg/time 
import datetime
import turtle


def readnplot(filesname):

    filesList = []
    for line in filesname:
        file_list = line.split(",")
        filesList.append(file_list)


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
        time_periods.append(curr_time)

        idx -= 1

    #time difference
    startTime = time_periods[0]
    stopTime = time_periods[-1]
    time_diff = stopTime - startTime
    total_time = time_diff.days
    print(total_time)
    time_periods = time_periods[::-1]
    #highest mpg
    highest_mpg = 0
    for i in mpgList:
        if i > highest_mpg:
            highest_mpg = i
    print(highest_mpg)
    #plot using turtle
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.tracer(100)

    #mark the points
    screen.setworldcoordinates(0,0,total_time,highest_mpg)
    t.penup()
    t.goto(0,mpgList[0])
    t.pendown()
    for j in range(len(mpgList)-1):
        time_diffx = stopTime - time_periods[j]
        
        x = time_diffx.days
        y = mpgList[j]
        print(x)

        #t.penup()
        t.goto(x,y)
        #t.pendown
        t.dot()

    screen.update()
    turtle.mainloop()

# nissan_file = open("NissanVersa.csv","r")   
# readnplot(nissan_file) 
# nissan_file.close()

# toyota_file = open("Toyota4Runner.csv","r")   
# readnplot(toyota_file) 
# toyota_file.close()

suzuki_file = open("SuzukiS40.csv","r")   
readnplot(suzuki_file) 
suzuki_file.close()