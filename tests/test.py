import unittest
import json
from slacking import Slacking


class TestSlacking(unittest.TestCase):

    def setUp(self):
        self.slackConnection = Slacking('TestMessage', 'https://hooks.slack.com/services/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')

    def test_send_message_to_slack(self):
        response = self.slackConnection.send_message_to_slack()
        self.assertEqual(response.status, 200)

    def test_send_json_to_slack(self):
        self.slackConnection.message = {"testing": "This is a Test"}
        response = self.slackConnection.send_json_to_slack()
        self.assertEqual(response.status, 200)

    def test_pass_message_as_json(self):
        '''
        If a user calls the send_json_to_slack method while passing in a flat
        message, should return None and not call the API
        '''

        response = self.slackConnection.send_json_to_slack()
        self.assertEqual(response, None)

if __name__ == '__main__':
    unittest.main()
