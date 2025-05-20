# app/utils.py

import pandas as pd
import matplotlib.pyplot as plt

def load_data(path, country_name=None):
    df = pd.read_csv(path)
    if country_name:
        df['Country'] = country_name
    return df

def generate_boxplot(df, column='GHI'):
    fig, ax = plt.subplots()
    df.boxplot(column=column, by='Country', ax=ax)
    plt.title(f'{column} Distribution by Country')
    plt.suptitle('')
    plt.xlabel('Country')
    plt.ylabel(column)
    return fig

def get_top_regions(df, column='GHI', top_n=5):
    if 'Region' in df.columns:
        return df.sort_values(by=column, ascending=False)[['Region', 'Country', column]].head(top_n)
    else:
        return df.sort_values(by=column, ascending=False)[['Country', column]].head(top_n)
