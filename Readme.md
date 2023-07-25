# API Gateway Testing with Pytest

This repository contains tests implemented using `pytest` to test an API Gateway with AWS Lambda backend. The API Gateway provides endpoints to access coverage data related to NDVI (Normalized Difference Vegetation Index) for different geographic positions and areas.

## Setup

1. Clone this repository:

```bash
$ git clone https://github.com/watcharap0n/test-ndvi-gateway.git
$ cd test-ndvi-gateway
```

1. Install the require dependencies

```bash
$ pip install -r requirements.txt
```
2. Set up the required environment variables:

Create a .env file in the root directory of the project and set the following environment variables:

```bash
API_GATEWAY_URL=<Your API Gateway URL>
X_API_KEY=<Your API Gateway API Key>
POLYGON=<Your geographic coordinates for testing>
```
## Running Tests

To run the tests, use the following command:

```bash
pytest
```
The tests will be executed, and you will see the test results along with any failures or errors displayed in the terminal.

## Test Cases

The test cases implemented in pytest cover the following scenarios:

1. Response Time: The tests check the response time of the API to ensure it responds within 3 seconds.
2. Response Status: The tests verify that the API responds with a 200 OK status for successful requests.
3. JSON Format: The tests validate the JSON format of the API responses to ensure they are in the expected coverageJson format.
4. Response Data Structure: The tests check the structure of the ranges section in the coverageJson response to match the expected format.
5. Data Values: The tests ensure that the values in the coverageJson response are either floats or null, as expected.


## Contributing

Feel free to contribute to this project by opening issues or pull requests. Your contributions are valuable and will help improve the testing of the API Gateway.

## License

This project is licensed under the MIT License.


```angular2html
Replace `
<Your API Gateway URL>`, `
    <Your API Gateway API Key>`, and `
        <Your geographic coordinates for testing>` with your actual API Gateway URL, API Key, and geographic coordinates
            used for testing.
```

In this `README.md`, you've described the setup, running of tests, and what each test case checks for. Additionally, you've included a section on contributing and licensing, making it a comprehensive guide for users and potential contributors.

