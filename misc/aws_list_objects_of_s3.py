# python imports
from dotenv import load_dotenv
import os
import boto3
import traceback

# constants
S3_BUCKET_NAME = "ci-cd-test-project-s3-bucket"

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

    # get list of objects in a s3 bucket
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME)
    for obj in response["Contents"]:
        print(f"    {obj['Key']}")
except Exception as e:
    print(f"Exception: {e}")
    traceback.print_exc()