import time
import crypt
from scapy.all import *
import imgtest

def splitter():
    offset = 10
    x = 1
    y = 2
    count = 0
    cryptlist = []

    with open('testme.txt','rb') as f:

        read_bytes='xOn'

        while read_bytes!='':
            read_bytes=f.read(offset)
            #lst.append(read_bytes)
            cryptlist.append(crypt.crypt(read_bytes))
            count += 1
            if y>x:
                f.seek(offset,0)
                y=y-x

    #ans = "\n".join(cryptlist)
    print "Count : {}".format(count*10)
    return cryptlist


def creator():
    lstt= []
    count = 0
    lst= splitter()
    #print lst
    for i in lst:
        print i
        for j in i:
            #print "NUMBER TO BE SEND: "+str(ord(j))
            lstt.append(j)

    ele=0
    #src='192.168.43.17'
    #dst='192.168.43.13'
    src = '127.0.0.1'
    dst = '127.0.0.1'
    sent=''
    packet=''
    out=open('output.txt','w')
    for i in range(len(lstt)):
        out.write(lstt[i])
        print lstt[i]
        sent2 = sr1(IP(src=src,dst=dst)/ICMP( seq = ord(lstt[i] ))/Raw(), inter=0.1,retry=0,timeout=0.1 )
        count += 1
        #print "Reply: {}".format(sent2)
        print " Total Number Of Packets Sent:  {}".format(count)

    out.close()
if __name__ == "__main__":
	creator()
