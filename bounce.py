from scapy.all import *

pkts = sniff(timeout=200, filter="tcp")
lst = 0
count = 0
for packet in pkts:
    if packet.haslayer(IP) and str(packet.getlayer(IP).src) == "127.0.0.1" and packet.getlayer(TCP).dport == 3232:
        if lst % 2 == 0:
            key = random.randint(0,1)
            ValueOfPort = packet.sport + 1
            SeqNr = packet.seq
            AckNr =packet.seq + 1
            print chr(SeqNr)
            ip = IP(src = "127.0.0.1", dst = "127.0.0.1")
            TCP_SYNACK = TCP(sport = 3232, dport = 1145, flags = "SA", seq = SeqNr, ack = AckNr, options = [('MSS', 1460)])
            ans = sr1(ip / TCP_SYNACK / Raw(), inter=0.1,retry=0,timeout=0.1 )
            print " Total Number Of Packets Sent:  {}".format(count)
            count += 1
        lst += 1