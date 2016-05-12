import io
import Image
import decrypt
from scapy.all import *

raw = ''
download = []
ans = []
count = 0
pkts = sniff(filter="icmp", timeout=200)

print(pkts.summary())

f= open("capture","ab")
for packet in pkts:
    if packet.haslayer(IP) and str(packet.getlayer(IP).src)=="127.0.0.1":

        print "packet arrived"
        # print "payload: {}".format(packet.getlayer(ICMP).payload)
        if packet.haslayer(ICMP) and str(packet.getlayer(ICMP).type) == "8":

            raw = packet.getlayer(ICMP).seq

            #if raw not in download:
            count +=1
            ans.append(chr(raw))
            #download.append(raw)
            print "Total packets recieved: {}".format(count)

ans1 = []
for i in range(0,len(ans),2):
    ans1.append(ans[i])

text = "".join(ans1)
#print "Recieved Data: " + text
ans = []

for i in range(0,len(text),20):
	data = decrypt.decrypt(text[i:i+20])
	#print "DATA: " + str(data)
	ans.append(data)
#print "FINAL ANS: " + "".join(ans)	
image = Image.open(io.BytesIO("".join(ans)))
image.save("testresult.png")
#data = decrypt.decrypt(text)
f.write("".join(ans))

f.close()
