import json
import boto3
import os

region = 'eu-west-1'
neo4j_instance_id = "i-***"


def lambda_handler(event, context):
    # print(event)
    http_method=event['httpMethod']
    if http_method=='GET':
        ec2_client = boto3.client('ec2', region_name=region)
        ec2 = ec2_client.describe_instances()
        for i in list(range(len(ec2["Reservations"]))):
            instance_info = ec2["Reservations"][i]["Instances"][0]
            if instance_info["InstanceId"] == ec2instance_id:
                instance_state = instance_info["State"]["Name"]
        state=instance_state
        
    elif http_method=='POST':
        ec2_client = boto3.client('ec2', region_name=region)
        ec2 = ec2_client.describe_instances()
        body=json.loads(event['body'])
        state=body['state']
        if state==0:
            ec2_client.stop_instances(InstanceIds=[ec2instance_id])
        else:
            ec2_client.start_instances(InstanceIds=[ec2instance_id])

    return {
        'statusCode': 200,
        'body': json.dumps({'state':state})
    }

