#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS
import proj
from reportlab.lib.pagesizes import  A6,A5,A4, A3,A2,A1, A0, landscape, portrait 

m=proj.StarsMap(magLim=10,projection="moll  +ellps=sphere +R=1  ",paper=landscape(A4),costellation_list='',city='Madrid',altaz=0)
ra_step=60
dec_step=45

for ra in range(0,360,ra_step):
	for dec in range(-45,45,dec_step):
		print ra,dec
		m.projection="merc  +ellps=sphere +R=5  +lon_0="+str(ra+ra_step)+" +lat_0="+str(dec)
		m.update()
#		m.c.scale(5.5,4.5)
		x0,y0=m.p(ra,dec)
		x1,y1=m.p(ra+ra_step,dec+dec_step)
		m.c.translate(-x1,-y0)
#		m.drawBodies()
		m.drawCostellationsLimits()
		m.drawCostellationsFigures()
		m.drawEcuatorialGrid(step=5)
		m.drawEcliptic()
		m.starsNames(10)
		s=m.H.filter(ra,dec,ra+ra_step,dec+dec_step)
		m.drawStars(s)
		s=m.n.filter(ra,dec,ra+ra_step,dec+dec_step)
		m.drawNGC(s)
		m.c.showPage()
m.close()
