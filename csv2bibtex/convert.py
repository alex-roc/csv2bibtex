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
    if data_clean.at[i, 'tipo_doc'] in ['libro', 'informe', 'cartilla']:
        bib_file += str(bibtex['book']['type'])
    else:
        bib_file += str(bibtex['article']['type'])
    bib_file += f"""{{{data_clean.at[i, 'autor'].split()[0].lower()}{data_clean.at[i, 'anio']},
    title = "{data_clean.at[i, 'titulo']}",
    author = "{data_clean.at[i, 'autor']}",
    year = {data_clean.at[i, 'anio']},
    """
    if data_clean.at[i, 'tipo_doc'] in ['libro', 'informe', 'cartilla']:
        bib_file += f"""place = "{data_clean.at[i, 'departamento']}",
    publisher = "{data_clean.at[i, 'editorial_institucion']}",
    """
    else:
        bib_file += f"""journal = "{data_clean.at[i, 'nombre_revista_compilacion']}",
    number = {data_clean.at[i, 'numero_revista']},
    """
    bib_file += f"""url = "{data_clean.at[i, 'url']}",
    keywords = "{data_clean.at[i, 'temas']}"
}}
"""


# save to bibtex
file = open('csv2bibtex/output/convert.bib', 'w')
file.write(bib_file)
file.close()