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
