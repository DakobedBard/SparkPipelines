Here we will be simulating an online game

Consider a multiplayer game in which a User can create a game, and allow other users to join the game.  First we will consider
the access patterns that will be necessarry

User Profile access Patterns
- Create user profile (Write)
- Update user profile (Write)
- Get user profile (read)


Pregame access patterns 

- Create game (Write)
- Find open games (Read)
- Find open games by map (Read)
- Join Game (Write)
- View game (Read)
- View users in game (Read)
- Start game (Write)

In-game & postgame access patterns 
- update game for user (Write)
- update game (Write)
- Find all past games for a user (read)

When designing the primary key for a DynamoDB table keep the following best practices in mind

- Start with the different entities in your table
- Use prefixes to distinguish between entity types
- For a primary key it's important that you can satisfy the read and write options on a single item by using the single item
by using the single-item APIS (GetItem, PutItem, UpdateItem, and DeleteItem)


In this example we have 
- User
- Game
- UserGameMapping -> record that indicates a user joined a game.  There is a many-to-many relationship between User and Game.
            -> Having a many to many mapping is usually an indication that you want to satisfy two query patterns, and this game
            is no exception.  We have access pattern that needs to find all users that have joined a game as well as another pattern to find all games that a user has played
            


If your data model has multiple entities with relationships among them, you generally use a composite primary key with both HASH and RANGE values. The composite primary key gives us the Query ability on the HASH key to satisfy one of the query patterns we need. In the DynamoDB documentation, the partition key is called HASH and the sort key is called RANGE, and in this guide we use the API terminology interchangeably and especially when we discuss the code or DynamoDB JSON wire protocol format.
