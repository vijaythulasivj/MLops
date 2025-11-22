import sys
import os
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Add ROOT folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.data.load_data import load_data

DATA_PATH = "data/housing.csv"
MODEL_PATH = "models/model.pkl"

def train():
    X, y = load_data(DATA_PATH)

    model = LinearRegression()
    model.fit(X, y)

    pred = model.predict(X)
    mse = mean_squared_error(y, pred)

    print("Training complete. MSE =", mse)

    os.makedirs("models", exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train()
