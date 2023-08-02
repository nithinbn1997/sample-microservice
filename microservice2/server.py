import uvicorn

if '__main__' == __name__:
    uvicorn.run("reciever_po:app", host='localhost', port=8082)