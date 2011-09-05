#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS

import PIL.ImageOps
from sesame import * 
from proj import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  A6,A5,A4, A3,A2,A1, A0, landscape, portrait 
	
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont( TTFont( 'arial', 'arial.ttf') )

paper=portrait(A4)
paperwidth, paperheight = paper
c = canvas.Canvas('14_5_2011.pdf', pagesize=paper)
c.setFont("Helvetica", 10)


def mapa():
	m=StarsMap(magLim=6,projection="moll +lon 0=90w +lat 1=20n +lat 2=60 moll +lat_0=42  +ellps=sphere +R=1.",paper=landscape(A4),costellation_list='',city='Madrid',altaz=1,date=ephem.now()+ephem.hour*(24*3)+ephem.hour*2)
	#m.observer.date=m.s.issNext() -ephem.minute
	#m.update()


	"""
	s=m.H.filter(0,0,50,50)
	print s
	m.drawStars(s)
	
	m.drawComet('103P/Hartley')


	m.drawComet('81P/Wild')
	m.drawComet('C/2009 R1')

	m.drawISS()
	m.starsNames(4)
"""
	m.drawMarks("skymaps.obj")
	m.drawHorizontalGrid()
#	m.drawComet('103P/Hartley',interval=10)
	m.drawBodies()
#	m.drawNGC(m.n.filter(0,-90,360,90))
	m.drawCostellationsLimits()
	m.drawCostellationsFigures()
	m.drawEcuatorialGrid()
	m.drawEcliptic()
	m.starsNames(5)
	s=m.H.filter(0,-90,360,90,plx=0)
	m.drawStars(s)
	m.drawGalacticPlane()
	m.drawGalacticGrid()
#	m.drawISS()


def objBook():
	se=sesame.sesame()
	#se.fromFile("valladar22_1_2010.obj")
	se.fromFile("skymaps.obj")
	imsize=180
	sep=10
	x=20
	y=paperheight-sep*2-imsize
	pagina=1
	pie0="AAM Grupo IO. Propuesta de observación 14 Mayo 2011. Fernando Fernandez/Nacho Mas."
	pie1="Imágenes del DSS2 (http://www.skymap.com). Todas las imágenes tiene 0.5 grados de ancho/alto."
	for o in se.obj_data:
		se.skyMapImage(o)
		image = Image.open(o[0]+'.png')
		#image=image.resize((400,400))
		inverted_image = PIL.ImageOps.invert(image)
		inverted_image.save('inverted_'+o[0]+'.png')
		c.drawString(x,y,o[0])
		#c.drawString(x+30,y,str(o[1]))
		#c.drawString(x+60,y,str(o[2]))
		c.drawImage('inverted_'+o[0]+'.png',x,y+10,imsize,imsize)
		#c.drawImage(o[0]+'.png',x,y+10,imsize,imsize)
		x=x+sep+imsize
		if (x+imsize+sep)>paperwidth:
			x=20
			y=y-sep*2-imsize
		if y<sep:
			c.setFont("Helvetica", 8)
			c.drawString(20,20,pie0)
			c.drawString(20,10,pie1)
			c.drawString(paperwidth-40,10,'Pag.'+str(pagina))
			pagina=pagina+1
			x=20
			y=paperheight-sep*2-imsize
			c.showPage()
			c.setFont("Helvetica", 10)
		#se.toRGB565(o[0])
	c.drawString(20,20,pie0)
	c.drawString(20,10,pie1)
	c.drawString(paperwidth-40,10,'Pag.'+str(pagina))
	c.showPage()
	c.save()

mapa()
c.showPage()
#objBook()
