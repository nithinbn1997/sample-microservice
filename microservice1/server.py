"""
code to run uvicorn server
"""
import uvicorn
# import app

if '__main__' == __name__:
    uvicorn.run("sender_po:app1", host='localhost', port=8081)
    