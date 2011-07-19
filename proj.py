#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS

import sys, os, pyproj
import datetime
from pylab import *

import catalogues,solarsystem,util,sesame
import ephem

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  A6,A5,A4, A3,A2,A1, A0, landscape, portrait 

from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont( TTFont( 'arial', 'arial.ttf') )

fontscale=1.8

class styles:
	def Cross(self,c,x,y):
		c.saveState()
		c.setStrokeColor(Color( 0.,0., 0., alpha=0.6))
		c.setFillColor(Color( 0.2,0.2, 0.8, alpha=0.6))
		c.setLineWidth(0.1)
		c.setFont("Helvetica", 2.5*fontscale)
		c.translate(x,y)
		c.scale(2,2)
		c.circle(0,0,r=0.2,stroke=1,fill=1)
		p=c.beginPath()
		p.moveTo(0,1)
		p.lineTo(0,-1)
		p.moveTo(1,0)
		p.lineTo(-1,0)
		c.drawPath(p,stroke=1,fill=0)
		c.restoreState()

	def OC(self,c,x,y):
		c.saveState()
		c.setStrokeColor(Color(0.8,0.2, 0.8, alpha=0.6))
		c.setFillColor(Color( 0.8,0.2, 0.8, alpha=0.6))
		c.setLineWidth(0.1)
		c.setFont("Helvetica", 2.5*fontscale)
		c.translate(x,y)
		c.scale(2,2)
		for i in xrange(0,10):
			beta=i*pi/5
			xx=cos(beta)
			yy=sin(beta)
			c.circle(xx,yy,0.2,fill=0,stroke=1)
		c.restoreState()

	def Gb(self,c,x,y):
		c.saveState()
		c.setStrokeColor(Color( 0.,0., 0., alpha=0.6))
		c.setFillColor(Color( 0.2,0.2, 0.8, alpha=0.6))
		c.setLineWidth(0.1)
		c.setFont("Helvetica", 2.5*fontscale)
		c.translate(x,y)
		c.scale(2,2)
		c.circle(0,0,r=1,stroke=1,fill=1)
		p=c.beginPath()
		p.moveTo(0,1)
		p.lineTo(0,-1)
		p.moveTo(1,0)
		p.lineTo(-1,0)
		c.drawPath(p,stroke=1,fill=0)
		c.restoreState()

	def Pl(self,c,x,y):
		c.saveState()
		c.setStrokeColor(Color( 0.5,0.1, 0.2, alpha=0.6))
		c.setFillColor(Color( 0.5,0.1, 0.2, alpha=0.6))
		c.setLineWidth(0.1)
		c.setFont("Helvetica", 2.5*fontscale)
		c.translate(x,y)
		c.scale(2,2)
		c.setDash(0.6,0.3)
		c.circle(0,0,r=1,stroke=1,fill=0)
		c.restoreState()

	def Gx(self,c,x,y):
		c.saveState()
		c.setStrokeColor(Color(  0.1,0.3, 0.1, alpha=0.6))
		c.setFillColor(Color(  0.1,0.3, 0.1, alpha=0.4))
		c.setLineWidth(0.1)
		c.setFont("Helvetica", 2.5*fontscale)
		c.translate(x,y)
		c.scale(2,2)
		c.ellipse(-1,-0.5,1,0.5,stroke=1,fill=0)
		c.restoreState()

	def Nb(self,c,x,y):
		c.saveState()
		c.setStrokeColor(Color( 0.2,0.8, 0.8, alpha=0.8	))
		c.setFillColor(Color( 0.2,0.8, 0.8, alpha=0.8	))
		c.setLineWidth(0.1)
		c.setFont("Helvetica", 2.5*fontscale)
		c.translate(x,y)
		c.scale(2,2)
		c.setDash(0.3,0.015)
		c.rect(-1,-1,2,2,stroke=1,fill=0)
		c.restoreState()


	def C_N(self,c,x,y):
		c.saveState()
		c.setStrokeColor(Color( 0.1,0.6, 0.6, alpha=0.8	))
		c.setFillColor(Color( 0.1,0.6, 0.6, alpha=0.15	))
		c.setLineWidth(0.05)
		c.setFont("Helvetica", 2.5*fontscale)
		c.translate(x,y)
		c.scale(2,2)
		c.rect(-1,-1,2,2,stroke=1,fill=1)
		c.setDash(0.3,0.15)
		c.rect(-1.1,-1.1,2.4,2.4,stroke=1,fill=0)
		c.restoreState()

	def Mark(self,c,x,y):
		print x,y
		c.saveState()
		c.setStrokeColor(Color( 1,0., 0., alpha=0.8))
		c.setFillColor(Color( 1,0.0, 0.0, alpha=0.01))
		c.setLineWidth(0.05)
		c.setFont("Helvetica", 2.5*fontscale)
		c.translate(x,y)
		c.scale(4,4)
		c.circle(0,0,r=1,stroke=1,fill=1)
		p=c.beginPath()
		p.moveTo(0,1)
		p.lineTo(0,-1)
		p.moveTo(1,0)
		p.lineTo(-1,0)
		c.drawPath(p,stroke=1,fill=0)
		c.restoreState()

