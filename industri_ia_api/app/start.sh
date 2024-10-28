#!/bin/bash

serverless dynamodb install --config serverless.dev.yml --stage dev

exec serverless offline start --host "0.0.0.0" --reloadHandler --config serverless.dev.yml --stage dev