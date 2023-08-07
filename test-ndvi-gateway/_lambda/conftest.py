import json
import logging
import os

import pytest
import requests
from fake_useragent import UserAgent

ua = UserAgent()

LOGGER = logging.getLogger(__name__)
API_GATEWAY_URL = os.environ.get('API_GATEWAY_URL')
X_API_KEY = os.environ.get('X_API_KEY')
PARAM_POLYGON = os.environ.get('POLYGON')
CSR = '4326'
DATETIME = '2022-01-01T00:00Z/2022-12-31T00:00Z'


@pytest.fixture
def ndvi_position_response_format_json_coverage():
    # initialize response json
    yield response.json()


def test_api_gateway_ndiv_position_response_time_within_limit():
    url_to_test = API_GATEWAY_URL + f'/position?coords={PARAM_POLYGON}&datetime={DATETIME}&csr={CSR}'
    LOGGER.info(f'url: {url_to_test}')
    response = requests.get(url_to_test, headers={'User-Agent': ua.chrome, 'x-api-key': X_API_KEY})
    assert response.status_code == 200, f'API request failed with status code {response.status_code}'
    # Check if the response time is within 3 seconds
    assert response.elapsed.total_seconds() <= 3, f"API response time exceeds 3 seconds (actual: {response.elapsed.total_seconds()} seconds)"


def test_api_gateway_ndvi_position_status_success():
    # Check status code success with 200OK
    url_to_test = API_GATEWAY_URL + f'/position?coords={PARAM_POLYGON}&datetime={DATETIME}&csr={CSR}'
    response = requests.get(url_to_test, headers={'User-Agent': ua.chrome, 'x-api-key': X_API_KEY})
    assert response.status_code == 200


def test_api_gateway_ndvi_position_coverage_json_response_is_valid_json(ndvi_position_response_format_json_coverage):
    # Check if the API response in valid JSON format
    try:
        url_to_test = API_GATEWAY_URL + f'/position?coords={PARAM_POLYGON}&datetime={DATETIME}&csr={CSR}'
        response = requests.get(url_to_test, headers={'User-Agent': ua.chrome, 'x-api-key': X_API_KEY})
        json.loads(json.dumps(ndvi_position_response_format_json_coverage))
    except json.JSONDecodeError:
        assert False, "Invalid JSON format in the coverageJson response."


def test_api_gateway_ndvi_position_coverage_json_response_has_expected_keys(
        ndvi_position_response_format_json_coverage):
    # Define the expected keys in the coverageJson response
    expected_keys = {"type", "domain", "parameters", "ranges"}  # Add other expected keys

    # Check if the response contains the expected keys
    assert set(
        ndvi_position_response_format_json_coverage.keys()) == expected_keys, "coverageJson response has unexpected keys."


def test_api_gateway_ndvi_position_coverage_json_ranges_have_expected_structure(
        ndvi_position_response_format_json_coverage):
    # Define the expected structure of the "ranges" section
    expected_range_structure = {
        "type": "NdArray",
        "dataType": "float",
        "axisNames": [],
        "shape": [],
        "values": []
    }

    # Check if each range in the "ranges" section has the expected structure
    for range_key, range_data in ndvi_position_response_format_json_coverage.get("ranges", {}).items():
        assert set(range_data.keys()) == set(
            expected_range_structure.keys()), f"Range '{range_key}' has unexpected keys."


def test_api_gateway_ndvi_position_coverage_json_values_have_expected_length(
        ndvi_position_response_format_json_coverage):
    # Check if the length of "values" in each range matches the length of "shape"
    for range_key, range_data in ndvi_position_response_format_json_coverage.get("ranges", {}).items():
        assert len(range_data["values"]) == range_data["shape"][
            0], f"Range '{range_key}' has unexpected length of values."


"""
/area
UnitTest NDVI AREA (Grid)
"""


@pytest.fixture
def ndvi_area_response_format_json_coverage():
    url_to_test = API_GATEWAY_URL + f'/area?coords={PARAM_POLYGON}&datetime={DATETIME}&csr={CSR}'
    response = requests.get(url_to_test, headers={'User-Agent': ua.chrome, 'x-api-key': X_API_KEY})
    yield response.json()


def test_api_gateway_ndiv_area_response_time_within_limit():
    url_to_test = API_GATEWAY_URL + f'/area?coords={PARAM_POLYGON}&datetime={DATETIME}&csr={CSR}'
    LOGGER.info(f'url: {url_to_test}')
    response = requests.get(url_to_test, headers={'User-Agent': ua.chrome, 'x-api-key': X_API_KEY})
    assert response.status_code == 200, f'API request failed with status code {response.status_code}'
    # Check if the response time is within 3 seconds
    assert response.elapsed.total_seconds() <= 3, f"API response time exceeds 3 seconds (actual: {response.elapsed.total_seconds()} seconds)"


def test_api_gateway_ndvi_area_status_success():
    # Check status code success with 200OK
    url_to_test = API_GATEWAY_URL + f'/area?coords={PARAM_POLYGON}&datetime={DATETIME}&csr={CSR}'
    response = requests.get(url_to_test, headers={'User-Agent': ua.chrome, 'x-api-key': X_API_KEY})
    assert response.status_code == 200


def test_api_gateway_ndvi_area_coverage_json_response_is_valid_json(ndvi_area_response_format_json_coverage):
    # Check if the API response in valid JSON format
    try:
        json.loads(json.dumps(ndvi_area_response_format_json_coverage))
    except json.JSONDecodeError:
        assert False, "Invalid JSON format in the coverageJson response."


def test_api_gateway_ndvi_area_coverage_json_response_has_expected_keys(ndvi_area_response_format_json_coverage):
    # Define the expected keys in the coverageJson response
    expected_keys = {"type", "domain", "parameters", "ranges"}  # Add other expected keys

    # Check if the response contains the expected keys
    assert set(
        ndvi_area_response_format_json_coverage.keys()) == expected_keys, "coverageJson response has unexpected keys."


def test_api_gateway_ndvi_area_coverage_json_ranges_have_expected_structure(ndvi_area_response_format_json_coverage):
    # Define the expected structure of the "ranges" section
    expected_range_structure = {
        "type": "NdArray",
        "dataType": "float",
        "axisNames": [],
        "shape": [],
        "values": []
    }

    # Check if each range in the "ranges" section has the expected structure
    for range_key, range_data in ndvi_area_response_format_json_coverage.get("ranges", {}).items():
        assert set(range_data.keys()) == set(
            expected_range_structure.keys()), f"Range '{range_key}' has unexpected keys."


def test_api_gateway_ndvi_coverage_json_range_values_are_float_or_null(ndvi_area_response_format_json_coverage):
    # Check if the values in the "values" array are either floats or null
    for range_key, range_data in ndvi_area_response_format_json_coverage.get("ranges", {}).items():
        for value in range_data["values"]:
            assert isinstance(value,
                              (float, type(None))), f"Invalid value in range '{range_key}'. Expected float or null."
