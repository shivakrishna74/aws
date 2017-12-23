import boto3
import argparse

parser = argparse.ArgumentParser(description='create update stack')
parser.add_argument('--env', type=str, help='Provide the environment')
parser.add_argument('--filename', type=str, help='Provide the filename')
parser.add_argument('--s3path', type=str, help='Provide the s3 file path')

args = parser.parse_args()
path=args.s3path;
stack_name=args.env+'-'+args.filename

client = boto3.client('cloudformation', region_name='us-east-1')

response = client.create_stack(
    StackName=stack_name,
    TemplateURL=args.s3path
    )




# def update_stack(stack_name,path):
#     response_update_stack = client.update_stack(
#         StackName=event['stackname'],
#         TemplateURL=event['url']
#     )

