from flask import Flask
from flask import request
import json
import time
import external_api
 
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def handel_request():
    client = XMLRPC_API(url=ODOO_URL, db=ODOO_DB, username=ODOO_USERNAME, password=ODOO_PASSWORD)
 
 
    return client.read(model_name='purchase.order',
                        conditions=[('id', '>=', 1)],
                        params={'fields': ['name', 'partner_id', 'user_id'], })


