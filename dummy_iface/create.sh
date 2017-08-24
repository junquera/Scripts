IFACE='eth10'
ADDR='10.0.2.1'
PREFIX='24'
modprobe dummy
ip link set name $IFACE dev dummy0
ifconfig $IFACE hw ether 00:22:22:ff:ff:ff
ip addr add $ADDR/$PREFIX brd + dev $IFACE label $IFACE:0
