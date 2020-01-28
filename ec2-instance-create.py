import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-00b6a8a2bd28daf19',
     MinCount=1,
     MaxCount=3,
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )
#ec2details = ec2.describe_instances()
#print(ec2details)
