import serial
import time
serial_port = '/dev/cu.usbserial-DN035LY4' # rename to your serial port
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
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
            line = ser.readline();
            line = line.decode("utf-8") #ser.readline returns a binary, convert to string
            print(line);
            output_file.write(line);
        else:
            timestr = newtimestr
            write_to_file_path = newminstr + ".txt"
            output_file = open(write_to_file_path, "a+")
    except:
        #        print("Please reconnect USB")
        time.sleep(0)

