import json
import os
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all  # Patch all supported libraries for X-Ray - More info: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-patching.html
patch_all()


def lambda_handler(event, context):
    # print(event)
    runtime_region = os.environ['AWS_REGION']
    # print(runtime_region)
    github_token = os.environ['GITHUB_TOKEN']
    # print(github_token)
    ecr_repository = os.environ['ECR_REPOSITORY']
    # print(ecr_repository)
    
    # print(event['detail']['image-digest'])
    
    new_version_image_tag = get_image_tag_with_hash(event['detail']['image-digest'], ecr_repository)
    print(new_version_image_tag)

    return event

def get_image_tag_with_hash(image_digest, ecr_repository_name):
    client_ecr = boto3.client('ecr')
    response_images = client_ecr.batch_get_image(
        repositoryName= ecr_repository_name,
        imageIds=[
            {
                'imageDigest': image_digest
            },
        ]
    )
    for image in response_images['images']:
        print(image)
        # if image['imageId']['imageTag'] != 'main-latest' and image['imageId']['imageTag'] != 'latest':
            # new_version_image_tag = image['imageId']['imageTag']
    
    return "test"



# response = client.batch_get_image(
#     registryId='string',
#     repositoryName='string',
#     imageIds=[
#         {
#             'imageDigest': 'string',
#             'imageTag': 'string'
#         },
#     ],
#     acceptedMediaTypes=[
#         'string',
#     ]
# )



