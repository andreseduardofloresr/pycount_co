from pycounts_co.pycounts_co import count_words
from pycounts_co.plotting import plot_words
counts = count_words("zen.txt")
fig = plot_words(counts, 10)
