import threading

class hashtagclass():
    hashtagdict={} #store the #tag and tagcount as key value pair
    def __init__(self,tags):
        self.tags=tags
        self.top10tags=[]
        self.keylock=threading.Lock()
    def find_toptags(self): #This method return top 10 trending #tags
        self.tags = self.tags.split(" ")
        for i in self.tags:
            if i[0] == '#': #finding #tags from the given text
                tag = i[1:len(i)]
                try:
                    self.keylock.acquire() #locking to maintain synchronization incase of multithredaing
                    if tag in hashtagclass.hashtagdict:
                        c = hashtagclass.hashtagdict[tag]
                        hashtagclass.hashtagdict[tag] = c + 1 #updating the dictionary
                    else:
                        hashtagclass.hashtagdict[tag] = 1
                finally:
                    self.keylock.release()
            a=sorted(hashtagclass.hashtagdict.items(),key=lambda x: x[1]) #sorting and storing key value pairs from the dictionary to list a
        a = a[::-1]
        c = 0
        for i in a:
            if c < 10:
                c += 1
                self.top10tags.append(i[0])
            else:
                break
        return self.top10tags
def executionmain(text):
    obj = hashtagclass(text)
    print(obj.find_toptags())
t1=threading.Thread(target=executionmain,args=(input(), ))
t2=threading.Thread(target=executionmain,args=(input(), ))
t3=threading.Thread(target=executionmain,args=(input(), ))
t1.start()
t2.start()
t3.start()