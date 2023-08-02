from fastapi import FastAPI

app = FastAPI()

@app.post("/receive_po_message")
async def receive_po_message(po_data: dict):
    try:
        po_id = po_data['podetails']['id']
        po_name = po_data['podetails']['fields']['tranid']
        
        # Process the PO data (In this example, we just return it)
        return {"message": "PO data received and processed successfully", "po_id": po_id, "po_name": po_name}
    except KeyError:
        return {"error": "Invalid PO data format."}
