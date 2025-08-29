import os
from triggercmd import client
import asyncio

async def main():
    with open(os.path.expanduser('~/.TRIGGERcmdData/token.tkn')) as f:
        token = f.readlines()[0]

    print(token)

    status_code = await client.async_connection_test(token, None)

    print(status_code)

if __name__ == "__main__":
    asyncio.run(main())