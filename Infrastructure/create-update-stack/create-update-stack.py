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

def create_stack(StackName,TemplateUrl):
    response = client.create_stack(
    TemplateUrl=path,
    StackName=stack_name
    )


def delete_stack(StackName,TemplateUrl):
    response = client.delete_stack(
        TemplateUrl=path,
        StackName=stack_name
    )
def update_stack(StackName,TemplateUrl):
    response = client.update_stack(
        TemplateUrl=path,
        StackName=stack_name
    )

def check_status(StackName,TemplateUrl):
    response = client.describe_stacks(
        TemplateUrl=path,
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
    delete_stack("luftwaffe");
    print("stack deleted")







# def update_stack(stack_name,path):
#     response_update_stack = client.update_stack(
#         StackName=event['stackname'],
#         TemplateURL=event['url']
#     )

