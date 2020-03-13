import boto3
from Pipelines.data_utils.dynamoConnection import getDynamoDBClient

dynamodb = getDynamoDBClient()

try:
    dynamodb.delete_table(TableName='Books')
    print("Table deleted successfully.")
except Exception as e:
    print("Could not delete table. Please try again in a moment. Error:")
    print(e)
