import json

message = {
  "name": "John Doe",
  "age": 30,
  "isStudent": False
}

# Encode the message as JSON
encoded_message = json.dumps(message).encode('utf-8')

# Calculate the byte size
byte_size = len(encoded_message)

print("Byte size of message:", byte_size)
