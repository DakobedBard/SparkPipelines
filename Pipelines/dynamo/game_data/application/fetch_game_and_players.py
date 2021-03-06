from Pipelines.dynamo.game_data.application.entities import Game, UserGameMapping
from Pipelines.data_utils.dynamoConnection import getDynamoDBClient

dynamoDB = getDynamoDBClient()

GAME_ID = "3d4285f0-e52b-401a-a59b-112b38c4a26b"

def fetch_game_and_users(game_id):
    resp = dynamoDB.query(
        TableName='battle-royale',
        KeyConditionExpression="PK = :pk and SK between :metadata AND :users",
        ExpressionAttributeValues={
            ":pk": {"S": "GAME#{}".format(game_id)},
            ":metadata": {"S": "#METADATA#{}".format(game_id)},
            ":users": {"S": "USER$"},
        },
        ScanIndexForward=True
    )
    game = Game(resp['Items'][0])
    game.users = [UserGameMapping(item) for item in resp['Items'][1:]]
    return game
game = fetch_game_and_users(GAME_ID)
print(game)
for user in game.users:
    print(user)