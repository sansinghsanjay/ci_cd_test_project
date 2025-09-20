# python imports
import boto3
from dotenv import load_dotenv
import os
import traceback

# load .env and required secrets
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

    # get list of s3 buckets and print their name
    response = s3_client.list_buckets()
    print("Following are the S3 buckets:")
    for bucket in response["Buckets"]:
        print(f"    {bucket['Name']}")
except Exception as e:
    print(f"Exception: {e}")
    traceback.print_exc()