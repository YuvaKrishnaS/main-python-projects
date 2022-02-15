import os

def Alarm(query):

    TimeHere = open('E:\\Krishnaaaaa\\MyJarvis\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("E:\\Krishnaaaaa\\MyJarvis\\Alarm.py")

Alarm("set 14 and 44")
