import boto3

ec2 = boto3.resource('ec2')

instance_id = ['i-0e9ad655ef879c2a2']

ec2.instances.filter(InstanceIds = instance_id).terminate()