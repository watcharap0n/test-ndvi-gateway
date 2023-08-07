import json
import os
from datetime import datetime

import boto3
import pytest
import pytz
from pytest_jsonreport.plugin import JSONReport


def lambda_handler(event, context):
    try:
        print('Starting testing with pytest.')

        # Run pytest path conftest.py & keep report for output
        plugin = JSONReport()
        pytest.main([
            '--json-report-file=none',
            'conftest.py'
        ],
            plugins=[plugin])

        bucket = os.environ.get('BUCKET')

        # define key path s3 report/{collection}/report.json
        tz = pytz.timezone('Asia/Bangkok')
        dt = datetime.now(tz)
        formatted_string = dt.strftime('%Y-%m-%dT%H:%M')

        key = f'report/{os.environ.get("COLLECTION")}/report.json'
        plugin.report['datetime'] = formatted_string

        # save file json to s3 bucket
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=bucket, Key=key, Body=json.dumps(plugin.report))

        return {
            'statusCode': 200,
            'body': {
                'summary': plugin.report['summary'],
                'duration': plugin.report['duration']
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Internal Server error for detail {e}'
        }
