from astropy.utils.data import download_file
from astropy.io import fits
from matplotlib import pyplot as plt
from astropy.coordinates import SkyCoord
from urllib.parse import urlencode
from urllib.request import urlretrieve
from IPython.display import Image
import astropy.units as u

def in_a_galaxy_far_far_away(galaxy_name='NGC234', pixels=1024):
    im_size = 12 * u.arcmin
    im_pixels = pixels
    urlCutOut = 'http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx'
    fuente = SkyCoord.from_name(galaxy_name) #NGC234
    print("Coordinates", fuente)
    query_string = urlencode(dict(ra=fuente.ra.deg,
                                dec=fuente.dec.deg,
                                width=im_pixels, 
                                height=im_pixels,
                                scale=im_size.to(u.arcsec).value/im_pixels))
    url = urlCutOut + '?' + query_string
    print(query_string)
    urlretrieve(url, "assets/"+galaxy_name+".jpg")
    return Image("assets/"+galaxy_name+".jpg")