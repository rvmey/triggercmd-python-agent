import json, os
from triggercmd import agent

with open(os.path.expanduser('~/.TRIGGERcmdData/computerid.cfg')) as f:
    computer_id = f.readlines()[0]

with open(os.path.expanduser('~/.TRIGGERcmdData/token.tkn')) as f:
    token = f.readlines()[0]

print(computer_id, token)

def my_function(msg):
    print(msg)
    message = json.loads(msg)
    print("Received this trigger:", message['trigger'], "and these parameters:", message['params'])

agent.connect(computer_id, token, my_function)