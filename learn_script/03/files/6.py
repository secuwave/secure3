#!/usr/bin/python

import json

dic1 = {'name':'ykkim', 'birth':'1002', 'age': 33}
print('dict original ==> name: {}, birth: {}'.format(dic1.get('name'), dic1.get('birth')))

json_string = json.dumps(dic1)
print('json_string: ' + json_string)

dic_comeback = json.loads(json_string)
print('dic_comeback  ==> name: {}, birth: {}'.format(dic_comeback.get('name'), dic_comeback.get('birth')))