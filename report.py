#!/usr/bin/python3

from yattag import Doc, indent
import slumber
import json
import time

doc, tag, text = Doc().tagtext()

api = slumber.API("https://cymon.io:443/api/nexus/v1/")

blacklist = api.blacklist.ip.phishing().get(days=3, limit=20)

results = []
for ip in blacklist['results']:
    addr = ip['addr']
    created = api.ip(addr).get()['created']
    date = time.strftime('%Y-%m-%d', time.strptime(created, '%Y-%m-%dT%H:%M:%SZ'))
    results.append((addr, date))

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('style'):
            text('* { font-family: monospace; } td, th { padding: 5px 20px; }')
    with tag('body'):
        with tag('h1'):
            text('IP Addresses Flagged for Phishing')
        with tag('table'):
            with tag('tr'):
                with tag('th'):
                    text('IP Address')
                with tag('th'):
                    text('Date')
            for result in results:
                with tag('tr'):
                    with tag('td'):
                        text(result[0])
                    with tag('td'):
                        text(result[1])

output = indent(
    doc.getvalue(),
    indentation = '    ',
    newline = '\r\n'
)

print(output)

