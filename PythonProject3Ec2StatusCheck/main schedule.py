import boto3
import schedule
import time

ec2_client = boto3.client('ec2', region_name='us-east-2')
ec2_resource = boto3.resource('ec2', region_name='us-east-2')

def check_instance_status():
    statuses = ec2_client.describe_instance_status(  #this alone only displays statuses of running instances
        IncludeAllInstances=True   #this makes it include even broken servers
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        print(f"Instance {status['InstanceId']} status is {ins_status} and the system status is {sys_status}")
    print("-----------------------------------------------------------------------------------------------")

#use schedule library
schedule.every(5).seconds.do(check_instance_status)

#in order to use the schedular, use a while loop
while True:
    schedule.run_pending()
    time.sleep(1)

