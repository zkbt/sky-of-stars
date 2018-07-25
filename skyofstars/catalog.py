import matplotlib.pyplot as plt
import numpy as np
import astropy.coordinates as coord
import astropy.units as u


class Catalog:
    '''
    This defines a Catalog object, which can be plotted or written
    out into a variety of formats.
    '''

    def __init__(self, coordinates, name="skyofstars", apparentmagnitudes=None):
        '''
        Initialize a Catalog object from some astropy coordinates,
        and a list of magnitudes. This function gets run when
        we create a new Catalog object, by calling

            `example = Catalog(somecoordinates)`

        Parameters
        ----------
        coordinates : astropy.coordinates.SkyCoord array
            An array of coordinates, which can
            contain positions and velocities, with
            which we can initialize this catalog.

        name : str
            A name to store with this catalog,
            (optional -- defaults to "skyofstars")

        apparentmagnitudes : array
            An array of apparent magnitudes,
            of the same length as the coordinates.
            (optional -- defaults to None)
        '''

        # store the array of coordinates inside this catalog object
        self.coordinates = coordinates.transform_to('icrs')

        # every variable we define with a self. in front of it is accessible everywhere else inside the object
        self.ra = self.coordinates.icrs.ra
        self.dec = self.coordinates.icrs.dec

        # let's store the apparent magnitudes, if they are known
        self.apparentmagnitudes = apparentmagnitudes


    def plot_celestial(self, color='black', title='Celestial Coordinates', **kwargs):
        '''
        This function makes a plot of RA + Dec
        (modify it to use the magnitudes to)

        Parameters
        ----------
        (optional)

        color : str
            The color for each point.
        title : str
            A title to put on the plot.
        **kwargs
            This means that any extra keyword arguments will be
            stored as a dictionary called `kwargs`. Those keywords
            can then be passed into other function, like in
            plt.scatter() below.
        '''

        plt.scatter(self.ra, self.dec, c=color, **kwargs)
        plt.xlabel('Right Ascension ($^\circ$)')
        plt.ylabel('Declination ($^\circ$)')
        plt.title("RA vs Dec")

    def plot_galactic(self):
        '''
        Make a plot of longitude and latitude in Galactic coordinates.
        '''

        # you can delete the "pass", and replace it with code!
        plt.scatter(self.l,self.b)
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Galactic Coordinates")

    def plot_galactic_xyz(self):
        '''
        Make some plots of xyz in Galactic.
        '''

        # you can delete the "pass", and replace it with code!
        plt.scatter(self.x,self.y)
        plt.xlabel("X")
        plt.ylabel("Y")
        
        plt.scatter(self.y,self.z)
        plt.xlabel("Y")
        plt.ylabel("Z")
        
        plt.scatter(self.x,self.z)
        plt.xlabel("X")
        plt.ylabel("Y")

    def animate(self):
        '''
        Make an animation of the position of stars through time?
        '''

        # you can delete the "pass", and replace it with code!
        pass
