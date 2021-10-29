```shell
git clone https://github.com/neelabalan/mongodb-sample-dataset.git
```

```shell
docker run \
  --rm \
  --name mongo \
  --env MONGO_INITDB_ROOT_USERNAME=root \
  --env MONGO_INITDB_ROOT_PASSWORD=example \
  --env MONGO_INITDB_DATABASE=sample \
  --volume $(pwd)/mongodb-sample-dataset/sample_analytics:/docker-entrypoint-initdb.d \
  --publish 27017:27017 \
  mongo
```


```shell
docker exec --interactive --tty mongo /bin/bash

mongoimport --host localhost --port 27017 --db sample --authenticationDatabase admin --username root --password example --collection accounts --file /docker-entrypoint-initdb.d/accounts.json 

mongoimport --host localhost --port 27017 --db sample --authenticationDatabase admin --username root --password example --collection customers --file /docker-entrypoint-initdb.d/customers.json 

mongoimport --host localhost --port 27017 --db sample --authenticationDatabase admin --username root --password example --collection transactions --file /docker-entrypoint-initdb.d/transactions.json 

```