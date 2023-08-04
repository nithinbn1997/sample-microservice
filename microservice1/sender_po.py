"""
Sample Micro service Application
----------------------

This is a FastAPI application that sends po id and po name and process the requests.
It provides endpoints for various operations.
"""


from fastapi import FastAPI, HTTPException
import requests

app1 = FastAPI()

@app1.post("/send_process_po")
async def process_po(po_data: dict):
    """
    Process Purchase Order (PO) data.

    This function takes a dictionary containing Purchase Order data
    and performs some processing on it. The exact details of the
    processing are specific to the application.

    Parameters:
        po_data (dict): A dictionary containing Purchase Order data.

    Returns:
        None: This function doesn't return any value directly.
              The processing results are updated in the application's state.
    """
    try:
        # URL for the receiver service
        receiver_url = "http://localhost:8082/receive_po_message"
        po_id = po_data['podetails']['id']
        po_name = po_data['podetails']['fields']['tranid']
        # Sending the po_data as JSON to the receiver service
        response = requests.post(receiver_url, json=po_data, timeout=10)
        response.raise_for_status()

        return {"message": "PO data sent successfully", "po_id": po_id, "po_name": po_name}
    except KeyError as exc:
        raise HTTPException(status_code=400, detail="Invalid PO data format.") from exc
    except requests.exceptions.RequestException as error:
        raise HTTPException(
                    status_code=500,
                    detail="Failed to communicate with the receiver service."
                    ) from error
     