#!/usr/bin/env python

# Copy file `recipes` from Factorio script-output folder
# and pretty-print it to `recipes.json`

import json
import os

SCRIPT_OUTPUT = os.path.join(
  os.environ['APPDATA'],
  'Factorio',
  'script-output'
)

files = ('recipes','technologies')

def parse_files(file_type):
    file_path = os.path.join(SCRIPT_OUTPUT,file_type)
    with open(file_path) as fp:
        obj = json.load(fp)

    output_file = file_type + '.json'
        
    with open(output_file, 'w') as out:
        json.dump(obj, out, indent=1, sort_keys=True)

def main():
    for i in files:
        parse_files(i)

if __name__ == '__main__':
    main()
