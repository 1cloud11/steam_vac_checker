from steam.client import SteamClient
from csgo.client import CSGOClient

client = SteamClient()
cs = CSGOClient(client)

request_recent_user_games(account_id)