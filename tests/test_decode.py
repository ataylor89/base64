from encode import encode
from decode import decode
from unittest import TestCase
import base64

class TestDecode(TestCase):

    def test_decode(self):
        with open('tests/test_data/messages.txt', 'r') as file:
            for message in file:
                message_bytes = message.encode('utf-8')
                std_encoding = base64.b64encode(message_bytes).decode('utf-8')
                my_encoding = encode(message_bytes)
                assert std_encoding == my_encoding
                std_decoding = base64.b64decode(std_encoding)
                my_decoding = decode(my_encoding)
                assert std_decoding == my_decoding == message_bytes
