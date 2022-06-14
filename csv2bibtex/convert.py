import pandas as pd
import numpy as np

# bibtex structure

bib_file = ''
bibtex = {
    'type1': '@book',
    'type2': '@article',
    'citation_key': '',
    'author': 'author = ',
    'title': 'title = ',
    'year': 'year = ',
    'publisher': 'publisher = '
}

# load CSV
data = pd.read_csv("csv2bibtex/data/urbana.csv")
data_clean = data[['autor', 'titulo', 'anio', 'editorial_institución', 'tipo_doc']]

# dataframe manipulation to string

for i in range(data_clean.shape[0]):
    if data_clean.iat(i, 4) in ['libro', 'informe'] :
        bib_file += str(bibtex['type1']) + '{' + data_clean.iat[i, 0][0: 4] + str(data_clean.iat[i, 2]) + ',\n'
    else:
        bib_file += str(bibtex['type1']) + '{' + data_clean.iat[i, 0][0: 4] + str(data_clean.iat[i, 2]) + ',\n'
    bib_file += '  ' + str(bibtex['author']) + '"'+  str(data_clean.iat[i, 0]) + '"' + ',\n'
    bib_file += '  ' + str(bibtex['title']) + '"' + str(data_clean.iat[i, 1]) + '"' + ',\n'
    bib_file += '  ' + str(bibtex['year']) + str(data_clean.iat[i, 2])
    bib_file += '  ' + str(bibtex['publisher']) + str(data_clean.iat[i, 3])
    bib_file += '\n}\n'


# save to bibtex
file = open('csv2bibtex/output/convert.bib', 'w')
file.write(bib_file)
file.close()