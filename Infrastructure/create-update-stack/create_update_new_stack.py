import boto3

client = boto3.client('cloudformation', region_name='us-east-1')

def check_stack_alive(stack_name):
    try:
        response = client.describe_stacks(
            StackName=stack_name
            )
        print(stack_name)


    except Exception as e:

        err_msg=str(e)
        print(err_msg)









check_stack_status=check_stack_alive('neDev-newThing')