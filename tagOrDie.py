import boto3

# get id from lambda event

# i-0a0f29c2e338fc66f is my sample
def get_instance_id(event):
    # identify instance
    global instance
    instanceId = event["detail"]["instance-id"]
    instance = client.describe_instances(
    Filters =[
        {
            'Name' : 'instance-id',
            'Values' : [
                instanceId
                ]
            }
        ]
    )
    # instance = client.describe_instances(InstanceIds = ["i-0a0f29c2e338fc66f"])
    print instance
    return instance

def create_tag_dict(instance):
    # get tags attached to instance
    print instance["Reservations"][0]["Instances"][0]["Tags"]
    # turn those into a dict
    global myTagDict
    myTagDict = {}
    for pair in instance"Reservations"][0]["Instances"][0]["Tags"]:
        myTagDict[pair["Key"]] = pair["Value"]
    print myTagDict

# # instantiate approved values:
# approvedUsers = ("Wes", "Kate", "Bill")
# approvedNames = ("Scarif", "Sandbox", "Jakku", "Stardust")
# approvedDepts = ("Monk", "Cosmotology", "Dwellers", "Catnip", "R&D")
# requiredTags = ("User", "Name", "Dept") #need a fix to use keys of requiredAndApproved on line 30
# requiredAndApproved = {
#     "User" : ["Wes", "Kate", "Bill"],
#     "Name" : ["Scarif", "Sandbox", "Jakku", "Stardust"],
#     "Dept" : ["Monk", "Cosmotology", "Dwellers", "Catnip", "R&D"]
# }#change tables to one table and each object is a list of values, then pull in the table, use number of items to set length

#pull in Dynamo table
def get_table():
    dynamo_resource =  boto3.resource('dynamodb')
    tag_values_table = dynamo_resource.Table('tag_values')
    data = tag_values_table.scan()
    global valid_tag_dict
    valid_tag_dict = {}
    for pair in data['Items']:
        valid_tag_dict[pair['tag_id']] = pair['value']
    print valid_tag_dict

# check values
def create_results_dict(instTags, validTags, event):
    global results
    results = {}
    if 'Name' in instTags:
        results['ServerName'] = instTags['Name']
    results['TimeCreated'] = event['time']
    #User
    if 'User' in instTags and instTags['User'] in validTags['user']:
        results['User'] = 'Correct'
    else:
        results['User'] = 'Error'
    #repeat as needed
    return results

# # REFACTOR INTO LIST AND LOOP
# for catagory in requiredTags:
#     if catagory in myTagDict:
#         if myTagDict[catagory] in requiredAndApproved[catagory]:
#             print "Valid"# sucess outcome
#         else:
#             print "Invalid value for " + catagory
#     else:
#         print "No value for " + catagory
#
# # check if required values are present in the dict
# # User
# if "User" in myTagDict:
#     # check if required values are valid
#     if myTagDict["User"] in approvedUsers:
#         print myTagDict["User"]
#     else:
#         print "User not valid"
# else:
#     print "No User Specified"
#
# # Name
# if "Name" in myTagDict:
#     # check if required values are valid
#     if myTagDict["Name"] in approvedNames:
#         print myTagDict["Name"]
#     else:
#         print "Name not valid"
# else:
#     print "No Name Specified"
#
# # Dept
# if "Dept" in myTagDict:
#     # check if required values are valid
#     if myTagDict["Dept"] in approvedDepts:
#         print myTagDict["Dept"]
#     else:
#         print "Dept not valid"
# else:
#     print "No Dept Specified"

# if any error returns, sent command to stop instance

# should we create tags with null values?
