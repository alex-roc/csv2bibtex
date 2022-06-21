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
columns = ['tipo_doc', 'titulo', 'autor', 'anio', 'departamento','editorial_institucion', 'nombre_revista_compilacion', 'numero_revista', 'url', 'temas']
data = pd.read_csv("csv2bibtex/data/urbana.csv")
data_clean = data[columns]

# dataframe manipulation to string

for i in range(data_clean.shape[0]):
    if data_clean.iat[i, 0] in ['libro', 'informe', 'cartilla']:
        bib_file += str(bibtex['book']['type'])
    else:
        bib_file += str(bibtex['article']['type'])
    bib_file += f"""{{{data_clean.iat[i, 2].split()[0].lower()}{data_clean.iat[i, 3]},
    title = "{data_clean.iat[i, 1]}",
    author = "{data_clean.iat[i, 2]}",
    year = {data_clean.iat[i, 3]},
    """
    if data_clean.iat[i, 0] in ['libro', 'informe', 'cartilla']:
        bib_file += f"""place = "{data_clean.iat[i, 4]}",
    publisher = "{data_clean.iat[i, 5]}",
    """
    else:
        bib_file += f"""journal = "{data_clean.iat[i, 6]}",
    number = {data_clean.iat[i, 7]},
    """
    bib_file += f"""url = "{data_clean.iat[i, 8]}",
    keywords = "{data_clean.iat[i, 9]}"
}}
"""


# save to bibtex
file = open('csv2bibtex/output/convert.bib', 'w')
file.write(bib_file)
file.close()