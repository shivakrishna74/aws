import boto3
import argparse
import time
import logging
import sys
from pathlib import Path

# class for handling errors
class error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
logging.basicConfig(level=logging.DEBUG)

#Statements for asking input at runtime
parser = argparse.ArgumentParser(description='create update stack')
parser.add_argument('--env', type=str, help='Provide the environment')
parser.add_argument('--filename', type=str, help='Provide the filename')
parser.add_argument('--s3path', type=str, help='Provide the s3 file path')
parser.add_argument('--stack_operation', type=str, help='provide the stack operation')
args = parser.parse_args()
#Template Url insisde S3 bucket
path=args.s3path
#StackName
stack_name = args.env + '-' + args.filename
#StackOperation
stack_operation=args.stack_operation
client = boto3.client('cloudformation', region_name='us-east-1')
#Waiter used for making it wait
waiter = client.get_waiter('stack_exists')
templateurl=path
stackname=stack_name

#describing stack
def describe_stack(stackname,stack_chk_value):
    response = client.describe_stacks(
        stackname
    )
    chk_status= response['Stacks'][0]['StackStatus'];
    if stack_chk_value==chk_status:
        logging.info("stack status is {0}".format(stack_chk_value))

#delete stack
def delete_stack(stackname):
    response = client.delete_stack(
        stackname
    )

#creating stack
def create_stack(stackname,templateurl):
    try:
        response = client.create_stack(stackname,templateurl);
    except Exception as e:
        if stackname.exists():
            delete_stack(stackname)
            create_stack(stackname,templateurl);
            print("execution Inside if block "),


def main():
    print("inside main")
    create_stack(stackname,templateurl);



if __name__ == "__main__":
    main()





