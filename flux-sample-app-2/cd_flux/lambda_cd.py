import json
import os
# import .dependency.boto3
from dependency.aws_xray_sdk.core import xray_recorder
from dependency.aws_xray_sdk.core import patch_all  # Patch all supported libraries for X-Ray - More info: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-patching.html
patch_all()


def lambda_handler(event, context):
    print(event)

    return event