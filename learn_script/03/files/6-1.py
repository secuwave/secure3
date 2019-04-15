#!/usr/bin/python

import json


with open('mydata.json') as f:
    dic_data = json.load(f)

print('dic_data  ==> name: {}, birth: {}'.format(dic_data.get('name'), dic_data.get('birth')))

with open('back.json', 'w') as of:
    # json.dump(dic_data, of)
    json.dump(dic_data, of, indent = 4)
