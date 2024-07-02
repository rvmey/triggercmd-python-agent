import os
from triggercmd import client

with open(os.path.expanduser('~/.TRIGGERcmdData/token.tkn')) as f:
    token = f.readlines()[0]

print(token)

sender = "Python Tester"
data = {"computer": "laptop", "trigger": "calculator", "params": "on", "sender": sender}

r = client.trigger(token,data)

print(r.json())