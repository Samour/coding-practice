#!/bin/bash

. .secrets

STACK_NAME="PlayDb"
CHANGE_SET_TYPE="UPDATE"

CS_VERSION=$(date -u +%FT%H-%M-%S)
CHANGE_SET_NAME="$STACK_NAME-$CS_VERSION"

aws cloudformation \
  create-change-set \
  --stack-name $STACK_NAME \
  --change-set-name $CHANGE_SET_NAME \
  --change-set-type $CHANGE_SET_TYPE \
  --template-body file://./database.yaml \
  --parameters ParameterKey=RootUser,ParameterValue="$DB_ROOT_USERNAME" \
    ParameterKey=RootPassword,ParameterValue="$DB_ROOT_PASSWORD" \
    ParameterKey=StackName,ParameterValue="$STACK_NAME"

echo
echo Change set created: $CHANGE_SET_NAME
echo
