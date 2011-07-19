#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
import pyfits
from pylab import *

class ngcCatalogue():
#Aladin Catalogue:
#catcat -fits  VII/118/ >ngc2000.fits
	"""
Byte-by-byte Description of file: ngc2000.dat

   Bytes Format  Units   Label    Explanations

   1-  5  A5     ---     Name     NGC or IC designation (preceded by I)
   7-  9  A3     ---     Type     Object classification (1)
  11- 12  I2     h       RAh      Right Ascension 2000 (hours)
  14- 17  F4.1   min     RAm      Right Ascension 2000 (minutes)
      20  A1     ---     DE-      Declination 2000 (sign)
  21- 22  I2     deg     DEd      Declination 2000 (degrees)
  24- 25  I2     arcmin  DEm      Declination 2000 (minutes)
      27  A1     ---     Source   Source of entry (2)
  30- 32  A3     ---     Const    Constellation
      33  A1     ---     l_size   [<] Limit on Size
  34- 38  F5.1   arcmin  size     ? Largest dimension
  41- 44  F4.1   mag     mag      ? Integrated magnitude, visual or photographic
                                      (see n_mag)
      45  A1     ---     n_mag    [p] 'p' if mag is photographic (blue)
  47- 96  A50    ---     Desc     Description of the object (3)

Note (1): the field is coded as follows:
     Gx  = Galaxy
     OC  = Open star cluster
     Gb  = Globular star cluster, usually in the Milky Way Galaxy
     Nb  = Bright emission or reflection nebula
     Pl  = Planetary nebula
     C+N = Cluster associated with nebulosity
     Ast = Asterism or group of a few stars
     Kt  = Knot  or  nebulous  region  in  an  external galaxy
     *** = Triple star
     D*  = Double star
     *   = Single star
     ?   = Uncertain type or may not exist
         = (blank) Unidentified at the place given, or type unknown
     -   = Object called nonexistent in the RNGC (Sulentic and Tifft 1973)
     PD  = Photographic plate defect
Note (2): sources that have been used to correct or update
    modern data in NGC 2000.0 (type, positions, magnitude, and size).
    Uppercase letters denote special NGC and IC errata lists, which have
    usually been accorded more weight than the source catalogues
    themselves. In parentheses after each citation is the number of times
    it has been used to update NGC entries (first number) and those in
    the IC (second number).
    A = Archinal, Brent A. Version 4.0 of an unpublished list of errata to
        the RNGC, dated March 19, 1987. (110,0)
    a = Arp, H., "Atlas of Peculiar Galaxies", 1966ApJS...14....1A (1,2)
        (Catalog VII/74)
    c = Corwin, Harold G., Jr., A. de Vaucouleurs, and G. de Vaucouleurs,
        "Southern Galaxy Catalogue", Austin, Texas: University of Texas
        Monographs in Astronomy No. 4, 1985. (152,564)
        (Catalog VII/116)
    d = Dreyer, J.L.E., New General Catalogue of Nebulae and Clusters of
        Stars (1888), Index Catalogue (1895), Second Index Catalogue (1908).
        London: Royal Astronomical Society, 1953. (28,2157)
    D = Dreyer, J.L.E., ibid. Errata on pages 237, 281-283, and 366-378.
        (158,28)
    F = Skiff, Brian, private communication of February 27, 1988.  (93,36)
    h = Holmberg, E., "A Study of Double and Multiple Galaxies",
        Lund Annals, 6, 1937. (13,2)
    k = Karachentsev, I.D., "A Catalogue of Isolated Pairs of Galaxies
        in the Northern Hemisphere"; also, Karachentseva, V.E.,
        "A Catalog of Isolated Galaxies." Astrofiz. Issled. Izv. Spetz.
        Astrofiz., 7, 3, 1972, and 8, 3, 1973. (0,4)
        (Catalogs VII/77, VII/82, VII/83)
    m = Vorontsov-Velyaminov, B.A., and V.P. Arhipova,
        "Morphological Catalog of Galaxies", Parts I-V.
        Moscow: Moscow State University, 1962-74. (9,679)
        (Catalogs VII/62 and VII/100)
    n = Reinmuth, K., "Photographische Positionsbestimmung von NebelRecken"
        Veroff der Sternwarte zu Heidelberg, several papers, 1916-40. (0,4)
    o = Alter, G., B. Balazs, and J. Ruprecht, Catalogue of Star Clusters
        and Associations, 2nd edition.  Budapest: Akademiai Kiado, 1970. (5,0)
        (Catalogs VII/5, VII/44 and VII/101)
    r = Sulentic, Jack W., and William G. Tifft, "The Revised New General
        Catalogue of Nonstellar Astronomical Objects (RNGC)".
        Tucson, Arizona:University of Arizona Press, 1973. (4016,0)
        (Catalog VII/1)
    s = Hirshfeld, Alan, and Roger W. Sinnott, eds., Sky Catalogue 2000.0,
        Vol.2, Cambridge, Massachusetts:
        Sky Publishing Corp. and Cambridge University Press, 1985. (3098,238)
    t = Tully, R.B., "Nearby Galaxies Catalog". New York: Cambridge
        University Press, 1988.
        A preliminary version on magnetic tape (1981) was used here. (23,17)
        (Catalog VII/145)
    u = Nilson P.N., Uppsala Ceneral Catalogue of Galaxies.
        Uppsala: Uppsala Astronomical Observatory, 1973. (15,543)
        (Catalog VII/26)
    v = de Vaucouleurs, G., A. de Vaucouleurs, and H.C. Corvin, Jr.,
        Second Reference Catalogue of Bright Galaxies. Austin, Texas,
        University of Texas Press, 1976.(118,206)
        (Catalog VII/112)
    x = Dixon, R.S., and George Sonneborn, "A Master List of Nonstellar
        Optical Astronomical Objects (MOL)".  Columbus, Ohio,
        Ohio State University Press, 1980.
        It should be noted that most of the information for codes
        a,h,k,m,n,o,u and z was extracted from the magnetic-tape
        version of this catalogue.
        The x code refers to IC objects identified in a literature
        search by these authors. (0,526)
    z = Zwicky, F., E. Herzog, and P. Wild, "Catalogue of Galaxies and
        Clusters of Galaxies", Vol.I. Pasadena, Calif., California Institute
        of Technology, 1961. Also, successive volumes through 1968. (1,380)
        (Catalog VII/49)
Note (3): description of the object, as given by Dreyer or
     corrected by him, in a coded or abbreviated form. The abbreviations
     and their combination are fully described in the introduction
     to the published catalog.
     ab       = about
     alm      = almost
     am       = among
     annul    = annular or ring nebula
     att      = attached
     b        = brighter
     bet      = between
     biN      = binuclear
     bn       = brightest to n side
     bs       = brightest to s side
     bp       = brightest to p side
     bf       = brightest to f side
     B        = bright
     c        = considerably
     chev     = chevelure
     co       = coarse, coarsely
     com      = cometic (cometary form)
     comp     = companion
     conn     = connected
     cont     = in contact
     C        = compressed
     Cl       = cluster
     d        = diameter
     def      = defined
     dif      = diffused
     diffic   = difficult
     dist     = distance, or distant
     D        = double
     e        = extremely, excessively
     ee       = most extremely
     er       = easily resolvable
     exc      = excentric
     E        = extended
     f        = following (eastward)
     F        = faint
     g        = gradually
     glob.    = globular
     gr       = group
     i        = irregular
     iF       = irregular figure
     inv      = involved, involving
     l        = little (adv.); long (adj.)
     L        = large
     m        = much
     m        = magnitude
     M        = middle, or in the middle
     n        = north
     neb      = nebula
     nebs     = nebulous
     neby     = nebulosity
     nf       = north following
     np       = north preceding
     ns       = north-south
     nr       = near
     N        = nucleus, or to a nucleus
     p        = preceding (westward)
     pf       = preceding-following
     p        = pretty (adv., before F. B. L, S)
     pg       = pretty gradually
     pm       = pretty much
     ps       = pretty suddenly
     plan     = planetary nebula (same as PN)
     prob     = probably
     P        = poor (sparse) in stars
     PN       = planetary nebula
     r        = resolvable (mottled, not resolved)
     rr       = partially resolved, some stars seen
     rrr      = well resolved, clearly consisting of stars
     R        = round
     RR       = exactly round
     Ri       = rich in stars
     s        = suddenly (abruptly)
     s        = south
     sf       = south following
     sp       = south preceding
     sc       = scattered
     sev      = several
     st       = stars (pl.)
     st 9...  = stars of 9th magnitude and fainter
     st 9..13 = stars of mag. 9 to 13
     stell    = stellar, pointlike
     susp     = suspected
     S        = small in angular size
     S*       = small (faint) star
     trap     = trapezium
     triangle = triangle, forms a triangle with
     triN     = trinuclear
     v        = very
     vv       = very
     var      = variable
     *        = a single star
     *10      = a star of 10th magnitude
     *7-8     = star of mag. 7 or 8
     **       = double star (same as D*)
     ***      = triple star
     !        = remarkable
     !!       = very much so
     !!!      = a magnificent or otherwise interesting object


Byte-by-byte Description of file: names.dat

   Bytes Format Units   Label     Explanations

   1- 35  A35   ---     Object    Common name (including Messier numbers)
  37- 41  A5    ---     Name     *NGC or IC name, as in ngc2000.dat
  43- 70  A28   ---     Comment   Text of comment, if any
"""
	ngc=[]
	def __init__(self):
		hdulist = pyfits.open("./data/ngc2000.fits")
		desc=hdulist[2].data
		IDs=map(lambda x:x[1],desc)
		for r in hdulist[1].data:
			
			ra=(r[2]+r[3]/60.)*15
			if r[4]=='+':
				signo=1
			else:
				signo=-1
			dec=signo*(float(r[5])+float(r[6])/60.)
			record=[]
			record.append(r[0])
			record.append(r[1])
			record.append(ra)
			record.append(dec)
			record.append(r[10])
			record.append(r[11])
			#Common names
			try:
				d=desc[IDs.index(r[0])]
				record.append(d[0])
				record.append(d[2])
			except:
				record.append('')
				record.append('')

			self.ngc.append(record)

	def filter(self,ra0,dec0,ra1,dec1,mag=20):
		s=filter(lambda x:(x[2]>ra0 and x[2]<ra1) and  (x[3]>dec0 and x[3]<dec1 and len(x[6])>0),self.ngc)
                #s=filter(lambda x:(x[2]>ra0 and x[2]<=ra1) and  (x[3]>dec0 and x[3]<=dec1 ),self.ngc)
		return s


