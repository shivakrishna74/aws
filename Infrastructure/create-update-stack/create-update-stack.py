import boto3
import argparse
import time

parser = argparse.ArgumentParser(description='create update stack')
parser.add_argument('--env', type=str, help='Provide the environment')
parser.add_argument('--filename', type=str, help='Provide the filename')
parser.add_argument('--s3path', type=str, help='Provide the s3 file path')

StackStatus= 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS'
args = parser.parse_args();
path=args.s3path;
stack_name = args.env + '-' + args.filename;

client = boto3.client('cloudformation', region_name='us-east-1')

TemplateURL=path,
StackName=stack_name

def create_stack(StackName,TemplateURL):
    response = client.create_stack(
    TemplateURL=path,
    StackName=stack_name
    )



def main():
    print("main started")
    create_stack(StackName,TemplateURL);
    check_status(StackName)


main()
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
        TemplateURL=path,
        StackName=stack_name)

    for StackStatus in create_stack(StackName,TemplateURL):
        if [Stacks][StackStatus]!='CREATE COMPLETE':
            print(StackStatus)
            time.sleep(200);
        elif [Stacks][StackStatus]=='CREATE COMPLETE':
            print(StackStatus)












# def update_stack(stack_name,path):
#     response_update_stack = client.update_stack(
#         StackName=event['stackname'],
#         TemplateURL=event['url']
#     )

