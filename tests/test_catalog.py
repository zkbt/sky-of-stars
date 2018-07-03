from skyofstars.catalog import *

def create_test_catalog(N=10000):
    '''
    This function creates an example catalog to play with. It's not
    realistic astrophysically, but it's fun to play with!
    '''

    x = np.random.uniform(-1, 1, N)*u.pc
    y = np.random.uniform(-1, 1, N)*u.pc
    z = np.random.uniform(-1, 1, N)*u.pc
    r, lat, lon = coord.cartesian_to_spherical(x,y,z)
    somecoordinates = coord.SkyCoord(l=lon, b=lat, distance=r, frame='galactic')
    example = Catalog(somecoordinates)

    return example

def test_catalog():
    example = create_test_catalog()
    example.plot_celestial()
