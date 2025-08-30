from . import client, utils
from .exceptions import TRIGGERcmdConnectionError

class Hub:
    """Hub for TRIGGERcmd."""

    manufacturer = "TRIGGERcmd"

    def __init__(self, token: str) -> None:
        """Init hub."""
        self._id = utils.user_id(token)
        self._token = token
        self.computers = []
        self.triggers = []
        self.online = False  # Set default
        self.httpx_client = None

    async def async_init(self, httpx_client):
        r = await client.async_list(self._token, httpx_client)
        self.computers = []
        self.httpx_client = httpx_client
        for item in r.json():
            computer = item["computer"]
            if Computer(computer, self) not in self.computers:
                self.computers.append(Computer(computer, self))
        self.triggers = []
        for item in r.json():
            trigger = item["trigger"]
            computer = item["computer"]
            if Trigger(computer, trigger, self) not in self.computers:
                self.triggers.append(Trigger(computer, trigger, self))
        self.online = True

    @property
    def hub_id(self) -> str:
        """ID for hub."""
        return self._id

    @property
    def token(self) -> str:
        """Token for hub."""
        return self._token
    
    async def connection_test(self, httpx_client):
        """Test connection."""
        r = await client.async_list(self._token, httpx_client)
        if not r.status_code == 200:
            raise TRIGGERcmdConnectionError

class Trigger:
    """trigger for TRIGGERcmd."""

    def __init__(self, computerid: str, name: str, hub: Hub) -> None:
        """Init trigger."""
        self._id = name
        self._computer_id = computerid
        self.hub = hub
        self.name = name
        self.firmware_version = "1.0.0"
        self.model = "TRIGGERcmd Computer"

    @property
    def trigger_id(self) -> str:
        """Return ID for trigger."""
        return self._id

    @property
    def computer_id(self) -> str:
        """Return ID for computer."""
        return self._computer_id


class Computer:
    """computer (device for HA) for TRIGGERcmd."""

    def __init__(self, name: str, hub: Hub) -> None:
        """Init computer."""
        self._id = name
        self.hub = hub
        self.name = name
        self.firmware_version = "1.0.0"
        self.model = "TRIGGERcmd Computer"

    @property
    def computer_id(self) -> str:
        """Return ID for computer."""
        return self._id
