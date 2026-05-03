from encode import encode
from unittest import TestCase
import csv

class TestEncode(TestCase):

    def test_encode(self):
        with open('tests/test_data/encoding_data.txt', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if not row:
                    continue
                input = row[0].strip()
                expected = row[1].strip()
                output = encode(input.encode('utf-8'))
                assert output == expected
