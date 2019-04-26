import serial
import time
serial_port = '/dev/cu.usbserial-DN042K2B' # rename to your serial port
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
        #        print("Please reconnect USB")
        time.sleep(0)

