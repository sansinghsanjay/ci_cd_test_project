# python imports
import boto3
import traceback

# utils imports
from utils.logger import log_status
from utils.readable_timestamp import get_readable_timestamp

# constants
S3_BUCKET_NAME = "ci-cd-test-project-s3-bucket"

# list objects of a S3 bucket
def list_s3_bucket_objects():
    try:
        # get s3 client
        s3_client = boto3.client("s3")
        # get list of objects in a s3 bucket
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME)
        object_names = ""
        for obj in response["Contents"]:
            object_names = object_names + obj["Key"] + ", "
        object_names = object_names.strip()
        return object_names
    except Exception as e:
        log_status(status="ERROR", source="/utils/list_s3_bucket_objects.py::list_s3_bucket_objects()", timestamp=get_readable_timestamp(), msg=f"Exception: {e}; traceback: {traceback.print_exc()}\n")
