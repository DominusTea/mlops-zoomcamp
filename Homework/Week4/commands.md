## Jupyter notebook to python script conversion
```commandline
jupyter nbconvert --to python starter.ipynb
```
## Docker image creation
From Dockerfile's directory run:
```commandline
docker build -t taxi-prediction .
```
## Run containerized application
```commandline
docker run -i -t --rm taxi-prediction [year] [month]
```
where year and month are integers corresponding to the selected year and month for which the app will make predictions.