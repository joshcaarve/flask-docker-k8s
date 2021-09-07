#!/usr/bin/env python3
import requests
import sys
import json

def print_json(dict_json):
    print(json.dumps(dict_json, indent=4))

BASE = 'http://{}:{}/'.format(sys.argv[1], sys.argv[2])
response = requests.get(BASE + str(sys.argv[3]))
print_json(response.json())
