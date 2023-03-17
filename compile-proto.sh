#!/bin/sh

protoc -I=. --python_out=. person.proto
