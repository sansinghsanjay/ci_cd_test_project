# python imports
from dotenv import load_dotenv
import os
import boto3
import traceback

# constants
S3_BUCKET_NAME = "ci-cd-test-project-s3-bucket"
OBJECT_NAME = "SpaceExploration.pdf"

# load .env and secrets
load_dotenv()
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

try:
    # get s3 client
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    # delete the file from the S3 bucket
    s3_client.delete_object(Bucket=S3_BUCKET_NAME, Key=OBJECT_NAME)
except Exception as e:
    print(f"Exception: {e}")
    traceback.print_exc()