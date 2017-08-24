IFACE='eth10'
ADDR='10.0.2.1'
PREFIX='24'
ip addr del $ADDR/$PREFIX brd + dev $IFACE label $IFACE:0
ip link delete $IFACE type dummy
rmmod dummy
