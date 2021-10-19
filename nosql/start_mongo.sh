#!/usr/bin/env bash

docker run \
  --env MONGO_INITDB_ROOT_USERNAME=python \
  --env MONGO_INITDB_ROOT_PASSWORD=secret \
  --publish 27017:27017 \
  --rm \
  --detach \
  --name mongo \
  mongo