# TRIGGERcmd Python Package

For the full TRIGGERcmd agent, visit https://triggercmd.com.

Use this package to listen for triggers sent to a computer in your TRIGGERcmd account.

Send triggers with Amazon Alexa, Google Assistant, IFTTT, Zapier, Smart Things, etc.  See [this page](https://www.triggercmd.com/forum/topic/30/list-of-ways-to-trigger-your-commands) for more ways.

## Usage:

```
import json
from triggercmd import agent

computer_id = (your triggercmd computer id)
token = (your triggercmd token)

def my_function(msg):
    print(msg)
    message = json.loads(msg)
    print("Received this trigger:", message['trigger'])

agent.connect(computer_id, token, my_function)
```

## Example output:

```
Connected
{"trigger":"Calculator","id":"13123391234567891acbf123"}
Received this trigger: Calculator
{"trigger":"Notepad","id":"13123391234567891acbf124"}
Received this trigger: Notepad
```

## Based on this project:
https://github.com/gilsdav/python_sails_websocket_client/tree/master