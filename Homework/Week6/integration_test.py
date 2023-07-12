import pandas as pd
import numpy as np
from datetime import datetime
import os
from batch import get_input_path, get_output_path
def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)

def dataframe():

    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2), dt(1, 10)),
        (1, 2, dt(2, 2), dt(2, 3)),
        (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
    ]
    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    return pd.DataFrame(data, columns=columns)


S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')
options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL
    }
}

df = dataframe()

input_file = get_input_path(2022, 1)
output_file = get_output_path(2022, 1)

print("output file is ", output_file)
df.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)

os.system('python batch.py 2022 1')

df_real = pd.read_parquet(output_file, storage_options=options)
predictions_sum = df_real['predicted_duration'].sum()
print(predictions_sum)
np.testing.assert_almost_equal(predictions_sum, 31.51, decimal=2)