class StarsMap:
	paper=landscape(A3)
	magLim=3.5
	projection="merc"
	altaz=0
	c = canvas.Canvas('carta.pdf')	
      	prj=pyproj.Proj("+proj=merc")
	s=[]
	H=catalogues.HiparcosCatalogue()
	Cross=catalogues.crossCatalogue()
	n=catalogues.ngcCatalogue()
	observer=ephem.city('Madrid')
	xfactor=0.
	yfactor=0.
	paperwidth, paperheight = A3
	lonmax,lonmin=0,0
	latmax,latmin=0,0
	scale=1
	brocha=styles()
	
	def __init__(self,paper=landscape(A3),magLim=3.5,projection="merc",output='carta.pdf',costellation_list='',altaz=0,city='Madrid',date=ephem.now()):


		self.paper=paper
		self.altaz=altaz
		self.observer=ephem.city(city)
		self.observer.date=date
		self.s=solarsystem.SolarSystem(self.observer)
		self.magLim=magLim
		self.projection=projection
		self.paperwidth, self.paperheight = self.paper			
		self.c = canvas.Canvas(output, pagesize=self.paper)




		from reportlab.lib.colors import Color
		self.c.setFillColor(Color( 0.,0., 0., alpha=1))	
#		self.c.rect(0,0,self.paperwidth,self.paperheight,fill=1,stroke=0)

		if altaz!=0:
			ra,dec=self.observer.radec_of(0,'90')
			ra=ra*180/pi
			dec=dec*180/pi
			zenit=" +lon_0="+str(ra)+" +lat_0="+str(dec)
			print zenit
		       	self.prj=pyproj.Proj("+proj="+self.projection+zenit)
		else:
			self.prj=pyproj.Proj("+proj="+self.projection)

       		self.prj_ra_dec=pyproj.Proj("+proj=lonlat +ellps=sphere")	


		self.xfactor=5.8
		self.yfactor=self.xfactor*self.paperheight/self.paperwidth
		self.scale=1
		(self.lonmin,self.latmin),(self.lonmax,self.latmax)=self.getCostellationsLimits(costellation_list)
		print (self.lonmin,self.latmin),(self.lonmax,self.latmax)
		x0,y0=self.p(self.lonmin,self.latmin)
		x1,y1=self.p(self.lonmax,self.latmax)
		self.scale=max((x1-x0)/self.paperwidth,(y1-y0)/self.paperheight)
		print x0,y0,self.scale
		#self.c.scale(1/self.scale,1/self.scale)
		#self.c.translate(-x0,-y0)

	def update(self):
		if self.altaz!=0:
			ra,dec=self.observer.radec_of(0,'90')
			ra=ra*180/pi
			dec=dec*180/pi
			zenit=" +lon_0="+str(ra)+" +lat_0="+str(dec)
			print zenit,self.observer.date
		  	self.prj=pyproj.Proj("+proj="+self.projection+zenit)
		else:
		       	self.prj=pyproj.Proj("+proj="+self.projection)

	def drawGalacticPlane(self):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.2,0.8, 0.2, alpha=0.2))
		self.c.setFillColor(Color( 0.2,0.8, 0.2, alpha=0.2))
		self.c.setLineWidth(1)
		#s=solarsystem.SolarSystem(self.observer)
		self.drawLine(self.s.galacticPlane())
			


	def drawNGC(self,filter_ngcs):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.,0., 0., alpha=0.6))
		self.c.setLineWidth(0.1)
		self.c.setFont("Helvetica", 2.5*fontscale)
		names=[]
		
		self.c.setFillColor(Color( 0.2,0.2, 0.8, alpha=0.4))
		filter_ngcs_Gb=filter(lambda x:'Gb' in x[1],filter_ngcs)
		names=[]
		for ngc in filter_ngcs_Gb:
			r=1
			x,y=self.p(ngc[2],ngc[3])
			#self.c.circle(x,y, r, stroke=1, fill=1)
			self.brocha.Gb(self.c,x,y)
			if (ngc[6] not in names):
				self.c.drawString(x,y+2,ngc[6])
				names.append(ngc[6])

		
		self.c.setFillColor(Color( 0.8,0.2, 0.8, alpha=0.5))
		filter_ngcs_OC=filter(lambda x:'OC' in x[1],filter_ngcs)
		names=[]
		for ngc in filter_ngcs_OC:
			r=1
			x,y=self.p(ngc[2],ngc[3])
		#	self.c.circle(x,y, r, stroke=1, fill=1)
			self.brocha.OC(self.c,x,y)
			if (ngc[6] not in names):
				self.c.drawString(x,y+2,ngc[6])
				names.append(ngc[6])

		self.c.setFillColor(Color( 0.2,0.8, 0.8, alpha=0.5))
		filter_ngcs_C_N=filter(lambda x:'C+N' in x[1],filter_ngcs)
		names=[]
		for ngc in filter_ngcs_C_N:
			r=1
			x,y=self.p(ngc[2],ngc[3])
		#	self.c.circle(x,y, r, stroke=1, fill=1)
			self.brocha.C_N(self.c,x,y)
			if (ngc[6] not in names):
				self.c.drawString(x,y+2,ngc[6])
				names.append(ngc[6])

		self.c.setFillColor(Color( 0.2,0.8, 0.8, alpha=0.5))
		filter_ngcs_Nb=filter(lambda x:'Nb' in x[1],filter_ngcs)
		names=[]
		for ngc in filter_ngcs_Nb:
			r=1
			x,y=self.p(ngc[2],ngc[3])
			#self.c.circle(x,y, r, stroke=1, fill=1)
			self.brocha.Nb(self.c,x,y)
			if (ngc[6] not in names):
				self.c.drawString(x,y+2,ngc[6])
				names.append(ngc[6])

		self.c.setFillColor(Color( 0.1,0.3, 0.1, alpha=0.4))
		filter_ngcs_Gx=filter(lambda x:'Gx' in x[1],filter_ngcs)
		names=[]
		for ngc in filter_ngcs_Gx:
			r=1
			x,y=self.p(ngc[2],ngc[3])
