import pandas as pd

def load_data(path: str):
    df = pd.read_csv(path)
    X = df.drop("price", axis=1)
    y = df["price"]
    return X, y
