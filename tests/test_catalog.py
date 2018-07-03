from skyofstars.catalog import *

def create_test_catalog(N=100):
    '''
    This function creates an example catalog to play with. It's not
    realistic astrophysically, but it's fun to play with!
    '''

    N = 100
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    z = np.random.uniform(-1, 1, N)
    c = coord.SkyCoord(x=x*u.pc, y=y*u.pc, z=z*u.pc, representation='cartesian')
    example = Catalog(c)
    return example

def test_catalog():
    example = create_test_catalog()
    example.plot_radec()