class crossCatalogue():
#Aladin Catalogue:
#catcat -fits  IV/27 / >cross_index.fits
	"""
   Bytes Format Units   Label   Explanations

   1-  6  I6    ---     HD      [1/257937] Henry Draper Catalog Number III/135
   8- 19  A12   ---     DM      Durchmusterung Identification from HD Catalog
                                 III/135 (1)
  21- 25  I5    ---     GC      ? [1/33342] Boss General Catalog (GC, I/113)
                                   number if one exists, othewise blank
  27- 30  I4    ---     HR      ? [1/9110] Harvard Revised Number=Bright Star
                                   Number V/50 if one exists, othewise blank
  32- 37  I6    ---     HIP     ? [1/118218] Hipparcos Catalog I/196 number
                                   if one exists, othewise blank
  39- 40  I2    h       RAh     Right Ascension 2000 (hours) (2)
  41- 42  I2    min     RAm     Right Ascension 2000 (minutes) (2)
  43- 47  F5.2  s       RAs     Right Ascension 2000 (seconds) (2)
      49  A1    ---     DE-     Declination 2000 (sign)
  50- 51  I2    deg     DEd     Declination 2000 (degrees) (2)
  52- 53  I2    arcmin  DEm     Declination 2000 (minutes) (2)
  54- 57  F4.1  arcsec  DEs     Declination 2000 (seconds) (2)
  59- 63  F5.2  mag     Vmag    ? [-1.44/13.4] Visual magnitude (2)
  65- 77  A13   ---     BFD     Bayer-Flamsteed designation of star with
                                 its extension  (3)

Note (1): Durchmusterung Identification from HD Catalog III/135
    consists of DM Catalog designation:
      BD north of -23 degrees,
      CD from -23 to -52 degrees,
      CP south of -52 degrees
    Sign of DM zone, DM zone, DM number and component identification if
    there are two or more HD stars with the same DM number (for multiple
    systems included in the Washington Catalog of Visual Double Stars the
    same designation are given).
Note (2): Right ascensions, declinations and visual magnitudes for all
    stars were taken from the Hipparcos catalog and from the CSI for the
    stars that has no number in catalog Hipparcos.
Note (3): Bayer-Flamsteed designation of star with its extension consists
    in a Flamsteed number if one exists, otherwise blank, a Bayer
    designation of star with greek letter or latin letter according to
    various authors, superscript number for letter designation if one
    exists, othewise blank, constellation abbreviation.

    Abbreviations for the greek letters (the same as in catalog Hipparcos):
    alpha = alf   beta= bet   gamma= gam   delta= del   epsilon= eps
    dzeta = zet   eta = eta   theta= the   iota = iot   kappa  = kap
    lambda= lam   mu  = mu.   nu   = nu.   xi   = ksi   omicron= omi
    pi    = pi.   rho = rho   sigma= sig   tau  = tau   upsilon= ups
    phi   = phi   chi = chi   psi  = psi   omega= ome


Byte-by-byte Description of file: table3.dat

   Bytes Format Units   Label   Explanations

   1-  6  I6    ---     HD      [1/257937] Henry Draper Catalog number
   8- 20  A13   ---     BFD     Bayer-Flamsteed designation of star in catalog
  22- 76  A55   ---     Name    Proper name for the star
  78-100  A23   ---     r_Name  References detailed in 'refs.dat'

"""
	stars=[]
	HD_IDs=[]
	HIP_IDs=[]
	alphabet={'alf  ':'α','alf01':'α¹','alf02':'α²',\
	  'bet  ':'β','bet01':'β¹','bet02':'β²','bet03':'β³',\
	  'gam  ':'γ','gam01':'γ¹','gam02':'γ²','gam03':'γ³',\
	  'del  ':'δ','del01':'δ¹','del02':'δ²','del03':'δ³',\
	  'eps  ':'ε','eps01':'ε¹','eps02':'ε²','eps03':'ε³',\
	  'zet  ':'ζ','zet01':'ζ¹','zet02':'ζ²','zet03':'ζ³',\
	  'eta  ':'η','eta01':'η¹','eta02':'η²','eta03':'η³',\
          'the  ':'θ','the01':'θ¹','the02':'θ²','the03':'θ³',\
	  'iot  ':'ι','iot01':'ι¹','iot02':'ι²',\
	  'kap  ':'κ','kap01':'κ¹','kap02':'κ²',\
	  'lam  ':'λ','lam01':'λ¹','lam02':'λ²','lam03':'λ³',\
	  'mu.  ':'μ','mu.01':'μ¹','mu.02':'μ²','mu.03':'μ³',\
          'nu.  ':'ν','nu.01':'ν¹','nu.02':'ν²','nu.03':'ν³',\
	  'ksi  ':'ξ','ksi01':'ξ¹','ksi02':'ξ²','ksi03':'ξ³',\
          'omi  ':'ο','omi01':'ο¹','omi02':'ο²','omi03':'ο³',\
	  'pi.  ':'π','pi.01':'π¹','pi.02':'π²','pi.03':'π³','pi.04':'π⁴','pi.05':'π⁵','pi.06':'π⁶',\
	  'rho  ':'ρ','rho01':'ρ¹','rho02':'ρ²','rho03':'ρ³',\
	  'sig  ':'σ','sig01':'σ¹','sig02':'σ²','sig03':'σ³',\
	  'tau  ':'τ','tau01':'τ¹','tau02':'τ²','tau03':'τ³','tau04':'τ⁴','tau05':'τ⁵','tau06':'τ⁶','tau07':'τ⁷','tau08':'τ⁸','tau09':'τ⁹',\
	  'ups  ':'υ','ups01':'υ¹','ups02':'υ²','ups03':'υ³',\
	  'phi  ':'φ','phi01':'φ¹','phi02':'φ²','phi03':'φ³','phi04':'φ⁴',\
	  'chi  ':'χ','chi01':'χ¹','chi02':'χ²','chi03':'χ³',\
	  'psi  ':'ψ','psi01':'ψ¹','psi02':'ψ²','psi03':'ψ³','psi04':'ψ⁴','psi05':'ψ⁵','psi06':'ψ⁶','psi07':'ψ⁷','psi08':'ψ⁸','psi09':'ψ⁹',\
	  'ome  ':'ω','ome01':'ω¹','ome02':'ω²','ome03':'ω³'}
	def __init__(self):
		hdulist = pyfits.open("./data/cross_index.fits")
		names=hdulist[4].data
		stars=hdulist[1].data
		self.HD_IDs=map(lambda x:x[0],names)
		self.HIP_IDs=map(lambda x:x[4],stars)

		for r in hdulist[1].data:
			ra=(r['RAh']+r['RAm']/60.+r['RAs']/3600.)*15
			if r['DE-']=='+':
				signo=1
			else:
				signo=-1
			dec=signo*(r['DEd']+r['DEm']/60.+r['DEs']/3600.)
			record=[]
			record.extend((r['HD'],r['DM'],r['GC'],r['HR'],r['HIP']))
			record.append(ra)
			record.append(dec)
			record.append(r['Vmag'])
			record.append(r['BFD'][0:3])
			try:
				record.append(self.alphabet[r['BFD'][4:9]])
				#print r['BFD'][4:9],self.alphabet[r['BFD'][4:9]]
			except:
				record.append('')
			record.append(r['BFD'][10:12])
			#Common names
			try:
				d=names[self.HD_IDs.index(r[0])]
				#record.append(d['BFD'].split())
				record.append(d['Name'].split(';')[0].split('(')[0])			
			except:
				#record.append('')
				record.append('')
			try:
				record.append(r['BFD'][4:9])
			except:
				record.append('')

			#print record
			self.stars.append(record)

	def search(self,HIP):
		try:
			star=self.stars[self.HIP_IDs.index(HIP)]
		except:
			star=[]
		return 	star

	def filter(self,ra0,dec0,ra1,dec1,mag=20):
                s=filter(lambda x:(x[5]>ra0 and x[5]<=ra1) and  (x[6]>dec0 and x[6]<=dec1 ),self.stars)
		return s





