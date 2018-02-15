import boto3

# get id from lambda event

# i-0a0f29c2e338fc66f is my sample

# identify instance
newInstance = client.describe_instances(InstanceIds = ["i-0a0f29c2e338fc66f"])
print newInstance

# get tags attached to instance
print newInstance["Reservations"][0]["Instances"][0]["Tags"]
# turn those into a dict
myTagDict = {}
for pair in newInstance["Reservations"][0]["Instances"][0]["Tags"]:
    myTagDict[pair["Key"]] = pair["Value"]
print myTagDict

# instantiate approved values:
approvedUsers = ("Wes", "Kate", "Bill")
approvedNames = ("Scarif", "Sandbox", "Jakku", "Stardust")
approvedDepts = ("Monk", "Cosmotology", "Dwellers", "Catnip", "R&D")
requiredTags = ("User", "Name", "Dept") #need a fix to use keys of requiredAndApproved on line 30
requiredAndApproved = {
    "User" : ["Wes", "Kate", "Bill"],
    "Name" : ["Scarif", "Sandbox", "Jakku", "Stardust"],
    "Dept" : ["Monk", "Cosmotology", "Dwellers", "Catnip", "R&D"]
}#change tables to one table and each object is a list of values, then pull in the table, use number of items to set length
# REFACTOR INTO LIST AND LOOP
for catagory in requiredTags:
    if catagory in myTagDict:
        if myTagDict[catagory] in requiredAndApproved[catagory]:
            print "Valid"# sucess outcome
        else:
            print "Invalid value for " + catagory
    else:
        print "No value for " + catagory

# check if required values are present in the dict
# User
if "User" in myTagDict:
    # check if required values are valid
    if myTagDict["User"] in approvedUsers:
        print myTagDict["User"]
    else:
        print "User not valid"
else:
    print "No User Specified"

# Name
if "Name" in myTagDict:
    # check if required values are valid
    if myTagDict["Name"] in approvedNames:
        print myTagDict["Name"]
    else:
        print "Name not valid"
else:
    print "No Name Specified"

# Dept
if "Dept" in myTagDict:
    # check if required values are valid
    if myTagDict["Dept"] in approvedDepts:
        print myTagDict["Dept"]
    else:
        print "Dept not valid"
else:
    print "No Dept Specified"

# if any error returns, sent command to stop instance

# should we create tags with null values?
