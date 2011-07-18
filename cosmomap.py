#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS

from optparse import OptionParser
from proj import *

usage = "usage: cosmomap.py [-p proyection ] [-b ((xleft,ybottom),(xright,ytop))] "
parser = OptionParser(usage=usage)

# general options
parser.add_option("-p", "--proyection", action="store",dest="proyection",type="string",
                  help="Proyection type")
parser.add_option("-c", "--city", action="store",dest="city",type="string",
                  help="City")
parser.add_option("-d", "--date", action="store_true",dest="date",
                  help="Map date")

parser.add_option("-a", "--alt_az", action="store_true",dest="altaz",default=False,
                  help="alt-az map")

parser.add_option("-t", "--title", action="store",dest="title",type="string",
                  help="Title text")

parser.add_option("-m", "--mag", action="store",dest="mag",type="string",
                  help="limit magnitude")


#include options
parser.add_option("-b", "--boundingbox", action="store_true",dest="bbox",
                  help="Map bounding box")
parser.add_option("-i", "--iss", action="store_true",dest="iss",
                  help="ISS Next pass")

parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default=True,
                  help="quite operation")

parser.add_option("-v", "--version", action="store",dest="version",
                  help="Version 0.1 nacho+")


(options, args) = parser.parse_args()



if options.proyection:
	p=options.proyection + "   +ellps=sphere +R=1"

else:
	p="moll  +ellps=sphere +R=1"

if options.city:
	city=options.city
else:
	city="Madrid"

if options.date:
	date=options.date
else:
	date=ephem.now()

if options.mag:
	mag=int(options.mag)
else:
	mag=8


		

m=StarsMap(magLim=mag,projection=p,paper=landscape(A3),costellation_list='',city=city,altaz=options.altaz,date=date)
m.drawHorizontalGrid()
m.drawComet('103P/Hartley',interval=10)
m.drawBodies()
m.drawNGC(m.n.filter(0,-90,360,90))
m.drawCostellationsLimits()
m.drawCostellationsFigures()
m.drawEcuatorialGrid()
m.drawEcliptic()
m.starsNames(4)
s=m.H.filter(0,-90,360,90,plx=0)
m.drawStars(s)
m.drawGalacticPlane()
m.drawGalacticGrid()
m.close()

