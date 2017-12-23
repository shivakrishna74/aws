import boto3
import argparse
import time
import logging


parser = argparse.ArgumentParser(description='create update stack')
parser.add_argument('--env', type=str, help='Provide the environment')
parser.add_argument('--filename', type=str, help='Provide the filename')
parser.add_argument('--s3path', type=str, help='Provide the s3 file path')
parser.add_argument('--stack_operation', type=str, help='provide the stack operation')

args = parser.parse_args()
path=args.s3path
stack_name = args.env + '-' + args.filename
stack_operation=args.stack_operation

client = boto3.client('cloudformation', region_name='us-east-1')

TemplateURL=path,
StackName=stack_name

def create_stack(StackName,TemplateURL):
    response = client.create_stack(
    TemplateURL=path,
    StackName=stack_name
    )

def delete_stack(StackName):
    response = client.delete_stack(
        StackName=StackName
    )

def check_stack_status(stack_name,stack_chk_value):
    response = client.describe_stacks(
        StackName=stack_name

    )

    chk_status=response['Stacks'][0]['StackStatus']
    i=0
    while i<60:
        try:
            if chk_status == stack_chk_value:
                logging.info("Stack status is {0}".format(stack_chk_value))
        except:
            logging.error("stack status has an error")
            raise
    i+=1
    return chk_status

def main():
    print("main started")
    if stack_operation == 'CREATE':
        response = client.describe_stacks(
            StackName=stack_name

        )

        chk_status = response['Stacks'][0]['StackStatus']
        if chk_status != 'DELETE_COMPLETE':
            delete_stack(StackName)
            check_stack_status(StackName, stack_chk_value='DELETE_COMPLETE')
        create_stack(StackName, TemplateURL)
        check_stack_status(StackName, stack_chk_value='CREATE_COMPLETE')

    elif stack_operation == 'UPDATE':
        stack_chk_value = 'UPDATE_COMPLETE'



if __name__ == "__main__":
    main()

