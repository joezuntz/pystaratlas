#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS
import commands,os
import Image
import math
import time

class sesame:
	obj=[]
	obj_data=[]
	def __init__(self):
		pass

	def fromFile(self,FICHERO):
		fi=open(FICHERO)
		for l in fi.readlines():
			r=[]
			for f in l.split():
				r.append(f)
			self.obj.append(r)
		fi.close()
		self.cds_sesame()

	def cds_sesame(self):
		for o in self.obj:
			print o[0]
			res=commands.getoutput('sesame -ol '+o[0])
			res=res.split('\n')
			for r in res:
				rr=r.split()
				try:
					if rr[0]=='%J':					
						self.obj_data.append([o[0],float(rr[1]),float(rr[2])])
				except:
					pass

	def tileN(self,Gsize,N):
		#raN*(360/Gsize)+decN
		raN=N % (360/Gsize)
		decN=(int)(N / (360/Gsize))
		ra=raN * Gsize+Gsize/2
		dec=-90+decN * Gsize+Gsize/2
		print N,raN,decN,ra,dec
		self.skyTile(Gsize,ra,dec,str(N))
		self.toRGB565(str(N))

	def allSky(self,Gsize):
		N=(360/Gsize)*(180/Gsize)
		for i in range(0,N):
			self.tileN(Gsize,i)

	def skyTile(self,Gsize,RA,DEC,prename):
		import urllib
		image = urllib.URLopener()

		x_n=1
		y_n=1
		angle=Gsize
		angle_ra=angle/math.cos(DEC*(math.pi/180))
		print angle,angle_ra
		for i in range(x_n):
			for j in range(y_n):
				ra=(RA+(-i+x_n/2.-0.5)*angle_ra)/15
				de=DEC+(-j+y_n/2.-0.5)*angle
				url="http://www.sky-map.org/imgcut?survey=DSS2&angle="+str(angle)+"&ra="+str(ra)+"&de="+str(de)
				print url
				try:
					urllib.urlretrieve(url,prename+"_"+str(i)+"_"+str(j)+".jpg")
				except:
					print "Problemas con el servidor ..."
					time.sleep(4)
					self.skyTile(Gsize,RA,DEC,prename)
					return

	#crea y ensambla todos los tiles de una bbox
		size=(256*x_n,256*y_n)
		Im=Image.new("RGB",size,"#FFFFFF")

		for i in range(x_n):
			x0=256*(i)
			x1=256*(1+i)
			for j in range(y_n):
				y0=256*(j)
				y1=256*(j+1)
				Fname=prename+"_"+str(i)+"_"+str(j)+".jpg"
				ima=Image.open(Fname)
				os.remove(Fname)
				Im.paste(ima,(x0,y0,x1,y1)) 
		Im.save(prename+".png","PNG")

	def skyMapImage(self,obj):
		self.skyTile(4,obj[1],obj[2],obj[0])


	def toRGB565(self,prename):
		try:
			os.remove(prename+".rgb565")
		except:
			pass

		res=commands.getoutput("convert "+prename+".png"+" -resize 128x128 "+prename+"_128x128.jpg")
		print res

		res=commands.getoutput("ffmpeg -vcodec mjpeg -i "+prename+"_128x128.jpg -f rawvideo -vcodec rawvideo -pix_fmt rgb565 -s 128x128  "+prename+".rgb565")

		print res
		try:
			os.remove(prename+"_128x128.jpg")
		except:
			pass


if __name__=='__main__':
	se=sesame()
	"""
	s=18	
	se.allSky(s)
	N=(360/s)*(180/s)
	for i in range(0,N):
		res=commands.getoutput("cat "+str(i)+".rgb565>>image"+str(s)+".rgb565.raw")
		print res
#	se.skyTile(4,289.147917,30.184500,prename=str(289.147917)+"_"+str(30.184500))

"""
	se.fromFile("obj_salida_grupoIO_23_7_2011.txt")
	for o in se.obj_data:
		se.skyMapImage(o)





