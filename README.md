# skyofstars
Sky of Stars is a project to convert Gaia astrometric and photometric data into formats that can be visualized in planeteria, particularly the Fiske Planetarium on the CU Boulder campus.

It is still a *work in progress*.

## Usage

*Let's include some basic examples (snippets of code) showing how people can use the code here. For example, this might show how someone can create a catalog from a downloaded Gaia DR2 data table, and output it in a particular planetarium format.*

## Installation
If you want to install the existing code, but not modify it at all, you should be able to install simply by running `pip install git+https://github.com/zkbt/sky-of-stars.git` from a command prompt.

If you want to be able to modify the code yourself, please also feel free to fork/clone this repository onto your own computer and install directly from that editable package. For example, this might look like:
```
git clone https://github.com/zkbt/sky-of-stars.git
cd craftroom/
pip install -e .
```
This will link the installed version of the `skyofstars` package to your local repository. Changes you make to the code in the repository should be reflected in the version Python sees when it tries to `import skyofstars`.

## Contributors

This package was written mostly by [Luci Ibarra Perez](https://github.com/luib0557), with contributions from [Zach Berta-Thompson](https://github.com/zkbt).
