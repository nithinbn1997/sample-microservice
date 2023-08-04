"""
test cases for sender po
"""
import requests
from fastapi.testclient import TestClient
from sender_po import app1

client = TestClient(app1)

# Test Case 1: Valid PO Data
def test_valid_po_data():
    """
    Test the sending and processing of valid Purchase Order (PO) data.

    This function sets up a mock receiver service and tests the sending
    and processing of a valid PO data using the FastAPI client.

    The mock_receiver_service simulates the receiver service's response,
    allowing the test to run independently of the actual receiver service.

    The test sends a sample valid PO data to the endpoint, asserts the
    response status code is 200, and checks the response JSON for expected
    content."""

    # Mock the receiver service response
    def mock_receiver_service():
        return requests.Response()

    # Set up the FastAPI app
    app1.dependency_overrides[requests.post] = mock_receiver_service

    # Sample valid PO data
    po_data = {
        "podetails": {
            "id": "12345",
            "fields": {
                "tranid": "PO12345"
            }
        }
    }

    response = client.post("/send_process_po", json=po_data)
    assert response.status_code == 200
    assert response.json() == {
        "message": "PO data sent successfully",
        "po_id": "12345",
        "po_name": "PO12345"
    }

# Test Case 2: Invalid PO Data Format
def test_invalid_po_data_format():
    """
    Test handling of invalid Purchase Order (PO) data format.

    This function tests the handling of invalid PO data format by sending
    a sample invalid PO data (missing 'id' field) to the endpoint using the
    FastAPI client.

    The test expects the response status code to be 400 (Bad Request) and
    checks that the response JSON contains the expected error detail.
    """
    # Sample invalid PO data format missing 'id'
    invalid_po_data = {
        "podetails": {
            "fields": {
                "tranid": "PO54321"
            }
        }
    }

    response = client.post("/send_process_po", json=invalid_po_data)
    assert response.status_code == 400
    assert response.json() == {
                "detail": "Invalid PO data format."}
    