def CostellationBounds():
#Data from stellarium 0.8 sources
		fi=open('./data/costellations_bound_20.dat')
		p=[]
		for l in fi.readlines():
			r=[]
			for f in l.split():
				try:
					r.append(float(f))
				except:
					r.append(f)
			pp=(r[0]*15,r[1],r[2])
			p.append(pp)
		fi.close()		
		return p

def CostellationFigures():
#Data from stellarium 0.8 sources
		fi=open('./data/constellationship.fab')
		p=[]
		for l in fi.readlines():
			r=[]
			for f in l.split():
				try:
					r.append(int(f))
				except:
				 	r.append(f)	
			p.append(r)
		fi.close()	
		return p



class HiparcosCatalogue:
#PENDIENTE PASARLO FITS
#catcat -fits I/311 >HIP.fits
	"""
HIP Sn So Nc RArad DErad Plx pmRA pmDE e_RArad e_DErad e_Plx e_pmRA e_pmDE Ntr F2 F1 var ic Hpmag e_Hpmag sHp VA B_V e_B_V V_I UW1 UW2 UW3 UW4 UW5 UW6 UW7 UW8 UW9 UW10 UW12 UW13 UW14 UW15

   1-  6  I6    ---      HIP     Hipparcos identifier
   8- 10  I3    ---      Sn      [0,159] Solution type new reduction (1)
      12  I1    ---      So      [0,5] Solution type old reduction (2)
      14  I1    ---      Nc      Number of components
  16- 28 F13.10 rad      RArad   Right Ascension in ICRS, Ep=1991.25
  30- 42 F13.10 rad      DErad   Declination in ICRS, Ep=1991.25
  44- 50  F7.2  mas      Plx     Parallax
  52- 59  F8.2  mas/yr   pmRA    Proper motion in Right Ascension
  61- 68  F8.2  mas/yr   pmDE    Proper motion in Declination
  70- 75  F6.2  mas    e_RArad   Formal error on DErad
  77- 82  F6.2  mas    e_DErad   Formal error on DErad
  84- 89  F6.2  mas    e_Plx     Formal error on Plx
  91- 96  F6.2  mas/yr e_pmRA    Formal error on pmRA
  98-103  F6.2  mas/yr e_pmDE    Formal error on pmDE
 105-107  I3    ---      Ntr     Number of field transits used
 109-113  F5.2  ---      F2      Goodness of fit
 115-116  I2    %        F1      Percentage rejected data
 118-123  F6.1  ---      var     Cosmic dispersion added (stochastic solution)
 125-128  I4    ---      ic      Entry in one of the suppl.catalogues
 130-136  F7.4  mag      Hpmag   Hipparcos magnitude
 138-143  F6.4  mag    e_Hpmag   Error on mean Hpmag
 145-149  F5.3  mag      sHp     Scatter of Hpmag
     151  I1    ---      VA      [0,2] Reference to variability annex
 153-158  F6.3  mag      B-V     Colour index
 160-164  F5.3  mag    e_B-V     Formal error on colour index
 166-171  F6.3  mag      V-I     V-I colour index
 172-276 15F7.2 ---      UW      Upper-triangular weight matrix (G1)


I/311               Hipparcos, the New Reduction       (van Leeuwen, 2007)
================================================================================
Hipparcos, the new Reduction of the Raw data
     van Leeuwen F.
    <Astron. Astrophys. 474, 653 (2007)>
    =2007A&A...474..653V
================================================================================
ADC_Keywords: Positional data ; Proper motions ; Parallaxes, trigonometric ;
              Photometry ; Fundamental catalog
Mission_Name: Hipparcos
Keywords: space vehicles: instruments - methods: data analysis  - catalogs -
         astrometry  - instrumentation: miscellaneous

Abstract:
    A new reduction of the astrometric data as produced by the Hipparcos
    mission has been published, claiming accuracies for nearly all stars
    brighter than magnitude Hp=8 to be better, by up to a factor 4, than
    in the original catalogue.

    The new Hipparcos astrometric catalogue is checked for the quality of
    the data and the consistency of the formal errors as well as the
    possible presence of error correlations. The differences with the
    earlier publication are explained.

    Methods. The internal errors are followed through the reduction
    process, and the external errors are investigated on the basis of a
    comparison with radio observations of a small selection of stars, and
    the distribution of negative parallaxes. Error correlation levels are
    investigated and the reduction by more than a factor 10 as obtained in
    the new catalogue is explained.

    Results. The formal errors on the parallaxes for the new catalogue are
    confirmed. The presence of a small amount of additional noise, though
    unlikely, cannot be ruled out.

    Conclusions. The new reduction of the Hipparcos astrometric data
    provides an improvement by a factor 2.2 in the total weight compared
    to the catalogue published in 1997, and provides much improved data
    for a wide range of studies on stellar luminosities and local galactic
    kinematics.

Notice:
    The files included are slightly different from the ones published in
    the book, as an error that sometimes affected the goodness of fit
    value for the solution was corrected. The first version of these files
    (between June and 15 September 2008) also contained errors corrected
    after this date.

File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records    Explanations
--------------------------------------------------------------------------------
ReadMe         80        .    This file
hip2.dat      276   117955    The Astrometric Catalogue
hip7p.dat     129     1338    Seven-parameter solutions
hip9p.dat     274      104    Nine-parameter solutions
hipvim.dat    129       25   *Variability-induced (VIM) solutions
--------------------------------------------------------------------------------
Note on hipvim.dat: solution for double stars having one variable component.
--------------------------------------------------------------------------------

See also:
    I/239 : The Hipparcos and Tycho Catalogues (ESA 1997)

Byte-by-byte Description of file: hip2.dat
--------------------------------------------------------------------------------
   Bytes Format Units    Label   Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---      HIP     Hipparcos identifier
   8- 10  I3    ---      Sn      [0,159] Solution type new reduction (1)
      12  I1    ---      So      [0,5] Solution type old reduction (2)
      14  I1    ---      Nc      Number of components
  16- 28 F13.10 rad      RArad   Right Ascension in ICRS, Ep=1991.25
  30- 42 F13.10 rad      DErad   Declination in ICRS, Ep=1991.25
  44- 50  F7.2  mas      Plx     Parallax
  52- 59  F8.2  mas/yr   pmRA    Proper motion in Right Ascension
  61- 68  F8.2  mas/yr   pmDE    Proper motion in Declination
  70- 75  F6.2  mas    e_RArad   Formal error on DErad
  77- 82  F6.2  mas    e_DErad   Formal error on DErad
  84- 89  F6.2  mas    e_Plx     Formal error on Plx
  91- 96  F6.2  mas/yr e_pmRA    Formal error on pmRA
  98-103  F6.2  mas/yr e_pmDE    Formal error on pmDE
 105-107  I3    ---      Ntr     Number of field transits used
 109-113  F5.2  ---      F2      Goodness of fit
 115-116  I2    %        F1      Percentage rejected data
 118-123  F6.1  ---      var     Cosmic dispersion added (stochastic solution)
 125-128  I4    ---      ic      Entry in one of the suppl.catalogues
 130-136  F7.4  mag      Hpmag   Hipparcos magnitude
 138-143  F6.4  mag    e_Hpmag   Error on mean Hpmag
 145-149  F5.3  mag      sHp     Scatter of Hpmag
     151  I1    ---      VA      [0,2] Reference to variability annex
 153-158  F6.3  mag      B-V     Colour index
 160-164  F5.3  mag    e_B-V     Formal error on colour index
 166-171  F6.3  mag      V-I     V-I colour index
 172-276 15F7.2 ---      UW      Upper-triangular weight matrix (G1)
--------------------------------------------------------------------------------
Note (1): Solution type.
    The solution type is a number 10xd+s consisting of two parts d and s:
    - s describes the type of solution adopted:
      1 = stochastic solution (dispersion is given in the 'var' column)
      3 = VIM solution (additional parameters in file hipvim.dat)
      5 = 5-parameter solution (this file)
      7 = 7-parameter solution (additional parameters in hip7p.dat)
      9 = 9-parameter solution (additional parameters in hip9p.dat)
    - d describes peculiarities, as a combination of values:
      0 = single star
      1 = double star
      2 = variable in the system with amplitude > 0.2mag
      4 = astrometry refers to the photocenter
      8 = measurements concern the secondary (fainter) in the double system

Note (2): as follows:
      0 = standard 5-parameter solution
      1 = 7- or 9-parameter solution
      2 = stochastic solution
      3 = double and multiple stars
      4 = orbital binary as resolved in the published catalog
      5 = VIM (variability-induced mover) solution
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hip7p.dat
--------------------------------------------------------------------------------
   Bytes Format Units     Label  Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---       HIP    Hipparcos identifier
   8- 12  F5.2  ---       Fg     Detection statistic
  14- 19  F6.2  mas/yr2   dpmRA  Acceleration in Right Ascension
  21- 26  F6.2  mas/yr2   dpmDE  Acceleration in Declination
  28- 32  F5.2  mas/yr2 e_dpmRA  Formal error on dpmRA
  34- 38  F5.2  mas/yr2 e_dpmDE  Formal error on dpmDE
  39-129 13F7.2 ---       UW     Upper-triangular weight matrix U16..U28 (G1)
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hip9p.dat
--------------------------------------------------------------------------------
   Bytes Format Units     Label   Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---       HIP     Hipparcos identifier
   8- 12  F5.2  ---       Fg      Detection statistic
  14- 19  F6.2  mas/yr2   dpmRA   Acceleration in Right Ascension
  21- 26  F6.2  mas/yr2   dpmDE   Acceleration in Declination
  28- 33  F6.2  mas/yr3   ddpmRA  Acceleration change in Right Ascension
  35- 40  F6.2  mas/yr3   ddpmDE  Acceleration change in Declination
  42- 46  F5.2  mas/yr2 e_dpmRA   Formal error on dpmRA
  48- 52  F5.2  mas/yr2 e_dpmDE   Formal error on dpmDE
  54- 58  F5.2  mas/yr3 e_ddpmRA  Formal error on ddpmRA
  60- 64  F5.2  mas/yr3 e_ddpmDE  Formal error on ddpmDE
  65-274 30F7.2 ---       UW      Upper-triangular weight matrix U16..U45 (G1)
--------------------------------------------------------------------------------

Byte-by-byte Description of file: hipvim.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6    ---     HIP       Hipparcos identifier
   8- 12  F5.2  ---     Fg        Detection statistic
  14- 19  F6.2  mas     upsRA     VIM in Right Ascension (1)
  21- 26  F6.2  mas     upsDE     VIM in Declination (1)
  28- 32  F5.2  mas   e_upsRA     Formal error on upsRA
  34- 38  F5.2  mas   e_upsDE     Formal error on upsDE
  39-129 13F7.2 ---     UW        Upper-triangular weight matrix U16..U28 (G1)
--------------------------------------------------------------------------------
Note (1): the variability-induced movement is due to the variability
     of one component of the binary which changes the position of the
     photocenter along the RA (or Dec) axis with the quantity
         ups*(1 - dexp(-0.4(m_r_-m)))
     where m_r_ is the reference magnitude of the binary and m
     the observed magnitude of the binary, and dexp the decimal
     exponentiation (dexp(x) = 10^x^)
--------------------------------------------------------------------------------

Global Notes:
Note (G1): The upper-triangular weight matrix U is related to the
     covariance matrix C by
         C^-1^ = ~U U    (~U represents transposed U)
     The elements U_i_ forming the upper triangular matrix are stored as
         +-                         -+
         |  (1)  (2)  (4)  (7)  (11) |
         |   0   (3)  (5)  (8)  (12) |
         |   0    0   (6)  (9)  (13) |
         |   0    0    0  (10)  (14) |
         |   0    0    0    0   (15) |
         +-                         -+
     on the astrometric parameters RA, Dec, plx, pmRA, pmDE,
     and derivatives of proper motions for 7- and 9-parameter
     solutions.

Acknowledgements:
    Floor van Leeuwen, Institute of Astronomy, Cambridge University
    Cambrisge, UK

References:
    Floor van Leeuwen, 2007 "Hipparcos, the New Reduction of the Raw Data"
    Astrophysics & Space Science Library #350.

History:
  * 09-Jun-2008: Original version (with errors)
  * 16-Sep-2008: new files from author
================================================================================
(End)                                   Francois Ochsenbein [CDS]    16-Sep-2008 
"""


	""" fields=("HIP","Sn","So","Nc","RArad","DErad","Plx","pmRA","pmDE","e_RArad",\
		"e_DErad","e_Plx","e_pmRA","e_pmDE","Ntr","F2","F1","var","ic","Hpmag","e_Hpmag",\
		"sHp","VA","B_V","e_B_V","V_I","UW1","UW2","UW3","UW4","UW5","UW6","UW7",\
		"UW8","UW9","UW10","UW12","UW13","UW14","UW15")
	"""

	stars=[]
	IDs=set()
	def __init__(self):
		self.readfile("./data/hip2.dat")
		#self.IDs=set(map(lambda x:x[0],self.stars))
		self.IDs=map(lambda x:x[0],self.stars)

	def readfile(self,fich):
		fi=open(fich)
		for l in fi.readlines():
			r=[]
			for f in l.split():
				try:
					r.append(float(f))
				except:
					r.append(f)
			self.stars.append(r)
		self.fields=self.stars[0]
		self.stars.remove(self.fields)
		fi.close()

	def search(self,ID):
		try:
			s=self.stars[self.IDs.index(ID)]
		except:
			s=None
		return s

	def filter(self,ra0,dec0,ra1,dec1,mag=20,plx=0):
		s=filter(lambda x:(x[4]*180/pi>ra0 and x[4]*180/pi<ra1) and  (x[5]*180/pi>dec0 and x[5]*180/pi<dec1) and x[19] < mag and x[6]>plx,self.stars)
		return s



