# This script appends a value to the value matched to `table_value` on key `table_key` on table `table_name`

import sys
import boto3
from boto3.dynamodb.conditions import Key, Attr


dynamo_resource =  boto3.resource('dynamodb')

table_name = 'valid_tags'
table_key = 'tag_id'
table_value = 'Color'

def add_value(input):
    table = dynamo_resource.Table(table_name)

    response = table.query(
        KeyConditionExpression = Key(table_key).eq(table_value)
    )

    values = response['Items'][0]['values']

    values.append(input)

    table.put_item(
        Item = {
            table_key : table_value,
            'values' : values
        }
    )

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    add_value(*sys.argv[1:])
