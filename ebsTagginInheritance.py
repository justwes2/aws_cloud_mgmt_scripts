import boto3

ec2Client = boto3.client('ec2')
ec2Resource = boto3.resource('ec2')


def get_instance_id(event):
    # Passing in test inst for dev
    # instance_id = event["detail"]["instance-id"]
    instance_id = 'i-0e9d4b20432516e9f'
    # instance = ec2Client.describe_instances(
    #     Filters = [
    #         {
    #             'Name' : 'instance-id',
    #             'Values' : [
    #                 instance_id
    #             ]
    #         }
    #     ]
    # )
    return instance_id

def make_vol_tags(vm_tags, vol_tags):
    final_tags_list = []
    final_tags = {}
    for pair in vol_tags:
        final_tags[pair["Key"]] = pair["Value"]
    for vm_tag_pair in vm_tags:
        if vm_tag_pair["Key"] in final_tags:
            print '{} already exists'.format(vm_tag_pair["Key"])
        else:
            final_tags[vm_tag_pair["Key"]] = vm_tag_pair["Value"]
    print final_tags
    for key, value in final_tags.iteritems():
        print key, value
        final_tags_list.append({"Key" : key, "Value" : value})
    return final_tags_list

def get_tags(instance):
    for instance in ec2Resource.instances.filter(
        Filters = [
            {
                'Name' : 'instance-id',
                'Values' : [
                    instance
                ]
            }
        ]
    ):
        ec2_tags = instance.tags
        for volume in instance.volumes.all():
            vol_tags = volume.tags
            if vol_tags == None:
                volume.create_tags(Tags = ec2_tags)
            else:
                volume.create_tags(Tags = make_vol_tags(ec2_tags, vol_tags))

def lambda_handler(event, context):
    get_tags(get_instance_id('event'))

lambda_handler('event', 'context')
