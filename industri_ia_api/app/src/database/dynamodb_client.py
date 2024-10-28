import boto3
import os

instance = boto3.resource(
    'dynamodb',
    endpoint_url=os.getenv('AWS_DB_URL'),
)