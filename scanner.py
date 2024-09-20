#!/usr/bin/python
import socket  # socket kutubxonasini import qilib olamiz

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # va bular orqali connection hosil qilamiz
# IPv4 va IPv6 bog'lanishlarni uchun ""socket.AF_INET,socket.SOCK_STREAM""
host = "127.0.0.1"  # bu bizning local hostimiz
port = 80  # bu port raqami


def portscanner(port):  # method yaratamiz
    if conn.connect_ex((host, port)):  # bu yerda portga  connection hosil qila olmasa xabar beradi
        print("%d porti yopiq ekan" % (port))
    else:
        print("%d porti yopiq ekan" % (port))


portscanner(port)  # methodimizni ishlatamiz
