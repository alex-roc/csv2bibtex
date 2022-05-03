import pandas as pd

# bibtex structure

bibtex = {
    'type': '@article',
    'citation_key': '',
    'author': 'author = ',
    'title': 'title = ',
    'year': 'year = '
}

# load CSV
data = pd.read_csv("csv2bibtex/data/urbana.csv")

# dataframe manipulation

# transform to strings with format

# save to bibtex