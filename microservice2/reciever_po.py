"""
API to receive po details
"""
from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.post("/receive_po_message")
async def receive_po_message(po_data: dict):
    """
    Receive and process Purchase Order (PO) data.

    This function receives a dictionary containing Purchase Order data
    and processes it to extract relevant information such as PO id and name.

    Parameters:
        po_data (dict): A dictionary containing Purchase Order data.

    Returns:
        dict: A dictionary with a message indicating successful processing,
              along with extracted PO id and name.

    Raises:
        HTTPException: If the PO data is in an invalid format (missing keys).
    """
    try:
        po_id = po_data['podetails']['id']
        po_name = po_data['podetails']['fields']['tranid']
        # Process the PO data (In this example, we just return it)
        return {"message": "PO data received and processed successfully",
                "po_id": po_id, "po_name": po_name}
    except KeyError as exc:
        raise HTTPException(status_code=400, detail="Invalid PO data format.") from exc
