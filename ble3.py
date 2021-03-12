import os
import subprocess
import select
import serial
import time
import json
import re
import threading

wpa_supplicant_conf = "/etc/wpa_supplicant/wpa_supplicant.conf"
sudo_mode = "sudo "
 
class SerialComm:
    def __init__(self):
        self.port = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=1)
 
    def read_serial(self):
        res = self.port.read(50)
        if len(res):
            return res.splitlines()
        else:
            return []
 
    def send_serial(self, text):
        self.port.write(text)
		
def inToSend():
	while(True):
		try:
			ble_comm = SerialComm()
			msg = raw_input()
			ble_comm.send_serial(msg) 
		except serial.SerialException:
			time.sleep(1)
	

def read():
	ble_comm = None
	isConnected = False
	while (True):
		try:
			ble_comm = SerialComm()
			out = ble_comm.read_serial()
			for ble_line in out:
				print(out)
		except serial.SerialException:
			print("waiting for connection")
			ble_comm = None
			isConnected = False
			time.sleep(1)
 
 
def main():
	thread = threading.Thread(target = inToSend, args = ())
	thread2 = threading.Thread(target = read, args = ())
	thread.start()
	thread2.start()
    

            
if __name__ == "__main__":
    main()