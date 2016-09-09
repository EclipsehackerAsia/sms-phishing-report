#!/usr/bin/python3

from yattag import Doc, indent
import slumber

doc, tag, text = Doc().tagtext()

api = slumber.API("https://cymon.io:443/api/nexus/v1/")

blacklist = {}
for i in range(1,4):
    blacklist[i] = api.blacklist.ip.phishing().get(days=i, limit=5000)

"""
with tag('ul'):
    for ip in blacklist['results']:
        with tag('li'):
            text(ip['addr'])

result = indent(
    doc.getvalue(),
    indentation = '    ',
    newline = '\r\n'
)

print(result)
"""

results = [blacklist[i]['count'] for i in range(1,4)]
print(results)
