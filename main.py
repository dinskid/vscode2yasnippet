import os
import sys
import json

def main(template, directory):
    with open(template, 'r') as f:
        template = f.read()
    d = json.loads(template)
    for (name, contents) in d.items():
        key = contents.get("prefix")
        body = contents.get("body")
        assert(body is not None)
        if isinstance(body, list):
            body = '\n'.join(body)

        # create a file and store it in yasnippet
        # format
        base_template = f'# -*- mode: snippet -*-\n# name: {name}\n# key: {key}\n# --\n'
        base_template += body

        with open(os.path.join(directory, name), 'w') as f:
            f.write(base_template)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: python3 {sys.argv[0]} template.json directory')
    template, directory = sys.argv[1:]
    main(template, directory)

'''
# -*- mode: snippet -*-
# name: CPTemplate
# key: cpp
# --
body
'''
