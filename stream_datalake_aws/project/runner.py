import boto3
import os
from dotenv import dotenv_values
from project.aws.aws import UtilsAWS

#! Load environment all variables in '.env' file in a python dictionary
_env_var = dotenv_values(".env")