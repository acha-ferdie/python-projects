import boto3

ec2_client = boto3.client('ec2', region_name='us-east-2')
ec2_resource = boto3.resource('ec2', region_name='us-east-2')

reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    print(reservation['Instances'])
    for instance in reservation['Instances']:
        print(f"Status of instance {instance['InstanceId']} is:  {instance['State']['Name']}")


statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemStatus']['Status']
    print(f"Instance {status['InstanceId']} status is {ins_status} and the system status is {sys_status}")



#Ec2 server status state
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html

#describe instance status
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_status.html

#task 3: Get everything in one API call
