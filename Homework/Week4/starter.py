import pickle
import pandas as pd
import sys

def load_model(model_path:str):
    with open(model_path, 'rb') as f_in:
        dv, model = pickle.load(f_in)
    return dv, model



def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def prepare_data(df:pd.DataFrame, columns:list):
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    return dicts, X_val

def make_predictions(model, X):
    return model.predict(X)


def store_results(output_dir:str, df:pd.DataFrame):
    print("storing results to output path: ", output_dir)
    df_result = pd.DataFrame()

    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    df_result['ride_id'] = df['ride_id']
    df_result['predicted_duration'] = y_pred

    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )

if __name__ == "__main__":
    taxi_type = 'yellow'
    year = int(sys.argv[1])  # 2022
    month = int(sys.argv[2])  # 02

    input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet'
    output_file = f'output/{taxi_type}-{year:04d}-{month:02d}.parquet'
    model_path = 'model.bin'

    categorical = ['PULocationID', 'DOLocationID']

    df = read_data(input_file)
    dv, model = load_model(model_path)

    dicts, X_val = prepare_data(df, categorical)
    y_pred = make_predictions(model, X_val)

    print("predictions std is ", y_pred.std())
    print("prediction mean is ", y_pred.mean())

    store_results(output_file, df)





