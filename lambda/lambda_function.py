# Visitor Counter Lambda for hasansyed.dev
# Increments visitor count in DynamoDB and returns new count
import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter2.0')

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'id': 'visitors'},
            UpdateExpression='SET #vc = if_not_exists(#vc, :start) + :inc',
            ExpressionAttributeNames={
                '#vc': 'visitor_count'
            },
            ExpressionAttributeValues={
                ':inc': 1,
                ':start': 0
            },
            ReturnValues='UPDATED_NEW'
        )

        new_count = int(response['Attributes']['visitor_count'])

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'count': new_count
            })
        }

    except ClientError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': e.response['Error']['Message']
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }