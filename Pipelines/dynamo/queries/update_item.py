from Pipelines.data_utils.dynamoConnection import getDynamoResource

dynamoDB = getDynamoResource()
table = dynamoDB.Table('Books')
resp = table.get_item(Key={'Author':"John Grisham", "Title":"The Rainmaker"})

print("Item before update:")
print(resp['Item'])

resp = table.update_item(
    Key={'Author':"John Grisham", "Title":"The Rainmaker"},
    ExpressionAttributeNames={
        '#formats':"Formats",
        "#audiobook":"Audiobook"
    },
    ExpressionAttributeValues={
        ":id": "8WE3KPTP",
    },
    UpdateExpression="SET #formats.#audiobook = :id",
)
resp = table.get_item(Key={'Author':"John Grisham", "Title":"The Rainmaker"})

print("Item after update:")
print(resp['Item'])