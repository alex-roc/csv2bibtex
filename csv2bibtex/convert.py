import pandas as pd
import numpy as np

# bibtex structure

bib_file = ''
bibtex = {
    'type': '@article',
    'citation_key': '',
    'author': 'author = ',
    'title': 'title = ',
    'year': 'year = '
}

# load CSV
data = pd.read_csv("csv2bibtex/data/urbana.csv")
data_clean = data[['autor', 'titulo', 'anio']]

# dataframe manipulation to string

for i in range(data_clean.shape[0]):
    bib_file += str(bibtex['type']) + '{' + data_clean.iat[i, 0][0: 4] + str(data_clean.iat[i, 2]) + ',\n'
    bib_file += '  ' + str(bibtex['author']) + '"'+  str(data_clean.iat[i, 0]) + '"' + ',\n'
    bib_file += '  ' + str(bibtex['title']) + '"' + str(data_clean.iat[i, 1]) + '"' + ',\n'
    bib_file += '  ' + str(bibtex['year']) + str(data_clean.iat[i, 2])
    bib_file += '\n}\n'


# save to bibtex
file = open('csv2bibtex/output/convert.bib', 'w')
file.write(bib_file)
file.close()