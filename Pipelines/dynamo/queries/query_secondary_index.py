from boto3.dynamodb.conditions import Key
from Pipelines.data_utils.dynamoConnection import getDynamoResource
import time
dynamodb = getDynamoResource()
table = dynamodb.Table('Books')

# When adding a global secondary index to an existing table, you cannot query the index until it has been backfilled.
# This portion of the script waits until the index is in the “ACTIVE” status, indicating it is ready to be queried.

while True:
    if not table.global_secondary_indexes or table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
        print('Waiting for index to backfill...')
        time.sleep(5)
        table.reload()
    else:
        break

# When making a Query call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
# If we want to use a specific index, we also need to pass the IndexName in our API call.

response = table.query(
    IndexName='CategoryIndex',
    KeyConditionExpression=Key('Category').eq('Suspense'),
)
print("The query returned the following items:")
for item in response['Items']:
    print(item)
