import boto3
import argparse
import time

parser = argparse.ArgumentParser(description='create update stack')
parser.add_argument('--env', type=str, help='Provide the environment')
parser.add_argument('--filename', type=str, help='Provide the filename')
parser.add_argument('--s3path', type=str, help='Provide the s3 file path')
StackStatus= 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS',


args = parser.parse_args()
path = args.s3path;
stack_name = args.env + '-' + args.filename

client = boto3.client('cloudformation', region_name='us-east-1')

def create_stack():
    response = client.create_stack(
        StackName=stack_name,
        TemplateURL=args.s3path
    )


def delete_stack():
    response = client.delete_stack(
        StackName=stack_name

    )
def update_stack():
    response = client.update_stack(
        StackName=stack_name,
        TemplateURL=args.s3path
    )

def check_status():
    response = client.describe_stacks(
        StackName=stack_name)
    for StackStatus in stack_name:
        if StackStatus!='CREATE_COMPLETE':
            time.sleep(500)


        elif StackStatus=='CREATE_COMPLETE':
            print("Stack Created")





def main():
    create_stack();
    update_stack();
    check_status();
    delete_stack();







# def update_stack(stack_name,path):
#     response_update_stack = client.update_stack(
#         StackName=event['stackname'],
#         TemplateURL=event['url']
#     )

