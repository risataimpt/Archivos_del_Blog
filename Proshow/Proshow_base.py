#!/usr/bin/python
# _*_ coding:utf-8 _*_

junk  = "\x41" * 20000

arch = open("load", "wb")
arch.write(junk)
arch.close()

print "\nArchivo creado\n"
print "Basura  " + str(len(junk))
