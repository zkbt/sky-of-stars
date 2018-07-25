from .catalog import *

def create_test_catalog(N=10000):
    
    
    '''
    This function creates an example catalog to play with. It's not
    realistic astrophysically, but it's fun to play with!
    '''

    x = np.random.uniform(-1, 1, N)*u.pc
    y = np.random.uniform(-1, 1, N)*u.pc
    z = np.random.uniform(-1, 1, N)*u.pc
    
    #also create random dx, dy, dz? pmra, pmdec, random radial velocity? 
    pml = np.random.uniform ( -100,100,N) *u.mas/u.yr
    pmb = np.random.uniform ( -100,100,N) *u.mas/u.yr
    radial = np.random.uniform ( -100,100,N) *u.km/u.s
    
  
    
    
    r, lat, lon = coord.cartesian_to_spherical(x,y,z)
    
    
    somecoordinates = coord.SkyCoord(l=lon, b=lat, distance=r,pm_l_cosb = pml,pm_b=pmb,radial_velocity=radial, frame='galactic') #add pm_l_cosb = pmra, pm_b = pmdec, radial_velocity= radial? 
    example = Catalog(somecoordinates)

    return example