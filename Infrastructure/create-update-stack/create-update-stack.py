import boto3
import argparse
import time
import logging
import sys
import botocore
from botocore.exceptions import ValidationError
from botocore.exceptions import ClientError


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
TemplateURL=path
StackName=stack_name
chk_stack=" ";

#describing stack
def describe_stack(StackName):
    print("inside descrive stack")
    response = client.describe_stacks(
        StackName=stack_name
    )
    chk_stack= response['Stacks'][0]['StackName'];
    if stack_chk_value==chk_status:
        logging.info("stack status is {0}")

#delete stack
def delete_stack(StackName):
    print("inside delete")
    response = client.delete_stack(
        StackName=stack_name
    )

#creating stack
def create_stack(StackName,TemplateURL):
        try:
            print("inside try")
            if chk_stack in describe_stack(StackName):
                print("inside if")
                delete_stack(StackName)
                create_stack(StackName, TemplateURL)
                print("inside creeate stack ")



        except (ValidationError,ClientError) as err:
            print("inside except block")
            print(err);
            if err.response['Error']['Code'] == 'does not exist':
                create_stack(StackName, TemplateURL)
            # if 'does not exist'.format(stack_name) in error_msg:




def main():
        print("inside main")
        create_stack(StackName,TemplateURL)



if __name__ == "__main__":
    main()





