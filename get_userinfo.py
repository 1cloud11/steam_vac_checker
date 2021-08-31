import requests
import xml.etree.ElementTree as et
from webapp.config import STEAM_API_KEY, FACEIT_API_KEY

user_url = 'https://steamcommunity.com/id/1cloud/'

def get_userinfo(steam_user_url):
    #Getting steam info
    steam_user_url_xml = steam_user_url + "?xml=1"
    root = et.fromstring(requests.get(steam_user_url_xml).content)
        
    steamid64 = root.find("steamID64").text #steamid
    steam_name = root.find("steamID").text #steamname
    vac = root.find("vacBanned").text #VAC_count

    json_url = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=" + STEAM_API_KEY + "&steamids=" + steamid64
    print(json_url)
    params = {
        "format": "json",
    }

    result = requests.get(json_url, params=params)
    steam_json_data = result.json()

    if "players" in steam_json_data:
        try:
            last_vac = steam_json_data["players"][0]["DaysSinceLastBan"] #days sine last vac
        except(IndexError, TypeError):
            return "Возникла ошибка"

    #Getting Faceit info
    first_faceit_url = "https://open.faceit.com/data/v4/players?game=csgo&game_player_id="+steamid64
    headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {FACEIT_API_KEY}",
            }

    faceit_info = requests.get(first_faceit_url, headers=headers).json()
       
    faceit_id = faceit_info["player_id"]
    faceit_name = faceit_info["nickname"]
    faceit_level = faceit_info["games"]["csgo"]["skill_level_label"]
    faceit_elo = faceit_info["games"]["csgo"]["faceit_elo"]

    user_info = {
        "steamID64": steamid64, 
        "steamname": steam_name, 
        "VAC": vac, 
        "DaysSinceLastBan": last_vac,
        "FACEITID": faceit_id,
        "FACEIT_NAME": faceit_name,
        "FACEIT_LEVEL": faceit_level,
        "FACEIT_ELO": faceit_elo,
        }

    return user_info

if __name__ == "__main__":
    g = get_userinfo(user_url)
    print(g)


    #Добавить инфу из: http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=STEAM_API_KEY&steamid=STEAMID%20&format=json
    #	"Counter-Strike: Global Offensive"
    #playtime_2weeks
    #playtime_forever
    #
    #Добавить инфу из http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=STEAM_API_KEY&steamids=STEAMID
    #timecreated
    #
    #===============FACEIT======================
    #Запросы нужно делать через FACEIT app API_KEY (serverside)
    #запрос https://open.faceit.com/data/v4/players?game=csgo&game_player_id=76561198021543621
    #"player_id"
    #"nickname"
    #"skill_level"
    #"faceit_elo"
    #запрос https://open.faceit.com/data/v4/players/4c568fce-ef08-4e4d-a90d-3b0da03a6a35/stats/csgo
    #"Average Headshots %"
    #"Matches"
    #"Win Rate %"
    #"Average K/D Ratio"