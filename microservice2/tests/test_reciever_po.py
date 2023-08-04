"""
 test case for reciever po
"""
from fastapi.testclient import TestClient
from reciever_po import app

client = TestClient(app)

def test_receive_po_message_valid_data():
    """
    Test receiving and processing of valid Purchase Order (PO) data.

    This function tests the receiving and processing of a valid PO data by
    sending a sample valid PO data to the "/receive_po_message" endpoint using
    the FastAPI client.

    The test expects the response status code to be 200 (OK) and checks that
    the response JSON contains the expected content."""

    po_data = {
        "podetails": {
            "id": "12345",
            "fields": {
                "tranid": "PO12345"
            }
        }
    }
    response = client.post("/receive_po_message", json=po_data)
    assert response.status_code == 200
    assert response.json() == {
        "message": "PO data received and processed successfully",
        "po_id": "12345",
        "po_name": "PO12345"
    }

def test_receive_po_message_invalid_data():
    """
    Test handling of invalid Purchase Order (PO) data format.

    This function tests the handling of invalid PO data format by sending
    a sample invalid PO data (missing 'id' field) to the "/receive_po_message"
    endpoint using the FastAPI client.

    The test expects the response status code to be 400 (Bad Request) and
    checks that the response JSON contains the expected error detail."""

    invalid_po_data = {
        "podetails": {
            "fields": {
                "tranid": "PO54321"
            }
        }
    }
    response = client.post("/receive_po_message", json=invalid_po_data)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid PO data format."
    }
