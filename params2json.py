"""Takes parameter store secrets and decrypts them to JSON that can be used by test-automation."""
import boto3
import json
import pprint


def get_secret(parameter_key, is_secure=True):
    client = boto3.client('ssm', region_name='us-west-2')

    response = client.get_parameter(
        Name=parameter_key,
        WithDecryption=is_secure
    )

    return response['Parameter']['Value']

def dump_secrets():
    secrets = {
      "users": {
        "ldap": {
          "email": 'iam_test@mozilla.com',
          "password": get_secret('/iam/automated-test/iam_test_at_mozilla.com'),
          "secret_seed" : get_secret('/iam/automated-test/iam_test_at_mozilla.com_seed')
        },
        "passwordless":{
          "email": get_secret('/iam/automated-test/auth0_test_user_6d576ce8-07d7-11e7-aa80-74d435b2b680_at_restmail.net')
        },
        "github": {
          "username": 'moz.parsys@gmail.com',
          "password": get_secret('/iam/automated-test/moz.parsys_at_gmail.com'),
          "secret_seed": get_secret('/iam/automated-test/moz.parsys_at_gmail.com_seed')
        },
        "google": {
          "email": 'test.parsys@gmail.com',
          "password": get_secret('/iam/automated-test/test.parsys_at_gmail.com')
        },
        "fxa": {
            "email": 'moz.parsys@gmail.com',
            "password": get_secret('/iam/automated-test/moz.parsys_at_gmail.com'),
            "secret_seed": get_secret('/iam/automated-test/moz.parsys_at_gmail.com_seed')
        }
      }
    }

    return secrets

if __name__ == "__main__":
    print(dump_secrets())
