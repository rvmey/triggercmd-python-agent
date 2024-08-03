import jwt

def user_id(token):
    tokenData = jwt.decode(token, options={"verify_signature": False})
    return tokenData["id"]
