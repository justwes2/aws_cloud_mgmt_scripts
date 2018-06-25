import boto3

# List the instances you want to tag here. They should be in quotes, and separated by a comma
instances = ()

# Below are the values that are required for each instance.
# Enter the value you want applied in the 'VALUE' slot
ApplicationTag = 'VALUE'
OwnerTag = 'VALUE'
DeptTag = 'VALUE'
ClientTag = 'VALUE'

ec2 =  boto3.client('ec2')

for instance in instances:
    ec2.create_tags(
    #     if you want to make sure the script behaves as intended without making any changes,
    #     uncomment the next line (remove the '#')
    #     DryRun=True,
        Resources=[
            instance,
        ],
        Tags=[
        #     These are the reqired tags for each vm.
        #     If you do not want to apply a specified tag to the instances, comment that object out
        #      Comment it out by adding a '#' in front of the four lines, from '{' to '},'
            {
                'Key': 'Application',
                'Value': ApplicationTag
            },
            {
                'Key': 'Owner',
                'Value': OwnerTag
            },
            {
                'Key': 'Dept',
                'Value': DeptTag
            },
            {
                'Key': 'Client',
                'Value': ClientTag
            },
        ]
    )