class TychoCatalogue:
#ftp://cdsarc.u-strasbg.fr/pub/cats/I/259/
#	int 	TYC1 	#TYC1 or GSC
#	int 	TYC2 	#TYC2 or GSC
#	int 	TYC3 	#TYC3 from TYC
#	str 	pflag 	#[PX] mean position flag
#	float 	mRAdeg 	#alpha mean position, ICRS at epoch J2000 (deg)
#	float 	mDEdeg 	#delta mean position, ICRS at epoch J2000 (deg)
#	float 	pmRA   	#mu-alpha ICRS at epoch J2000 (mas/yr)
#	float 	pmDE   	#mu-delta ICRS at epoch J2000 (mas/yr)
#	float 	e_mRA  	#sigma-alpha (model-based) at mean epoch (mass)
#	float 	e_mDE  	#sigma-alpha (model-based) at mean epoch (mass)
#	float 	e_pmRA 	#sigma-alpha (model-based)  (mass/yr)
#	float 	e_pmDE 	#sigma-alpha (model-based)  (mass/yr)
#	float 	mepRA  	#mean epoch of alpha (yr)
#	float 	mepDE  	#mean epoch of alpha (yr)
#	int   	Num	#Number of positions used
#	float 	g_mRA	#goodness of fit for mean alpha
#	float 	g_mDE	#goodness of fit for mean alpha
#	float 	g_pmRA	#goodness of fit for mean mu-alpha
#	float 	g_pmDE	#goodness of fit for mean mu-alpha
#	float 	BT	#Tycho-2 Bt magnitude (mag)
#	float 	e_BT	#sigmaTycho-2 Bt magnitude (mag)
#	float 	VT	#Tycho-2 Vt magnitude (mag)
#	float 	e_VT	#sigmaTycho-2 Vt magnitude (mag)
#	int	proc	#proximity indicator
#	str	TYC	#Tycho-1 star flag
#	int	HIP	#Hipparcos number
#	str	CCDM	#CCDM Componet identifier for HIP stars
#	float	RAdeg	#alpha observed Tycho-2 position,ICRS (deg)
#	float	DEdeg	#delta observed Tycho-2 position,ICRS (deg)
#	float	epRA	#epoch-1990 of RAdeg (a)
#	float	epDE	#epoch-1990 of DEdeg (a)
#	float 	e_RA	#sigma alpha (model based) observed position (mas)
#	float 	e_DE	#sigma alpha (model based) observed position (mas)
#	str	posflg	#[DP] type of tycho-2 solution
#	float	corr	#correlation ro(delta-alpha)observed  position


	


	fields=("TYC1","TYC2","TYC3","pflag","mRAdeg","mDEdeg","pmRA","pmDE","e_mRA","e_mDE", \
		"e_pmRA","e_pmDE","mepRA","mepDE","Num","g_mRA","g_mDE","g_pmRA","g_pmDE", \
		"BT","e_BT","VT","e_VT","proc","TYC","HIP","CCDM","RAdeg","DEdeg","epRA","epDE","e_RA","e_DE","posflg","corr")
	stars=[]
	def readfile(self,fich):
		fi=open(fich)
		for l in fi.readlines():
			r=[]
			for f in l.split('|'):
				try:
					r.append(float(f))
				except:
					r.append(f)
			self.stars.append(r)
		fi.close()


		

if __name__=='__main__':
#	C=TychoCatalogue()
#	C.readfile("./tycho/tyc2.dat.00")
#	C=HiparcosCatalogue()
#	print C.filter(0,0,45,45,plx=200)

#	CostellationFigures()
#	print C.stars[0][0],C.stars[0][1],C.stars[0][2],C.stars[0][3]
#	ngc=ngcCatalogue()
#	for t in ngc.ngc_names:
#	print t
#	ngc=ngcCatalogue()
#	print ngc.ngc
	bsc=crossCatalogue()
	for l in set(map(lambda x:x[-3],bsc.stars)):
		print l,
