import datetime
def convert24format(x):
    ti = x.split(':')
    if x.endswith("pm") and int(ti[0]) < 12:
        t = int(ti[0]) + 12
        t = str(t) + ':' + ti[1][:2]
    elif x.endswith("am") and int(ti[0]) == 12:
        t = "00" + ':' + ti[1][:2]
    else:
        t = x[0:len(x) - 2]
    return t
def readfile(file):
    no_of_transactions=0
    f = open(file, "r")
    #print(f.read())
    out=f.readlines()
    endtimedict={}
    timedict={}
    seconds=0
    for i in out:
        no_of_transactions+=1
        s=""
        for j in i:
            if j!=' ': #Removing all extra spaces
                s=s+j
        list1=s.split(',')
        if list1[3]=="start\n":
            timedict[list1[0]]=list1[1]+','+list1[2]
        else:
            #get the start date time
            #endtime- start time
            #stored the diff into array
    #till end of the file
    #read the array and find the average
            timedict[list1[0]]+="/"+list1[1]+','+list1[2]
    for key ,value in timedict.items():
        timeinterval=value.split('/')
        tt=[]
        for i in range(0,len(timeinterval)):
            pass
            t=timeinterval[i].split(',')
            ti=convert24format(t[1])
            timeinterval[i]=timeinterval[i][0:11]+ti
            ti=ti.split(':')
            tt.append(int(ti[0]))
            tt.append(int(ti[1]))
        t1=timeinterval[0]
        t2=timeinterval[1]
        a = datetime.datetime(int(t1[0:4]), int(t1[5:7]), int(t1[8:10]),tt[0],tt[1],0)
        b = datetime.datetime(int(t2[0:4]), int(t2[5:7]), int(t2[8:10]),tt[2],tt[3],0)
        c=b-a
        seconds+=c.seconds
    no_of_transactions=no_of_transactions/2
    totalseconds=(seconds//no_of_transactions)
    print("average time taken by all the transaction is",totalseconds//60,"minutes",totalseconds%60, "seconds")
readfile("myfile.txt")
