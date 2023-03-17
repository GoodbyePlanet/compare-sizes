import json

person = {
  "name": "John Doe",
  "age": 30,
  "isStudent": False
}

# Encode the message as JSON
encoded_person = json.dumps(person).encode('utf-8')

# Calculate the byte size
byte_size = len(encoded_person)

print("Byte size of message:", byte_size)
