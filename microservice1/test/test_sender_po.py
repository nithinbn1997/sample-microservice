import requests
from fastapi.testclient import TestClient
from sender_po import app1
import httpx

client = TestClient(app1)

# Test Case 1: Valid PO Data
def test_valid_po_data():
    # Mock the receiver service response
    def mock_receiver_service(url, json):
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
        "detail": "Invalid PO data format."
    }

# Test Case 3: Receiver Service Unavailable
# def test_receiver_service_unavailable():
#     # Mock the receiver service response to simulate unavailability and return status code 500
#     def mock_receiver_service_unavailable(url, json):
#         return requests.Response(status_code=500, json={"detail": "Receiver service is not available."})
#     # Set up the FastAPI app
#     app1.dependency_overrides[requests.post] = mock_receiver_service_unavailable

#     # Sample valid PO data
#     po_data = {
#         "podetails": {
#             "id": 98765,
#             "fields": {
#                 "tranid": "PO98765"
#             }
#         }
#     }

#     response = client.post("/send_process_po", json=po_data)
#     assert response.status_code == 500
#     assert response.json() == {"detail": "Receiver service is not available."}