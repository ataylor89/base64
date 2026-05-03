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
