import boto3

AWS_ACCESS_KEY = "AKIAS2EJK64D2SQHE6HI"
AWS_SECRET_KEY = "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"
REGION = "ap-northeast-2"
BUCKET_NAME = "dongheon97"
BUCKET_URL = "s3://{BUCKET_NAME}/silicon_valley/"


def s3_connection():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=REGION,
    )
    return s3
