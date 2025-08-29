import httpx
from .exceptions import TRIGGERcmdConnectionError

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

# For Home Assistant integration:
async def async_trigger(token, data, hass):
    url = "https://www.triggercmd.com/api/run/trigger"
    headers = {"Authorization": "Bearer " + token}
    from homeassistant.helpers.httpx_client import get_async_client
    async with get_async_client(hass) as client:
        r = await client.post(url, headers=headers, data=data)
        return r

async def async_list(token, hass):
    url = "https://www.triggercmd.com/api/command/simplelist"
    headers = {"Authorization": "Bearer " + token}
    from homeassistant.helpers.httpx_client import get_async_client
    async with get_async_client(hass) as client:
        r = await client.get(url, headers=headers)
        return r
    
async def async_connection_test(token, hass):
    url = "https://www.triggercmd.com/api/ha/connection_test"
    headers = {"Authorization": "Bearer " + token}
    from homeassistant.helpers.httpx_client import get_async_client
    async with get_async_client(hass) as client:
        try:
            r = await client.get(url, headers=headers)
        except Exception as e:
            raise TRIGGERcmdConnectionError
        else:
            return r.status_code
