import unittest
import json
from app import app  # Make sure this imports your Flask app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_loads(self):
        """Test if the home page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    def test_predict_endpoint(self):
        """Test the predict endpoint with mock data"""
        sample_input = {
            "crop_name": "Rice",
            "region": "South India",
            "season": "Kharif",
            "soil_type": "Clayey",
            "market_demand": "High",
            "rainfall": 350  # Include all required fields based on your model
        }
        response = self.app.post('/predict',
                                 data=json.dumps(sample_input),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("predicted_price", response.get_json())

if __name__ == '__main__':
    unittest.main()