## Localstack s3 container creation
```
docker-compose up -d
export S3_ENDPOINT_URL="http://localhost:4566"
aws --endpoint-url="${S3_ENDPOINT_URL}" s3 mb s3://nyc-duration
```

```commandline
export INPUT_FILE_PATTERN="s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"
```