# password encryption program

import base64

def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode("utf-8")
    print(decode_data)

encode_string = input("Enter your the base64 string: ")
decode_pass(encode_string)