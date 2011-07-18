#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS
import commands,os

Gsize=9
N=(360/Gsize)*(180/Gsize)
for i in range(0,N):
	res=commands.getoutput("cat "+str(i)+".rgb565>>image9.rgb565.raw")
	print res
