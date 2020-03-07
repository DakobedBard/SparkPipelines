Kafka Connect Notes

The configuration file. The file must be formatted as a valid JSON or Java properties file and must contain a correct configuration for a connector whose name matches the one specified in the command-line.

confluent local load sink-1 -- -d sink-postgres.json
curl -X DELETE http://localhost:8083/connectors/sink-2

confluent local list connectors

List the connectors this is easier lol
confluent local status connectors


bin/kafka-topics --create --zookeeper localhost:2181 --topic connect-configs --replication-factor 3 --partitions 1 --config cleanup.policy=compact

Double Dash in bash
More precisely, a double dash (--) is used in most bash built-in commands and many other commands to signify the end of command options, after which only positional parameters are accepted.


confluent local config tweets-source-d <path-to-connector>/wikipedia-file-source.json


confluent local config wikipedia-file-source -d /tweet-file-source.properties --path ${CONFLUENT_HOME}

confluent local config kafka-tweets-source -- -d $(pwd)/tweet-file-source.properties --path ${CONFLUENT_HOME}