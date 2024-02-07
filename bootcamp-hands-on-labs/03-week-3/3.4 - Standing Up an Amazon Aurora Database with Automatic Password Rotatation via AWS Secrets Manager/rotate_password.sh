#!/bin/bash

SECRET_ID='CHANGE_ME'

aws secretsmanager rotate-secret --secret-id ${SECRET_ID}
