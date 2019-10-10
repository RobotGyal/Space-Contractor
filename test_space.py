import unittest
from bson.objectid import ObjectId
from app import app


sample_cart_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_cart = {
    'title': 'Rocket Ship',
    'description': 'To take off on adventures'
    }

sample_form_data = {
    'title': sample_cart['title'],
    'description': sample_cart['description']
}


class SpaceClass(unittest.TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_home(self):
        """Test the space homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    def test_devices_new(self):
        """Test the new cart creation page."""
        result = self.client.get('/cart/add')
        self.assertEqual(result.status, '200 OK')

if __name__ == '__main__':
    unittest.main()