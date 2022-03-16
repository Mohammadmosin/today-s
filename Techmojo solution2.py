import datetime
''' function convert24format()  will convert time from 12 hour format to 24 hour format'''
def convert24format(x):
    ti = x.split(':')
    if x.endswith("pm") and int(ti[0]) < 12:
        t = int(ti[0]) + 12
        t = str(t) + ':' + ti[1][:2]
    elif x.endswith("am") and int(ti[0]) == 12:
        t = "00" + ':' + ti[1][:2]
    elif x.endswith("am") and len(ti[0])<2:
        t='0'+x[0:len(x) - 2]
    else:
        t = x[0:len(x) - 2]
    return t
''' function readfile() will take filename as input paramter 
    and prints average time taken for all completed tranactions'''
def readfile(file):
    no_of_transactions=0
    f = open(file, "r")
    out=f.readlines() #reading file line by line
    timedict={}
    total_seconds=0
    for line in out:
        s=""
        for j in line:
            if j!=' ' and j!='\n': #Removing all extra spaces
                s=s+j
        list1=s.split(',')

        if list1[3]=="start":
            # finding starttime from the list1 and storing transaction id and start as key,value pair in timedict dictionary
            timedict[list1[0]]=list1[1]+','+list1[2]
        else:
            no_of_transactions += 1
            # getting the starttime of the transaction based on transactionid
            starttime=timedict[list1[0]]
            # finding endtime from the list1 in format (YYYY-MM-DAY,h:mmam/pm)
            endtime=list1[1]+','+list1[2]
            # Converting time to 24 hour format
            starttime=starttime[0:11]+convert24format(starttime[11:])
            endtime = endtime[0:11] + convert24format(endtime[11:])
            # creating datetime.datetime object
            a=datetime.datetime(int(starttime[0:4]),int(starttime[5:7]),int(starttime[8:10]),int(starttime[11:13]),int(starttime[14:16]))
            b=datetime.datetime(int(endtime[0:4]),int(endtime[5:7]),int(endtime[8:10]),int(endtime[11:13]),int(endtime[14:16]))
            # finding the time between start and end of transacion
            c = b-a
            total_seconds += c.seconds
    average_time=total_seconds//no_of_transactions

    print("average time taken by all the transactions is",average_time//60,"minutes",average_time%60, "seconds")
readfile("myfile.txt")
