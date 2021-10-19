#!/usr/bin/env bash

docker run \
  --env MONGO_INITDB_ROOT_USERNAME=root \
  --env MONGO_INITDB_ROOT_PASSWORD=example \
  --publish 27017:27017 \
  --rm \
  --detach \
  --name mongo \
  mongo