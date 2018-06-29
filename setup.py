# The template for this setup.py came from Tim Morton,
#  who I understand took it from Dan F-M. Thanks guys!

# import our ingredients
from setuptools import setup, find_packages
import os,sys

# return the README as a string
def readme():
    with open('README.md') as f:
        return f.read()

# a little kludge to be able to get the version number from the package
import sys
if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins
builtins.__SKYOFSTARS__ = True
import thefriendlystars
version = skyofstars.__version__

setup(name = "skyofstars",
    version = version,
    description = "Python toolkit creating star catalogs to visualize in planetaria, particularly the Fiske Planetarium at CU Boulder.",
    long_description = readme(),
    author = "Luci Ibarra Perez",
    author_email = "luib0557@colorado.edu",
    url = "https://github.com/zkbt/sky-of-stars",
    packages = find_packages(),
    package_data = {'skyofstars':[]},
    include_package_data=False,
    scripts = [],
    classifiers=[
      'Intended Audience :: Science/Research',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Astronomy'
      ],
    install_requires=['numpy', 'astropy', 'scipy', 'matplotlib'],
    zip_safe=False,
    license='MIT',
)
