import boto3

client = boto3.client('cloudformation', region_name='us-east-1')

def check_stack_alive(stack_name):
    response = client.describe_stacks(
        StackName=stack_name
    )

    return response

check_stack_status=check_stack_alive()
