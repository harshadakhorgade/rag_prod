import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def get_s3_client():
    bucket = os.getenv("S3_BUCKET_NAME")
    if not bucket:
        raise RuntimeError("S3_BUCKET_NAME is not set")

    s3 = boto3.client("s3")
    return s3, bucket


def upload_pdf(file_bytes: bytes, filename: str):
    s3, bucket = get_s3_client()
    key = f"pdfs/{filename}"

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=file_bytes,
        ContentType="application/pdf"
    )

    return f"s3://{bucket}/{key}"