#			self.c.circle(x,y, r, stroke=1, fill=1)	
			self.brocha.Gx(self.c,x,y)
			if (ngc[6] not in names):
				self.c.drawString(x,y+2,ngc[6])
				names.append(ngc[6])


		self.c.setFillColor(Color( 0.5,0.1, 0.2, alpha=0.4))
		filter_ngcs_Pl=filter(lambda x:'Pl' in x[1],filter_ngcs)
		names=[]
		for ngc in filter_ngcs_Pl:
			r=1
			x,y=self.p(ngc[2],ngc[3])
			#self.c.circle(x,y, r, stroke=1, fill=1)
			self.brocha.Pl(self.c,x,y)
			if (ngc[6] not in names):
				self.c.drawString(x,y+2,ngc[6])
				names.append(ngc[6])



	def drawStars(self,stars):
		self.c.setLineWidth(0.1)
		for s in stars:
			if s[19] <=self.magLim:
				self.c.setFillColor(self.mapColor(s[23]))
				r=(self.magLim-s[19])*0.2*7/self.magLim+0.005
				x,y=self.p(s[4]*180/pi,s[5]*180/pi)
				self.c.circle(x,y, r, stroke=1, fill=1)


	def starsNames(self,mag):

		self.c.setLineWidth(0.1)
		self.c.setStrokeColor(Color( 0.,0., 0., alpha=1))
		self.c.setFillColor(Color( 0,0,0, alpha=0.4))
		self.c.setFont("arial", 2*fontscale)
		stars=filter(lambda x:len(x[-2])!=0 and x[7] < mag,self.Cross.stars)
		#print set(map(lambda x:x[-3],self.Cross.stars))
		for s in stars:
			if len(s[-3])==0:
				name=s[-4]+' '+s[-1]
			else:
				name=s[-3]+' '+s[-1]
			x,y=self.p(s[5],s[6])
			self.c.drawString(x+1,y+1,name)
	

	def drawBodies(self,bodieslist='ALL'):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.,0., 0., alpha=0.6))
		self.c.setFillColor(Color( 0.8,0.2, 0.2, alpha=0.4))
		self.c.setLineWidth(0.2)
		self.c.setFont("Helvetica", 2.5*fontscale)
		for b in self.s.bodiesPosition():
				r=(5*b[3]/3600)
				x,y=self.p(b[1]*180/pi,b[2]*180/pi)
				self.c.circle(x,y, r, stroke=1, fill=1)		
				self.c.drawString(x,y-2,b[0])
		

	def p(self,lon,lat):
		if 0==1:
			g=ephem.Galactic(ephem.Equatorial(lon*pi/180.,lat*pi/180., epoch=ephem.J2000), epoch=ephem.J2000)
			lon= g.long*180/pi
			lat= g.lat*180/pi			
		#print lon,lat
		try:
			x,y = pyproj.transform(self.prj_ra_dec,self.prj,lon,lat)	
		except:
			return (-999999,-999999)
		x=-x*self.paperwidth/self.xfactor+self.paperwidth/2
		y=y*self.paperheight/self.yfactor+self.paperheight/2
