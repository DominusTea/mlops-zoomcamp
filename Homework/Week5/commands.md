## Environment Setup
```
conda create -n "mlops_zoomcamp_week5" python=3.11
```  
```
pip3 install -r requirements.txt
```
```commandline
conda activate mlops_zoomcamp_week5
```
## Monitoring Container run
From the Week5 directory, run:
```commandline
docker-compose up --build
```
## Populate dashboards
```commandline
python3 evidently_metrics_calculation.py
```
