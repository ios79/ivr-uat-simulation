import unittest
from unittest.mock import patch
import json

# Load the call flow configuration
with open('call_flows/sample_call_flow.json', 'r') as file:
    call_flow = json.load(file)

class TestIVRSimulation(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', return_value='1')
    def test_sales_option(self, mock_input, mock_print):
        from ivr_simulation import call_flow  # reuse loaded data
        response = call_flow["options"]["1"]["message"]
        self.assertEqual(response, "You selected Sales. Please wait while we connect you.")

    @patch('builtins.print')
    @patch('builtins.input', return_value='2')
    def test_support_option(self, mock_input, mock_print):
        response = call_flow["options"]["2"]["message"]
        self.assertEqual(response, "You selected Support. Please describe your issue after the beep.")

    @patch('builtins.print')
    @patch('builtins.input', return_value='0')
    def test_operator_option(self, mock_input, mock_print):
        response = call_flow["options"]["0"]["message"]
        self.assertEqual(response, "Connecting you to the operator.")

    @patch('builtins.print')
    @patch('builtins.input', return_value='9')
    def test_invalid_option(self, mock_input, mock_print):
        invalid_msg = call_flow["invalid_option"]
        self.assertEqual(invalid_msg, "Sorry, that is not a valid selection. Please try again.")

if __name__ == '__main__':
    unittest.main()
 