#		x=x*self.paperwidth/self.scale+self.paperwidth/2
#		y=y*self.paperwidth/self.scale+self.paperheight/2
		return x,y
		
	def close(self):
		self.c.showPage()
		self.c.save()
		
	def drawEcliptic(self):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.8,0.2, 0.8, alpha=0.4))
		self.c.setLineWidth(0.2)
		#s=solarsystem.SolarSystem(self.observer)
		self.drawLine(self.s.ecliptic())
#		self.drawLine(self.s.moonPath())
#		self.drawLine(self.s.issPath())								

	def mapColor(self,B_V):
		from reportlab.lib.colors import Color
		B_V=B_V
		if B_V <= -0.29:
			c=Color(0.100*1.5,0.149*1.5,0.237*1.5)
			return c
		if B_V <= 0.0:
			c=Color(0.255*1.5,0.250*1.5,0.205*1.5)
			return c
		if B_V <= 0.31:
			c=Color(0.255,0.250,0.205)
			return c
		if B_V <= 0.59:
			c=Color(0.255,0.255,0.0)
			return c
		if B_V <= 0.82:
			c=Color(0.255,0.127,0.80)
			return c
		if B_V <= 1.41:
			c=Color(0.255,0.99,0.71)
			return c
		c=Color(0.255,0.0,0.0)
		return c

	def drawHorizontalGrid(self):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.7,0.4, 1, alpha=0.4))
		self.c.setFillColor(Color( 0.7,0.4, 1, alpha=0.4))
		self.c.setLineWidth(0.4)
		self.c.setFont("Helvetica", 2.5*fontscale)
		date=ephem.localtime(self.observer.date).strftime('%d-%m-%Y %H:%M')
		#zenit
		ra,dec=self.observer.radec_of(0,'90')
		x,y=self.p(ra*180/pi,dec*180/pi)
		self.c.circle(x,y, 5, stroke=1, fill=0)
		self.c.circle(x,y, 2, stroke=1, fill=0)		
		self.c.drawString(x,y,'ZENIT'+date)

		#North
		ra,dec=self.observer.radec_of('0','20')
		x,y=self.p(ra*180/pi,dec*180/pi)
		self.c.circle(x,y, 2, stroke=1, fill=0)	
		self.c.drawString(x,y,'N'+date)

		#Sud
		ra,dec=self.observer.radec_of('180','20')
		x,y=self.p(ra*180/pi,dec*180/pi)
		self.c.circle(x,y, 2, stroke=1, fill=0)	
		self.c.drawString(x,y,'S'+date)

		#EAST
		ra,dec=self.observer.radec_of('90','20')
		x,y=self.p(ra*180/pi,dec*180/pi)
		self.c.circle(x,y, 2, stroke=1, fill=0)	
		self.c.drawString(x,y,'E'+date)

		#WEST
		ra,dec=self.observer.radec_of('270','20')
		x,y=self.p(ra*180/pi,dec*180/pi)
		self.c.circle(x,y, 2, stroke=1, fill=0)	
		self.c.drawString(x,y,'0'+date)
		
		#horizon
		for k in (0,20):
			ra,dec=self.observer.radec_of(1,str(k))
			x,y=self.p(ra*180/pi,dec*180/pi)
			self.c.drawString(x,y,'Horizonte:'+str(k)+' º'+date)
		        for i in range(0,360):
				ra,dec=self.observer.radec_of(str(i),str(k))
				x,y=self.p(ra*180/pi,dec*180/pi)
				self.c.circle(x,y, 0.4, stroke=1, fill=0)	
		
	

	def drawEcuatorialGrid(self,step=10):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.2,0.2, 0.2, alpha=0.1))
		self.c.setLineWidth(0.3)
		self.c.setFont("Helvetica", 4)
		#equalat lines
		for lat in range(-90,90,step):
			p=[]
			t=self.p(0,lat)
			self.c.drawString(t[0],t[1],str(lat))
			t=self.p(180,lat)
			self.c.drawString(t[0],t[1],str(lat))

			for x in range (0,360):
				pp=(x,lat)
				p.append(pp)
			self.drawLine(p)	
		#equalon lines
		for lon in range(0,360,step):
			p=[]
			t=self.p(lon,0)
			self.c.drawString(t[0],t[1],str(lon))
			for y in range (-90,90):
				pp=(lon,y)
				p.append(pp)
			self.drawLine(p)	

	def drawGalacticGrid(self):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.2,0.8, 0.2, alpha=0.2))
		self.c.setFillColor(Color( 0.2,0.8, 0.2, alpha=0.2))
		self.c.setLineWidth(0.3)
		self.c.setFont("Helvetica", 2.5*fontscale)
		#equalat lines
		for lat in range(-90,90,10):
			p=[]
			g=ephem.Equatorial(ephem.Galactic(0,lat*pi/180,epoch=ephem.J2000),epoch=ephem.J2000)
			t=self.p(g.ra*180/pi,g.dec*180/pi)
			self.c.drawString(t[0],t[1],str(lat))

			for x in range (-180,180):
				g=ephem.Equatorial(ephem.Galactic(x*pi/180,lat*pi/180,epoch=ephem.J2000),epoch=ephem.J2000)
				pp=(g.ra*180/pi,g.dec*180/pi)
				p.append(pp)
			self.drawLine(p)	
		#equalon lines
		for lon in range(-180,180,10):
			p=[]
			for y in range (-90,90):
				g=ephem.Equatorial(ephem.Galactic(lon*pi/180,y*pi/180,epoch=ephem.J2000),epoch=ephem.J2000)
				pp=(g.ra*180/pi,g.dec*180/pi)
				p.append(pp)
			self.drawLine(p)	
		#n Y s
		nn=ephem.Equatorial(ephem.Galactic(0,pi/2,epoch=ephem.J2000),epoch=ephem.J2000)
		ss=ephem.Equatorial(ephem.Galactic(0,-pi/2,epoch=ephem.J2000),epoch=ephem.J2000)
		zz=ephem.Equatorial(ephem.Galactic(0,0,epoch=ephem.J2000),epoch=ephem.J2000)
		x,y=self.p(nn.ra*180/pi,nn.dec*180/pi)
		self.c.circle(x,y, 2, stroke=1, fill=1)
		x,y=self.p(ss.ra*180/pi,ss.dec*180/pi)
		self.c.circle(x,y, 2, stroke=1, fill=1)
		x,y=self.p(zz.ra*180/pi,zz.dec*180/pi)		
		self.c.circle(x,y, 2, stroke=1, fill=1)





	def drawLine(self,pointlist):
		i=0
		pa = self.c.beginPath()
		if (-999999,-999999) in pointlist:
			print "drawline ERROR:",pointlist
			return
		for pp in pointlist:
			x,y=self.p(pp[0],pp[1])		
			if i==0:
				pa.moveTo(x,y)
				i=1
			else:
				if (x-xold)**2+(y-yold)**2 >=(self.paperwidth/2.5)**2:   #demasido lejos no la pinto
					pa.moveTo(x,y)
				else:
					pa.lineTo(x,y)
			xold,yold=x,y
		self.c.drawPath(pa, fill=0)

	def drawCostellationsLimits(self):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.2,0.2, 0.4, alpha=0.2))
		self.c.setLineWidth(0.2)
		bounds=catalogues.CostellationBounds()
		costellations=set(map(lambda x:x[2],bounds))
		for costellation in costellations:
			l=filter(lambda x:x[2]==costellation,bounds)
			l=map(lambda x:[x[0],x[1]],l)
			self.drawLine(l)		

	def drawCostellationsFigures(self):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.1,0.2, 0.7, alpha=0.5))
		self.c.setLineWidth(0.2)
		figures=catalogues.CostellationFigures()
		costellations=set(map(lambda x:x[0],figures))
		for costellation in costellations:
			data=filter(lambda x:x[0]==costellation,figures)[0]		
			data=list(util.group(data[2:],2))
			for s in data:	
				star1=self.H.search(s[0])
				star2=self.H.search(s[1])
				if star1!=None and star2!=None:
					costellation_line=((star1[4]*180/pi,star1[5]*180/pi),(star2[4]*180/pi,star2[5]*180/pi))
					self.drawLine(costellation_line)

	def getCostellationsLimits(self,costellation_list):
		if costellation_list == (''):
			return (0,-90),(360,90)
		bounds=catalogues.CostellationBounds()
		bounds=filter(lambda x:x[2] in costellation_list,bounds)
		lons=map(lambda x:x[0],bounds)
		lats=map(lambda x:x[1],bounds)
		return (min(lons),min(lats)),(max(lons),max(lats))

	def checkInCostellation(self,pointList):
		pass			


	def drawComet(self,obj,interval=40):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 1,0.2, 0.7, alpha=0.2))
		self.c.setFillColor(Color( 1,0.2, 0.7, alpha=0.8))
		self.c.setLineWidth(0.5)
		self.c.setFont("Helvetica", 2.5*fontscale)
		pos=self.s.cometOrbit(obj,self.observer.date,interval)
		path=map(lambda x:(x[1],x[2]),pos)
		self.drawLine(path)
		i=0
		for s in pos:
			if i % 3 == 0:
				name=s[0].strftime('%d-%m-%Y')
				x,y=self.p(s[1],s[2])
				self.c.drawString(x,y,name)		
			i=i+1
		
	def drawISS(self):
		from reportlab.lib.colors import Color
		self.c.setStrokeColor(Color( 0.2,0.2, 1, alpha=0.2))
		self.c.setFillColor(Color( 0.2,0.2, 1, alpha=0.8))
		self.c.setLineWidth(0.5)
		self.c.setFont("Helvetica", 2.5*fontscale)
		pos=self.s.issOrbit(self.s.issNext(),30)
		path=map(lambda x:(x[1],x[2]),pos)
		self.drawLine(path)
		for s in pos:
			name=s[0].strftime('%d-%m-%Y %H:%M:%S')
			x,y=self.p(s[1],s[2])
			self.c.drawString(x,y,'ISS at:'+name)
		

	def drawMarks(self,fichero):
		self.c.setFont("Helvetica", 2.5*fontscale)
		self.c.setFillColor(Color( 1,0.0, 0.0, alpha=0.4))
		se=sesame.sesame(fichero)
		for o in se.obj_data:
			x,y=self.p(o[1],o[2])
			self.brocha.Mark(self.c,x,y)
			self.c.drawString(x+1,y-8,o[0])


if __name__ == "__main__":

	m=StarsMap(magLim=8,projection="moll +lat_0=42  +ellps=sphere +R=1.4",paper=landscape(A3),costellation_list='',city='Madrid',altaz=1,date=ephem.now()+ephem.hour*24*0+ephem.hour*7)
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
#	m.drawMarks("valladar22_1_2010.obj")
	m.drawHorizontalGrid()
#	m.drawComet('103P/Hartley',interval=10)
	m.drawBodies()
	m.drawNGC(m.n.filter(0,-90,360,90))
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

	m.close()



