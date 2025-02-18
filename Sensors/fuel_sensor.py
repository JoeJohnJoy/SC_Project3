import socket
import time
import sys 
#import random


try:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    signal_port = 33000 + 10*arg1 + arg2

except IndexError:
    print("Must provide two arguments: the vehicle number and the sensor number")
    exit()
except ValueError:
    print("The vehicle number and the sensor number must be valid integers.")
    exit()

signal_host = "10.35.70.2"

print("UDP target IP:", signal_host)
print("UDP target port:", signal_port)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP

f = 0.0 

while True:
    f = f + 0.5
    print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " FUEL CONSUMED = " + str(f) + "%.")
    x = str(f)
    sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
    time.sleep(0.1)
    
    if(f == 0 or f < 0):
        f = 0.0 
        print("Vehicle " + str(arg1) + ", Sensor " + str(arg2) + " FUEL CONSUMED = " + str(f) + "%.")
        x = str(f)
        sock.sendto(x.encode('utf-8'), (signal_host, signal_port))
        time.sleep(0.1)
    if(f == 100):
        break;

sock.close()
    