import serial
import time
SN = "DN042K2B"
from serial.tools.list_ports import comports
a=list(comports())
i = 0
while (True):
    a=list(comports())
    if a[i].serial_number == None:
        if i == len(a)-1:
            i = 0
            continue
        else:
            i = i+1
            continue
    elif SN in a[i].serial_number:
        break
    else:
        i = i+1
serial_port = a[i].device # rename to your serial port
baud_rate = 38400; #In arduino, Serial.begin(baud_rate)
#yearstr = time.strftime("%Y")
#monthstr = time.strftime("%m")
#daystr = time.strftime("%d")
#minstr = time.strftime("%M")
timestr = time.strftime("%Y-%m-%d")
write_to_file_path = timestr + ".txt"
output_file = open(write_to_file_path, "a+")
while (True):
    try:
        newtimestr = time.strftime("%Y-%m-%d")
        if (timestr == newtimestr):
            ser = serial.Serial(serial_port, baud_rate)
            line1 = ser.readline();
            line1 = line1.decode("utf-8") #ser.readline returns a binary, convert to string
            line2 = ser.readline();
            line2 = line2.decode("utf-8") #ser.readline returns a binary, convert to string
            line3 = ser.readline();
            line3 = line3.decode("utf-8") #ser.readline returns a binary, convert to string
            print(line1)
            print(line2)
            print(line3)
            output_file.write(line1)
            output_file.write(line2)
            output_file.write(line3)
        else:
            timestr = newtimestr
            write_to_file_path = timestr + ".txt"
            output_file = open(write_to_file_path, "a+")
    except:
        #print("Please reconnect USB")
        i = 0
        while (True):
            a=list(comports())
            if a[i].serial_number == None:
                if i == len(a)-1:
                    i = 0
                    continue
                else:
                    i = i+1
                    continue
            elif SN in a[i].serial_number:
                break
            else:
                i = i+1
        serial_port = a[i].device
        continue
        #time.sleep(0)

