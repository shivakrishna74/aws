import boto3

client = boto3.client('cloudformation', region_name='us-east-1')

def list_stacks():
    response = client.list_stacks()
    return response

stack_list=list_stacks()
print (stack_list)

