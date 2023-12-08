import requests
import json
class RequestUtilities(object):
    
    def __init__(self):
        self.base_url = "https://reqres.in/"
    
    
    def get(self, endpoint, headers=None, payload=None, expected_status_code=201):
        if headers is None:
            headers = {"Content-Type":"application/json"}
        url = self.base_url + endpoint
        session = requests.session()
        response = session.get(url, headers=headers)
        
        return response

    
    def post(self, endpoint, headers=None, payload=None):
        if headers is None:
            headers = {"Content-Type":"application/json"}
        url = self.base_url + endpoint
        session = requests.session()
        response = session.post(url, data = json.dumps(payload),  headers=headers)
        
        return response
    
    def update(self, endpoint, headers=None, payload=None):
        if headers is None:
            headers = {"Content-Type":"application/json"}
        url = self.base_url + endpoint
        session = requests.session()
        response = session.put(url, data = json.dumps(payload),  headers=headers)
        
        return response
    
    def delete(self, endpoint, headers=None, payload=None):
        if headers is None:
            headers = {"Content-Type":"application/json"}
        url = self.base_url + endpoint
        session = requests.session()
        response = session.delete(url, headers=headers)
        
        return response