# List opened ports

from scapy.all import *

dst = sys.argv[1]

for i in range(2**15)[1:]:
	if i%10 == 0:
		print "It %d"%i
	ip = IP(dst=dst)
	tcp = TCP(dport=i)
	packet = ip/tcp
	recv = sr1(packet, timeout=0.1, verbose=0)
	if recv is not None:
		if recv[TCP].seq > 0:
			print i
