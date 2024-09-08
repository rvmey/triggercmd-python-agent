import httpx

def trigger(token, data):
    url = "https://www.triggercmd.com/api/run/trigger"
    headers = {"Authorization": "Bearer " + token}
    r = httpx.post(url, headers=headers, data=data)
    return r

def list(token):
    url = "https://www.triggercmd.com/api/command/simplelist"
    headers = {"Authorization": "Bearer " + token}
    r = httpx.get(url, headers=headers)
    return r

async def async_trigger(token, data):
    url = "https://www.triggercmd.com/api/run/trigger"
    headers = {"Authorization": "Bearer " + token}
    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, data=data)
        return r

async def async_list(token):
    url = "https://www.triggercmd.com/api/command/simplelist"
    headers = {"Authorization": "Bearer " + token}
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers)
        return r
    
async def async_connection_test(token):
    url = "https://www.triggercmd.com/api/ha/connection_test"
    headers = {"Authorization": "Bearer " + token}
    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headers)
        return r.status_code