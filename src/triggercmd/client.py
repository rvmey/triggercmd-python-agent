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
