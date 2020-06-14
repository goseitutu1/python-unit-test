import requests

class ItemResource(object):    
    def __init__(self, data_interface):        
        self.di = data_interface

    def create_item_by_name(self, name, price):
        new_item = {
            'name': name,
            'price': price
        }
        try:
            requests.post("http://127.0.0.1:500/store/"+name)
            result = new_item
        except ConnectionError:        
            result = "Connection error occurred. Try Again."    
        return result

    def get_item_by_name(self, name):
        try:        
            result = requests.get("http://127.0.0.1:500/store/"+name)
        except ConnectionError:        
            result = "Connection error occurred. Try Again."    
        return result

    def put_item_by_name(self, name, price):
        try:
            requests.put("http://127.0.0.1:500/store/"+name)
            return { 
                'name': name,
                'price': price
            }
        except ConnectionError:
            return "Connection error occurred. Try Again."

    def delete_item_by_name(self, name):
        try:
            requests.delete("http://127.0.0.1:500/store/"+name)
            return '200'
           
        except ConnectionError:
            return "Connection error occurred. Try Again."

