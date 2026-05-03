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
