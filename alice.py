#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS
#ALICE Advance Live Inspector Cosmo Explorer

import sesame
import catalogues
import math
import struct

ngc=catalogues.ngcCatalogue()
stars=catalogues.crossCatalogue()
se=sesame.sesame()


Gsize=18


master_format='24sIIIII'
MM=struct.Struct(master_format)
print MM.format
print MM.size


ngc_format='HHfffH24s4sH'
s=struct.Struct(ngc_format)
print s.format
print s.size

stars_format='IfffH5s3s18s'
SS=struct.Struct(stars_format)
print SS.format
print SS.size

obj_format='HHHHHHH'
obj=struct.Struct(obj_format)
print obj.format
print obj.size

n_ngc=0
n_messier=0
n_stars=0
messier_list=[]

N_TILE=(180/Gsize)*(360/Gsize)
SD=(
('NGC',s.size*n_ngc,s.size,n_ngc,Gsize),
('MESSIER',s.size*n_messier,s.size,n_messier,Gsize),
('NAMED_STARS',SS.size*n_stars,SS.size,n_stars,Gsize),
('OBJECTS_IN_TILE',obj.size*N_TILE,obj.size,N_TILE,Gsize),
('DSS2atlas',32768*N_TILE,32768,N_TILE,Gsize),
('atlas',32768*N_TILE,32768,N_TILE,Gsize)
)

f_MASTER=open('master.ixd','w')
f_NGC=open(SD[0][0]+str(Gsize)+'.ixd','w')
f_MESSIER=open(SD[1][0]+str(Gsize)+'.ixd','w')
f_STARS=open(SD[2][0]+str(Gsize)+'.ixd','w')
f_OBJECTS=open(SD[3][0]+str(Gsize)+'.ixd','w')


for N in range((180/Gsize)*(360/Gsize)):
   raN=N % (360/Gsize)
   decN=(int)(N / (360/Gsize))
   ra=raN * Gsize+Gsize/2
   dec=-90+decN * Gsize+Gsize/2

   ra0=ra-Gsize/2
   dec0=dec-Gsize/2
   ra1=ra+Gsize/2
   dec1=dec+Gsize/2
   #print N,ra0,dec0,ra1,dec1

   n_ngc_in_tile=0
   n_messier_in_tile=0	

   for o in ngc.filter(ra0,dec0,ra1,dec1):
	n_ngc=n_ngc+1
	n_ngc_in_tile=n_ngc_in_tile+1
	Iflag=0
	NG=o[0].replace(' ','').strip()
	if NG.startswith('I'):
		Iflag=1
		NG=NG.replace('I','')
	NG=int(NG)
        DESC=o[6].strip()[0:24]
	if DESC.startswith('M ') :
  	        n_messier=n_messier+1	
		n_messier_in_tile=n_messier_in_tile+1
		Iflag=2
		DESC=DESC.replace(' ','')
		messier_list.append((NG,Iflag,o[2]*math.pi/180.,o[3]*math.pi/180.,o[5],n_ngc,DESC,o[1],N))
#	        print  NG,Iflag,o[2]*math.pi/180.,o[3]*math.pi/180.,n_ngc,DESC,o[1],N
	line= s.pack(NG,Iflag,o[2]*math.pi/180.,o[3]*math.pi/180.,o[5],n_ngc,DESC,o[1],N)
	f_NGC.write(line)
        fname="NGC4_IMAGE_N"+str(n_ngc)
	try:
		pass
        	#se.skyTile(0.1,o[2],o[3],fname)
        	#se.toRGB565(fname)		
	except:
		print "error... "+fname
		pass
   


   n_stars_in_tile=0   
   for o in stars.filter(ra0,dec0,ra1,dec1):
	n_stars=n_stars+1
	n_stars_in_tile=n_stars_in_tile+1
	if len(o[8].strip())>=1:
		F=int(o[8].strip())
	else:
		F=0
        print  int(o[4]),o[5]*math.pi/180.,o[6]*math.pi/180.,o[7],F,o[12].strip(),o[10].strip(),o[11].strip()
	line= SS.pack(int(o[4]),o[5]*math.pi/180.,o[6]*math.pi/180.,o[7],F,o[12].strip(),o[10].strip(),o[11].strip())
  	f_STARS.write(line)

#   print N,n_stars-n_stars_in_tile,n_stars,n_ngc-n_ngc_in_tile,n_ngc,n_messier-n_messier_in_tile,n_messier
   line= obj.pack(N,n_stars-n_stars_in_tile,n_stars,n_ngc-n_ngc_in_tile,n_ngc,n_messier-n_messier_in_tile,n_messier)
   f_OBJECTS.write(line)

print messier_list
messier_list_sorted=sorted(messier_list, key=lambda x: int(x[6][1:]))
for o in messier_list_sorted:
   #line= s.pack(NG,Iflag,o[2]*math.pi/180.,o[3]*math.pi/180.,o[5],n_ngc,DESC,o[1],N)
   print o[0],o[1],o[2],o[3],o[4],o[5],o[6],o[7],o[8]
   line= s.pack(o[0],o[1],o[2],o[3],o[4],o[5],o[6],o[7],o[8])
   f_MESSIER.write(line)



SD=(
('NGC',s.size*n_ngc,s.size,n_ngc,Gsize),
('MESSIER',s.size*n_messier,s.size,n_messier,Gsize),
('NAMED_STARS',SS.size*n_stars,SS.size,n_stars,Gsize),
('OBJECTS_IN_TILE',obj.size*N_TILE,obj.size,N_TILE,Gsize),
('DSS2atlas',32768*N_TILE,32768,N_TILE,Gsize),
('atlas',32768*N_TILE,32768,N_TILE,Gsize)
)

offset=512
for r in SD:
	print r[0]+str(Gsize),offset,r[1],r[2],r[3],r[4]
	line= MM.pack(r[0]+str(Gsize),offset,r[1],r[2],r[3],r[4])
   	f_MASTER.write(line)
	offset=offset+int(int(r[1])/512)*512+1024

f_MASTER.close()
f_STARS.close()
f_MESSIER.close()
f_NGC.close()
f_OBJECTS.close()

