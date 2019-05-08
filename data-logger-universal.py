from serial.tools.list_ports import comports
from sys import exit
import serial
import time
import argparse

parser = argparse.ArgumentParser(
    description='Log Serial data stream into files.')
parser.add_argument(
    '--sn', dest='sn', nargs=1, help='Serial number of USB device.')
parser.add_argument(
    '--vid', dest='vid', nargs=1, help='Vendor ID of the device.', type=int)
parser.add_argument(
    '--pid', dest='pid', nargs=1, help='Product ID of the device.', type=int)
parser.add_argument(
    '--port', dest='port', nargs=1, help='Port Address of the device',
)
parser.add_argument(
    '--baud', dest='baud', nargs=1, help='Baud rate of the connection',
    type=int, default=115200)


def find_device(sn=None, vid=None, pid=None, port=None):
    if sn is None and vid is None and pid is None and port is None:
        raise ValueError('At least specify one of the filters.')
    for port in comports():
        if sn is not None and port.serial_number != port[0]:
            continue
        if vid is not None and port.vid != vid[0]:
            continue
        if pid is not None and port.pid != pid[0]:
            continue
        if port is not None and port.device != port[0]:
            continue
        return port.device
    return None


args = parser.parse_args()
serial_port = find_device(args.sn, args.vid, args.pid, args.port)
baud_rate = args.baud

if serial_port is None:
    print('No serial port that matches your spec exists!')
    exit(1)

print('Now recording from %s at baud %d' % (serial_port, baud_rate))

timestr = time.strftime("%Y-%m-%d")
write_to_file_path = timestr + ".txt"
output_file = open(write_to_file_path, "a+")
ser = serial.Serial(serial_port, baud_rate)

try:
    while (True):
        try:
            newtimestr = time.strftime("%Y-%m-%d")
            if (timestr == newtimestr):
                line = ser.readline().decode('utf-8')
                output_file.write(line)
            else:
                if not output_file.closed:
                    output_file.close()
                timestr = newtimestr
                write_to_file_path = timestr + ".txt"
                output_file = open(write_to_file_path, "a+")
        except Exception:
            print("Connection is severed. Waiting for reconnect.")
            # Must close the port before moving on
            if not ser.closed:
                ser.close()
            serial_port = None
            # Wait until a new port is found
            while (serial_port is None):
                serial_port = find_device(
                    args.sn, args.vid, args.pid, args.port)
                time.sleep(2)
            print('Device is found! Address = %s' % serial_port)
            ser = serial.Serial(serial_port, baud_rate)

except KeyboardInterrupt:
    if not output_file.closed:
        output_file.close()
