# lets-get-it-started-in-here

A demo project that uses Python to play around with some of acloudguru's starting AWS labs for my own personal use.   

## About 

The projects include the following: 

	### Meteors 
	
	Absolutely first project using Git with an SSH key and making all sorts of amendments from the cli.
	
	### Shotty
	
	Project involving listing some EC2 instances started through the AWS management console.
	Steps included creating a user with EC2 Full Access permissions directly (instead of using a group).
	From powershell, configuring this user's profile:
	
	`aws configure --profile shotty`
	
	After installing boto3, list all the EC2 instances, and use `%history` to copy code and paste it in shotty.py.
	Running: `pipenv run python shotty/shotty.py <command> <--project=PROJECT>`
	
	where *command* is list, start, or stop;
		  *project* is the tag Value matching the tag Key `project` given to the ec2 instances 
	