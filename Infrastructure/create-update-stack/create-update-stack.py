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

waiter = client.get_waiter('stack_exists')

TemplateURL=path,
stackname=stack_name


def stack_exists(stackname):
    waiter.wait(
        StackName=stackname,
        WaiterConfig={
            'Delay': 2,
            'MaxAttempts': 5
            }
    )


def create_stack(stackname,path):
    response = client.create_stack
    TemplateURL=path,
    StackName=stackname
    )


def delete_stack(stackname):
    response = client.delete_stack(
        StackName=stackname
    )


def check_stack_status(stackname,stack_chk_value):
    response = client.describe_stacks(
        StackName=stackname

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
    try:
        if stack_operation == 'CREATE':
            create_stack(StackName, TemplateURL)
            check_stack_status(stackname, stack_chk_value='CREATE_COMPLETE')
    except:
        logging.error("something screwed up with the stack status")
        raise

    logging.info("trying to create the stack")


if __name__ == "__main__":
    main()

