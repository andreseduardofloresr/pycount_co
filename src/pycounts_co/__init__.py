# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_co")

# populatepackagenamespace
from pycounts_co.pycounts_co import count_words
from pycounts_co.plotting import plot_words