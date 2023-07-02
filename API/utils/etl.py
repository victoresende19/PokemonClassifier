import pandas as pd 

def etl_process():
    df = pd.read_csv('data\pokemon.csv')
    df = df[df['Type 1'].map(df['Type 1'].value_counts()) < 30]

    natureza = ['Grass', 'Ground', 'Bug', 'Poison', 'Fire', 'Water']
    # elementares = ['Fire', 'Water', 'Ice', 'Electric', 'Steel', 'Rock']
    sombrios = ['Fairy', 'Dark', 'Psychic', 'Ghost']
    outros = ['Normal']

    df.loc[df['Type 1'].isin(natureza), 'Type 1'] = 'Natureza'
    # df.loc[df['Type 1'].isin(elementares), 'Type 1'] = 'Elementar'
    df.loc[df['Type 1'].isin(sombrios), 'Type 1'] = 'Sombras'
    df.loc[df['Type 1'].isin(outros), 'Type 1'] = 'Normal'

    return df
