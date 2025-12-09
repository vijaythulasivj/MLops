import pandas as pd
import os

def load_data(path: str, output_path="data/processed/clean_data.csv"):
    df = pd.read_csv(path)
    
    # Example preprocessing (modify based on your actual needs)
    X = df.drop("price", axis=1)
    y = df["price"]
    clean_df = pd.concat([X, y], axis=1)

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save output
    clean_df.to_csv(output_path, index=False)

    return X, y


if __name__ == "__main__":
    load_data("data/housing.csv")
