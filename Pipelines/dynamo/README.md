Relational databases can be a great fit for analytical applications. 
    - Start with the entities first -> normalized relational model can satisfy any query pattern 
    
NonRelational databases are designed for speed and scale, not flexibility.  Horizontally scaling databases such as 
DynamoDB provides consisten performance at any scale.  

1) Focus on access patterns
When doing any kind of data modeling, you will start with an entity-relationship diagram that describes the different objects (or entities) in your application and how they are connected (or the relationships between your entities).

In relational databases, you will put your entities directly into tables and specify relationships using foreign keys. After you have defined your data tables, a relational database provides a flexible query language to return data in the shape you need.

In DynamoDB, you think about access patterns before modeling your table. NoSQL databases are focused on speed, not flexibility. You first ask how you will access your data, and then model your data in the shape it will be accessed.

2. Optimize for the number of requests to DynamoDB
After you have documented your application’s access pattern needs, you are ready to design your table. You should design your table to minimize the number of requests to DynamoDB for each access pattern. Ideally, each access pattern should require only a single request to DynamoDB because network requests are slow, and this limits the number of network requests you will make in your application.

To optimize for the number of requests to DynamoDB, you need to understand some core concepts:

- Primary keys
- Secondary indexes
- Transactions

3. Don’t fake a relational model
People new to DynamoDB often try to implement a relational model on top of nonrelational DynamoDB. If you try to do this, you will lose most of the benefits of DynamoDB.

The most common anti-patterns (ineffective responses to recurring problems) that people try with DynamoDB are:

-Normalization: In a relational database, you normalize your data to reduce data redundancy and storage space, and then use joins to combine multiple different tables. However, joins at scale are slow and expensive. DynamoDB does not allow for joins because they slow down as your table grows.

-One data type per table: Your DynamoDB table will often include different types of data in a single table. In our example, we have User, Game, and UserGameMapping entities in a single table. In a relational database, this would be modeled as three different tables.

-Too many secondary indexes: People often try to create a secondary index for each additional access pattern they need. DynamoDB is schemaless, and this applies to your indexes, too. Use the flexibility in your attributes to reuse a single secondary index across multiple data types in your table. This is called index overloading.
  
  psql --host=adolindb.cju35raiyeyw.us-west-2.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=adolindb 

  adolindb.cju35raiyeyw.us-west-2.rds.amazonaws.com
  
  List the tables 
  aws dynamodb list-tables --endpoint-url http://localhost:8000
  
  psql "host=hostName port=portNumber sslmode=verify-full sslrootcert=certificateFile dbname=DBName user=userName"