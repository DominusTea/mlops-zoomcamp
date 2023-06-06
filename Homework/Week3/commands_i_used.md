I run the following commands from the repository's base directory.  

## starting the server
```
prefect server start
```

## Initializing a prefect project
```
prefect project init  
```

## Creating work pool  
Through the Prefect UI. Else:
```
prefect work-pool create --type process taxi-pool
```

## Deployment creation
```
prefect deploy --cron "0 9 3 * *" ./Homework/Week3/orchestrate.py:main_flow -n taxi-deployment-Ja
n-Feb  -p taxi-pool
```

## Worker start
```
prefect worker start -p taxi-pool
```

## Deployment creation with param override (Q4)
```
prefect deploy --param train_path="./Homework/Week3/data/green_tripdata_2023-02.parquet" --param val_path="./Homework/Week3/data/green_tripdata_2023-03.parquet"  --cron "0 9 4 * *"  ./Homework/Week3/orchestrate.py:main_flow -n taxi-deployment-Feb-Mar  -p taxi-pool
```

## Login to prefect cloud
```
prefect cloud login
```

## Run experiment using prefect cloud
```
prefect worker start -p taxi-pool
```
and on a seperate terminal:  
```
python Homework/Week3/orchestrate.py
```

## Logout from prefect cloud
```
prefect cloud logout
```
