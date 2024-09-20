#!/usr/bin/python
import socket  # socket kutubxonasini import qilib olamiz
from termcolor import colored
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # va bular orqali connection hosil qilamiz

socket.setdefaulttimeout(5)
# IPv4 va IPv6 bog'lanishlarni uchun ""socket.AF_INET,socket.SOCK_STREAM""
host = input("-[#]- IP Manzilni kiriting:")  # bu bizning local hostimiz
# port = int(input("-[#]- Port raqamini kiriting:"))   # bu port raqami


def portscanner(port):  # method yaratamiz
    if conn.connect_ex((host, port)):  # bu yerda portga  connection hosil qila olmasa xabar beradi
        print(colored("%d porti yopiq ekan" % (port),'grey',attrs=['reverse']))
    else:
        print(colored("%d _________[[[[ porti ochiq ekan ]]]]______________" % (port),'green',attrs=['bold']))


for port in range(1, 10000):
    portscanner(port)

