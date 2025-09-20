# python imports
from dotenv import load_dotenv
import os
import boto3
import traceback

# paths
PDF_FILE_PATH = "C:/Users/Public/Documents/GitHub/ci_cd_test_project/data/SpaceExploration.pdf"

# constants
S3_BUCKET_NAME = "ci-cd-test-project-s3-bucket"
DESTINATION_FOLDER_NAME = "ci_cd_test_project_data"
DESTINATION_OBJECT_NAME = os.path.basename(PDF_FILE_PATH)

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

    # upload the file to the S3 bucket
    s3_client.upload_file(PDF_FILE_PATH, S3_BUCKET_NAME, DESTINATION_FOLDER_NAME + "/" + DESTINATION_OBJECT_NAME)
    
except Exception as e:
    print(f"Exception: {e}")
    traceback.print_exc()