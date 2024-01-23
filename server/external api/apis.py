from fastapi import FastAPI
from external_api import *
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    client = XMLRPC_API(url=ODOO_URL, db=ODOO_DB, username=ODOO_USERNAME, password=ODOO_PASSWORD)


    return client.read(model_name='purchase.order',
                        conditions=[('id', '>=', 1)],
                        params={'fields': ['name', 'partner_id', 'user_id'], })[1]

if __name__ == "__main__":
    uvicorn.run('apis:app', port=443, host='127.0.0.1',
                reload=True,
                ssl_keyfile="./https/127.0.0.1-key.pem",
                ssl_certfile="./https/127.0.0.1.pem")



