from pathlib import Path
import pandas as pd

def load_data(filepath: Path = None) -> pd.DataFrame:
    if filepath is None:
        base_path = Path(__file__).resolve().parent.parent 
        filepath = base_path / 'data' / 'amazon_uk_data.csv'
    return pd.read_csv(filepath)
 
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
 df = df.drop_duplicates()
 df = df.dropna(subset=['title', 'price', 'stars', 'categoryName'])
 df['price'] = df['price'].replace('[£,]', '', regex=True).astype(float)
 df['stars'] = df['stars'].astype(float)
 df['reviews'] = pd.to_numeric(df['reviews']).fillna(0).astype(int)
 df['boughtInLastMonth'] = pd.to_numeric(df['boughtInLastMonth']).fillna(0).astype(int)
 df['isBestSeller'] = df['isBestSeller'].astype(bool)
 return df