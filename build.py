import json
import sys
from hashlib import sha256
from jinja2 import Environment, FileSystemLoader

def short_hash(value):
    byte = value.encode('utf-8')
    return sha256().hexdigest()[:8]

env = Environment(
    loader=FileSystemLoader('.')
)
env.filters["short_hash"] = short_hash
data = json.load(sys.stdin)
template = env.get_template("nginx.template")
print(template.render(servers=data))