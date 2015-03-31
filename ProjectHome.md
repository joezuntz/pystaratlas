# PYSTARATLAS #
_README.txt file_

PYSTARATLAS is a collection of libraries and command line programs aim to
draw different start maps and sky images in styles.

## Dependences ##

It is written in python with the following dependences:

  * pyproj4. A powerful python library implementing the projections algorithms of the Proj4 project.
  * pylab to manage arrays.
  * pyfits for reading FITs astronomical format.
  * ephemerides for solar system ephemerides calculation.
  * reportlab to draw pdf files.
  * Image (PIL image library) to manipulate images.
  * Several common used libraries (math,system,datetime ...).

## Data Sources ##

Also it use a lot of sources of astronomical data, mainly:

Catalogues form CDS(Centre de Strasbourg):
  * Hipparcos.
  * NGC2000.
  * BSC (Bright Stars Catalogue).
  * Cross catalogue for Stars names.

Several files from Stellarium project:
  * Constellations bounds.
  * Constellation figures.

Up to date online data:
  * TLE elements from Minor Planet Institute. Comments, Asteroids and spacecraft.
  * DSS2 Imagen form www.sky-map.com

# Main Components #
## Libraries ##
  * catalogues.py -> Reads datafiles.
  * internetcatalogues.py -> Recover TLE data from internet.
  * sesame.py -> Find objects coords and download DSS2 image from sky-maps.org. Need sesame package in order to work

## Command line executables ##
  * proy.py ->Draw map showing a whole sky projection.
  * imagebook.py -> Draw astronomical objects from a list
