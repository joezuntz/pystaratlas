#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS
import sys, os, pyproj
import datetime
from pylab import *


projection="moll  +ellps=sphere +R=1"
prj_ra_dec=pyproj.Proj("+proj=lonlat +ellps=sphere")
prj=pyproj.Proj("+proj="+projection)
x,y=0,10

lon,lat = pyproj.transform(prj,prj_ra_dec,x,y)	
try:
	pass
except:
	print "EXcept.."
