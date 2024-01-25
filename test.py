import unittest
import requests
from requests.auth import HTTPBasicAuth

class TestFlaskAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'
    username = 'pratham'
    password = 'pratham12'

    def test_add_book(self):
        response = requests.post(
            f'{self.base_url}/books',
            json={
                'title': 'A Game of Thrones',
                'author': 'George R.R. Martin',
                'isbn': '978-0553593716',
                'price': "Rs. 480",
                'quantity': 8
            },
            auth=HTTPBasicAuth(self.username, self.password)
        )
        self.assertEqual(response.status_code, 200)

    def test_get_all_books(self):
        response = requests.get(
            f'{self.base_url}/books',
            auth=HTTPBasicAuth(self.username, self.password)
        )
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_isbn(self):
        response = requests.get(
            f'{self.base_url}/books/978-0316453363',
            auth=HTTPBasicAuth(self.username, self.password)
        )
        self.assertEqual(response.status_code, 200)

    def test_update_book(self):
        response = requests.put(
            f'{self.base_url}/books/978-0439023528',
            json={
                'title': 'The Hunger Games',
                'author': 'Suzanne Collins',
                'isbn': '978-0439023528',
                'price': "Rs. 420",
                'quantity': 9
            },
            auth=HTTPBasicAuth(self.username, self.password)
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = requests.delete(
            f'{self.base_url}/books/978-0590353427',
            auth=HTTPBasicAuth(self.username, self.password)
        )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()