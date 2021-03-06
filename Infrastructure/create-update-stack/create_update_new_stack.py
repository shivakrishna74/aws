import boto3
import argparse
import time
import logging
import sys
import random
from retrying import retry

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


@retry(wait_fixed=30000)
def create_stack(stackname,path):
    try:
        crt_response = client.create_stack(
            TemplateURL=path,
            StackName=stackname
            )
        logging.info("Stack creation command issued")
        check_stack_status(stackname,stack_chk_value='CREATE_COMPLETE')
    except Exception as e:
        if "AlreadyExistsException" in e:
            logging.info("Stack - {0} exists. SO deleting the stack {0}".format(stackname))
            delete_response = client.delete_stack(
                StackName=stackname)
            logging.info("Issued delete stack")
            check_stack_status(stackname,stack_chk_value='DELETE_COMPLETE')


        else:
            logging.error("error - {0}".format(e))
            logging.error("Cannot create stack")
            raise





def check_stack_status(stackname,stack_chk_value):
    min_count = 0
    max_count = 120

    while True and min_count <= max_count:
        time.sleep(30)
        min_count = min_count + 1
        try:
            response = client.describe_stacks(
                StackName=stackname
                )

            chk_status=response['Stacks'][0]['StackStatus']
            if chk_status == stack_chk_value:
                logging.info("Stack status is {0}".format(chk_status))
                break
        except Exception as e:
            error_string = str(e)
            if "does not exist" in error_string:
                break
            else:
                logging.error("stack status has an error")
                raise

def main():
    if stack_operation == 'CREATE':
        create_stack(stack_name, args.s3path)

if __name__ == "__main__":
    main()







