import boto3
import argparse
import time

parser = argparse.ArgumentParser(description='create update stack')
parser.add_argument('--env', type=str, help='Provide the environment')
parser.add_argument('--filename', type=str, help='Provide the filename')
parser.add_argument('--s3path', type=str, help='Provide the s3 file path')


args = parser.parse_args();
path=args.s3path;
stack_name = args.env + '-' + args.filename;

client = boto3.client('cloudformation', region_name='us-east-1')


main();
def create_stack(stack_name,path):
    response = client.create_stack(
    TemplateUrl=path,
    StackName=stack_name
    )

#
# def delete_stack(stack_name,path):
#     response = client.delete_stack(
#         TemplateUrl=path,
#         StackName=stack_name
#     )
# def update_stack(stack_name,path):
#     response = client.update_stack(
#         TemplateUrl=path,
#         StackName=stack_name
#     )

def check_status(stack_name,path):
    response = client.describe_stacks(
        TemplateUrl=path,
        StackName=stack_name)
    for StackStatus in create_stack():
        if StackStatus!='CREATE_COMPLETE':
            time.sleep(500)


        elif StackStatus=='CREATE_COMPLETE':
            print("Stack Created")





def main():
    print("main started")
    create_stack();








# def update_stack(stack_name,path):
#     response_update_stack = client.update_stack(
#         StackName=event['stackname'],
#         TemplateURL=event['url']
#     )

