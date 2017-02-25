# Traceroute specifying the host wich has to receive the ICMP packages
from scapy.all import *

src = sys.argv[1]
dst = sys.argv[2]
sport = random.randint(1024,65535)
dport = int(sys.argv[3])

for i in range(20)[1:]:
  ip=IP(src=src,dst=dst,ttl=i)
  SYN=TCP(sport=sport,dport=dport,flags='S',seq=1000)
  SYNACK=sr1(ip/SYN)
