import os
from triggercmd import client

with open(os.path.expanduser('~/.TRIGGERcmdData/token.tkn')) as f:
    token = f.readlines()[0]

print(token)

r = client.list(token)

print(r.json())
