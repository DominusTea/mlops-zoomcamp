import pandas as pd

import pandas as pd
import pytest
from datetime import datetime
from batch import prepare_data
def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)




@pytest.fixture(name='categorical')
def categorical_creator():
    return  ['PULocationID', 'DOLocationID']

@pytest.fixture(name='columns')
def columns_creator():
    return  ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']


@pytest.fixture(name='df')
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
    print(data)
    return pd.DataFrame(data, columns=columns)


def test_prepare_data(df, categorical, columns):
    df_prepared = prepare_data(df, categorical)
    assert len(df_prepared) == 3
    df_true_result = pd.DataFrame([
        ['-1', '-1', dt(1,2,0), dt(1,10,0), 8.0],
        ['1', '-1', dt(1,2,0), dt(1,10), 8.0],
        ['1', '2', dt(2,2,0), dt(2,3,0), 1.0]
    ],
    columns=columns+['duration']
    )
    # from IPython import embed; embed()

    assert df_prepared.to_dict() == df_true_result.to_dict()
