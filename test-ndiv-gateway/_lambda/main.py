import subprocess
import sys


def lambda_handler(event, context):
    # Define the pytest command and arguments
    command = ['pip', 'list']
    result_package = subprocess.run(command, capture_output=True, text=True)
    list_package = result_package.stdout
    print(list_package)

    try:
        layer_path = '/opt/python'
        sys.path.append(layer_path)
        # Execute the pytest command
        command = ["pytest", "conftest.py", "-vv", "-o", "log_cli=true", "--html=report.html"]
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout

        # Log the output or send it to CloudWatch Logs or S3 for analysis
        print(output)
        return {
            "statusCode": 200,
            "body": "Tests executed successfully.",
        }
    except Exception as e:
        # Log any errors and return an error response
        print(str(e))
        return {
            "statusCode": 500,
            "body": "Error executing tests.",
        }
