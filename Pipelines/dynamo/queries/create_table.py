from Pipelines.data_utils.dynamoConnection import getDynamoDBClient

dbb = getDynamoDBClient(local=True)

try:
    response = dbb.create_table(
        TableName="Books",
        KeySchema=[
            {
                "AttributeName":"Author",
                "KeyType":"HASH"
            },
            {
                "AttributeName":"Title",
                "KeyType":"RANGE"
            }
        ],
        # Attributes used in the KeySchema or Indexes
        AttributeDefinitions=[
            {
                "AttributeName":"Author",
                "AttributeType":"S"
            },
            {
                "AttributeName":"Title",
                "AttributeType":"S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits":1,
            "WriteCapacityUnits":1
        }
    )
    print("Table Create succesfully")
except Exception as e:
    print("Error creating table")
    print(e)