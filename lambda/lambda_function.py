import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'id': 'visitors'},
            UpdateExpression='SET count = if_not_exists(count, :start) + :inc',
            ExpressionAttributeValues={
                ':inc': 1,
                ':start': 0
            },
            ReturnValues='UPDATED_NEW'
        )
        
        # Extract the new count from the response
        new_count = response['Attributes']['count']
        
        # Return success response to API Gateway
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Allows your frontend to call it
            },
            'body': json.dumps({'count': new_count})
        }
        
    except Exception as e:
        # Return error response
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }