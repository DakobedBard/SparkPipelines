import json
from Pipelines.data_utils.dynamoConnection import getDynamoResource
dynamoDB = getDynamoResource()

table = dynamoDB.Table('battle-royale')
items = []

with open('Pipelines/dynamo/game_data/scripts/items.json') as f:
    for row in f:
        items.append(json.loads(row))

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

        