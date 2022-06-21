import pandas as pd

# bibtex structure

bib_file = ''
bibtex = {
    'book': {
        'type': '@book',
        'title': 'title =',
        'author': 'author = ',
        'year': 'year = ',
        'place': 'address = ',
        'publisher': 'publisher = ',
        'url': 'url ='
    },
    'article': {
        'type': '@article',
        'title': 'title =',
        'author': 'author = ',
        'year': 'year = ',
        'journal': 'journal =',
        'number': 'number = ',
        'url': 'url ='
    }
}

# load CSV
data = pd.read_csv("csv2bibtex/data/urbana.csv")
data_clean = data[['autor', 'titulo', 'anio', 'editorial_institucion', 'tipo_doc']]

# dataframe manipulation to string

for i in range(data_clean.shape[0]):
    if data_clean.iat[i, 4] in ['libro', 'informe', 'cartilla']:
        bib_file += str(bibtex['type1']) 
    else:
        bib_file += str(bibtex['type2']) 
    bib_file += '{' + data_clean.iat[i, 0].split()[0] + str(data_clean.iat[i, 2]) + ',\n'
    bib_file += '  ' + str(bibtex['author']) + '"'+  str(data_clean.iat[i, 0]) + '"' + ',\n'
    bib_file += '  ' + str(bibtex['title']) + '"' + str(data_clean.iat[i, 1]) + '"' + ',\n'
    bib_file += '  ' + str(bibtex['year']) + str(data_clean.iat[i, 2]) + ',\n'
    bib_file += '  ' + str(bibtex['publisher']) + '"' + str(data_clean.iat[i, 3]) + '"'
    bib_file += '\n}\n'


# save to bibtex
file = open('csv2bibtex/output/convert.bib', 'w')
file.write(bib_file)
file.close()