import boto3
import argparse

import boto3
import argparse
import time
import logging
import sys

class error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


logging.basicConfig(level=logging.DEBUG)

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
TemplateURL=path
StackName=stack_name



def create_stack(StackName,TemplateURL):
    response = client.create_stack(
        StackName=stack_name,TemplateURL=path
       )

def delete_stack(StackName):
    response = client.delete_stack(
        StackName=stack_name

    )


def check_stack_alive(stack_name):
    print("inside alive block")
    try:
        response = client.describe_stacks(
            StackName=stack_name
            )
        print("inside try block")
        print(stack_name)


    except Exception as e:
        print("inside exception block")

        if "does not exist" in e:
            print("inside does not exist if in exception not main")
            create_stack(StackName,TemplateURL)
        elif "Already exists" in e:
            print("inside  exist if in exception not main")
            delete_stack(StackName)


def main():
    print("inside mainblock")
    try:
        print("inside try main block")
        if stack_operation == "CREATE":
            print("inside try if before create main block")
            create_stack(StackName, TemplateURL)
            print("inside try if after create before check status function in main main block")

            check_stack_alive(StackName)
    except Exception as e:
        if "does not exist" in e:
            print("inside if in main")
            create_stack(StackName,TemplateURL)
        elif "Already exists" in e:
            print("inside elif in main")
            delete_stack(StackName)

if __name__ == "__main__":
    main()






check_stack_status=check_stack_alive('neDev-newThing')