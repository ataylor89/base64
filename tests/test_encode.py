from encode import encode
from unittest import TestCase
import base64

class TestEncode(TestCase):

    def test_encode(self):
        with open('tests/test_data/messages.txt', 'r') as file:
            for message in file:
                message_bytes = message.encode('utf-8')
                std_encoding = base64.b64encode(message_bytes).decode('utf-8')
                my_encoding = encode(message_bytes)
                assert std_encoding == my_encoding
