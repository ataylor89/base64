from tables import decoding_table
from util import from_sextets
import argparse

def decode(text):
    sextets = []
    for ch in text:
        if ch in decoding_table:
            sextets.append(decoding_table[ch])
    byte_data = from_sextets(sextets)
    return byte_data

def main():
    argparser = argparse.ArgumentParser(prog='decode.py', description='Decode text using base64')
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
    decoded_message = decode(message).decode('utf-8')
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(decoded_message)
    else:
        print(decoded_message, end='')

if __name__ == '__main__':
    main()
