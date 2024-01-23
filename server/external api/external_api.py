import xmlrpc.client

### Configuration
ODOO_URL = 'https://chanhtest.odoo.com/'
ODOO_DB = 'chanhtest'
ODOO_USERNAME = 'chanh.huynhcong@ricoh.com.vn'
ODOO_PASSWORD = '@dmin123'

def myprint(data_list, title=''):
    if title:
        print(title)
    for line in data_list:
        print('-', line)
    pass

def myprintCustomer(data_list, title=''):
    if title:
        print(title)
    for customer in data_list:
        print(customer)
class XMLRPC_API():
    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        pass
    #get fields names of the model
    def get_fields(self, model_name, required=False):
        data = self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model_name,
            'fields_get',
            [],
            {'attributes': ['string', 'help', 'type', 'required', 'readonly']})
        if required:
            key_list = list(data.keys())
            for k in key_list:
                if not data[k].get('required', False):
                    data.pop(k)
                pass
        return data
    #search
    def search(self, model_name, conditions=[()]):
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model_name,
            'search',
            [conditions])
    #Create
    def create(self, model_name, data_dict):
        """
        Eg.
        :param model_name: 'purchase.order'
        :param data_dict: { 'name': "Chanh", 'age': 18}
        """
        id = self.models.execute_kw(self.db, self.uid, self.password,
                                    model_name, 'create', [data_dict])
        return id
    #Read
    def read(self, model_name, conditions=[()], params={}):
        """
        Eg.
        :param model_name: 'purchase.order'
        :param conditions: [('id', '>', 1)]
        :param params: {'fields': ['name', 'country_id', 'comment'], 'limit': 5}
        """
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model_name,
            'search_read',
            [conditions],
            params)
    #Update
    def update(self, model_name, id_list, new_data_dict):
        """
        Eg.
        :param model_name: 'purchase.order'
        :param id_list: [7]
        :param new_data_dict: {'name': 'ChanhOdoo', 'age': 20}
        """
        self.models.execute_kw(self.db, self.uid, self.password,
                               model_name, 'write', [id_list, new_data_dict])
    #Delete
    def delete(self, model_name, id_list):
        self.models.execute_kw(self.db, self.uid, self.password,
                               model_name, 'unlink', [id_list])
        pass

    def call(self, model_name, method, params=[]):
        return self.models.execute_kw(self.db, self.uid, self.password,
                                      model_name, method, params)
    def call2(self, model_name, method, param1, param2):
        return self.models.execute_kw(self.db, self.uid, self.password,
                                      model_name, method, param1, param2)

def main():
    client = XMLRPC_API(url=ODOO_URL, db=ODOO_DB, username=ODOO_USERNAME, password=ODOO_PASSWORD)
    myprintCustomer(client.read(model_name='purchase.order',
                        conditions=[('id', '>=', 1)],
                        params={'fields': ['name', 'partner_id', 'user_id'], }))
    pass

if __name__ == '__main__':
    main()