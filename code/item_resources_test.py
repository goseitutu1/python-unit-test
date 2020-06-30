import unittest
from mock import Mock, patch


from item_resources import ItemResource

class ItemResourceTesting(unittest.TestCase):
    def setUp(self): 
        self.Item = ItemResource(Mock()) #To create instance of the 'Mock()' class
        self.stores = [ # Item 'car' in the 'stores' list to test the http verbs
            {
                'name': 'car',
                'price': 12
            }
        ]

    @patch('item_resources.requests') #Patching the request target from 'item_resources' file. 
    def test_create_item_by_name(self, mock_requests):
        self.stores.append(self.Item.create_item_by_name('toffee', 34)) #Append new dict from the 'create_item_by_name' method to the store list.
        mock_requests.post.return_value = self.stores[1] #To return the new created item as a result of the post method from this url 'http://127.0.0.1:500/store/"+name'. 
        self.assertDictEqual(mock_requests.post.return_value, self.Item.create_item_by_name('toffee', 34)) #To verify that the new item dict is appended to the list.

    @patch('item_resources.requests') #Patching the request target from 'item_resources' file.   
    def test_create_item_by_name_when_connect_exception_raised(self, mock_requests):
        mock_requests.post.side_effect = ConnectionError()
        self.assertEqual("Connection error occurred. Try Again.", self.Item.create_item_by_name('toffee', 34))

    @patch('item_resources.requests') #Patching the request target from 'item_resources' file. 
    def test_get_item_by_name(self, mock_requests):
        for item in self.stores:
            if item['name'] == 'car':
                mock_requests.get.return_value = item
        self.assertDictEqual(mock_requests.get.return_value, self.Item.get_item_by_name('car'))

    @patch('item_resources.requests') #Patching the request target from 'item_resources' file.   
    def test_get_item_by_name_when_connect_exception_raised(self, mock_requests):
        mock_requests.get.side_effect = ConnectionError()
        self.assertEqual("Connection error occurred. Try Again.", self.Item.get_item_by_name('car'))

    @patch('item_resources.requests') #Patching the request target from 'item_resources' file. 
    def test_put_item_by_name(self, mock_requests):
        for item in self.stores:  #Loops through store list and then update if already exist
            if item['name'] == 'car':
                item['price'] = 45
                mock_requests.put.return_value = self.stores[0]
                self.assertDictEqual(mock_requests.put.return_value , self.Item.put_item_by_name('car', 45))
        else: #If no item by 'name' already exixts, then create new item
            self.stores.append(self.Item.put_item_by_name('car', 45))
            mock_requests.put.return_value = self.stores[1]
            self.assertDictEqual(mock_requests.put.return_value , self.Item.put_item_by_name('car', 45))

    @patch('item_resources.requests') #Patching the request target from 'item_resources' file.   
    def test_put_item_by_name_when_connect_exception_raised(self, mock_requests):
        mock_requests.post.side_effect = ConnectionError()
        self.assertEqual("Connection error occurred. Try Again.", self.Item.create_item_by_name('car', 45))

    
    @patch('item_resources.requests') #Patching the request target from 'item_resources' file. 
    def test_delete_item_by_name(self, mock_requests):
        self.stores = list(filter( lambda x: x['name'] != 'car',self.stores)) #Deleting car item. Hence making the store list empty
        if self.stores == []:
            mock_requests.delete.return_value = '200'
            self.assertEqual(mock_requests.delete.return_value , self.Item.delete_item_by_name('car'))

    @patch('item_resources.requests') #Patching the request target from 'item_resources' file.   
    def test_delete_item_by_name_when_connect_exception_raised(self, mock_requests):
        mock_requests.delete.side_effect = ConnectionError()
        self.assertEqual("Connection error occurred. Try Again", self.Item.delete_item_by_name('car'))


if __name__ == '__main__':   
    unittest.main()


   