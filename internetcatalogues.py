#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS
import ephem,urllib
from pylab import *
import util

#Code to get TLE and Comet (format Xephem) from Minor Planet Center

class internetCatalogue:



	def comet(self,name=''):
		url="http://www.minorplanetcenter.org/iau/Ephemerides/Comets/Soft03Cmt.txt"
		f=urllib.urlopen(url)
		s=f.read().split('\n')
		#Elimino texto sobrante
		s=filter(lambda x:x!='' and x[0]!='#',s)
		#busco una entrada concreta
		CometID=name
		comet=filter(lambda x:x.find(CometID)!=-1, s)
		print comet[0]
		return ephem.readdb(comet[0])

	#TLE from http://celestrak.com/NORAD/elements/
	def readTLE(self,url):
		url=url
		f=urllib.urlopen(url)
		data=f.read().split('\r\n')
		s=util.group(data,3)
		return s

	def TLE(self,url,name):
		data=self.readTLE(url)
		element=filter(lambda x:x[0].find(name)!=-1, data)
		element=element[0]
		print element
		return ephem.readtle(element[0],element[1],element[2])
		

	def ISS(self):	
	#ISS http://celestrak.com/NORAD/elements/stations.txt
		url="http://celestrak.com/NORAD/elements/stations.txt"
		return self.TLE(url,'ISS')



	def iridium(self,n):
		#Iridium http://celestrak.com/NORAD/elements/iridium.txt
		url="http://celestrak.com/NORAD/elements/iridium.txt"
		return self.TLE(url,'IRIDIUM '+ str(n))

#Los 100 mas brillantes
#http://celestrak.com/NORAD/elements/visual.txt


	def allIridium(self):
		url="http://celestrak.com/NORAD/elements/iridium.txt"
		iri=[]
		s=self.readTLE(url)
		for element in s:
			if element[0].split('[')[1][0]=='+':
				iri.append(ephem.readtle(element[0],element[1],element[2]))
		return iri
		
	def allTLE(self,url):
		TLEs=[]
		s=self.readTLE(url)
		for element in s:
				TLEs.append(ephem.readtle(element[0],element[1],element[2]))
		return TLEs

if __name__=='__main__':
	i=internetCatalogue()
	iss=i.ISS()
	iss=i.comet('103P')
	iss.compute()
	print iss.ra,iss.dec
	print map(lambda x:x.name,i.allIridium())



