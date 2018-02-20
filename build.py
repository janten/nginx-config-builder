import json
import sys
from hashlib import sha256
from jinja2 import Environment, FileSystemLoader
from glob import glob

def short_hash(value):
    encoded = value.encode('utf-8')
    return sha256(encoded).hexdigest()[:8]

env = Environment(
    loader=FileSystemLoader('.')
)
env.filters["short_hash"] = short_hash
servers = []
for filename in glob("/sites/*.json"):
    data = json.load(open(filename))
    if "add_headers" not in data:
        data["add_headers"] = {}
    servers.append(data)
template = env.get_template("nginx.template")
print(template.render(servers=servers))