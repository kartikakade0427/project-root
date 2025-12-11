import requests
import unittest
import time


# Wait for the service to start before running tests (critical in CI)
# The script includes a short hard sleep, but your CI pipeline also performs its own readiness checks.
time.sleep(2)


# When the test runs *inside the API container* the service is reachable at localhost:5000
API_URL = "http://localhost:5000/health"


class TestApiHealth(unittest.TestCase):


def test_health_endpoint_status(self):
"""Checks if the /health endpoint is reachable and returns 200."""
try:
response = requests.get(API_URL, timeout=10)
self.assertEqual(response.status_code, 200)
self.assertEqual(response.json()['status'], 'ok')
print("Test passed: Health check successful.")
except requests.exceptions.ConnectionError:
self.fail(f"Test failed: Could not connect to API at {API_URL}")


if __name__ == '__main__':
unittest.main()
