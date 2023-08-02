import uvicorn
# import app

if '__main__' == __name__:
    uvicorn.run("sender_po:app", host='localhost', port=8081)