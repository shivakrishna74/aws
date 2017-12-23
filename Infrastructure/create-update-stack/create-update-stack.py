import boto3
import argparse
import time

parser = argparse.ArgumentParser(description='create update stack')
parser.add_argument('--env', type=str, help='Provide the environment')
parser.add_argument('--filename', type=str, help='Provide the filename')
parser.add_argument('--s3path', type=str, help='Provide the s3 file path')


args = parser.parse_args()
path = args.s3path;
stack_name = args.env + '-' + args.filename;
TemplateURL=args.s3path;
client = boto3.client('cloudformation', region_name='us-east-1')

def create_stack(stack_name,TemplateURL):
    response = client.create_stack(
        StackName=stack_name,
        TemplateURL=args.s3path

    )


def delete_stack(stack_name):
    response = client.delete_stack(
        StackName=stack_name

    )
def update_stack(stack_name,TemplateURL):
    response = client.update_stack(
        StackName=stack_name,
        TemplateURL=args.s3path
    )

def check_status(stack_name,TemplateURL):
    response = client.describe_stacks(
        StackName=stack_name)
    for StackStatus in stack_name:
        if StackStatus!='CREATE_COMPLETE':
            time.sleep(500)


        elif StackStatus=='CREATE_COMPLETE':
            print("Stack Created")





def main():
    print("main stearted")
    create_stack();
    print("stack created")
    update_stack();
    print("stack updated")
    check_status();
    print("check status")
    delete_stack();
    print("stack deleted")







# def update_stack(stack_name,path):
#     response_update_stack = client.update_stack(
#         StackName=event['stackname'],
#         TemplateURL=event['url']
#     )

