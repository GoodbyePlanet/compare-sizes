#!/usr/bin/python

import person_pb2

# Create an instance of the message
person = person_pb2.Person()
person.name = "John Doe"
person.age = 30
person.isStudent = False

# Encode the message
encoded_message = person.SerializeToString()

# Calculate the byte size
byte_size = len(encoded_message)

print("Byte size of message:", byte_size)

