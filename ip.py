red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
purple="\033[0;35m"
blue="\033[1;34m"
import socket, requests, os, sys
from requests import get
os.system('clear')
print(blue)
os.system('figlet IPChecker')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(10)
try:
	ip = get('https://api.ipify.org').text
	print(yellow+'Your public IP Address is:\n'+green+format(ip))
	s.connect(("8.8.8.8", 80))
	ip=s.getsockname()[0]
	if (ip.find("192") != -1):
		print(purple+"You are using Router based Wi-Fi.\n"+yellow+"Your localhost IP Address is:\n"+green+ip)
		exit()
	if (ip.find("172") != -1):
		print(purple+"You are using Router based Wi-Fi.\n"+yellow+"Your localhost IP Address is:\n"+green+ip)
		exit()
	else:
	    print(purple+"You are using BroadBand.\n"+yellow+"Your private IP Address is:\n"+green+ip)
except:
	print(red+"No internet")
s.close()