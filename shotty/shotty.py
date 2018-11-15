import boto3
import sys
import click


session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')


#Click will execute the Function
@click.command()

#Function to list all EC2-Insances of an AWS Account
def list_instances():
	"List EC2 instances"
	for i in ec2.instances.all():
		print(', '.join((
			i.id,
			i.instance_type,
			i.placement['AvailabilityZone'],
			i.state['Name'],
			i.public_dns_name)))

	return



if __name__ == '__main__':
	#List the arguments passed to the script
	print(sys.argv)
	
	list_instances()

