import boto3
from boto3.dynamodb.conditions import Key
from Pipelines.data_utils.dynamoConnection import getDynamoResource

dynamoDB = getDynamoResource()
table = dynamoDB.Table('Books')

response = table.query(KeyConditionExpression=Key('Author').eq('John Grisham'))
print("The query has returned the following items")
for item in response['Items']:
    print(item)

