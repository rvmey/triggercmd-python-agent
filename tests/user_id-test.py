import os
from triggercmd import utils

with open(os.path.expanduser('~/.TRIGGERcmdData/token.tkn')) as f:
    token = f.readlines()[0]

id = utils.user_id(token)

print(id)
