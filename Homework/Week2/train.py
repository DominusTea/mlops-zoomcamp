import os
import pickle
import click

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

import mlflow



def setup_mlflow():
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("Week-2")

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)

def run_train(data_path: str, max_depth:int, random_state:int):

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    rf = RandomForestRegressor(max_depth=max_depth, random_state=random_state)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_val)

    rmse = mean_squared_error(y_val, y_pred, squared=False)
    return rmse

@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)

@click.option(
    "--max_depth",
    default=10,
    help="Random Forest's maximum depth."
)
@click.option(
    "--random_state",
    default=10,
    help="Random Forest's random state."
)

def main(data_path: str, max_depth:int, random_state:int):
    setup_mlflow()
    mlflow.autolog()
    with mlflow.start_run():
        run_train(data_path, max_depth, random_state)



if __name__ == '__main__':
    main()
