from tables import encoding_table
from util import to_sextets
import argparse

def encode(byte_data):
    encoded_text = ''
    sextets = to_sextets(byte_data)
    for sextet in sextets:
        encoded_text += encoding_table[sextet]
    while len(encoded_text) % 4 != 0:
        encoded_text += '='
    return encoded_text

def main():
    argparser = argparse.ArgumentParser(prog='encode.py', description='Encode text using base64')
    group = argparser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    argparser.add_argument('-o', '--outputfile', type=str)
    args = argparser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            message = file.read()
    else:
        message = args.message
    message_bytes = message.encode('utf-8')
    encoded_message = encode(message_bytes)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(encoded_message)
    else:
        print(encoded_message, end='')

if __name__ == '__main__':
    main()
