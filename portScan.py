#!/usr/bin/python
import socket, re
# set user expectations for what program will do
print ("Port scan for a single subnet with a range of IP addresses, IP range start must be less than IP range end, port range start must be less than port range end. ")
print ("IP addresses are assumed to be in same subnet. Start and finish are the last octet of the IP address. (Use same IP/Port to scan single IP/Port)")
ip1 = raw_input("enter the IP range start: ")
ip2 = raw_input("enter the IP range end: ")
port_start = input("enter the port range start: ")
port_end = input("enter the port range end: ")

# check user input values, apply to variables
list1 = ip1.split('.')
try:
    ip_start = int(list1[3])
    subnet1 = ('{0}.{1}.{2}.').format(list1[0],list1[1],list1[2])
except Exception as ex:
    print ("error: ").format(ex)
    exit(1)

list2 = ip2.split('.')
try:
    ip_end = int(list2[3])
    subnet2 = ('{0}.{1}.{2}.').format(list2[0],list2[1],list2[2])
except Exception as ex:
    print ("error: ").format(ex)
    exit(1)

# error handling
if subnet1 != subnet2:
    print "error: 2 subnets entered, this program can only scan 1 subnet at a time"
    exit(1)
if ip_start > ip_end:
    print "error: IP range start is greater than IP range end"
    exit(1)
if port_start > port_end:
    print "error: port range start is greater than port range end"
    exit(1)

for ip in range(ip_start, ip_end + 1):
    print ("Scanning IP: {0}{1}").format(subnet1, ip)
    current_ip = subnet1 + str(ip)
    for port in range(port_start, port_end + 1):
        # try to connect to the current port on current IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        # logic for if port is open or not
        if s.connect_ex((current_ip, port)):
            print ("port {0} is closed on IP: {1}").format(port, current_ip)
        else:
            print("port {0} is open on IP: {1}").format(port, current_ip)
print "Scan ended"
exit(0)

