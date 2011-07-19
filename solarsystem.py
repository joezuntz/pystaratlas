#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS
import ephem,internetcatalogues
from pylab import *
import copy

class SolarSystem:
	bodies=[ephem.Neptune(),ephem.Uranus(),ephem.Saturn(),ephem.Jupiter(),ephem.Mars(),ephem.Venus(),ephem.Mercury(),ephem.Sun(),ephem.Moon()]
	sobserver=[]
	iss=[]
	i=[]                             #internet catalogue for TLE and Comets

	def __init__(self,observer):
		self.sobserver=observer
		self.i=internetcatalogues.internetCatalogue()
		self.iss=self.i.ISS()



	def bodiesPosition(self,listbodies='ALL'):
		if listbodies=='ALL':
			bodies=self.bodies
		else:
			bodies=[]
			for b in listbodies:
				bb=filter(lambda x:x.name==b,self.bodies)
				bodies.append(bb[0])
		position=[]
		for b in bodies:
			b.compute(self.sobserver)
			position.append((b.name,b.a_ra,b.a_dec,b.size))
		return position

	def ecliptic(self):
		p=[]
		for t in range(-180,180):
			e=ephem.Equatorial(ephem.Ecliptic(t*pi/180,0,epoch=ephem.J2000),epoch=ephem.J2000)
			p.append((e.ra*180/pi,e.dec*180/pi))
		return p		
		
	def galacticPlane(self):
		p=[]
		for t in range(0,360):
			e=ephem.Equatorial(ephem.Galactic(t*pi/180,0,epoch=ephem.J2000),epoch=ephem.J2000)
			p.append((e.ra*180/pi,e.dec*180/pi))
		return p			

	
	def moonPath(self):
		p=[]
		m=ephem.Moon()
		olddate=self.sobserver.date
		obs=self.sobserver
		for t in range(0,5):
			obs.date+=ephem.hour*24*t
			m.compute(obs)	
			p.append((m.ra*180/pi,m.dec*180/pi))
		self.sobserver.date=olddate
		return p	


	def issNext(self):

		olddate=self.sobserver.date
		obs=self.sobserver
		sun=ephem.Sun()
		info = obs.next_pass(self.iss)
		obs.date=info[0]
		sun.compute(obs)
		#Solo considero avistamientos nocturnos o crepusculares y a mas de 20º de altura
		while sun.alt >=0 or ephem.degrees(info[3]) <=ephem.degrees('20:00:00'):
			obs.date=info[4]+ephem.minute
			info = obs.next_pass(self.iss)
			obs.date=info[0]
			sun.compute(obs)		
			#print sun.alt,ephem.degrees(info[3])
			#print "ISS Rise time: %s azimuth: %s setting: %s transit alt: %s" % (info[0], info[1],info[4],info[3])
		self.sobserver.date=olddate
		return info[0]

	def cometOrbit(self,obj,date=ephem.now(),interval=10):
		olddate=self.sobserver.date
		comet=self.i.comet(obj)
		obs=self.sobserver
		obs.date=date
		pos=[]
		for d in range(0,interval):
			obs.date=obs.date+ephem.hour*24
			comet.compute(obs)
			l=list((ephem.localtime(obs.date),comet.ra*180/pi,comet.dec*180/pi))
			pos.append(l)
		self.sobserver.date=olddate
		return pos
		

	def issOrbit(self,date=ephem.now(),interval=10):
		olddate=self.sobserver.date
		iss=self.iss
		obs=self.sobserver
		obs.date=date
		pos=[]
		for d in range(0,interval):
			obs.date=obs.date+ephem.second*20
			iss.compute(obs)
			l=list((ephem.localtime(obs.date),iss.ra*180/pi,iss.dec*180/pi))
			pos.append(l)
		self.sobserver.date=olddate
		return pos

	def iridiumNext(self,date=ephem.now(),interval=100000):
	#No usar sin acabar!
		olddate=self.sobserver.date
		sun=ephem.Sun()
		iri=self.i.allIridium()
		obs=self.sobserver
		obs.date=date
		pos=[]
		for d in range(0,interval):
			obs.date=obs.date+ephem.second*10
			sun.compute(obs)
			for iridium in iri:
				iridium.compute(obs)
				#print iridium.range
				if sun.alt <=0 and iridium.alt <=ephem.degrees('20:00:00') and iridium.range<=500000:
					l=list((iridium.name,ephem.localtime(obs.date),iridium.ra*180/pi,iridium.dec*180/pi,iridium.range))
					print l
					pos.append(l)

		self.sobserver.date=olddate
		return pos

if __name__=='__main__':
	s=SolarSystem(ephem.city('Madrid'))
	print s.bodiesPosition()
	s.iridiumNext()


