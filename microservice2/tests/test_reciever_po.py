from fastapi.testclient import TestClient
from reciever_po import app

client = TestClient(app)

def test_receive_po_message_valid_data():
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
