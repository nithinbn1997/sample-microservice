from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.post("/send_process_po")
async def process_po(po_data: dict):
    try:
        # URL for the receiver service
        receiver_url = "http://localhost:8082/receive_po_message"

        po_id = po_data['podetails']['id']
        po_name = po_data['podetails']['fields']['tranid']
        
        # Sending the po_data as JSON to the receiver service
        response = requests.post(receiver_url, json=po_data)
        response.raise_for_status()

        return {"message": "PO data sent successfully", "po_id": po_id, "po_name": po_name}
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid PO data format.")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to communicate with the receiver service.")
