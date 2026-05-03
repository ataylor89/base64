encoding_table = []

for i in range(26):
    encoding_table.append(chr(ord('A') + i))

for i in range(26):
    encoding_table.append(chr(ord('a') + i))

for i in range(10):
    encoding_table.append(chr(ord('0') + i))

encoding_table.append('+')
encoding_table.append('/')

decoding_table = {val: i for i, val in enumerate(encoding_table)}

def encode(byte_data):
    encoded_text = ''
    sextets = to_sextets(byte_data)
    for sextet in sextets:
        encoded_text += encoding_table[sextet]
    while len(encoded_text) % 4 != 0:
        encoded_text += '='
    return encoded_text

def decode(text):
    sextets = []
    for ch in text:
        if ch in decoding_table:
            sextets.append(decoding_table[ch])
    byte_data = from_sextets(sextets)
    return byte_data

def to_sextets(byte_data):
    bit_str = ''.join(f"{byte:08b}" for byte in byte_data)        
    while len(bit_str) % 6 != 0:
        bit_str += '0'
    sextets = [int(bit_str[i:i+6], 2) for i in range(0, len(bit_str), 6)]
    return sextets

def from_sextets(sextets):
    bit_str = ''.join(f"{sextet:06b}" for sextet in sextets)
    pad_length = len(bit_str) % 8
    if pad_length > 0:
        bit_str = bit_str[:-pad_length]
    n = int(bit_str, 2)
    byte_data = n.to_bytes((len(bit_str) + 7) // 8, 'big')
    return byte_data

message = 'hello world today is sunday may 3 2026'
message_bytes = message.encode('utf-8')
print(message)

encoded_message = encode(message_bytes)
print(encoded_message)

decoded_message = decode(encoded_message).decode('utf-8')
print(decoded_message)
