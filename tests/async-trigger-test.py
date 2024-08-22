import os
from triggercmd import client
import asyncio

async def main():
    with open(os.path.expanduser('~/.TRIGGERcmdData/token.tkn')) as f:
        token = f.readlines()[0]

    print(token)

    sender = "Python Tester"
    data = {"computer": "laptop", "trigger": "calculator", "params": "on", "sender": sender}

    r = await client.async_trigger(token,data)

    print(r.json())

if __name__ == "__main__":
    asyncio.run(main())